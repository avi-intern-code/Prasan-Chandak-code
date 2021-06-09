import matplotlib.pyplot as plt
import cv2
import numpy as np

def region_of_interest(img, vertices):
    mask = np.zeros_like(img) # Return an array of zeros with the same shape and type as a given array.
    #channel_count = img.shape[2] # 3rd value of the array img.shape
    match_mask_color = 255 #,) * channel_count # Create a match color with the same color channel count
    cv2.fillPoly(mask, vertices, match_mask_color) # Fill the area bounded by 1 or more polygons
    masked_image = cv2.bitwise_and(img, mask) 
    return masked_image

def draw_the_lines(img, lines):
    img = np.copy(img)
    blank_image = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8) 
    # img.shape[0]-width img.shape[1]-height
    for line in lines:
        for x1, y1, x2, y2 in line: # Coordinates of the first and second points on the line
            cv2.line(blank_image, (x1, y1), (x2, y2), (0, 255, 0), thickness=3)
            # Draw line on the blank image that is the same size as the original image and then merge them

    img = cv2.addWeighted(img, 0.8, blank_image, 1, 0.0) # Function used to merge 2 images with some weights
    return img

#image = cv2.imread('road.jpg')
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB) # Convert in RGB format as we have to use matplotlib
# We will use cv2 not matplotlib so this conversion is not needed
# The region of interest will be in the shape of a triangle as the 2 parallel lanes converge in image

def process(image):

    height = image.shape[0] # height of the image
    width = image.shape[1] # width of the image

    region_of_interest_vertices = [
        (0, height), # (leftmost_corner, midpoint/center of image, width, height)
        (width/2, height/2),
        (width, height)
    ]

    gray_image = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    canny_image = cv2.Canny(gray_image, 100, 200)

    cropped_image = region_of_interest(canny_image,
                    np.array([region_of_interest_vertices], np.int32))

    lines = cv2.HoughLinesP(cropped_image,
                            rho=2,
                            theta=np.pi/60,
                            threshold=50,
                            lines=np.array([]),
                            minLineLength=40,
                            maxLineGap=100)
    # Using the probabilistic hough lines transform
    # Returns the line vector of all the lines which are detected inside the image provided as the source

    if lines is not None:
        image_with_lines =  draw_the_lines(image, lines)
        return image_with_lines

    else:
        return image

cap = cv2.VideoCapture("test_road.mp4")

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        frame = process(frame) # Processing the frame to draw lines
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()