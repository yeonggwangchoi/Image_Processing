import cv2
import numpy as np

img = cv2.imread('Lenna_dark.png',cv2.IMREAD_COLOR)

src = cv2.add(img, (150, 150, 150, 0))
dst = np.zeros(img.shape[:2],img.dtype)

dst = cv2.normalize(src,None,0,255,cv2.NORM_MINMAX)

cv2.imshow('img', img)
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()