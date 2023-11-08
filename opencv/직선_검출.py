import cv2
import numpy as np
src = cv2.imread('./data/road.jpg')
dst = src.copy()
gray=cv2.cvtColor(src,cv2.COLOR_RGB2GRAY)
canny = cv2.Canny(gray,5000,1500,apertureSize=5,L2gradient=True)
#cv2.HoughLines(검출이밎, 거리, 각도, 임계값,거리약수, 최소 각도, 최대 각도)
#를 이용하여 직선 검출을 진행합니다
#허프 변환 함수는 시작점과 도착점을 알려주는 함수가 아닌 가장 직선일 가능성이 높은 거리와
#각도를 검출합니다
lines=cv2.HoughLines(canny,0.8,np.pi/180,150,srn=100,stn=200,min_theta=0,max_theta=np.pi)

for i in lines:
    rho, theta = i[0][0], i[0][1]
    a, b = np.cos(theta), np.sin(theta)
    x0,y0=a*rho,b*rho
    scale = src.shape[0]+src.shape[1]

    x1=int(x0+scale * -b)
    y1=int(y0+scale * a)
    x2=int(x0+scale * -b)
    y2=int(y0+scale * a)

    x0, y0 = int(x0),int(y0)
    cv2.line(dst,(x1,y1),(x2,y2),(0,0,255),2)
    cv2.circle(dst,(x0,y0),3,(255,0,0),5,cv2.FILLED)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()