import cv2

img = cv2.imread('Area.bmp',cv2.IMREAD_COLOR)

(rows, cols) = img.shape[:2]

bgr = cv2.split(img)

(minx,miny)=500,500
(maxx,maxy)=0,0

for i in range(rows):
    for j in range(cols):
        if bgr[0].item(i,j) > 200:
            if i<miny:
                miny=i
            if i<minx:
                minx=j
            if maxx<j:
                maxx=j
            if maxy<i:
                maxy=i
print((maxx-minx)*(maxy-miny))

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()