import numpy as np
import cv2
img = np.zeros(shape=(512,512,3),dtype=np.uint8)+255
x1,x2 = 100,400
y1,y2 = 100,400
cv2.rectangle(img,(x1,y1),(x2,y2),(0,0,255))
pt1 = 120,50
pt2 = 300,500
         #캔버스, 시작점, 끝점, BGR, 선굵기
cv2.line(img,pt1,pt2,(255,0,0),2)
imgRect = (x1,y1,x2-x1,y2-y1)
retval, rpt1,rpt2 = cv2.clipLine(imgRect,pt1,pt2)
if retval:
    cv2.circle(img,rpt1,radius=5,color=(0,255,0),thickness=-1)
    cv2.circle(img,rpt2,radius=5,color=(0,255,0),thickness=-1)
cv2.imshow('img',img) #이미지 출력
cv2.waitKey()
cv2.destroyAllWindows()