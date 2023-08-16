import cv2

image=cv2.imread('data/img.png') #사진 파일 로드
cv2.imshow('Image',image) #이미지 출력
cv2.waitKey(0)
cv2.destroyAllWindows()