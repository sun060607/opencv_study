import numpy as np
import cv2

src = cv2.imread('./data/fox.png')
number = np.ones_like(src)*127

_max=cv2.max(src,number) #최대값
# 의료 영상에서 최대 투과력 투영 : 스캔 데이터의 스택 중에 각 픽셀위치에서 가장 밝은 값 선택
# 자율주행 차량에서 장매물 감지 : 라이다 또는 카메라 데이터 중에서 장애물의 위치를 찾을때 사용
_min=cv2.min(src,number) #최소값
#의료 영상에서 최소 투과력 투영: ct 스캔 데이터의 스택 중에 각 픽셀 위치에서 가장 어두운 값 
# 영상에서 노이즈 제거: 노이즈 픽셀을 제거하기 위해 이미지에서 가장 어둥운 값을 사용
_abs=cv2.absdiff(src,number) #잘대값주의
#보안 모니터링 : 현재 프레임과 이전 프레임간의 차이 이미지를 생성하여 움직임을 감지하고 보안 목적
#영상 흐름 분석 : 영상에서 오브젝트 움직임 및 흐름을 분석하는 활용
compare=cv2.compare(src,number,cv2.CMP_GT) #비교(비교결과가 true이면 255, false이면 0)
#얼굴 인식 : 입력 얼굴과 저장된 얼굴 이미지를 비교하여 개인을 인증하는데 식별
#물체 일치 검사: 두 이미지를 비교하여 물체의 일치 여부를 판단하는데 사용
src = np.concatenate((src,src,src,src),axis=1)
number=np.concatenate((number,number,number,number),axis=1)
dst=np.concatenate((_max,_min,_abs,compare),axis=1)

dst=np.concatenate((src,number,dst),axis=0)
cv2.imshow('dst',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()