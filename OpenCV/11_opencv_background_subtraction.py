import numpy as np
import cv2

cap = cv2.VideoCapture("vtest.avi")
fgbg = cv2.bgsegm.createBackgroundSubtractorMOG() #Background and foreground segmentation method
fgbg2 = cv2.createBackgroundSubtractorMOG2() #detectShadows attribute True by default
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
fgbg3 = cv2.bgsegm.createBackgroundSubtractorGMG()
fgbg4 = cv2.createBackgroundSubtractorKNN() #detectShadows attribute True by default

while True:
    ret, frame = cap.read()
    
    if frame is None:
        break

    fgmask = fgbg.apply(frame) #Create mask image from segmented and processed image
    fgmask2 = fgbg2.apply(frame)
    fgmask3 = fgbg3.apply(frame)
    fgmask3 = cv2.morphologyEx(fgmask, cv2. MORPH_OPEN, kernel)
    fgmask4 = fgbg4.apply(frame)

    cv2.imshow("Frame", frame)
    cv2.imshow("FG MAsk Frame", fgmask) #Output masked image
    cv2.imshow("FG MAsk Frame 2", fgmask2)
    cv2.imshow("FG MAsk Frame 3", fgmask3)
    cv2.imshow("FG MAsk Frame 4", fgmask4)

    keyboard = cv2.waitKey(30)

    if keyboard == 'q' or keyboard == 27:
        break

cap.release()
cv2.destroyAllWindows()