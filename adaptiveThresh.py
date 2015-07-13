import cv2
from heuristics import Heuristics
from camerahelper import CameraHelper as ch
from camera_util import Camera

class Thresholding:
    @staticmethod
    def checkThresh(image, heuristic):
        heuristic.refreshFrame(image)
        line_stats = heuristic.average_angle()
        return (False, heuristic.cutImage, line_stats)
        #if len(heuristic.lines)*(lineAngles['LeftStd'] + lineAngles['RightStd']) < 5:
        #    return True
        #else:
        #    return False

    @staticmethod
    def findThresh(cap):
        h = Heuristics()
        thresh = 60
        while True:
            thresh += 10
            ret, frame = cap.read() #TODO: Change this
            h.refreshFrame(frame)
            frame = ch.resizeImage(frame, 4, 4)
            lineAngles = h.average_angle()
            cv2.imshow('hi', h.lineIMG)
            if cv2.waitKey(1000) and 0xFF == ord('q'):
                break
            if lineAngles['std_dev'] < 0.1:
                return thresh
            if thresh > 255:
                return None
