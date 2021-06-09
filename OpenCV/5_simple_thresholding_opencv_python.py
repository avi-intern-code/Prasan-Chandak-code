import cv2 as cv
import numpy as np

# Thresholding is a segmentaion technique used for separating an object from its background
# Comparing each pixel of an image with a predefined threshold value and divides it into 2 groups
# based on whether their intensity is lower or higher than the threshold value

# If pixel value=0 colour=black if value=255 colour=white
img = cv.imread('gradient.png', 0) # 0 implies that the image will be read in grayscale mode

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY) # _ is the ret value
# binary threshold if value<127 value=0 else value=255
_, th2 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV) 
# inverse of binary threshold
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC) 
# values less than 127 will remain same and the remaining will be 127
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO) 
# pixel if value<threshold value=0 else will remain the same
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV) 
# inverse of THRESH_TOZERO


cv.imshow("Image", img)
cv.imshow("th1", th1)
cv.imshow("th2", th2)
cv.imshow("th3", th3)
cv.imshow("th4", th4)
cv.imshow("th5", th5)

cv.waitKey(0)
cv.destroyAllWindows()