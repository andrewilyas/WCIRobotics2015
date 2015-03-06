#This is a program for the drag race section
from cv2.cv import *
import cv2 #Importing OpenCV into the file
import numpy as np #Import number processing library as np
c = cv2.VideoCapture(0) #Initialize the video capture instance, 0 refers to the webcam number
while True:
    _,f = c.read() #Getting the image from the camera
    f = cv2.cvtColor(f, CV_BGR2GRAY)
    cv2.imshow("Webcam feed", f) #Show the image with Title "Webcam Feed"
    arrCoords = lineDetect(f)
    for line in arrCoords:
        
    if cv2.waitKey(5) == 27: #Wait for 5ms for a Ctrl+W, break if found
        break
cv2.destroyAllWindows()
