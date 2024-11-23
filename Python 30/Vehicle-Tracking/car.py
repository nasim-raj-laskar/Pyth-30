import cv2 
import imutils

cascade_src='Vehicle-Tracking/cars.xml'
car_cascade=cv2.CascadeClassifier(cascade_src)


# cam = cv2.VideoCapture(0)  ## Uses webcam

sample_video='Vehicle-Tracking/sample1.mp4'  #uses sample video
cam=cv2.VideoCapture(sample_video)

while True:
    # _,img=cam.read()  ##frame reading for webcam
    ret,img=cam.read() #frame reading for sample video

    if not ret:
        print("End of video or error reading video.")
        break

    img=imutils.resize(img,width=500)
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    cars=car_cascade.detectMultiScale(gray,1.1,1)
    
    for(x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

    cv2.imshow("Frame",img)

    car_count = len(cars)
    print("--------------------------------------------------")
    print(f"North: {car_count}")
    if car_count>=8:
        print("North More Traffic,Please be on the RED Signal")
    else:
        print("no traffic")
    if cv2.waitKey(33)==27:
        break

cam.release()
cv2.destroyAllWindows()
