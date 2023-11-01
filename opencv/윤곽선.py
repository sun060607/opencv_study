import cv2
src = cv2.imread('./data/contours.png')
#영상이나 이미지의 윤곽선(컨투어)을 검출
#예시) 자동차 번호판 검출, 지도 및 지형분석, 얼굴 인식
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)
binary = cv2.bitwise_not(binary)

contours, hierarchy=cv2.findContours(binary,cv2.RETR_CCOMP,cv2.CHAIN_APPROX_NONE)

for i in range(len(contours)):
    cv2.drawContours(src,[contours[i]],0,(0,0,255),2)
    cv2.putText(src,str(i),tuple(contours[i][0][0]),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),1)

    cv2.imshow('src',src)
    cv2.waitKey(0)
cv2.destroyAllWindows()
