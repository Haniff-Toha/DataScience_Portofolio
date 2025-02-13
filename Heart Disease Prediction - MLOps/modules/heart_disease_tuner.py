"""Tuner module."""

import tensorflow as tf
import tensorflow_transform as tft
from kerastuner.tuners import RandomSearch
from tfx.components.tuner.component import TunerFnResult
from tfx.components.trainer.fn_args_utils import FnArgs

from heart_disease_transform import (
    CATEGORICAL_FEATURES,
    LABEL_KEY,
    NUMERICAL_FEATURES,
    transformed_name,
)

NUM_EPOCHS = 5


def gzip_reader_fn(filenames):
    """Load compressed data."""
    return tf.data.TFRecordDataset(filenames, compression_type="GZIP")


def input_fn(file_pattern, tf_transform_output, num_epoch, batch_size=64):
    """Generate a dataset for training or evaluation.

    Args:
        file_pattern: Input tfrecord file pattern.
        tf_transform_output: A TFTransformOutput.
        num_epoch: Number of epochs.
        batch_size: Batch size.

    Returns:
        A dataset.
    """
    feature_spec = tf_transform_output.transformed_feature_spec().copy()

    dataset = tf.data.experimental.make_batched_features_dataset(
        file_pattern=file_pattern,
        batch_size=batch_size,
        features=feature_spec,
        reader=gzip_reader_fn,
        label_key=transformed_name(LABEL_KEY),
        num_epochs=num_epoch,
    )
    return dataset


def build_tuner_model(hyperparameters):
    """Build an NN model with tunable hyperparameters.

    Args:
        hyperparameters: A dictionary of hyperparameters.

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
    x = tf.keras.layers.Dense(hyperparameters.Choice("dense_units1", [256, 512]), activation="relu")(concatenate)
    x = tf.keras.layers.Dropout(hyperparameters.Choice("dropout_rate1", [0.2, 0.3, 0.5]))(x)
    x = tf.keras.layers.Dense(hyperparameters.Choice("dense_units2", [64, 128]), activation="relu")(x)
    x = tf.keras.layers.Dense(hyperparameters.Choice("dense_units3", [16, 32]), activation="relu")(x)
    x = tf.keras.layers.Dropout(hyperparameters.Choice("dropout_rate2", [0.2, 0.3, 0.5]))(x)
    outputs = tf.keras.layers.Dense(1, activation="sigmoid")(x)

    model = tf.keras.models.Model(inputs=input_features, outputs=outputs)
    model.compile(
        optimizer=tf.keras.optimizers.Adam(learning_rate=hyperparameters.Choice("lr", [0.001, 0.0001, 0.00001])),
        loss="binary_crossentropy",
        metrics=[tf.keras.metrics.BinaryAccuracy()],
    )
    return model


def tuner_fn(fn_args: FnArgs) -> TunerFnResult:
    """Tuner function for TFX pipeline.

    Args:
        fn_args: Holds args used to tune the model.

    Returns:
        A TunerFnResult.
    """
    tf_transform_output = tft.TFTransformOutput(fn_args.transform_graph_path)

    train_dataset = input_fn(fn_args.train_files, tf_transform_output, NUM_EPOCHS, 64)
    eval_dataset = input_fn(fn_args.eval_files, tf_transform_output, NUM_EPOCHS, 64)

    tuner = RandomSearch(
        build_tuner_model,
        objective="val_binary_accuracy",
        max_trials=5,
        executions_per_trial=1,
        directory=fn_args.working_dir,
        project_name="classification_tuning",
    )

    early_stop = tf.keras.callbacks.EarlyStopping(
        monitor="val_binary_accuracy",
        patience=3,
        mode="max",
        restore_best_weights=True,
    )

    fit_kwargs = {
        "x": train_dataset,
        "validation_data": eval_dataset,
        "epochs": NUM_EPOCHS,
        "callbacks": [early_stop],
    }

    return TunerFnResult(tuner=tuner, fit_kwargs=fit_kwargs)
