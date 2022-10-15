#좌우 대칭
# import cv2

# img = cv2.imread('cat.jpg')
# flip_horizontal = cv2.flip(img, 1) #flipCode > = : 좌우 대칭 Horizontal

# cv2.imshow('img', img)
# cv2.imshow('flip_horizontal', flip_horizontal)
# cv2.waitKey(0)
# cv2.destoryAllWindows()

# 상하
# import cv2

# img = cv2.imread('cat.jpg')
# flip_vertical = cv2.flip(img, 0) #flipCode > = : 좌우 대칭 Horizontal

# cv2.imshow('img', img)
# cv2.imshow('flip_vertical', flip_vertical)
# cv2.waitKey(0)
# cv2.destoryAllWindows()

#상하 좌우
import cv2

img = cv2.imread('cat.jpg')
flip_both = cv2.flip(img, -1) #flipCode > = : 좌우 대칭 Horizontal

cv2.imshow('img', img)
cv2.imshow('flip_both', flip_both)
cv2.waitKey(0)
cv2.destoryAllWindows()

