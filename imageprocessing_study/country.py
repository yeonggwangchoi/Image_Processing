import cv2
import numpy as np

img1 = np.zeros((300,400,3), np.uint8)

rows, cols = img1.shape[:2]

width = cols // 3

colors = [(0,0,0), (32,219,253), (62,48,239)]
ger = img1 
for i in range(3):
    w = width * i
    ger[:,w:w+width] = colors[i]


img2 = np.zeros((300,400,3), np.uint8)
height = rows // 3

c = [colors[0], colors[2], colors[1]]
bel = img2 
for i in range(3):
    h = height * i
    bel[h:h+height,:] = c[i]

jap = np.full((300,400,3), 255, np.uint8)

cv2.circle(jap, (200,150), 80, (0,0,255),cv2.FILLED)
cv2.imshow("ger", ger)
cv2.imshow("bel", bel)
cv2.imshow("jap", jap)
cv2.waitKey(0)
cv2.destroyAllWindows()