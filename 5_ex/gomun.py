import cv2

img = cv2.imread("gomungwan.jpg", cv2.IMREAD_GRAYSCALE)

dst = cv2.threshold(img, 160, 255, cv2.THRESH_BINARY)[1]

cv2.imshow('img', img)
cv2.imshow('dst', dst)

cv2.waitKey(0)
cv2.destroyAllWindows(0)