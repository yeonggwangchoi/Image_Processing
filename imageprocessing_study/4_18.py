import numpy as np, cv2

img = np.full((300, 400, 3), 255, np.uint8)
cv2.ellipse(img, (200, 150), (100, 100), 0, 180, 360, (0,0,255), cv2.FILLED)
cv2.ellipse(img, (200, 150), (100, 100), 0, 0, 180, (255,0,0), cv2.FILLED)
cv2.ellipse(img, (150, 150), (50, 50), 0, 0, 180, (0,0,255), cv2.FILLED)
cv2.ellipse(img, (250, 150), (50, 50), 0, 180, 360, (255,0,0), cv2.FILLED)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()