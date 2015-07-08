import cv2
import numpy as np
from math import *

class CameraHelper:
    @staticmethod
    def thresholdImage(image, maxValue=255, blockSize=11, C=2):
        return cv2.adaptiveThreshold(image, maxValue, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, blockSize, C)

    @staticmethod
    def nonAdaptiveThreshold(image, maxval=255, thresh=140):
        ret, thresh = cv2.threshold(image, thresh, maxval, cv2.THRESH_BINARY)
        return thresh

    @staticmethod
    def colourCount(image, minColor, maxColor):
        BLUE_MIN = np.array(minColor, np.uint8)
        BLUE_MAX = np.array(maxColor, np.uint8)

        dst = cv2.inRange(image, BLUE_MIN, BLUE_MAX)
        no_blue = cv2.countNonZero(dst)
        return no_blue

    @staticmethod
    def realScreen(y, x, camerastats):
        h = float(camerastats['cameraHeight'])
        f = float(camerastats['focalLength'])
        m = float(camerastats['middleFOV'])
        b = float(camerastats['bottomFOV'])
        p = float(camerastats['pixelHeight'])
        pw = float(camerastats['pixelWidth'])
        R = sqrt(h**2+m**2)
        sinA = h/R
        cosA = m/R
        smallToBig = sqrt(h**2 + m**2)/f #Conversion between real and camera triangles (cm)
        screenHeight = 2*f*(h*m-h*b)/(m*b+h**2) #Height of camera screen (cm)
        pixToReal = screenHeight/p
        realTriangle = h/(f*sinA + (p/2 - y)*pixToReal*cosA)
        smallTriangleResult = f*cosA - (p/2 - y)*pixToReal*sinA
        vertResult = realTriangle*smallTriangleResult

        #HORIZONTAL STUFF
        horiConversion = sqrt((h**2 + vertResult**2)/(f**2 + ((p/2 - y)*pixToReal)**2))
        horiResult = (pw/2-x)*pixToReal*horiConversion

        return (horiResult, vertResult)

    @staticmethod
    def findLinesP(image, minLineLength=100, maxLineGap=10):
        edges = cv2.Canny(image,50,150,apertureSize = 3)
        lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)
        linesArr = []
        for x1,y1,x2,y2 in lines[0]:
            linesArr += [(x1, y1, x2, y2)]
            cv2.line(image,(x1,y1),(x2,y2), (255,0,0),2)
        return [linesArr, image]

    @staticmethod
    def findLines(image):
        edges = cv2.Canny(image,50,150,apertureSize = 3)
        lines = cv2.HoughLines(edges,1,np.pi/180,20)
        linesArr = []
        for rho,theta in lines[0]:
            a = np.cos(theta)
            b = np.sin(theta)
            x0 = a*rho
            y0 = b*rho
            x1 = int(x0 + 1000*(-b))
            y1 = int(y0 + 1000*(a))
            x2 = int(x0 - 1000*(-b))
            y2 = int(y0 - 1000*(a))
            linesArr += [(x1, y1, x2, y2)]
            cv2.line(image,(x1,y1),(x2,y2),(0,0,255),2)
        return [linesArr, image]

    @staticmethod
    def cropImage(self, image, (startx, endx), (starty, endy)):
        return image[starty:endy, startx:endx]

    @staticmethod
    def grayToRGB(self, image):
        return cv2.cvtColor(image,cv2.COLOR_GRAY2RGB)

    @staticmethod
    def resizeImage(self, image, xfactor, yfactor):
         newx,newy = image.shape[1]/xfactor,image.shape[0]/yfactor #new size (w,h)
         return cv2.resize(image,(newx,newy))

    @staticmethod
    def grayscaleImage(self, image):
        return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
