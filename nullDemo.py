import os
from cv import *
from cv2 import *
import numpy
import sys
import cv2

__author__ = 'hc'

#This is the main script so yeah...
#There is a lot of code in this, I will move it into files soon...

import lib.libScX_GUI.ShowImage
import lib.libScX_GUI.ShowMenu
import lib.libScX_GUI.FileChooser

#This function just tests if you have installed ImageTK
def showDemoImage():
    lib.libScX_GUI.ShowImage.showImage(imageFile="img/demo.gif", caption="Demo Image")

#TODO Move this to a separate file
#This is an implementation of HoughLines that auto-adjusts the threshold for each image.
def testLineBasic():

    #Adjustable Variables
    masterThreshold = 5 #This is the master threshold, it controls the optimal number of lines detected

    #Canny and Houghlines stuff
    cannyThreshold1 = 100 #This is the starting Canny Threshold1, it is auto adjusted (You shouldn't touch this)
    cannyThreshold2 = 100 #This is the starting Canny Threshold2, it is auto adjusted (You shouldn't touch this)
    houghLinesThreshold = 200 #This is the HoughLines Threshold, it is constant, change it if you want...

    #Some other variables...
    sensitivity = 100 #This is the starting sensitivity, you shouldn't touch it... (It's also backwards)
    linesFound = 0
    thresholdFound = False
    oldCannyThreshold1 = cannyThreshold1
    oldCannyThreshold2 = cannyThreshold2

    #================[Actual Code]================#

    #Select the file
    file = lib.libScX_GUI.FileChooser.fileChooser(title="Image to Process")

    #Set Destination File
    nothingHeretoUse, fileExtension = os.path.splitext(file)
    dst_file = "img/dst" + fileExtension

    #Read the image file
    src = cv2.imread(file)
    dst = cvtColor(src, CV_BGR2GRAY)
    dst_img = src

    while thresholdFound != True:
        edges = cv2.Canny(cvtColor(src, CV_BGR2GRAY), threshold1=cannyThreshold1, threshold2=cannyThreshold2,apertureSize = 3)
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
                cannyThreshold1 = oldCannyThreshold1
                cannyThreshold2 = oldCannyThreshold2

        if linesFound <= masterThreshold and errorFound == False:
            thresholdFound = True
            print "Jackpot buddy, we've got the right amount of lines: " + str(linesFound)

            #Write the lines to image
            for rho,theta in lines[0]:
                a = numpy.cos(theta)
                b = numpy.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))
                cv2.line(dst_img,(x1,y1),(x2,y2),(0,0,255),2)
        else:
            if errorFound == False:
                print "Too many lines (" + str(linesFound) + ") continuing search!"
                cannyThreshold1 = cannyThreshold1 + sensitivity
                cannyThreshold2 = cannyThreshold2 + sensitivity
                linesFound = 0

    imwrite( dst_file, dst_img );
    lib.libScX_GUI.ShowImage.showImage(imageFile=dst_file, caption="Result")

def main(argv=None):
    #Dynamically fill the arguments (Cause I'm smart...)
    if argv is None:
        argv = sys.argv

    #Show this demo image for now...
    lib.libScX_GUI.ShowMenu.init_menu()
    lib.libScX_GUI.ShowMenu.add_button(text="Show Demo Image",side="LEFT",function=showDemoImage)
    lib.libScX_GUI.ShowMenu.add_button(text="Test Line Recognition",side="LEFT",function=testLineBasic)
    lib.libScX_GUI.ShowMenu.show_menu()

if __name__ == "__main__":
    sys.exit(main()) #Sys.exit would usually make Python exit so here is a workaround