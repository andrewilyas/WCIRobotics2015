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
        x, y = polar2cart(line[0], line[1])
        x1, x2, y1, y2 = x[0], x[1], y[0], y[1]
        cv2.line(f, (x1, y1), (x2, y2), (0,0,0))
    if cv2.waitKey(5) == 27: #Wait for 5ms for a Ctrl+W, break if found
        break
cv2.destroyAllWindows()

def polar2cart(rho, theta):
    x = rho*np.cos(theta)
    y = rho*np.sin(theta)
    return x,y

