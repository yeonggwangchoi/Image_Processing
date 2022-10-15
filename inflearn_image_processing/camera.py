import cv2
cap = cv2.VideoCapture(0)

while cap.isOpened(): 
    ret, frame = cap.read() # ret : 성공 여부, frame : 받아온 이미지(프레임)
    if not ret:
        exit()
    cv2.imshow('video',frame)
    if cv2.waitKey(1) == ord('q'): #ord는 아스키코드 반환 함수
        break
    
cap.release() #자원 해제
cv2.destroyAllWindows()