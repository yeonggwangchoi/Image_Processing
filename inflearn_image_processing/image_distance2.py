import cv2
import numpy as np
img = cv2.imread("poker.jpg")

width, height = 530,710
src = np.array([[708,163], [1134,412], [730, 1000], [280,683]], dtype=np.float32) #input 4개 지점
dst = np.array([[0, 0], [width, 0], [width, height], [0,height]], dtype=np.float32)#output 4개 지점

matrix = cv2.getPerspectiveTransform(src, dst)
result = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("img", img)
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()