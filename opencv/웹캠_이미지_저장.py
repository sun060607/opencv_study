import cv2
cap = cv2.VideoCapture(0)
frame_width=int(cap.get(3))
frame_height=int(cap.get(4))
fps=int(cap.get(5))
num = 1
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('data/save_Webcam.avi',fourcc,fps,(frame_width,frame_height))
while cap.isOpened():
    ret, frame=cap.read()
    if not ret:
        break
    cv2.imshow('Video',frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite('data/save_Webcam_'+str(num)+'_img.png',frame)
        print("Image save successfully")
        num+=1
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()