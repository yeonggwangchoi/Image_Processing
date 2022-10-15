import cv2
import numpy as np

img = cv2.imread("poker.jpg")

point_list=[]

COLOR = (255,0,255)
THICKNESS = 3
drawing = False #선 그릴지 여부

def mouse_handler(event, x, y, flags, param):
    global drawing
    dst_img = img.copy()
    
    if event == cv2.EVENT_LBUTTONDOWN:
       point_list.append((x,y))
       drawing = True #선 그리기 시작
       
    if drawing:
        prev_point = None
        for point in point_list:
            cv2.circle(dst_img, point,5, COLOR, cv2.FILLED)
            if prev_point:
                cv2.line(dst_img, prev_point, point, COLOR, THICKNESS, cv2.LINE_AA)
            prev_point = point
            
        next_point = (x,y)
        if len(point_list)==4:
            show_result()  
            next_point = point_list[0]
        
        cv2.line(dst_img, prev_point, next_point, COLOR, THICKNESS, cv2.LINE_AA)
        
    cv2.imshow("img", dst_img)
    cv2.imwrite("new_img.jpg", dst_img)   
        
def show_result():
    width, height = 530,710
    src = np.float32(point_list)
    dst = np.array([[0, 0], [width, 0], [width, height], [0,height]], dtype=np.float32)#output 4개 지점

    matrix = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(img, matrix, (width, height))
    
    cv2.imshow("result_img", result)
    cv2.imwrite("new_result_img.jpg", result) 

cv2.namedWindow("img",cv2.WINDOW_NORMAL)
cv2.setMouseCallback("img", mouse_handler)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()