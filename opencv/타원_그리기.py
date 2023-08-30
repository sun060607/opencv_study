import numpy as np
import cv2
img = np.zeros(shape=(512,512,3),dtype=np.uint8)+255
ptCenter=img.shape[0]//2, img.shape[1]//2
size = 200,100
cv2.ellipse(img,ptCenter,size,0,0,360,(255,0,0))
cv2.ellipse(img,ptCenter,size,90,0,360,(0,0,255))

box = (ptCenter,size,0)
cv2.ellipse(img,box,(255,0,0),5)
box = (ptCenter,size,90)
cv2.ellipse(img,box,(0,0,255),5)
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()