# **Crowd Counting with YOLO Model**

This [project](https://github.com/nasim-raj-laskar/pyth-30/blob/main/Python%2030/Crowd-Counting/main.py) demonstrates a crowd counting system that uses the YOLO (You Only Look Once) [model](https://github.com/nasim-raj-laskar/pyth-30/blob/main/Python%2030/Crowd-Counting/yolo11s.pt) to detect and track people in video frames. The system identifies people entering and exiting a specific area and displays this information in real-time. The model processes each frame of a [video](https://github.com/nasim-raj-laskar/pyth-30/blob/main/Python%2030/Crowd-Counting/people1.avi), drawing bounding boxes around detected individuals and using unique tracking IDs to distinguish them. The flow of people is visualized with colored markers, and the number of people entering and exiting the monitored area is displayed on the frame.

## **Tools**
- **YOLO (You Only Look Once)**: Pre-trained object detection model used to detect people in the video.
- **OpenCV**: Used for video capture, frame processing, and displaying results.
- **cvzone**: A Python library to overlay text and graphics on frames.
- **NumPy**: Used for numerical operations on frames.
- **Python**: Programming language used for the implementation of the project.
 ## Output Visualization

![Demo Video](https://github.com/nasim-raj-laskar/pyth-30/blob/main/Python%2030/Crowd-Counting/output.gif)
