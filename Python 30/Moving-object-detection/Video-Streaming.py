import cv2
vs=cv2.VideoCapture(0)
while True:
    _,img=vs.read()
    cv2.imshow("VideoStreaming",img)
    Key=cv2.waitKey(1)
    print(Key)
    if Key==ord("q"):
        break
vs.release()
cv2.destroyAllWindows()