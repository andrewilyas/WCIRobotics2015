import cv2
from math import *
from camerahelper import CameraHelper
import numpy as np

class Heuristics:
    ch = CameraHelper(bottomfov=10,middlefov=19,cameraheight=10.4,focallength=0.36, pixelheight = 1944/4, pixelwidth = 2592/4)
    image = None
    lines = None

    def  __init__(self, image):
        ch = self.ch
        self.image = image
        gray = ch.grayscaleImage(image)
        thresholded = ch.nonAdaptiveThreshold(gray)
        #cutImage = ch.resizeImage(thresholded, 4, 4)[-400:-200, :]#[-1000:-200, :] #TODO: MAKE THIS DYNAMIC
        #self.lines = ch.findLines(cutImage)[0]
        #self.lineIMG = ch.findLines(ch.grayToRGB(cutImage))[1]

    def trafficLight(self):
        ch = self.ch
        return float(ch.colourCount(self.image, [0, 0, 150], [50, 50, 255]))/float(ch.colourCount(self.image, [0, 100, 0], [50, 255, 50])+0.1)

    def lineAngles(self):
        negatives = []
        positives = []
        for (x1, y1, x2, y2) in self.lines:
            try:
                x = atan(float(y2-y1)/float(0.0001+x2-x1))
                if x < 0:
                    negatives += [abs(x)]
                else:
                    positives += [x]
            except:
                pass
        return {
            'Left': degrees(np.mean(negatives)),
            'Right': degrees(np.mean(positives))
            }

    def threeDimensions(self):
        ch = self.ch
        lineAngles = self.lineAngles()
        print lineAngles
        leftSlope = tan(radians(lineAngles['Left']))
        rightSlope = tan(radians(lineAngles['Right']))

        minLeftSlope = 100
        minRightSlope = 100

        minLeftLine = None
        minRightLine = None

        for x1, y1, x2, y2 in self.lines:
            slope = float(y2-y1)/float(0.001+x2-x1)
            length = ((y2-y1)**2 + (x2-x1)**2)**0.5
            if (abs(slope-leftSlope) < minLeftSlope or minLeftLine == None) and length > 100:
                minLeftSlope = abs(slope-leftSlope)
                minLeftLine = (x1, y1+200, x2, y2+200)
            if (abs(slope-rightSlope) < minRightSlope or minRightLine == None) and length > 100:
                minRightSlope = abs(slope-rightSlope)
                minRightLine = (x1, y1+200, x2, y2+200)

        realRightOne = ch.realScreen(minRightLine[3], minRightLine[2])
        realRightTwo = ch.realScreen(minRightLine[1], minRightLine[0])

        realRightSlope = float(realRightOne[1] - realRightTwo[1]) / float(0.0001 + realRightOne[0] - realRightTwo[0])

        realLeftOne = ch.realScreen(minLeftLine[3], minLeftLine[2])
        realLeftTwo = ch.realScreen(minLeftLine[1], minLeftLine[0])

        realLeftSlope = float(realLeftTwo[1] - realLeftOne[1]) / float(0.0001 + realLeftTwo[0] - realLeftOne[0])

        print degrees(atan(realRightSlope)), degrees(atan(realLeftSlope))
