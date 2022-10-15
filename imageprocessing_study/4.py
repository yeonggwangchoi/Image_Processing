import cv2
import numpy as np

img = cv2.imread('Lenna_dark.png',cv2.IMREAD_COLOR)

src = cv2.add(img, (150, 150, 150, 0))

f_max = src.max()  # 최대픽셀값
f_min = src.min()  # 최소픽셀값
nframe = src.astype('int64')  
dst = np.clip(((nframe - f_min)/(f_max - f_min))*255, 0, 255).astype('uint8')

cv2.imshow('img', img)
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()