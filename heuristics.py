import cv2
from math import *
from camerahelper import CameraHelper as ch
import numpy as np

class Heuristics:
    camerastats = {'bottom_fov': 28, 'middle_fov':68, 'camera_height': 21, 'focal_length':0.36, 'pixel_height': 2448, 'pixel_width': 3264}
    image = None
    lines = None
    pixel_offset = None
    cutImage = None

    def refreshFrame(self, image, camerastats=None, thresh=210):
        self.image = image
        self.camerastats['pixel_width'] = max(image.shape[0], image.shape[1])
        self.camerastats['pixel_height'] = min(image.shape[0], image.shape[1]) 
        gray = ch.grayscaleImage(image)
        thresholded = ch.nonAdaptiveThreshold(gray, thresh=thresh)
        ts = thresholded.shape[0]
        self.cutImage = thresholded[int(-ts*0.40):int(-ts*0.15), :]
        self.pixel_offset = int(ts*0.15)
        if camerastats:
            self.camerastats = camerastats
        try:
            lines = ch.findLines(ch.grayToRGB(self.cutImage))
            self.lines = lines[0]
            self.lineIMG = lines[1]
            cv2.imshow("frame", self.lineIMG)
            cv2.waitKey(1)
        except Exception, e:
            self.lines = []
            self.lineIMG =  self.cutImage
            print e

    def traffic_light(self):
        return float(ch.colourCount(self.image, [0, 0, 150], [50, 50, 255]))/float(ch.colourCount(self.image, [0, 100, 0], [50, 255, 50])+0.1)

   
    def average_angle(self):
        slopes = []
        for (x1, y1, x2, y2) in self.lines:
            x = float(y2-y1)/float(0.00001+x2-x1)
            slopes += [x]
        return {
            'lines_angle': degrees(atan(np.mean(slopes))),
            'lines_slope': np.mean(slopes),
            'std_dev': np.std(slopes)
            }

    def threeDimensions(self):
        line_angles = self.average_angle()
        print line_angles
        avg_slope = line_angles['lines_slope']

        min_slope = 100
        min_line = None
        length = None
        for x1, y1, x2, y2 in self.lines:
            slope = float(y2-y1)/float(x2-x1+0.00001)
            length = ((y2-y1)**2 + (x2-x1)**2)**0.5
            if (abs(slope-avg_slope) < min_slope or min_line == None):
                min_slope = abs(slope-avg_slope)
                min_line = (x1, (0.25*self.image.shape[0] - y1)+self.pixel_offset, x2, (0.25*self.image.shape[0]-y2)+self.pixel_offset)


        real_point_one = ch.realScreen(min_line[3], min_line[2], self.camerastats)
        real_point_two = ch.realScreen(min_line[1], min_line[0], self.camerastats)

        real_slope = float(real_point_one[1] - real_point_two[1]) / float(0.00001 + real_point_one[0] - real_point_two[0])
        print min_line, real_point_one, real_point_two
        return degrees(atan(real_slope))
