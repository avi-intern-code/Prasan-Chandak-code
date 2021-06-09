import numpy as np
import cv2

img = cv2.imread("shapes.jpg")
imGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imGray, 240, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True) # Approximates a polygonal curve with a specific precision
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5) # Draw contours on original image
    x = approx.ravel()[0] # x-coordinate for the shape location
    y = approx.ravel()[1] -5 # y-coordinate for the shape location (-5 shifts text upwards) square and rectangle text

    if len(approx) == 3: # if 3 points are present in approx, then the shape is a triangle
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0)) # (0,0,0) is black colour

    elif len(approx) == 4:
        x1, y1, w, h = cv2.boundingRect(approx) # Gives the x, y coordinates and width and height of the bounding rectangle of the approx points. 
        # Name x1, y1 is given so that it is offset with the -5 above and a local variable with same name is not declared.
        aspectRatio = float(w)/h
        
        if aspectRatio>=0.95 and aspectRatio<=1.05:
            cv2.putText(img, "Square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
            cv2.putText(img, "Rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    elif len(approx) == 10:
        cv2.putText(img, "Star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

    else:
        cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))

cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()