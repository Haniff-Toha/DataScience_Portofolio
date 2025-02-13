"""Training module."""

import os

import tensorflow as tf
import tensorflow_transform as tft

from heart_disease_transform import (
    CATEGORICAL_FEATURES,
    LABEL_KEY,
    NUMERICAL_FEATURES,
    transformed_name,
)
from heart_disease_tuner import gzip_reader_fn


def input_fn(file_pattern, tf_transform_output, batch_size=64):
    """Generates features and labels for tuning/training.

    Args:
        file_pattern: input tfrecord file pattern.
        tf_transform_output: A TFTransformOutput.
        batch_size: representing the number of consecutive elements of
        returned dataset to combine in a single batch.

    Returns:
        A dataset that contains (features, indices) tuple where features
        is a dictionary of Tensors, and indices is a single Tensor of
        label indices.
    """
    transformed_feature_spec = tf_transform_output.transformed_feature_spec().copy()

    dataset = tf.data.experimental.make_batched_features_dataset(
        file_pattern=file_pattern,
        batch_size=batch_size,
        features=transformed_feature_spec,
        reader=gzip_reader_fn,
        label_key=transformed_name(LABEL_KEY),
    )

    return dataset


def get_model(hyperparameters, show_summary=True):
    """Define a Keras model and return the model as a Keras object.

    Args:
        hyperparameters: A dictionary of hyperparameters.
        show_summary: Whether to print the model summary.

    Returns:
        A compiled Keras model.
    """
    input_features = []

    for key, dim in CATEGORICAL_FEATURES.items():
        input_features.append(
            tf.keras.Input(shape=(dim + 1,), name=transformed_name(key))
        )

    for feature in NUMERICAL_FEATURES:
        input_features.append(
            tf.keras.Input(shape=(1,), name=transformed_name(feature))
        )

    concatenate = tf.keras.layers.concatenate(input_features)
    deep = tf.keras.layers.Dense(hyperparameters["dense_units1"], activation="relu")(concatenate)
    drop = tf.keras.layers.Dropout(hyperparameters["dropout_rate1"])(deep)
    deep = tf.keras.layers.Dense(hyperparameters["dense_units2"], activation="relu")(deep)
    deep = tf.keras.layers.Dense(hyperparameters["dense_units3"], activation="relu")(deep)
    drop = tf.keras.layers.Dropout(hyperparameters["dropout_rate2"])(deep)
    outputs = tf.keras.layers.Dense(1, activation="sigmoid")(drop)

    model = tf.keras.models.Model(inputs=input_features, outputs=outputs)
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=hyperparameters["lr"]),
        loss="binary_crossentropy",
        metrics=[tf.keras.metrics.BinaryAccuracy()],
    )

    if show_summary:
        model.summary()

    return model


def get_serve_tf_examples_fn(model, tf_transform_output):
    """Returns a function that parses a serialized tf.Example.

    Args:
        model: A trained Keras model.
        tf_transform_output: A TFTransformOutput.

    Returns:
        A function that parses a serialized tf.Example.
    """
    model.tft_layer = tf_transform_output.transform_features_layer()

    @tf.function
    def serve_tf_examples_fn(serialized_tf_examples):
        """Returns the output to be used in the serving signature."""
        feature_spec = tf_transform_output.raw_feature_spec()
        feature_spec.pop(LABEL_KEY)
        parsed_features = tf.io.parse_example(serialized_tf_examples, feature_spec)

        transformed_features = model.tft_layer(parsed_features)

        outputs = model(transformed_features)
        return {"outputs": outputs}

    return serve_tf_examples_fn


def run_fn(fn_args):
    """Train the model based on given args.

    Args:
        fn_args: Holds args used to train the model as name/value pairs.
    """
    tf_transform_output = tft.TFTransformOutput(fn_args.transform_output)

    best_hyperparameters = fn_args.hyperparameters
    hyperparameters = best_hyperparameters["values"]

    train_dataset = input_fn(fn_args.train_files, tf_transform_output, 64)
    eval_dataset = input_fn(fn_args.eval_files, tf_transform_output, 64)

    model = get_model(hyperparameters)

    log_dir = os.path.join(os.path.dirname(fn_args.serving_model_dir), "logs")
    tensorboard_callback = tf.keras.callbacks.TensorBoard(
        log_dir=log_dir, update_freq="batch"
    )

    early_stop = tf.keras.callbacks.EarlyStopping(
        monitor="val_binary_accuracy",
        patience=2,
        mode="max",
        restore_best_weights=True,
    )

    model.fit(
        train_dataset,
        steps_per_epoch=fn_args.train_steps,
        validation_data=eval_dataset,
        validation_steps=fn_args.eval_steps,
        callbacks=[tensorboard_callback, early_stop],
        epochs=10,
    )

    signatures = {
        "serving_default": get_serve_tf_examples_fn(
            model, tf_transform_output
        ).get_concrete_function(
            tf.TensorSpec(shape=[None], dtype=tf.string, name="examples")
        ),
    }
    model.save(fn_args.serving_model_dir, save_format="tf", signatures=signatures)
