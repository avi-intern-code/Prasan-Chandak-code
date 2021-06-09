import cv2

# Haar feature based cascade classifiers is a ML-based approach where a Cascade function is trained for 
# a lot of +ve and -ve images 
# First, a classifier is trained with a few hundred sample views of a particular object i.e. a face or a 
# car called +ve images(which contains the object to be detected).
# Similarly, it is trained with -ve images, i.e. images that don't contain the object to be detected
# After the classifier is trained, it can be applied to a region of interest in an input image 1-True 0-False

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade =  cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')

# For Vidoes

cap = cv2.VideoCapture('test.mp4')

while cap.isOpened():
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4) # Scale factor specifies how much image size is decreased

    for (x, y , w ,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (255, 0 , 0), 3)
        roi_gray = gray[y:y+h, x:x+w] # ROI for eye detection lies within the face rectangle detected
        roi_color = img[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, eh, ew) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0, 255, 0), 5)

    # Display the output
    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == (ord('q')):
        break

cap.release()