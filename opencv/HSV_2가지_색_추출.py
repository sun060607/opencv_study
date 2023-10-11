import cv2
src = cv2.imread('./data/tomato.jpg',cv2.IMREAD_COLOR)
hsv = cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
lower_orange = (8,50,50) #주황색 범위
upper_orange =(20,255,255)
lower_blue = (100,50,50)
upper_blue = (140,255,255)
mask_orange = cv2.inRange(hsv,lower_orange,upper_orange)
mask_blue = cv2.inRange(hsv,lower_blue,upper_blue)
mask_combined = cv2.bitwise_or(mask_blue,mask_orange)
orange_and_blue = cv2.bitwise_and(src,src,mask = mask_combined)
cv2.imshow('orange and blue',orange_and_blue)
cv2.waitKey()
cv2.destroyAllWindows()