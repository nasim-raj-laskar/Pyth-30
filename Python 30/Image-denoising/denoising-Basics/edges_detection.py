import cv2
#import numpy as np
#from matplotlib import pyplot as plt

img=cv2.imread("Images/nosy.png",0)

edges=cv2.Canny(img,100,200 )

cv2.imshow("original",img)
cv2.imshow("edgyy image",edges)

cv2.waitKey(0)
cv2.destroyAllWindows()