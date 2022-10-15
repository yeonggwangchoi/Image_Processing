# cv2.line()
# 그릴 위치, 시작점, 끝점, 색깔, 두께, 선종류
# 선종류 : 
# cv2.LINE_4  : 상하 좌우 4방향으로 연결된 선
# cv2.LINE_8  : 대각선을 포함한 8방향으로 연결된 선(default)
# cv2.LINE_AA : 부드러운선(anti-aliasing)


import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8) #가로 480, 세로 680, 3차원 형태의 공간을 0으로 채움
COLOR = (0,255,255) #색깔
THICKNESS = 3 #두께
cv2.line(img, (50,100), (400,50), COLOR, THICKNESS, cv2.LINE_8)
cv2.line(img, (50,200), (400,150), COLOR, THICKNESS, cv2.LINE_4)
cv2.line(img, (50,300), (400,250), COLOR, THICKNESS, cv2.LINE_AA)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()