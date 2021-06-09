import cv2
import numpy as np

# Black part performs as zeroes and white part performs as 1

img1 = np.zeros((250, 500, 3), np.uint8) # creates a completely black image
img1 = cv2.rectangle(img1,(200, 0), (300, 100), (255, 255, 255), -1) # creates white rectangle in img1
img2 = np.full((250, 500, 3), 255, dtype=np.uint8)
img2 = cv2.rectangle(img2, (0, 0), (250, 250), (0, 0, 0), -1) # creates a black and white image from the video

cv2.imwrite('image_1.png', img2) # saves the image

bitAnd = cv2.bitwise_and(img2, img1) # bitwise and operation on 2 images
bitOr = cv2.bitwise_or(img2, img1) # bitwise or operation on the 2 images
bitXor = cv2.bitwise_xor(img1, img2) # bitswise xor operation on the 2 images
bitNot1 = cv2.bitwise_not(img1) # not operation on img1
bitNot2 = cv2.bitwise_not(img2) # not operation on img2

cv2.imshow("img1", img1)
cv2.imshow("img2", img2)
cv2.imshow('bitAnd', bitAnd)
cv2.imshow('bitOr', bitOr)
cv2.imshow('bitXor', bitXor)
cv2.imshow('bitNot1', bitNot1)
cv2.imshow('bitNot2', bitNot2)

cv2.waitKey(0)
cv2.destroyAllWindows()