##고정 크기로 설정
# import cv2
# img = cv2.imread('cat.jpg')
# dst = cv2.resize(img, (400,500))

# cv2.imshow('img', img)
# cv2.imshow('resize', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

##비율로 설정
# import cv2
# img = cv2.imread('cat.jpg')
# # dst = cv2.resize(img, None, fx=0.5, fy=0.5) #x,y비율 정의(0.5배로 축소)
# dst = cv2.resize(img, None, fx=2, fy=2) #x,y비율 정의(2배로 확대)

# cv2.imshow('img', img)
# cv2.imshow('resize', dst)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

##보간법
#1. cv2.INTER_AREA : 크기 줄일 때 사용
#2. cv2.INTER_CUBIC : 크기 늘릴 때 사용 (속도 느림, 퀄리티 좋음)
#3. cv2.INTER_LINEAR : 크기 늘릴 때 사용 (기본값)
#보간법 적용하여 축소
import cv2
img = cv2.imread('cat.jpg')
dst = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA) #x,y비율 정의(0.5배로 축소)

cv2.imshow('img', img)
cv2.imshow('resize', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()