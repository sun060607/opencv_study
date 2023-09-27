import cv2
image= cv2.imread('../data/img.png') #이미지 파일 로드
text = 'OpenCV'
org =(600,50)
font =cv2.FONT_HERSHEY_SIMPLEX
        #캔버스  ,내용, 시작점, 폰트, 크기 (색깔) 선굵기
cv2.putText(image,text,org,font,1, (0,0,255),3)                   #글자
cv2.imshow('img',image)
cv2.waitKey()
cv2.destroyAllWindows()