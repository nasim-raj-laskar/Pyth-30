# Facial Recognition

This project involves the creation of a facial recognition system using OpenCV. It consists of two main components: 

1. **Data Creation**: A [script](https://github.com/nasim-raj-laskar/pyth-30/blob/main/Python%2030/Face-Recognition/create_data.py) that captures face images from a webcam and stores them in a dataset for training the facial recognition model.
2. **Recognition**: A second [script](https://github.com/nasim-raj-laskar/pyth-30/blob/main/Python%2030/Face-Recognition/face_recog.py) that uses the trained [model](https://github.com/nasim-raj-laskar/pyth-30/blob/main/Python%2030/Face-Recognition/haarcascade_frontalface_default.xml) to recognize and identify faces in real-time from webcam input.

The system uses Haar cascades for face detection and the LBPH (Local Binary Pattern Histogram) algorithm for facial recognition. This project allows for real-time identification, with confidence scoring indicating how accurately the system recognizes a face. If an unknown person is detected, the system records the image for further review.

## Tools Used
- **Python**: Programming language used for implementing the system.
- **OpenCV**: Library for computer vision, used for face detection and recognition.
- **NumPy**: Library used for array manipulation and handling training data.
- **OS**: Module used for file management and creating necessary directories.
