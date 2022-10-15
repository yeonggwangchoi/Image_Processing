#이미지 잘라서 새창에 표시
# import cv2
# img = cv2.imread('cat.jpg')

# crop = img[100:200, 200:400]

# cv2.imshow('img', img)
# cv2.imshow('crop', crop)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#영역을 잘라서 기존 윈도우 표시

import cv2
img = cv2.imread('cat.jpg')

crop = img[100:200, 200:400]
img[100:200, 400:600] = crop

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
