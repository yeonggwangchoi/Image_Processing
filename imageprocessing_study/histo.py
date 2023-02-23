import numpy as np
import cv2
import matplotlib.pyplot as plt

img = cv2.imread('Lenna_dark.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('img', img)
hist = cv2.calcHist([img], [0], None, [256], [0,256])
plt.plot(hist)
plt.show()