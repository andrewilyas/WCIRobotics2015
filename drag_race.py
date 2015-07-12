from adaptiveThresh import Thresholding #static
from heuristics import Heuristics
from camerahelper import CameraHelper as ch
from camera_util import Camera
from picamera import *
import sys
import cv2
import time
import atexit

def main_loop():
    iterator = Camera.get_frame_iterator(capture_mode, cap, cam)
    h = Heuristics()
    time.sleep(0.1)
    for x in iterator:
        if Thresholding.checkThresh():
            image = Camera.read_frame(capture_mode, x, cap)
            h.refreshFrame(image)
            print h.lineAngles()['Right'] > h.lineAngles()['Left']
            #cv2.imshow("Frame", image)
            #cv2.waitKey(1)
        else:
            print  "Needs to be rethresholded"

def exit_handler():
    cap.release()
    cv2.destroyAllWindows()

capture_mode = str(sys.argv[1])
cap, cam = Camera.camera_capture_instance(capture_mode)
atexit.register(exit_handler)
main_loop()
