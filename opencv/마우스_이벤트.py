import cv2
import numpy as np
def onMouse(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDOWN:
        print('마우스 윈쪽 버튼 누리기')
    elif event == cv2.EVENT_RBUTTONDOWN:
        print('마우스 오른쪽 버튼 누리기')
    elif event == cv2.EVENT_LBUTTONUP:
        print('마우스 윈쪽 버튼 떼기')
    elif event == cv2.EVENT_RBUTTONUP:
        print('마우스 오른쪽 버튼 뗴기')
    print('마우스 이벤트 발생','x:',x,'y:',y)
img = np.zeros(shape=(512,512,3),dtype=np.uint8)+255
cv2.imshow('Mouse Events1',img)
cv2.imshow('Mouse Events2',img)
cv2.setMouseCallback('Mouse Events1',onMouse)
cv2.waitKey()
cv2.destroyAllWindows()