import numpy as np
import cv2
src = cv2.imread('./data/fox.png')
number1 = np.ones_like(src)*127 #회색 이미지(127,127,127)
number2 = np.ones_like(src)*2 #검정 이미지(2,2,2)
add = cv2.add(src,number1) #덧셈
#예시) 여러장 이미지 겹치기, 고해상도
sub = cv2.subtract(src,number1) #뺄셈
#예시) 배경제거, 움직임 감지
mul = cv2.multiply(src,number2) #곱셈
#예시) 명함 조절, 색상채도조절
div = cv2.divide(src,number2) #나눗셈
#예시) 노이즈를 줄이기 위해 사용
src = np.concatenate((src,src,src,src),axis=1)
number = np.concatenate((number1,number1,number2,number2), axis=1)
dst = np.concatenate((add,sub,mul,div),axis=1)
result = np.concatenate((src,number,dst),axis=0)
cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()