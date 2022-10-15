import cv2
cap = cv2.VideoCapture('catvideo.mp4')

while cap.isOpened(): #동영상 파일이 올바로 열렸는지?
    ret, frame = cap.read() # ret : 성공 여부, frame : 받아온 이미지(프레임)
    if not ret: #만약 성공이 아니면
        print('더 이상 가져올 프레임이 없어요')
        break
    cv2.imshow('video',frame)
    if cv2.waitKey(1) == ord('q'): #ord는 아스키코드 반환 함수
        break
    
cap.release() #자원 해제
cv2.destroyAllWindows()