import numpy as np
import cv2

img_color = cv2.imread('Area.bmp') # 이미지 파일을 컬러로 불러옴
height, width = img_color.shape[:2] # 이미지의 높이와 너비 불러옴, 가로 [0], 세로[1]

img_hsv = cv2.cvtColor(img_color, cv2.COLOR_BGR2HSV) # cvtColor 함수를 이용하여 hsv 색공간으로 변환

lower_blue = (90, 0, 0) # hsv 이미지에서 바이너리 이미지로 생성 , 적당한 값 30
upper_blue = (135, 255, 255)

img_mask = cv2.inRange(img_hsv, lower_blue, upper_blue) # 범위내의 픽셀들은 흰색, 나머지 검은색
img_result = cv2.bitwise_and(img_color, img_color, mask = img_mask) 
# 바이너리 이미지를 마스크로 사용하여 원본이미지에서 범위값에 해당하는 영상부분을 획득

contours, _ = cv2.findContours(img_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

area = cv2.contourArea(contours[0])
# cnt = contours[0]
# mmt = cv2.moments(cnt)
# for key, value in mmt.items():
#     print(key," : ",value)

# cx = int(mmt['m10']/mmt['m00'])
# cy = int(mmt['m01']/mmt['m00'])
# print(
#     'x 무게중심', cx, 'y 무게중심', cy
# )
# (minx,miny)=500,500
# (maxx,maxy)=0,0

# for i in range(height):
#     for j in range(width):
#         if img_mask.item(i,j) > 254:
#             if i<miny:
#                 miny=i
#             if j<minx:
#                 minx=j
#             if maxx<j:
#                 maxx=j
#             if maxy<i:
#                 maxy=i
                
# print((maxx-minx)*(maxy-miny))
print(area)
cv2.imshow('img_color', img_color)
cv2.imshow('img_mask', img_mask)
cv2.imshow('img_result', img_result)

cv2.waitKey(0)
cv2.destroyAllWindows()

#https://velog.io/@nayeon_p00/OpenCV-Python-HSV-%EC%83%89%EA%B3%B5%EA%B0%84%EC%97%90%EC%84%9C-%EC%9D%B4%EB%AF%B8%EC%A7%80%EC%9D%98-%ED%8A%B9%EC%A0%95%EC%83%89-%EC%B6%94%EC%B6%9C%ED%95%98%EA%B8%B0