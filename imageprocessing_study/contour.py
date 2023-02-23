import numpy as np, cv2

img = cv2.imread('face1.jpg', cv2.IMREAD_COLOR)
imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
rows, cols = imggray.shape[:2]
h,w = rows // 3, cols // 3
imggray_roi = imggray[h:h*2,:] 
blur = cv2.GaussianBlur(imggray_roi,(5,5),0)
thresh = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,25,9)

contours, _ = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

contours_dict = []
temp_result = np.zeros(imggray_roi.shape[:2], dtype=np.uint8)
for contr in contours:
    x,y,w,h = cv2.boundingRect(contr)
    cv2.rectangle(temp_result, pt1=(x,y), pt2=(x+w, y+h), color=(255,255,255), thickness=1)

    contours_dict.append({ #컨투어 정보를 딕셔너리에 저장
            'contour': contr,
            'x': x,
            'y': y,
            'w': w,
            'h': h,
            'cx': x + (w / 2),
            'cy': y + (h / 2)
        })
MIN_AREA,MAX_AREA = 2000, 5000
MIN_WH = 1
matchs = []
cnt=0
for d in contours_dict:
        area = d['w'] * d['h']
        ratio = d['w'] / d['h']
        
        if MIN_AREA < area < MAX_AREA and d['w'] / d['h'] > MIN_WH:
            d['idx'] = cnt
            cnt += 1
            matchs.append(d)
            
temp_result2 = np.zeros(imggray_roi.shape[:2], dtype = np.uint8)
for d in matchs:
        cv2.rectangle(thresh, pt1=(d['x'], d['y']), pt2=(d['x']+d['w'], d['y']+d['h']), color=(0, 255, 0), thickness=1)

cv2.imshow('thresh', thresh)
cv2.imshow('temp_result', temp_result)
cv2.imshow('temp_result2', temp_result2)
cv2.waitKey(0)