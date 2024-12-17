# **Leaf Disease Detection using CNN**

This [project](https://github.com/nasim-raj-laskar/pyth-30/blob/main/Python%2030/leaf-disease-detection/leaf-deetection%20(2).ipynb) uses a Convolutional Neural Network (CNN) built with Keras and TensorFlow to detect and classify plant leaf diseases from images. The model is trained on a dataset containing 38 different categories of leaf diseases and healthy leaves. The main goal is to identify the type of disease affecting the plant based on input images.

The architecture includes multiple convolutional, max-pooling, batch normalization, and dropout layers to improve model performance and prevent overfitting. The model outputs the predicted class and probability for any test image provided.

## **Tools Used**
- **Keras:** For building and training the CNN model.
- **TensorFlow:** Backend engine for computations.
- **ImageDataGenerator:** To preprocess and augment images for training.
- **Matplotlib & Plotly:** For visualizing training/validation performance and prediction results.
- **NumPy:** For numerical operations.

## **Output Visualization**
### 1. **Accuracy and Loss Graph**

![Accuracy Graph Example](https://github.com/nasim-raj-laskar/pyth-30/blob/main/Python%2030/leaf-disease-detection/img/metrics_graph(using%20plotly).png)

### 2. **Prediction Output**
A grid of test images is displayed with their predicted class and confidence probabilities.

![Prediction Visualization Example](https://github.com/nasim-raj-laskar/pyth-30/blob/main/Python%2030/leaf-disease-detection/img/1.png)


