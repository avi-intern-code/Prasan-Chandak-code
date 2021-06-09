import cv2

path = "Megamind.avi"
cap = cv2.VideoCapture(path) # 0 if the defaut device camera is to be used otherwise the path of the video
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # Get width of the frame, 3 can also work for it
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # Get height of the frame, 4 can also work

cap.set(3, 3000) # Set width of the frame of the video 
cap.set(4, 3000) # Set height of the frame of the video
# the default camera will only set value acc to resolution that is available to it
print(cap.get(3)) # Prints the width of the image
print(cap.get(4)) # Prints the height

while(cap.isOpened()): # While the capture is initialized
    ret, frame = cap.read()
    if ret == True:

       #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # Convert to grayscale
       cv2.imshow('frame', frame)

       if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()