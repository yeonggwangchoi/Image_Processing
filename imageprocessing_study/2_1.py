import cv2

img = cv2.imread("DeadPixel1.bmp", cv2.IMREAD_COLOR)

(rows, cols) = img.shape[:2]

cnt = 0

for i in range(rows):
    for j in range(cols):
        kb = img.item(i,j,0)
        if kb != 0:
            img.itemset((i,j,0),0)
        kg = img.item(i,j,1)
        if kg != 0:
            img.itemset((i,j,1),0)
        kr = img.item(i,j,2)
        if kr != 0:
            cnt += 1
            img.itemset((i,j,2),255)

TF = "정상"
          
if cnt >= 10:
    TF="불량"
    
width = cols // 3 + 1
height = rows // 3 + 1
c=0

for i in img.shape[height:height*2]:
    for j in img.shape[width:width*2]:
        kr = img.item(i,j,2)
        if kr == 255:
            c+=1
            
if c >= 2:
    TF="불량"
    
print(TF)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()