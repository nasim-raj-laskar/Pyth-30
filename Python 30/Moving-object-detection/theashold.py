import cv2
import imutils
img=cv2.imread("Moving-object-detection/picture.jpg")
rimg=imutils.resize(img,width=500)
grayImg=cv2.cvtColor(rimg,cv2.COLOR_BGR2GRAY)
thresholdImg=cv2.threshold(grayImg,180,180,cv2.THRESH_BINARY)[1]
cv2.imshow("original",rimg)
cv2.imshow("Threshold.jpg",thresholdImg)
cv2.waitKey(0)
cv2.destroyAllWindows()