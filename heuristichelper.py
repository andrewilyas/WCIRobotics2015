import cv2
from math import *
from camerahelper import CameraHelper
import numpy as np


class HeuristicHelper:
    @staticmethod
    def parse_frame(image, thresh):
        grayscale = CameraHelper.to_grayscale(image)
        thresholded = CameraHelper.non_adaptive_threshold(grayscale, thresh=thresh)
        ts = thresholded.shape[0]
        cutImage = thresholded[int(-ts * 0.40):int(-ts * 0.15), :]
        try:
            lines = CameraHelper.find_lines(CameraHelper.to_color(cutImage))
            return [lines[0], lines[1], None]
        except Exception, e:
            return [[], cutImage, e]

    @staticmethod
    def get_angle_info(lines):
        negatives = []
        positives = []
        for (x1, y1, x2, y2) in lines:
            try:
                x = atan(float(y2 - y1) / float(0.0001 + x2 - x1))
                if x < 0:
                    negatives += [abs(x)]
                else:
                    positives += [x]
            except:
                pass
        return {
            'Left': degrees(np.mean(negatives)),
            'Right': degrees(np.mean(positives)),
            'LeftStd': np.std(negatives),
            'RightStd': np.std(positives)
        }

    @staticmethod
    def get_light_info(image):  # Returns the ratio of red vs green
        x = float(CameraHelper.count_color(image, [0, 0, 150], [50, 50, 255]))
        y = float(CameraHelper.count_color(image, [0, 100, 0], [50, 255, 50]) + 0.1)
        print str(x) + ", " + str(y)
        return x / y

    def adjust_perspective(lines):
        lineAngles = HeuristicHelper.get_angle_info(lines)
        leftSlope = tan(radians(lineAngles['Left']))
        rightSlope = tan(radians(lineAngles['Right']))

        minLeftSlope = 100
        minRightSlope = 100

        minLeftLine = None
        minRightLine = None

        for x1, y1, x2, y2 in lines:
            slope = float(y2 - y1) / float(0.001 + x2 - x1)
            length = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
            if (abs(slope - leftSlope) < minLeftSlope or minLeftLine == None) and length > 100:
                minLeftSlope = abs(slope - leftSlope)
                minLeftLine = (x1, y1 + 200, x2, y2 + 200)
            if (abs(slope - rightSlope) < minRightSlope or minRightLine == None) and length > 100:
                minRightSlope = abs(slope - rightSlope)
                minRightLine = (x1, y1 + 200, x2, y2 + 200)

        realRightOne = CameraHelper.real_screen(minRightLine[3], minRightLine[2])
        realRightTwo = CameraHelper.real_screen(minRightLine[1], minRightLine[0])

        realRightSlope = float(realRightOne[1] - realRightTwo[1]) / float(0.0001 + realRightOne[0] - realRightTwo[0])

        realLeftOne = CameraHelper.real_screen(minLeftLine[3], minLeftLine[2])
        realLeftTwo = CameraHelper.real_screen(minLeftLine[1], minLeftLine[0])

        realLeftSlope = float(realLeftTwo[1] - realLeftOne[1]) / float(0.0001 + realLeftTwo[0] - realLeftOne[0])

        return degrees(atan(realRightSlope)), degrees(atan(realLeftSlope))

    def __init__(self):
        raise Exception("Cannot initialize helper class")
