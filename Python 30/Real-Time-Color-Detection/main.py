import cv2
import time
from collections import deque

cap = cv2.VideoCapture(0)

color_queue = deque(maxlen=10)  
start_time = time.time()

#Mouse callback to detect color at click point
def get_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        hsv_pixel = hsv_frame[y, x]
        print(f"HSV at clicked point: {hsv_pixel}")

cv2.namedWindow('frame')
cv2.setMouseCallback('frame', get_color)

while True:

    _, frame = cap.read()
    height, width, _ = frame.shape
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cx, cy = int(width / 2), int(height / 2)

    pixel_center = hsv_frame[cy, cx]
    hue_value = pixel_center[0]

    if hue_value < 10 or hue_value > 160:
        color = "RED"
    elif 10 <= hue_value < 25:
        color = "ORANGE"
    elif 25 <= hue_value < 35:
        color = "YELLOW"
    elif 35 <= hue_value < 85:
        color = "GREEN"
    elif 85 <= hue_value < 125:
        color = "BLUE"
    elif 125 <= hue_value < 160:
        color = "VIOLET"
    else:
        color = "Undefined"

    color_queue.append(color)
    stable_color = max(set(color_queue), key=color_queue.count)

    pixel_center_bgr = frame[cy, cx]
    b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])

    #Display color and HSV/RGB 
    cv2.putText(frame, f"{stable_color} (Hue: {hue_value})", (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (b, g, r), 2)
    cv2.putText(frame, f"RGB: ({r}, {g}, {b})", (10, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (b, g, r), 2)

    #Draw center circle
    cv2.circle(frame, (cx, cy), 5, (0, 0, 0), 3)

    #Draw a bounding box 
    rect_size = 10
    cv2.rectangle(frame, (cx - rect_size, cy - rect_size), (cx + rect_size, cy + rect_size), (0, 255, 0), 2)

    #display FPS
    fps = int(1 / (time.time() - start_time))
    start_time = time.time()
    cv2.putText(frame, f"FPS: {fps}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("frame", frame)

    key = cv2.waitKey(1)
    if key == 27:  # ESC to exit
        break
    elif key == ord('s'):  # 's' to save frame
        cv2.imwrite("detected_frame.jpg", frame)

cap.release()
cv2.destroyAllWindows()
