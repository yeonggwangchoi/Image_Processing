##한글 우회 방법
#PIL (Python Image Library)

from PIL import ImageFont, ImageDraw, Image
import numpy as np
import cv2

def myPutText(src, text, pos, font_size, font_color):
    img_pil = Image.fromarray(src)
    draw = ImageDraw.Draw(img_pil)
    font = ImageFont.truetype('fonts/gulim.ttc', font_size)
    draw.text(pos, text, font=font, fill=font_color)
    return np.array(img_pil)

img = np.zeros((480, 640,3), dtype=np.uint8)

FONT_SIZE = 30 #크기
COLOR = (255, 255, 255) #색깔


img = myPutText(img, "최영광", (20,50), FONT_SIZE,COLOR)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()