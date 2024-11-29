import cv2
import dlib
import imutils
import winsound
from scipy.spatial import distance as dist
from imutils import face_utils
import numpy as np

frequency = 2500  
duration = 1000  
EAR_THRESH = 0.3  
EAR_FRAMES = 48   


shape_predictor = 'Drowsiness-detection/shape_predictor_68_face_landmarks.dat'
cam = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(shape_predictor)

# coord left and right eye
(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']

def eyeAspectRatio(eye):
    #eye aspect ratio (EAR) to detect eye closure
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

count = 0
frame_counter = 0

while True:
    _, frame = cam.read()
    frame = imutils.resize(frame, width=800)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    rects = detector(gray, 0)

    for rect in rects:
        shape = predictor(gray, rect)
        shape = face_utils.shape_to_np(shape)

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        leftEAR = eyeAspectRatio(leftEye)
        rightEAR = eyeAspectRatio(rightEye)

        ear = (leftEAR + rightEAR) / 2.0

        if frame_counter % 10 == 0:
            left_eye_center = np.mean(leftEye, axis=0)
            right_eye_center = np.mean(rightEye, axis=0)
            nose_center = shape[30]  
            dx = right_eye_center[0] - left_eye_center[0]
            dy = right_eye_center[1] - left_eye_center[1]
            head_angle = np.arctan2(dy, dx) * 180 / np.pi
        else:
            head_angle = 0

        if abs(head_angle) > 10:  
            dynamic_threshold = EAR_THRESH + 0.05
        else:
            dynamic_threshold = EAR_THRESH

        #contours around the eyes
        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)
        cv2.drawContours(frame, [leftEyeHull], -1, (0, 0, 255), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 0, 255), 1)

        if ear < dynamic_threshold:
            count += 1
            if count >= EAR_FRAMES:
                cv2.putText(frame, "DROWSINESS DETECTED", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                winsound.Beep(frequency, duration)
        else:
            count = 0

    #dynamic threshold 
    cv2.putText(frame, f"Threshold: {dynamic_threshold:.2f}", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
    
    cv2.imshow("Drowsiness Detection", frame)
    key = cv2.waitKey(1) & 0xFF
    
    if key == ord("q"):
        break
    
    frame_counter += 1


cam.release()
cv2.destroyAllWindows()
