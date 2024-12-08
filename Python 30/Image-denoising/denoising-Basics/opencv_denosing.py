import cv2
import numpy as np
#from matplotlib import pyplot as plt

img=cv2.imread("Images/nosy.png",1)
kernel=np.ones((5,5),np.float32)/25
gaussian_blur=cv2.GaussianBlur(img, (5,5), 0)
medain_blur=cv2.medianBlur(img, 5)
bilateral_blur=cv2.bilateralFilter(img, 9, 75, 75)

filt_2D=cv2.filter2D(img,-1,kernel)
blur=cv2.blur(img,(5,5))

cv2.imshow("Original",img)
cv2.imshow("medain",medain_blur)
cv2.imshow("bialateral_blur",bilateral_blur)

cv2.waitKey(0)
cv2.destroyAllWindows()