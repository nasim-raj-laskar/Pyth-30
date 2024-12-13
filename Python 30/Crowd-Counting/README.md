# **Crowd Counting with YOLO Model**

## **Description**
This project demonstrates a crowd counting system that uses the YOLO (You Only Look Once) model to detect and track people in video frames. The system identifies people entering and exiting a specific area and displays this information in real-time. The model processes each frame of a video, drawing bounding boxes around detected individuals and using unique tracking IDs to distinguish them. The flow of people is visualized with colored markers, and the number of people entering and exiting the monitored area is displayed on the frame.

## **Tools**
- **YOLO (You Only Look Once)**: Pre-trained object detection model used to detect people in the video.
- **OpenCV**: Used for video capture, frame processing, and displaying results.
- **cvzone**: A Python library to overlay text and graphics on frames.
- **NumPy**: Used for numerical operations on frames.
- **Python**: Programming language used for the implementation of the project.
