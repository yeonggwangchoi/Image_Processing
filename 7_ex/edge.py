import numpy as np, cv2

img = cv2.imread("color.jpg", cv2.IMREAD_COLOR)

rows, cols = img.shape[:2]

h = rows // 2 + 1
w = cols // 2 + 1

blur_data = [[1/9, 1/9, 1/9],
             [1/9, 1/9, 1/9],
             [1/9, 1/9, 1/9]]
blur_mask = np.array(blur_data, np.float32)
blur = cv2.filter2D(img[:h,:w], cv2.CV_16S, blur_mask)
blur = cv2.convertScaleAbs(blur)

sharp_data = [[0, -1, 0],
             [-1, 5, -1],
             [0, -1, 0]]
sharp_mask = np.array(sharp_data, np.float32)
sharp = cv2.filter2D(img[:h,w:], cv2.CV_16S, sharp_mask)
sharp = cv2.convertScaleAbs(sharp)

sobel = cv2.Sobel(np.float32(img[h:,:w]), cv2.CV_32F, 0, 1, 3)
sobel = cv2.convertScaleAbs(sobel)

laplacian = cv2.Laplacian(img[h:,w:], cv2.CV_16S, 1)
laplacian = cv2.convertScaleAbs(laplacian)

img[:h,:w] = blur
img[:h,w:] = sharp
img[h:,:w] = sobel
img[h:,w:] = laplacian

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()