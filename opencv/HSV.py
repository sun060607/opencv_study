import cv2
import numpy as np
src = cv2.imread('./data/tomato.jpg',cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(src,cv2.COLOR_BGR2HSV)

h, s, v = cv2.split(hsv)
cv2.imshow('h',h) #색상(Hue) 0~360 -> opencv에서 0~180
cv2.imshow('s',s) #채도(Saturation) 0~255 이미지 색상 깊이 -> opencv에서 0~255
cv2.imshow('v',v) #명도(Value) 0~255 색의 밝고 어두운 정도 -> opencv에서 0~255
cv2.waitKey()
cv2.destroyAllWindows()