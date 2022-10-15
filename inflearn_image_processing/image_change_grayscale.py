import cv2
img = cv2.imread('cat.jpg', cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread('cat.jpg')
dst = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imshow('img', img)
cv2.imshow("img2", img2)
cv2.imshow("img3", dst)
cv2.waitKey(0)
cv2.destroyAllWindows()