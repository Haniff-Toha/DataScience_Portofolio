// ---- Variables ----
let input = document.querySelector('input');
let button = document.querySelector('button');

let isModelLoaded = false;
let model;

var myVar;

// Function to show page after a delay
function myFunction() {
    myVar = setTimeout(showPage, 3000);
}

function showPage() {
    document.getElementById("loaderlabel").style.display = "none";
    document.getElementById("loader").style.display = "none";       
    document.getElementById("mainAPP").style.display = "block";
}

// Function to detect WebGL context
function detectWebGLContext() {
    var canvas = document.createElement("canvas");
    var gl = canvas.getContext("webgl") || canvas.getContext("experimental-webgl");
    if (gl && gl instanceof WebGLRenderingContext) {
        console.log("Congratulations! Your browser supports WebGL.");
        init();
    } else {
        alert("Failed to get WebGL context. Your browser or device may not support WebGL.");
    }
}

detectWebGLContext();

// Function to get the image input
function getInput() {
    const inputElement = document.getElementById('input');
    return inputElement.files[0];
}

// Function to make predictions
async function predict(image) {
    const img = document.createElement('img');
    img.src = URL.createObjectURL(image);

    return new Promise((resolve) => {
        img.onload = async () => {
            const tensorImg = tf.browser.fromPixels(img).toFloat();
            const resizedImg = tf.image.resizeBilinear(tensorImg, [224, 224]).expandDims(0);
            const prediction = model.predict(resizedImg);
            const scores = prediction.dataSync();
            const classIndex = scores.indexOf(Math.max(...scores));
            const classLabels = ['battery', 'biological', 'brown-glass', 'cardboard', 'clothes', 
                                 'green-glass', 'paper', 'plastic', 'shoes', 'trash'];
            resolve(classLabels[classIndex]);
        };
    });
}

// Function to handle image selection
function handleImageSelection(event) {
    const image = event.target.files[0];
    if (!image) {
        return;
    }

    // Display the chosen image
    const imgElement = document.getElementById('selectedImage');
    imgElement.src = URL.createObjectURL(image);
    imgElement.style.display = 'block';
}

// Function to handle button click
async function onClick() {
    if (!isModelLoaded) {
        alert('Model not loaded yet');
        return;
    }

    const image = getInput();
    if (!image) {
        alert("Image Can't be null");
        return;
    }

    const result = await predict(image);
    alert('Predicted class: ' + result);
}

// Initialize the model
async function init() {
    // Load TensorFlow.js model
    model = await tf.loadLayersModel('http://127.0.0.1:5500/final_submission_MH/Submission_MH/tfjs_model/model.json');
    isModelLoaded = true;

    console.log(model.summary()); 
    console.log('Model & Metadata Loaded Successfully');
}

// Add event listener to handle file input change
input.addEventListener('change', handleImageSelection);
button.addEventListener('click', onClick);
