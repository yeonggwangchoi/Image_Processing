#윤곽선
import cv2

img = cv2.imread('card.png')

target_img = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

ret, otsu = cv2.threshold(gray,-1,255,cv2.THRESH_BINARY|cv2.THRESH_OTSU)
contours, hierarchy = cv2.findContours(otsu, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

#윤곽선 정보, 구조
#이미지, 윤곽선 찾는 모드[mode], 윤곽선 찾을때 사용하는 근사치 방법[method]
#모드
#1.cv2.RETR_EXTERNAL : 가장 외곽의 윤곽선만 찾음
#2.cv2.LIST : 모든 윤곽선을 찾음(계층정보 없음)
#3.cv2.RETR_TREE : 모든 윤곽선 찾음(계층 정보를 트리 구조로 생성)
cv2.drawContours(target_img, contours, -1, (0,200,0), 3)
#대상 이미지, 윤곽선 정보, 인덱스 (-1이면 전체), 색깔, 두께

cv2.imshow('img', img)
cv2.imshow('gray', gray)
cv2.imshow('otsu', otsu)
cv2.imshow('target_img', target_img)
cv2.waitKey(0)
cv2.destroyAllWindows()