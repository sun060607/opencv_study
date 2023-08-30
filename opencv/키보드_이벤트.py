import cv2
import numpy as np

switch_case = {
    ord('a'):'a키 입력',
    ord('b'):'b키 입력',
    0x41: 'A키 입력',
    int('0x41',16) : 'B키 입력'
}

img = np.zeros(shape=(512,512,3),dtype=np.uint8)+255
cv2.namedWindow('Keybord Event')
cv2.imshow('Keybord Event',img)
while True:
    key = cv2.waitKey(100)
    if key==27:
        break
    try:
        result=switch_case[key]
        print(result)
    except KeyError:
        result=-1
cv2.destroyAllWindows()