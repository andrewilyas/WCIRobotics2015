import os
from cv import *
from cv2 import *
import numpy
import sys
import cv2

__author__ = 'hc'

#This is the main script so yeah...

import lib.libScX_GUI.ShowImage
import lib.libScX_GUI.ShowMenu
import lib.libScX_GUI.FileChooser

def showDemoImage():
    lib.libScX_GUI.ShowImage.showImage(imageFile="img/demo.gif", caption="Demo Image")

def testLineBasic():
    file = lib.libScX_GUI.FileChooser.fileChooser(title="Image to Process")

    #Set Destination File
    nothingHeretoUse, fileExtension = os.path.splitext(file)
    dst_file = "img/dst" + fileExtension

    #Read the image file
    src = cv2.imread(file)
    dst = cvtColor(src, CV_BGR2GRAY)
    dst_img = src

    masterThreshold = 5
    sensitivity = 100 #100 is lowest sensitivity, 1 is highest (higher sensitivity, longer time, the sensitivity is auto adjusted)

    cannyThreshold1 = 100
    cannyThreshold2 = 100
    houghLinesThreshold = 200
    linesFound = 0
    thresholdFound = False

    oldCannyThreshold1 = cannyThreshold1
    oldCannyThreshold2 = cannyThreshold2
    while thresholdFound != True:
        edges = cv2.Canny(cvtColor(src, CV_BGR2GRAY), threshold1=cannyThreshold1, threshold2=cannyThreshold2,apertureSize = 3)
        #OPTIONAL REMOVED: , 80,lines, 30, 10

        lines = cv2.HoughLines(edges,1,CV_PI/180,houghLinesThreshold)
        errorFound = False
        try:
            for rho,theta in lines[0]:
                linesFound = linesFound + 1
                a = numpy.cos(theta)
                b = numpy.sin(theta)
                x0 = a*rho
                y0 = b*rho
                x1 = int(x0 + 1000*(-b))
                y1 = int(y0 + 1000*(a))
                x2 = int(x0 - 1000*(-b))
                y2 = int(y0 - 1000*(a))
                #cv2.line(dst_img,(x1,y1),(x2,y2),(0,0,255),2)
        except (TypeError):
            #No lines found lower sensitivity
            errorFound = True
            print "Sensitivity too high! Lowering sensitivity by 10 (new sensitivity is: " + str(sensitivity) + ")"
            if(sensitivity == 10):
                print "Sensitivity too low to adjust further, aborting"
                errorFound = True
                thresholdFound = True
            else:
                sensitivity = sensitivity - 10
                cannyThreshold1 = oldCannyThreshold1
                cannyThreshold2 = oldCannyThreshold2
        if linesFound <= masterThreshold and errorFound == False:
            thresholdFound = True
            print str(linesFound) + " is enough to exit loop!"

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