import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')

ret, frame1 = cap.read() # Reading 1 frame
ret, frame2 = cap.read() # Reading frame after frame1

while(cap.isOpened()):
    diff = cv2.absdiff(frame1, frame2) # Absolute difference b/w the 1st frame and the second frame
    # When we find the difference, we convert it into grayscale
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY) # finding out the contours is easier in grayscale
    blur = cv2.GaussianBlur(gray, (5, 5), 0) # Blur the grayscale image
    # (image, kernel size, sigma-x value)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    # (source, threshold value, max thresh value, type)
    dilated = cv2.dilate(thresh, None, 3)
    # (thresholded image, kernel, no of iterations)
    # dilate the thresholded image to fill in all the holes to help us find better contours 
    # It increases the white region in the image or size of foreground object increases
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    # (dilated image, mode-cv2.RETR_TREE most commonly used, method)

    # draw rectangles around moving objects  and remove noises (eg., rope that seems to move)
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour) # save all the coordinates of the found contours
        
        if cv2.contourArea(contour)<700: # If area<700 no rectangle. Used to remove noises
            continue
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2) # thickness=2
        cv2.putText(frame1, "Status: {}".format("Movement"), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
        1, (0, 0, 255), 3)
        # (image, text, origin of the text, font face, font scale, color, thickness)

    #cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2) 
    # # Using this draws contours around objects instead of rectangles
    # (image, contours, contour id - -1 applies all, color, thickness)
    # Draw contours on the original image/ 1st frame

    cv2.imshow('feed', frame1) # display the changed frame 1

    frame1 = frame2 # changing frame1 and frame2 values
    if cap.isOpened():
        ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()