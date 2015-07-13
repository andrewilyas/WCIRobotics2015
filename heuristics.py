import cv2
from math import *
from camerahelper import CameraHelper as ch
import numpy as np

class Heuristics:
    camerastats = {'bottomfov': 16, 'middlefov':55, 'cameraheight': 76, 'focallength':0.29, 'pixelheight': 2448, 'pixelwidth': 3264}
    image = None
    lines = None
    pixelOffset = None
    cutImage = None

    def refreshFrame(self, image, camerastats=None, thresh=120):
        self.image = image
        gray = ch.grayscaleImage(image)
        thresholded = ch.nonAdaptiveThreshold(gray, thresh=thresh)
        ts = thresholded.shape[0]
        self.cutImage = thresholded[int(-ts*0.40):int(-ts*0.15), :]
        self.pixelOffset = int(ts*0.15)
        if camerastats:
            self.camerastats = camerastats
        try:
            lines = ch.findLines(ch.grayToRGB(self.cutImage))
            self.lines = lines[0]
            self.lineIMG = lines[1]
        except Exception, e:
            self.lines = []
            self.lineIMG =  self.cutImage
            print e

    def traffic_light(self):
        ch = self.ch
        return float(ch.colourCount(self.image, [0, 0, 150], [50, 50, 255]))/float(ch.colourCount(self.image, [0, 100, 0], [50, 255, 50])+0.1)

    def average_angle(self):
        slopes = []
        for (x1, y1, x2, y2) in self.lines:
            x = atan(float(y2-y1)/float(0.0001+x2-x1))
            slopes += [x]
        return {
            'lines_angle': degrees(np.mean(slopes)),
            'lines_slope': tan(np.mean(slopes)),
            'std_dev': np.std(slopes)
            }

    def threeDimensions(self):
        ch = self.ch
        line_angles = self.average_angle()
        avg_slope = line_angles['lines_slope']

        min_slope = 100
        min_line = None
        for x1, y1, x2, y2 in self.lines:
            slope = float(y2-y1)/float(0.001+x2-x1)
            length = ((y2-y1)**2 + (x2-x1)**2)**0.5
            if (abs(slope-avg_slope) < min_slope or min_line == None):
                min_slope = abs(slope-avg_slope)
                min_line = (x1, y1+200, x2, y2+200)

        real_point_one = ch.realScreen(min_line[3], min_line[2])
        real_point_two = ch.realScreen(min_line[1], min_line[0])

        real_slope = float(realRightOne[1] - realRightTwo[1]) / float(0.0001 + realRightOne[0] - realRightTwo[0])
        return degrees(atan(realRightSlope)), degrees(atan(realLeftSlope))
