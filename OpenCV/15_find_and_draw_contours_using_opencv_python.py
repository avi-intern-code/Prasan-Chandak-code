import cv2
import numpy as np
from matplotlib import pyplot as plt

# Contours using OpenCV

img = cv2.imread("shapes.jpg")
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Converting color of img from BGR to grayscale

ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

print("Number of Contours = ", len(contours))
print(contours[0])

cv2.drawContours(img, contours, -1, (0, 255, 0), 3)

titles = ['Image Original', 'Image Grayscale']
images = [img, imgray]

for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv2.imshow('Image', img)
cv2.imshow('Image Gray', imgray)

cv2.waitKey(0)
cv2.destroyAllWindows()