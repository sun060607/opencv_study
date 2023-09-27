import cv2
import numpy as np
image=cv2.imread('data/img.png') 
cx = 100
cy = 100
while True:
    cv2.circle(image,(cx,cy),radius=50,color=(0,0,255),thickness=-1)
    if cv2.waitKey(10) == ord('a'):
        if(cx >50):
            cx = cx-3
        image=cv2.imread('data/img.png') 
    elif cv2.waitKey(10) == ord('d'):
        if(cx <718):
            cx = cx+3
        image=cv2.imread('data/img.png') 
    elif cv2.waitKey(10) == ord('s'):
        if(cy <526):
            cy = cy+3
        image=cv2.imread('data/img.png') 
    elif cv2.waitKey(10) == ord('w'):
        if(cy >50):
            cy = cy-3
        image=cv2.imread('data/img.png') 
    cv2.imshow('Image',image)
cv2.destroyAllWindows()