import cv2
src=cv2.imread('./data/img.png',cv2.IMREAD_COLOR);
dst = src[100:600,200:700].copy()
#opencv 이미지는 numpy배열 형식과 동일 합니다
cv2.imshow('src',src)
cv2.imshow('dst',dst)
cv2.waitKey()
cv2.destroyAllWindows()