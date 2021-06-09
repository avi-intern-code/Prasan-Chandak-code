import cv2
import numpy as np

# HSV - Hue Saturation and Value of an input image
# Hue - Color components
# Saturation - Amount of color
# Value - Brightness of the color

def nothing(x):
    pass

cap = cv2.VideoCapture("test.mp4")

cv2.namedWindow("Tracking") #Creating a tracking window
cv2.createTrackbar("LH", "Tracking", 0, 255, nothing) #Creating a trackbar with its name lower and upper values
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing)
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing)
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing)
cv2.createTrackbar("US", "Tracking", 255, 255, nothing)
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing)

while True:
    frame = cv2.imread("smarties.png") #To be used for images
    #_, frame = cap.read()

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV) #Convert color scheme from BGR to HSV 

    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    l_b = np.array([l_h, l_s, l_v]) #Lower color range for hsv color space ([110, 50, 50])
    u_b = np.array([u_h, u_s, u_v]) #Upper color range for hsv color space [130, 255, 255]

    mask = cv2.inRange(hsv, l_b, u_b) #Creating a mask to isolate the color using lower and upper range

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow("frame", frame)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    key = cv2.waitKey(1)

    if key == 27:
        break

#cap.release() #Release the cameras if video is being captured
cv2.destroyAllWindows()