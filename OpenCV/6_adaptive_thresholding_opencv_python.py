import cv2
import numpy as np

# In adaptive thresholding, thethreshold value is calculated for a smaller region, therefore, there will
# be different thresholds in different areas
# Used when the image has different lighting conditions in different regions

img = cv2.imread('sudoku.png', 0)

_, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
# (source img, max value non zero value here 255, adaptive method - THRESH_MEAN_C, threshold type, 
# block size - neighbourhood area, c - used in both constant subtracted from mean or weighted mean in 
# GAUSSIAN_C)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

cv2.imshow('img', img)
cv2.imshow('th1', th1)
cv2.imshow('th2', th2)
cv2.imshow('th3', th3)

cv2.waitKey(0)
cv2.destroyAllWindows()