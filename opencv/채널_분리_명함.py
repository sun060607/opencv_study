import cv2
import numpy as np
src = cv2.imread('./data/tomato.jpg',cv2.IMREAD_COLOR)
#oopencv BGR 순서 입니다
b, g, r = cv2.split(src)
b=src[:,:,0]
g=src[:,:,1]
r=src[:,:,2]
#분리된 채널들은 단일 채널이므로 흑백으로 표시
inverse = cv2.merge((r,g,b))
#빈이미지 생성
height , width,channel = src.shape
zero = np.zeros((height,width,1),dtype=np.uint8)
bgz=cv2.merge((zero,zero,r))

#cv2.imshow('b',b)
#cv2.imshow('g',g)
#cv2.imshow('r',r)
#cv2.imshow('inverse',inverse);
cv2.imshow('bgz',bgz)
cv2.waitKey()
cv2.destroyAllWindows()