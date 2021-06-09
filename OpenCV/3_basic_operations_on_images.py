import cv2

img = cv2.imread("messi5.jpg")
img2 = cv2.imread("opencv-logo.png")

cv2.imshow('img', img)
cv2.imshow('img2', img2)

print(img.shape) #returns a tuple of number of rows, columns and channels
print(img.size) #returns total number of pixels accessed
print(img.dtype) #returns image datatype is obained

b,g,r = cv2.split(img) #split image in 3 channels
img = cv2.merge((b,g,r)) #merge bgr channels into an image

ball = img[280:340, 330:390] # selecting the image array values that contain the ball
img[273:333, 100:160] = ball # pasting the ball on another area of the image 

img = cv2.resize(img, (512, 512)) #resize the image
img2 = cv2.resize(img2, (512, 512))

#dst = cv2.add(img, img2) #add 2 images
dst = cv2.addWeighted(img, .5, img2, .5, 0) #add the weights/percentages of the 2 images to be added
# (1st array/image, alpha - weight of the ist image, 2nd image, beta - weight of the 2nd image, 
# gamma - scalar value)
# dst = src1*alpha + src2*beta + gamma 

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()