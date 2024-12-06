import cv2
import numpy as np
from ultralytics import YOLO
import cvzone

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        point = [x, y]
        print(point)

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

model = YOLO("Crowd-Counting/yolo11s.pt")
names = model.model.names

cap = cv2.VideoCapture('Crowd-Counting/people1.avi')
count = 0
cy1 = 261
cy2 = 286
offset = 8
inp = {}
enter = []
exp = {}
exitp = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    count += 1
    if count % 3 != 0:
        continue

    frame = cv2.resize(frame, (1020, 600))
    
    results = model.track(frame, persist=True, classes=0)

    if results[0].boxes is not None and results[0].boxes.id is not None:
        # boxes
        boxes = results[0].boxes.xyxy.int().cpu().tolist() 
        class_ids = results[0].boxes.cls.int().cpu().tolist()  
        track_ids = results[0].boxes.id.int().cpu().tolist()  
        confidences = results[0].boxes.conf.cpu().tolist() 
        
        for box, class_id, track_id, conf in zip(boxes, class_ids, track_ids, confidences):
            c = names[class_id]
            x1, y1, x2, y2 = box
            cx = int(x1 + x2) // 2
            cy = int(y1 + y2) // 2

            # Person entering
            if cy1 < (cy + offset) and cy1 > (cy - offset):
                inp[track_id] = (cx, cy)
            if track_id in inp:
                if cy2 < (cy + offset) and cy2 > (cy - offset):
                    cv2.circle(frame, (cx, cy), 4, (0, 255, 0), -1)  # Green color for entry
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)  
                    cvzone.putTextRect(frame, f'Track ID: {track_id}', (x1, y2), 1, 1, (0, 255, 0), 2)
                    cvzone.putTextRect(frame, f'{c}', (x1, y1), 1, 1, (0, 255, 0), 2)
                    if track_id not in enter:
                        enter.append(track_id)

            # Person exiting
            if cy2 < (cy + offset) and cy2 > (cy - offset):
                exp[track_id] = (cx, cy)
            if track_id in exp:
                if cy1 < (cy + offset) and cy1 > (cy - offset):
                    cv2.circle(frame, (cx, cy), 4, (0, 0, 255), -1)  # Red color for exit
                    cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)  
                    cvzone.putTextRect(frame, f'Track ID: {track_id}', (x1, y2), 1, 1, (0, 0, 255), 2)
                    cvzone.putTextRect(frame, f'{c}', (x1, y1), 1, 1, (0, 0, 255), 2)
                    if track_id not in exitp:
                        exitp.append(track_id)

    cv2.line(frame, (440, 286), (1018, 286), (0, 0, 255), 2)  #Red line for exit
    cv2.line(frame, (438, 261), (1018, 261), (255, 0, 255), 2)  #Purple line for entry

    
    enter_count = len(enter)
    exit_count = len(exitp)
    
    cvzone.putTextRect(frame, f'Persons Entered: {enter_count}', (50, 60), 2, 2, (0, 255, 255), 2)
    cvzone.putTextRect(frame, f'Persons Exited: {exit_count}', (50, 100), 2, 2, (255, 255, 0), 2)

    cv2.imshow("RGB", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
