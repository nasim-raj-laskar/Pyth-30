import cv2
import imutils
img=cv2.imread("Moving-object-detection/picture.jpg")
resizeImg=imutils.resize(img,width=500)
GassianImg=cv2.GaussianBlur(resizeImg,(11,11),50)
GassianImg1=cv2.GaussianBlur(resizeImg,(41,41),0)
GassianImg2=cv2.GaussianBlur(resizeImg,(111,111),0)
cv2.imshow("resized",resizeImg)
cv2.imshow("Gaussian blur",GassianImg)
cv2.imshow("Gaussian blur 1",GassianImg1)
cv2.imshow("Gaussian blur 2",GassianImg2)
cv2.waitKey(0)
cv2.destroyAllWindows()
