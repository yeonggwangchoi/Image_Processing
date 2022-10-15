from pickletools import uint8
import cv2
import numpy as np

pizza1 = cv2.imread('pizza1.png',cv2.IMREAD_COLOR)
pizza2 = cv2.imread('pizza2.png',cv2.IMREAD_COLOR)

(rows, cols) = pizza1.shape[:2]

width = cols // 2 + 1

b1,g1,r1 = cv2.split(pizza1)
b2,g2,r2 = cv2.split(pizza2)

for i in range(rows):
    for j in range(width):
        k = b1.item(i,j)
        b2.itemset((i,j), k)
        k = g1.item(i,j)
        g2.itemset((i,j), k)
        k = r1.item(i,j)
        r2.itemset((i,j), k)
        
        
    
img = cv2.merge((b2,g2,r2))

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()