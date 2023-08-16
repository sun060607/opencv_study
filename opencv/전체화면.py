import numpy as np
import cv2

image=np.zeros((200,400),np.uint8)
image.fill(255)
screen_width=1920 #현재 모니터 해상도
screen_height=1080
image=cv2.resize(image,(screen_width,screen_height))

cv2.namedWindow('Fullscreen Image',cv2.WND_PROP_FULLSCREEN) # 이름이 동일해야 작동이 됨
cv2.setWindowProperty('Fullscreen Image',cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)
cv2.imshow('Fullscreen Image',image)
cv2.waitKey(0)
cv2.destroyAllWindows()