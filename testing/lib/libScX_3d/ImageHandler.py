import os
import PIL
import cv2

__author__ = 'hc'

#Deals with pictures :/

#Reads an image into cv2
#Arguments:
#path: The path of the image
def readCV2Image(path):
    src = cv2.imread(path)

    #Get file extension
    nothingHeretoUse, extension = os.path.splitext(path)

    return src, extension

#Writes an image to disk
#Arguments:
#path: The path to the output file
def writeCV2Image(imgData, path):
    cv2.imwrite( path, imgData );

def readTKImage(path):
    image = PIL.Image.open(path)

    #Get file extension
    nothingHeretoUse, extension = os.path.splitext(path)

    return image, extension

#Arguments:
#imgData: The OpenCV image data
#targetBGR1: The first RGB of the target color range
#targetBGR2: The second RGB of the target color range
#Example: filterImage(imgData, (255,255,255), (0,0,0))
#WARNING THE NUMBERS IN targetBGR1 SHOULD ALWAYS BE BIGGER THAT THE NUMBERS IN targetBGR2
def filterImage(imgData, targetBGR1, targetBGR2):
    targetBGR1 = (255,255,255)
    targetBGR2 = (0,0,0)
    outImgData = imgData
    rows, cols, somethingUseless = outImgData.shape
    for x in range(0,rows-1):
        for y in range(0,cols-1):
            curBlue, curGreen, curRed = outImgData[x,y]
            tB1, tG1, tR1 = targetBGR1
            tB2, tG2, tR2 = targetBGR2
            inRange = False
            if tB2 <= curBlue <= tB1:
                if tG2 <= curGreen <= tG1:
                    if tR2 <= curRed <= tR1:
                        inRange = True
            if not inRange:
                outImgData[x,y] = (0,0,0)
    return outImgData
