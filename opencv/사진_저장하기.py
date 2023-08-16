import cv2
image=cv2.imread('data/img.png')

cv2.imshow('Image',image)
#사용자 입력을 기다림
key=cv2.waitKey(0)
#'s'키를 누르면 이미지 저장
if key ==ord('s'):
    #print(ord('s')) 아스키코드 115
    cv2.imwrite('data/save_img.png',image)
    print("Image save successfully")
cv2.destroyAllWindows()