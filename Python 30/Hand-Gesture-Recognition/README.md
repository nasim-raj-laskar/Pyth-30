# Hand Gesture Recognition with CNN

## Description

This project is designed to recognize hand gestures using Convolutional Neural Networks (CNNs). The model is trained using a dataset of hand gestures, classified into 7 categories: "L", "background", "four", "three", "thumbsup", "two", and "up". The model uses multiple convolutional and pooling layers to learn hierarchical features, followed by fully connected layers to classify the gestures. After training, the model is saved in both JSON and H5 formats, enabling it to be reloaded for inference. The test phase evaluates the model's performance and visualizes the results of predictions for unseen hand gesture images.

## Tools Used
- **Python**: The primary programming language used for this project.
- **Keras & TensorFlow**: The deep learning libraries used to build, train, and evaluate the CNN model.
- **Matplotlib**: Used for visualizing the predicted results.
- **NumPy**: For numerical operations and data manipulation.
- **ImageDataGenerator**: For real-time data augmentation during model training.
- **OpenCV**: Used for loading and processing images for predictions.
- **EarlyStopping & ModelCheckpoint**: Callbacks to prevent overfitting and save the best model during training.


