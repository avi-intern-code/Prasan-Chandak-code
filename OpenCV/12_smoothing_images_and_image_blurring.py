import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread("lena.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB) #Conversion is necessary as malplotlib reads images in RGB format whereas opencv reads it in BGR format

kernel = np.ones((5, 5), np.float32)/25 #kernel = 1/(kwidth*kheight) which is 25 here
dst = cv2.filter2D(img, -1, kernel)
blur = cv2.blur(img, (5,5))
gblur = cv2.GaussianBlur(img, (5,5), 0) #Gaussian Blur
median= cv2.medianBlur(img, 5) #median filter
bilateralFilter = cv2.bilateralFilter(img, 5, 5, 75)

titles = ['image', '2D Convolution', 'blur', 'GaussianBlur', 'median', 'bilateralFilter']
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
