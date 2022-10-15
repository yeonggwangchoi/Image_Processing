import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8) #가로 480, 세로 680, 3차원 형태의 공간을 0으로 채움

COLOR = (255,255,0) #색깔
RADIUS = 50 #반지름
THICKNESS = 10 #두께

cv2.circle(img, (200,100), RADIUS, COLOR, THICKNESS, cv2.LINE_AA)
#그릴 위치, 원의 중심점, 반지름, 색깔, 두께, 선 종류
cv2.circle(img, (200,300), RADIUS, COLOR, cv2.FILLED, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()