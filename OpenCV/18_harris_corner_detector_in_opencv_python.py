import numpy as np
import cv2

# Harris Corner Detector

img = cv2.imread("chessboard.png")

cv2.imshow('img', img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray) # cornerHarris() method takes imput in float32 format

dst = cv2.cornerHarris(gray, 2, 3, 0.04) # Harris Detector Function

dst = cv2.dilate(dst, None) # Dilate result to get better results

img[dst>0.01*dst.max()] = [0, 0, 255] # Marking all the corners with red color

cv2.imshow('dst', img)

if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()

