import numpy as np
import cv2
img = np.zeros(shape=(512,512,3),dtype=np.uint8)+255
text = 'OpenCv Programming'
org = (50,100)
font = cv2.FONT_HERSHEY_SIMPLEX
        #캔버스, 글자, 시작점, 폰트, 글자크기, (색), 선굵기
cv2.putText(img, text, org, font, 1, (255,0,0),2)
size, baseLine= cv2.getTextSize(text,font,1,2)
cv2.rectangle(img,org,(org[0]+size[0],org[1]-size[1]),(0,0,255))
cv2.circle(img,org,3,(0,255,0),2)
cv2.imshow('img',img)   
cv2.waitKey()
cv2.destroyAllWindows()