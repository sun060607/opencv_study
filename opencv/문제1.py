import cv2
cap = cv2.VideoCapture(0)
text = 'SMH'
org =(500,40)
font =cv2.FONT_HERSHEY_SIMPLEX
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    cv2.putText(frame,text,org,font,1, (0,0,255),3)
    cv2.imshow('Video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    if cv2.waitKey(1) & 0xFF == ord('s'):  # 's' 키를 누르면 이미지 저장
        cv2.imwrite('test_num.png', frame)
        print('Image saved successfully!')
cap.release()
cv2.waitKey()
cv2.destroyAllWindows()