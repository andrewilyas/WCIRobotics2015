import cv2
from math import *
from camerahelper import CameraHelper

class Heuristics:
    ch = CameraHelper(bottomfov=11, middlefov=29, cameraheight=36, focallength=0.28, pixelheight = 1024)

    def lineAngles(self, image):
        gray = ch.grayscaleImage(image)
        thresholded = ch.nonAdaptiveThreshold(gray)
        cutImage = thresholded[-300:-100, :] #TODO: MAKE THIS DYNAMIC
        lines = ch.findLines(gray)[0]
        negatives = []
        positives = []
        for (x1, y1, x2, y2) in lines[0]:
            try:
                x = atan(float(y2-y1)/float(x2-x1))
                if x < 0:
                    negatives += [abs(x)]
                else:
                    positives += [x]
            except:
                pass
        return {'Left': degrees(np.mean(negatives), 'Right': degrees(np.mean(positives)}

    def threeDimensions(self, image):
        gray = ch.grayscaleImage(image)
        thresholded = ch.nonAdaptiveThreshold(gray)
        cutImage = thresholded[-300:-100, :] #TODO: MAKE THIS DYNAMIC
        lines = ch.findLines(gray)[0]
        leftPoint = (-1, -1)
        rightPo
        #TODO: Integrate

    def linesLengths(self, image):
        #TODO: Lenghts of left and right lines 
