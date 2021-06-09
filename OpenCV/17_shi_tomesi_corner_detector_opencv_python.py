import numpy as np
import cv2

# Shi Tomasi modification to detect corners in an image gives better results than Harris

img = cv2.imread("pic1.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corners = cv2.goodFeaturesToTrack(gray, 100, 0.1, 10) # 
corners = np.int0(corners) # int0 is int64

for i in corners:
    x, y = i.ravel()
    cv2.circle(img, (x, y), 3, 255, -1) # Makes 

cv2.imshow('dst', img)
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()

