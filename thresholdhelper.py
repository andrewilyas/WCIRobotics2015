import cv2 as cv
from heuristichelper import HeuristicHelper
from camerahelper import CameraHelper

class ThresholdHelper:
    @staticmethod
    def check_threshold(image, threshold):
        lines, image, exception = HeuristicHelper.parse_frame(image, threshold)
        if exception:
            if type(exception).__name__ != "TypeError":
                raise exception
        else:
            angles = HeuristicHelper.get_angle_info(lines)
            if len(lines) < 20 and (len(lines) * (angles['LeftStd'] + angles['RightStd']) < 5) and (
                    angles['Left'] > 45 or angles['Right'] > 45):
                return True
            else:
                return False

    @staticmethod
    def find_threshold(cap):
        thresh = 10
        while True:
            ret, frame = cap.read()
            frame = CameraHelper.resize_image(frame, 4, 4)
            if ThresholdHelper.check_threshold(frame, thresh):
                return thresh
            thresh += 10

    def __init__(self):
        raise Exception("Cannot instantiate helper class")