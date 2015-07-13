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
        image = cv2.flip(Camera.read_frame(capture_mode, x, cap), -1)
        if image != None:
            h.refreshFrame(image)
            print h.threeDimensions()
        else:
            print "No image"
        #threshdata = Thresholding.checkThresh(image, h)
        #if threshdata[0]:
        #    h.refreshFrame(image)
        #    print h.lineAngles()['Right'] > h.lineAngles()['Left']
        #else:
        #    print threshdata[2]
        #    cv2.imwrite("/tmp/cameratest.png", threshdata[1])
        #    return

def exit_handler():
    cap.release()
    cv2.destroyAllWindows()

capture_mode = str(sys.argv[1])
cap, cam = Camera.camera_capture_instance(capture_mode)
atexit.register(exit_handler)
main_loop()
