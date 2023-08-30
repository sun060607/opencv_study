import numpy as np
import cv2
img = np.zeros(shape=(512,512,3),dtype=np.uint8)+255
pts1 = np.array([[100,100],[200,100],[200,200],[100,200]])
pts2 = np.array([[300,200],[400,100],[400,200]])

cv2.polylines(img,[pts1,pts2],isClosed=True,color=(255,0,0))
cv2.imshow('img',img)
cv2.waitKey()
cv2.destroyAllWindows()