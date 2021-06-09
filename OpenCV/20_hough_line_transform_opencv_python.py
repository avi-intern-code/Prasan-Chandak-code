import cv2
import numpy as np

img = cv2.imread("sudoku.png")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray, 50, 150, apertureSize=3) # Canny edge detection function
cv2.imshow('edges', edges)
lines = cv2.HoughLines(edges, 1, np.pi/180, 200) # Hough Lines detection function

for line in lines:
    rho, theta = line[0]
    a = np.cos(theta)
    b = np.sin(theta)
    x0 = a*rho
    y0 = b*rho
    
    # x1 stores the rounded off value of r*cos(theta)-1000sin(theta)
    x1 = int(x0 + 1000*(-b))
    # y1 stores the rounded off value of r*cos(theta)+1000sin(theta)
    y1 = int(y0 + 1000*(a))
    # x1 stores the rounded off value of r*cos(theta)+1000sin(theta)
    x2 = int(x0 - 1000*(-b))
    # x1 stores the rounded off value of r*cos(theta)-1000sin(theta)
    y2 = int(y0 - 1000*(a))

    cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 2)

cv2.imshow('image', img)
k = cv2.waitKey(0)
cv2.destroyAllWindows()