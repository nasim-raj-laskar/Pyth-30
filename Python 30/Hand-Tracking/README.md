# Hand Tracking
---
## Project Overview

This project utilizes OpenCV and MediaPipe to perform real-time hand gesture recognition using a webcam. By leveraging the powerful hand tracking model provided by MediaPipe, the script is capable of detecting hands in the webcam feed and extracting key landmarks from them. These landmarks are essentially specific points on the hand, such as the tips of the fingers, the wrist, and other important regions, which can be used to understand the hand's position and movements.

In its current form, the project captures video frames, detects hand landmarks, and displays the hand landmarks in the form of dots connected by lines on the webcam feed. The FPS (Frames Per Second) is also calculated and displayed on the screen to monitor the real-time performance of the hand detection process.

## Requirements

- Python 3.x
- OpenCV
- MediaPipe
The project serves as a foundational system for any of these applications, where the next steps would be to analyze the landmark positions for specific movements or gestures and integrate the system into various interactive platforms.

## Key Components:
- **Real-time Hand Detection**: The system uses the webcam to detect hand gestures in real-time, which is crucial for applications requiring instant feedback.
- **Landmark Detection**: The system identifies specific points on the hand, including the wrist, fingers, and joints. These landmarks are valuable for gesture recognition, tracking hand movement, or interpreting specific actions.
- **FPS Monitoring**: The script calculates and displays the frames per second (FPS) to ensure smooth and responsive interaction. This also helps in understanding the system's performance in different environments.

