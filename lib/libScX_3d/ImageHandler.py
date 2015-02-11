import os
import cv2

__author__ = 'hc'

#Deals with pictures :/

#Reads an image into cv2
#Arguments:
#path: The path of the image
def readImage(path):
    src = cv2.imread(path)

    #Get file extension
    nothingHeretoUse, extension = os.path.splitext(path)

    return src, extension

#Writes an image to disk
#Arguments:
#path: The path to the output file
def writeImage(imgData, path):
    cv2.imwrite( path, imgData );