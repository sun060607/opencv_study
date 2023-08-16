import cv2
#비디오 캡쳐 객체 생성
cap = cv2.VideoCapture('data/video.avi')
while cap.isOpened():#동영상이 남아있을때 까지
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow('Video',frame) #비디오 출력
    #'q'를 눌렸을대 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()