import cv2, numpy as np

img = np.zeros((300, 400, 3), np.uint8)

rows, cols = img.shape[:2]

height = rows // 2

colors = [(255, 0, 0), (0, 255, 255)]

for i in range(2):
    h = height * i
    img[h:h+height,:] = colors[i]
    
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()