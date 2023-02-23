import numpy as np, cv2

img = np.zeros((500, 700, 3), np.uint8)

colors = [(0, 0, 0), (0, 0 ,255), (0, 255, 255)]

rows, cols = img.shape[:2]
height = rows // 3

for i in range(3):
    h = height * i
    img[h:h+height,:] = colors[i]

cv2.imshow("img", img)
cv2.waitKey()
cv2.destroyAllWindows()