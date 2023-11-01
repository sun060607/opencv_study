import cv2
src = cv2.imread('./data/coffee.jpg')
src = cv2.resize(src,dsize=(640,480),interpolation=cv2.INTER_AREA)
dst = src.copy()
#자율 주행 자동차: 도로에서의 코너를 검출하여 차선 유지 및 회전을 수행합니다
#로봇 내비게이션: 로봇은 환경의 구석구석을 찾아가서 코너를 검출합니다.
#영상 스티치: 여러 이미지를 합쳐 파노라마 이미지를 생성할때 이미지 정렬을 수행합니다
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
#...(입력 이미지,코너 최댓값, 코너 품질, 최소 거리, 마스크,블록 크기, 해리스 코너 검출기 유/무, 핼리스 코너 계수)
corners=cv2.goodFeaturesToTrack(gray,100,0.01,5,blockSize=3,useHarrisDetector=True,k=0.03)

for i in corners:
    x,y=i.ravel()
    center=(int(x),int(y))
    cv2.circle(dst,center,3,(0,0,255),2)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()