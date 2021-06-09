import numpy as np
import cv2

# Object tracking is the process of locating a moving object over time using a camera
# In mean shift we are given a small window-circle, rectangle or square 
# We have to move that window to an area to the maximum pixel density or maximum no of points

cap = cv2.VideoCapture('slow_traffic_small.mp4')

# take 1st frame of a video
ret, frame = cap.read()

# setup initial location of window
x, y, width, height = 300, 200, 100, 50 # Hardcoded as it is pre-calculated
track_window = (x, y, width, height)

# setup Region Of Interest (ROI) for tracking
roi = frame[y:y+height, x:x+width] # Select the region of interest in the image array

# Define the histogram back projection
hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV) # Convert in HSV color space
mask = cv2.inRange(hsv_roi, np.array((0., 60., 32.)), np.array((180., 255., 255.)))
# (hsv image, lower limit, upper limit) 
# inRange is considered as in the histogram only hue is considered form hsv 1st - channel
# low light values are also discarded using the inRange() function
roi_hist = cv2.calcHist([hsv_roi], [0], mask, [180], [0, 180])
# (hsv image, channels - [0] is the hue channel, mask, hist size - from 0 to 179, range - from 0 to 179)
cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
# (source image, destination image, alpha - here from 0, beta - here from 255, norm type)
# these steps give histogram back projected image

# Setup termination criteria, either 10 iterations or move by at least 1 point
term_criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1) 
# Either 10 iteration or by moving at least 1 point

cv2. imshow('roi', roi)

while(1):
    ret, frame = cap.read() # if frame is read correctly ret is True
    if ret == True:
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        dst = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1) # Function to calculating the back projected image
        # (image, channel - hue values here so [0], hist value, ranges, scale)
        # apply meanshift to get the new location
        ret, track_window = cv2.meanShift(dst, track_window, term_criteria) # Apply meanShift
        # (destination image, track image/window, termination criteria)
        # Draw it on a window
        x, y, w, h = track_window
        final_image = cv2.rectangle(frame, (x, y), (x+w, y+h), 255, 3)

        cv2.imshow('dst', dst) # destination image
        cv2.imshow('final_image', final_image) # car window tracked

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
    else:
        break


