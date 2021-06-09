import cv2

img = cv2.imread("lena.jpg", 1) # Reading the Image

print(img) # Prints a matrix

cv2.imshow('image', img) # Display image 

k = cv2.waitKey(0) & 0xFF # Wait for Key before disappear if time(in ms) is 0 them image is 
                          # loaded indefinitely until a key is pressed 0xFF is a mask recommended in 64 bits

if k == 27: # if esc key is pressed
    cv2.destroyAllWindows() # Closes all windows after specified argument in waitKey method

elif k == ord('s'): # if s is pressed
    cv2.imwrite('lena_copy.png', img) # Writes the img variable to lena_copy.png file
    cv2.destroyAllWindows() # Closes all windows after specified argument in waitKey method





