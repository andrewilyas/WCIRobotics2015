import cv2 as cv
from heuristics import Heuristics
from camerahelper import CameraHelper

class Thresholding:
    @staticmethod
    def check_threshold(image, thresh):
        lines, image, exception = Heuristics.parse_frame(image, thresh)
        if exception:
            if type(exception).__name__ != "TypeError":
                raise exception
        else:
            angles = Heuristics.get_angle_info(lines)
            print "Found %s lines" % len(lines)
            if len(lines) < 10 and (len(lines) * (angles['LeftStd'] + angles['RightStd']) < 5) and (
                    angles['Left'] > 45 or angles['Right'] > 45):
                cv.imshow('frame', image)
                return True
            else:
                return False

    @staticmethod
    def find_threshold(cap):
        thresh = 10
        while True:
            ret, frame = cap.read()
            cv.imshow('original', frame)
            frame = CameraHelper.resize_image(frame, 4, 4)
            if Thresholding.check_threshold(frame, thresh):
                return thresh
            thresh += 10

    def __init__(self):
        raise Exception("Cannot instantiate helper class")