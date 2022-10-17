import numpy as np, cv2

img = np.zeros((300, 400, 3), np.uint8)

rows, cols = img.shape[:2]

height = rows // 3

colors = [(255, 255, 255), (255, 0 ,0), (0, 0, 255)]

for i in range(3):
    h = height * i
    img[h:h+height,:] = colors[i]
    
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()