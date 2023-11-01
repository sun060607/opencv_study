import cv2
src = cv2.imread('./data/car.png')
gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)

ret, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU)
binary = cv2.bitwise_not(binary)
contours, hierarchy = cv2.findContours(binary, cv2.RETR_LIST, cv2.CHAIN_APPROX_TC89_KCOS)

for contour in contours:
    epsilon = cv2.arcLength(contour, True)*0.02

    approx_poly = cv2.approxPolyDP(contour, epsilon, True)
    
    for approx in approx_poly:
        cv2.circle(src, tuple(approx[0]), 3, (255, 0, 0), -1)
cv2.imshow('src', src)
cv2.waitKey(0)
cv2.destroyAllWindows()