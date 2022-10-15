import cv2
import numpy as np

img = cv2.imread("poker.jpg")

point_list=[]

COLOR = (0,0,0)

def mouse_handler(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
       point_list.append((x,y))
    for point in point_list:
        cv2.circle(img, point,5, COLOR, cv2.FILLED)
    
    cv2.imshow("img", img)    
    if len(point_list)==4:
        show_result()
    
        
def show_result():
    width, height = 530,710
    src = np.float32(point_list)
    dst = np.array([[0, 0], [width, 0], [width, height], [0,height]], dtype=np.float32)#output 4개 지점

    matrix = cv2.getPerspectiveTransform(src, dst)
    result = cv2.warpPerspective(img, matrix, (width, height))
    
    cv2.imshow("result_img", result)


cv2.namedWindow("img",cv2.WINDOW_NORMAL)
cv2.setMouseCallback("img", mouse_handler)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()