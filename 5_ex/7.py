import numpy as np, cv2

logo = cv2.imread("logo.jpg", cv2.IMREAD_COLOR)
if logo is None: raise Exception("영상파일 읽기 오류")

logo = cv2.threshold(logo, 220, 255, cv2.THRESH_BINARY)[1]

blue, green, red = cv2.split(logo)

# blue = cv2.threshold(blue, 220, 255, cv2.THRESH_BINARY)[1]
# green = cv2.threshold(green, 220, 255, cv2.THRESH_BINARY)[1]
# red = cv2.threshold(red, 220, 255, cv2.THRESH_BINARY)[1]

blue_img = cv2.bitwise_and(logo, logo, mask=blue)
green_img = cv2.bitwise_and(logo, logo, mask=green)
red_img = cv2.bitwise_and(logo, logo, mask=red)

cv2.imshow('logo', logo)
cv2.imshow('blue_img', blue_img)
cv2.imshow('green_img', green_img)
cv2.imshow('red_img', red_img)
cv2.waitKey(0)