import cv2
import numpy as np

class CameraHelper:
    cameraHeight = None
    focalLength = None
    bottomFOV = None
    middleFOV = None
    def __init__(self, cameraheight, focallength, bottomfov, middlefov):
        self.cameraHeight = cameraheight
        self.focalLength = focallength
        self.bottomFOV = bottomfov
        self.middleFOV = middlefov

    def thresholdImage(self, image, maxValue=255, blockSize=11, C=2):
        return cv2.adaptiveThreshold(image, maxValue, cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY, blockSize, C)

    def findLines(self, image, minLineLength=100, maxLineGap=10):
        edges = cv2.Canny(image,50,150,apertureSize = 3)
        lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
        linesArr = []
        for x1,y1,x2,y2 in lines[0]:
            linesArr += [(x1, y1, x2, y2)]
            cv2.line(image,(x1,y1),(x2,y2),(0,255,0),2)
        return [linesArr, image]
