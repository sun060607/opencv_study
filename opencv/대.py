import cv2
src=cv2.imread('./data/img.png',cv2.IMREAD_COLOR);
dst = cv2.flip(src,0)
#flipCode < 0 xy축 대칭 상하좌우 대칭
#flipCode = 0 xy축 대칭 상하 대칭
#flipCode > 0 xy축 대칭 좌우 대칭
cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()