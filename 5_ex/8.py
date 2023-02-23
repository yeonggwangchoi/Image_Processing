import numpy as np, cv2

img = cv2.imread("color.jpg", cv2.IMREAD_COLOR)

mask = np.zeros(img.shape[:2], np.uint8)
center = (190, 170)

cv2.ellipse(mask, center, (60, 100), 0, 0, 360, (255,255,255),cv2.FILLED)
mask=cv2.bitwise_and(img,img,mask=mask)

cv2.imshow('img', img)
cv2.imshow('mask', mask)
cv2.waitKey(0)
cv2.destroyAllWindows()