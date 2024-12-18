# Drowsiness Detection System

This [project](https://github.com/nasim-raj-laskar/pyth-30/blob/main/Python%2030/Drowsiness-detection/main.py) implements a real-time drowsiness detection system using computer vision techniques. It monitors eye aspect ratio (EAR) and head movement angles to detect signs of drowsiness. When drowsiness is detected, an alarm is triggered to alert the user. The system leverages a [pre-trained](https://github.com/nasim-raj-laskar/pyth-30/blob/main/Python%2030/Drowsiness-detection/shape_predictor_68_face_landmarks.dat) facial landmark detector and dynamically adjusts thresholds for more accurate detection under varying conditions.

## Tools Used
- **OpenCV**: For video capture and image processing.
- **dlib**: For face detection and landmark prediction.
- **imutils**: For utility functions in image processing.
- **SciPy**: For calculating Euclidean distances.
- **NumPy**: For numerical operations and calculations.
- **winsound**: For generating audio alerts.
