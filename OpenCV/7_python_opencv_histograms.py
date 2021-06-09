import cv2
import numpy as np
from matplotlib import pyplot as plt

# 

img = cv2.imread('lena.jpg', 0)

#img = np.zeros((200, 200), np.uint8) 200x200 pixel black image 
#cv2.rectangle(img, (0, 100), (200, 200), (255), -1) 
# Half of the image will become white, -1 will fill the rectangle
#cv2.rectangle(img, (0, 50), (100, 100), (127), -1) # Gray filled area between these coordinates

#b, g, r = cv2.split(img)

hist = cv2.calcHist([img], [0], None, [256], [0, 256])
# ([img in sq. brackets], index of channels for which hist is calculated, 
# image mask-None, [histsize], range)

plt.plot(hist)

#cv2.imshow("img", img)
#cv2.imshow("b", b)
#cv2.imshow("g", g)
#cv2.imshow("r", r)

#plt.hist(img.ravel(), 256, [0, 256])
# (image, max no of pixel values, range)
# The numpy.ravel() functions returns contiguous flattened array
# (1D array with all the input-array elements and with the same type as it)
#plt.hist(b.ravel(), 256, [0, 256])
#plt.hist(g.ravel(), 256, [0, 256])
#plt.hist(r.ravel(), 256, [0, 256])

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()

