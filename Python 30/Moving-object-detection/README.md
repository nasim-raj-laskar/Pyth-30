
# Motion Detection with OpenCV

This [project](/Moving-object-detection/project.py)
 showcases a real-time motion detection system using OpenCV. It captures video from a connected camera, detects motion based on frame differences, and highlights the regions of detected movement. This system is versatile and can be used for applications like security monitoring, activity detection, and more.

The workflow involves capturing live video feed, converting frames to grayscale, and applying Gaussian blurring for noise reduction. The script computes the difference between the first frame and subsequent frames to detect changes. Detected motion is highlighted with bounding boxes, and a message is displayed on the video feed to indicate activity.



## Tools Used

- **Python**: Core programming language for implementing the motion detection logic.
- **OpenCV**: For video capture, frame processing, and contour detection.
- **Imutils**: Simplifies image processing tasks like resizing and contour manipulation.

