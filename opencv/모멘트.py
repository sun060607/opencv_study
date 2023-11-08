import cv2
src = cv2.imread('./data/convex.png')

dst = src.copy()
gray=cv2.cvtColor(src,cv2.COLOR_RGB2GRAY)
ret, binary = cv2.threshold(gray,150,255,cv2.THRESH_BINARY_INV)

contours, hierarchy = cv2.findContours(binary,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)

for i in contours:
#cv2.moments()를 활용해 윤곽선이에서 모멘트를 계산합니다
#cv2.moments(배열, 이진화 이미지)을 의미한다

    M = cv2.moments(i)
    cX=int(M['m10']/M['m00'])
    cY=int(M['m01']/M['m00'])

    cv2.circle(dst,(cX,cY),3,(255,0,0),-1)
    cv2.drawContours(dst,[i],0,(0,0,255),2)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()