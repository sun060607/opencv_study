import cv2
cap = cv2.VideoCapture('data/video.avi')
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
fps=int(cap.get(5))
#동영상 저장을 위한 비디오 객체 설정
fourcc = cv2.VideoWriter_fourcc(*'XVID') # 코덱 설정(XVID)
out = cv2.VideoWriter('data/save_video.avi',fourcc,fps,(frame_width,frame_height))
while cap.isOpened():
    ret, frame=cap.read()
    if not ret:
        break
    out.write(frame)
    cv2.imshow('Video',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()