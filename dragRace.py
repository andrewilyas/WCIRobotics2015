#This is a program for the drag race section
from cv2.cv import *
import cv2 #Importing OpenCV into the file
import numpy as np #Import number processing library as np

def polar2cart(rho, theta):     #converts polar to cart
    x = rho*np.cos(theta)
    y = rho*np.sin(theta)
    return x,y

def detectLines(src, threshold=5, cannyThreshold1=100, cannyThreshold2=100, houghLinesThreshold=200, startingSensitivity=100):
    #Some other variables...
    linesFound = 0
    thresholdFound = False
    newCannyThreshold1 = cannyThreshold1
    newCannyThreshold2 = cannyThreshold2
    sensitivity = startingSensitivity

    #================[Actual Code]================#

    while thresholdFound != True:
        edges = cv2.Canny(cv2.cvtColor(src, CV_BGR2GRAY), threshold1=newCannyThreshold1, threshold2=newCannyThreshold2,apertureSize = 3)
        lines = cv2.HoughLines(edges,1,CV_PI/180,houghLinesThreshold)

        errorFound = False
        try:
            #Count the lines
            for rho,theta in lines[0]:
                linesFound = linesFound + 1

        except (TypeError):
            #No lines found so more sensitivity please...
            errorFound = True
            if(sensitivity <= 10):
                print "Sensitivity too low to adjust further, aborting..."
                errorFound = True
                thresholdFound = True
            else:
                #Increase sensitivity
                print "Sensitivity too low! Increasing sensitivity by 10 (new sensitivity is: " + str(sensitivity) + ")"
                sensitivity = sensitivity - 10 #The "-" here is not a mistake, the sensitivity is backwards...
                newCannyThreshold1 = cannyThreshold1
                newCannyThreshold2 = cannyThreshold2

        if linesFound <= threshold and errorFound == False:
            thresholdFound = True
            print "Jackpot buddy, we've got the right amount of lines: " + str(linesFound)

            #WE ARE DONE :)
            return lines[0]
        else:
            if errorFound == False:
                print "Too many lines (" + str(linesFound) + ") continuing search!"
                newCannyThreshold1 = newCannyThreshold1 + sensitivity
                newCannyThreshold2 = newCannyThreshold2 + sensitivity
                linesFound = 0

c = cv2.VideoCapture(0) #Initialize the video capture instance, 0 refers to the webcam number
while True:
    _,f = c.read() #Getting the image from the camera
    print f
    arrCoords = detectLines(np.asarray(f[:,:]))
    for line in arrCoords:
        print line
        x, y = polar2cart(line[0], line[1]) #Calls the polar2cart function        
        x1, x2, y1, y2 = x[0], x[1], y[0], y[1]
        cv2.line(f, (x1, y1), (x2, y2), (0,0,0))
    f = cv2.cvtColor(f, CV_BGR2GRAY)
    cv2.imshow("Webcam feed", f) #Show the image with Title "Webcam Feed"
    if cv2.waitKey(5) == 27: #Wait for 5ms for a Ctrl+W, break if found
        break
cv2.destroyAllWindows()
