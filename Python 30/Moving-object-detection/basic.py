import cv2
import imutils
img=cv2.imread("Moving-object-detection/picture.jpg")
resizeImg=imutils.resize(img,width=100)
cv2.imshow("Original",img)
cv2.imshow("Resize.jpg",resizeImg)
cv2.waitKey(0)
cv2.destroyAllWindows()