import cv2

# Haar feature based cascade classifiers is a ML-based approach where a Cascade function is trained for 
# a lot of +ve and -ve images 
# First, a classifier is trained with a few hundred sample views of a particular object i.e. a face or a 
# car called +ve images(which contains the object to be detected).
# Similarly, it is trained with -ve images, i.e. images that don't contain the object to be detected
# After the classifier is trained, it can be applied to a region of interest in an input image 1-True 0-False

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# For images

# Read the input image
img = cv2.imread('messi5.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.1, 4)
# scaleFactor determines how much the image size is reduced at each image scale (here, 10%) 
# minNeighbours how many neighbours each candidate rectangle should have to retain it
# it's used to control the number of false positives and false negatives. 
# If minNeighbors is set to 0, the slightest hint of a face will be counted as a definitive face, 
# even if no other facial features are detected near it.

for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 3)

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# For Vidoes

# cap = cv2.VideoCapture('test.mp4')

# while cap.isOpened():
#     _, img = cap.read()

#     gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#     faces = face_cascade.detectMultiScale(gray, 1.1, 4) # Scale factor specifies how much image size is decreased

#     for (x, y , w ,h) in faces:
#         cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)

#     # Display the output
#     cv2.imshow('img', img)
#     if cv2.waitKey(1) & 0xFF == (ord('q')):
#         break

# cap.release()