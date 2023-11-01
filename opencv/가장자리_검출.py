import cv2
#가장자리는 픽셀의 밝기가 급격하게 변하는 부분
src = cv2.imread('./data/fox.png')
gray = cv2.cvtColor(src,cv2.IMREAD_COLOR)
#1.입력 이미지(src) 2.출력 이미지 정밀도(ddepth) 3.방향 미분 차수(ksize)
sobel = cv2.Sobel(gray,cv2.CV_8U,1,0,3)

laplacian = cv2.Laplacian(gray,cv2.CV_8U,ksize=3)

canny = cv2.Canny(src,100,255)
cv2.imshow('sobel',sobel)
cv2.imshow('laplacian',laplacian)
cv2.waitKey(0)
cv2.destroyAllWindows()