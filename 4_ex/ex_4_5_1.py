import cv2

capture = cv2.VideoCapture("catvideo.mp4")
if capture.isOpened() == False:
    raise Exception("카메라 연결 안됨")

while True:
    ret, frame = capture.read()
    if not ret: break
    if cv2.waitKey(30) >= 0: break
    cv2.imshow('frame', frame)
    
capture.release()