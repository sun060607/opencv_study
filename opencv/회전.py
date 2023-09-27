import cv2
src=cv2.imread('./data/img.png',cv2.IMREAD_COLOR);
height, width, channel = src.shape
#높이,너비,채널 값을 저장해서 회전할 중심점을 설정
#                                  중심점,각도, 비율
matrix = cv2.getRotationMatrix2D((width/2,height/2),90,1)
#원본 이미지를 src애 M(아핀 맵 행렬)을 적용하고 출력 이미지 dsize로 변경
dst = cv2.warpAffine(src,matrix,(width,height))

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()