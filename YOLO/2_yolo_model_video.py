import cv2
import numpy as np

net = cv2.dnn.readNet('yolov3.weights', 'yolov3.cfg') # Values are for RGB format
classes = [] 
with open('coco.names', 'r') as f:
    classes = f.read().splitlines()

#img = cv2.imread("image.jpg") # Image is read in BGR format

cap = cv2.VideoCapture('1_yolo.mp4') # Link to the Video file that is to be read

while True:

    _, img = cap.read()

    height, width, _ = img.shape

    blob = cv2.dnn.blobFromImage(img, 1/255, (416, 416), (0, 0, 0), swapRB=True, crop=False)
    # (image, scaling, size of the image, mean subtraction is (0,0,0), BGR2RGB, crop the image)
    # Optionally resizes and crops image from center, subtract mean values,
    # scales values by scalefactor, swap Blue and Red channels.
    net.setInput(blob) # Set input form the block into the network
    output_layer_names = net.getUnconnectedOutLayersNames() # Get the output layers names
    layerOutputs = net.forward(output_layer_names) # Output will be obtained

    boxes = [] # extract bounding boxes
    confidences = [] # to store the confidence
    class_ids = [] # classes ids, stores their predicted classes

    for output in layerOutputs: # extract more info from the layers' outputs
        for detection in output: # extract info from each of the outputs 
            # for each detection - it should contain bounding box, offset, 1 box confidence goals, 
            # 80 class predictions probably 85 parameters overall
            # First for parameters are the locations of the bounding boxes and 5th is the box confidence i.e., 
            # how likely it is that the box contains an object and 80 class predictions probability
            scores = detection[5:] # 6th element to the end
            class_id = np.argmax(scores) # Gives the index of max value
            confidence = scores[class_id] # The confidence/probability of detection
            if confidence > 0.5:
                # Getting dimensions of the bounding box from detection
                center_x = int(detection[0] * width) # The values are normalized, so we need to scale them
                center_y = int(detection[1] * height)
                w = int(detection[2] * width)
                h = int(detection[3] * height)

                x = int(center_x - w/2)
                y = int(center_y - h/2)

                boxes.append([x, y, w, h])
                confidences.append(float(confidence))
                class_ids.append(class_id)

    #print(len(boxes))
            
    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
    #print(indexes.flatten())
    font = cv2.FONT_HERSHEY_PLAIN
    colors = np.random.uniform(0, 255, size=(len(boxes), 3))

    for i in indexes.flatten():
        x, y, w, h = boxes[i] # identify all the boxes detected
        label = str(classes[class_ids[i]]) # Classes list will tell us the class the object belongs to
        confidence = str(round(confidences[i], 2))
        color = colors[i]
        cv2.rectangle(img, (x, y), (x+w, y+h), color, 2)
        cv2.putText(img, label+" "+confidence, (x, y+20), font, 2, (255, 255, 255), 2) 
        # put text on upper left corner of img of the image

    cv2.imshow('Image', img)
    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
