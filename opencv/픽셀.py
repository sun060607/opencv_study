import cv2
src = cv2.imread('./data/tomato.jpg',cv2.IMREAD_COLOR)
print(src[300:400,500:600])
height , width,channel = src.shape
print(height)
print(width)
print('BGR ',src[300,500])
print('BGR B',src[500,500,0])
print('BGR G',src[500,500,1])
print('BGR R',src[500,500,2])
src[100:120,100:120] = (255,255,0)
cv2.imshow('updated image', src)
cv2.waitKey()
cv2.destroyAllWindows()