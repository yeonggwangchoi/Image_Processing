#고정
# import cv2
# cap = cv2.VideoCapture('catvideo.mp4')

# while cap.isOpened():
#     ret, frame = cap.read()
#     if not ret: 
#         break
#     frame_resized = cv2.resize(frame, (400,500))
#     cv2.imshow('video',frame_resized)
#     if cv2.waitKey(1) == ord('q'):
#         break

# cap.release()
# cv2.destroyAllWindows()

#비율로 
import cv2
cap = cv2.VideoCapture('catvideo.mp4')

while cap.isOpened():
    ret, frame = cap.read()
    if not ret: 
        break
    frame_resized = cv2.resize(frame, None, fx=1.5,fy=1.5, interpolation=cv2.INTER_CUBIC)
    cv2.imshow('video',frame_resized)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()