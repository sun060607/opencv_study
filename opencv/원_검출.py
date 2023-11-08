import cv2
import numpy as np
src = cv2.imread('./data/colorball.jpg')
dst = src.copy()
gray=cv2.cvtColor(src,cv2.COLOR_RGB2GRAY)
#cv2.HoughCircles(검출 이미지, 검출 방법, 해상도 비유르, 최소거리, 캐니 엣지 임계값,중심 임계값, 최소 반지름, 초대 반지름)을 이용하여 원 검출을 진행 합니다
circles=cv2.HoughCircles(gray,cv2.HOUGH_GRADIENT,1,100,param1=250,param2=10,minRadius=80,maxRadius=120)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0]:
        center=(i[0],i[1])
        radius = i[2]
        cv2.circle(dst,center,radius,(255,255,255),5)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()