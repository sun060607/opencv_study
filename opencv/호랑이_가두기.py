import cv2

image=cv2.imread('data/tiger.jpg') #사진 파일 로드
x1,x2 = 160,270
y1,y2 = 130,260
cv2.rectangle(image,(x1,y1),(x2,y2),(0,0,255),10)
pt1 = 160,130
pt2 = 270,260
         #캔버스, 시작점, 끝점, BGR, 선굵기
cv2.line(image,pt1,pt2,(255,0,0),10)
imgRect = (x1,y1,x2-x1,y2-y1)
retval, rpt1,rpt2 = cv2.clipLine(imgRect,pt1,pt2)
if retval:
    cv2.circle(image,rpt1,radius=5,color=(0,255,0),thickness=-1)
    cv2.circle(image,rpt2,radius=5,color=(0,255,0),thickness=-1)
cv2.imshow('Image',image) #이미지 출력
cv2.waitKey(0)
cv2.destroyAllWindows()