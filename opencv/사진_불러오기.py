import cv2
import numpy as np

image=cv2.imread('data/img.png') 
text = 'OpenCv'
org = (600,50)
font = cv2.FONT_HERSHEY_SIMPLEX
        #캔버스, 글자, 시작점, 폰트, 글자크기, (색), 선굵기
cv2.putText(image, text, org, font, 1, (0,0,255),4)
size, baseLine= cv2.getTextSize(text,font,1,2)
cv2.imshow('Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()