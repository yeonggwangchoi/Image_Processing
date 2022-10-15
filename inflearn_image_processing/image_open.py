import cv2
import sys
img = cv2.imread('cat.jpg')
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()