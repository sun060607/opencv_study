import cv2
src=cv2.imread('./data/img.png',cv2.IMREAD_COLOR);
#이미지 변경 방법1 = 절대 크기로 변경
dst = cv2.resize(src,dsize=(640,480),interpolation=cv2.INTER_LINEAR)
#이미지 변경 방법2 = 비율에 맞게 상대 크기로 변경
dst2 = cv2.resize(src,dsize=(0,0),fx=0.3,fy=0.7,interpolation=cv2.INTER_LINEAR)
#dst2 = cv2.resize(src,절대크기,상대크기(fx),상대크기(y),보간법)

cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.imshow('dst2',dst2)
cv2.waitKey()
cv2.destroyAllWindows()