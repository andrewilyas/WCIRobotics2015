import cv2
from heuristics import Heuristics
from camerahelper import CameraHelper as ch

class Thresholding:
    @staticmethod
    def checkThresh(image, heuristic):
        heuristic.refreshFrame(image)
        if len(heuristic.lines)*(lineAngles['LeftStd'] + lineAngles['RightStd']) < 5:
            return True
        else:
            return False

    @staticmethod
    def findThresh(cap):
        h = Heuristics()
        thresh = 60
        while True:
            thresh += 10
            ret, frame = cap.read()
            h.refreshFrame(frame)
            frame = ch.resizeImage(frame, 4, 4)
            lineAngles = h.lineAngles()
            cv2.imshow('hi', h.lineIMG)
            if cv2.waitKey(1000) and 0xFF == ord('q'):
                break
            if (len(h.lines)*(lineAngles['LeftStd'] + lineAngles['RightStd']) < 5 and len(h.lines) < 50 and (lineAngles['Left'] > 45 or lineAngles['Right'] > 45)):
                return thresh
            if thresh > 255:
                return None
