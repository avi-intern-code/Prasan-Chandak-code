import cv2
import numpy as np 

#Program to search for a template image in a larger image

img = cv2.imread("messi5.jpg")
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread("messi_face.jpg", 0)
w, h = template.shape[::-1] #Gives column and row value in reverse order

res = cv2.matchTemplate(gray_img, template, cv2.TM_CCOEFF_NORMED)
print(res)
threshold = 0.99 #Threshold should be closer to 0.8-1 range the more the threshold value, more sure the rectangle drawn will be
loc = np.where(res>=threshold)
print(loc)

for pt in zip(*loc[::-1]):
    cv2.rectangle(img, pt, (pt[0]+w, pt[1]+h), (0, 0, 255), 2) #Create a rectangle on the brightest point in res given in loc

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

