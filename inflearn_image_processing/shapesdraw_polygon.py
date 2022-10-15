import cv2
import numpy as np

img = np.zeros((480, 640, 3), dtype=np.uint8) #가로 480, 세로 680, 3차원 형태의 공간을 0으로 채움

COLOR = (255,255,0) #색깔
THICKNESS = 3 #두께

pts = np.array([[100,100], [200,100], [100,200]])
pts1 = np.array([[200,100], [300,100], [300,200]])

cv2.polylines(img, [pts, pts1], True, COLOR, THICKNESS, cv2.LINE_AA)
# 그릴 위치, 그릴 좌표들, 닫힘 여부, 색깔, 두께, 선 종류

img = np.zeros((480, 640, 3), dtype=np.uint8) #가로 480, 세로 680, 3차원 형태의 공간을 0으로 채움
pts2 = np.array([[[100,100], [200,300], [100,400]],[[200,300], [300,300], [300,400]]])

cv2.fillPoly(img, pts2, COLOR, cv2.LINE_AA)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()