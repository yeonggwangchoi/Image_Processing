# import cv2
# img = cv2.imread('book.jpg', cv2.IMREAD_GRAYSCALE)

# ret, binary = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)

# cv2.imshow('img', img)
# cv2.imshow('binary', binary)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Trackbar(값 변화에 따른 변형 확인)
import cv2

def empty(pos):
    #print(pos)
    pass

img = cv2.imread('book.jpg', cv2.IMREAD_GRAYSCALE)
name = "Trackbar"
cv2.namedWindow(name)

cv2.createTrackbar("threshold", name, 127, 255, empty)

while True:
    thresh = cv2.getTrackbarPos("threshold", "Trackbar")
    ret, binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)
    
    if not ret:
        break
    
    cv2.imshow(name, binary)
    if cv2.waitKey(1) == ord('q'):
        break
    
cv2.destroyAllWindows()