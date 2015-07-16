from adaptiveThresh import Thresholding #static
from heuristics import Heuristics
from camerahelper import CameraHelper as ch
from camera_util import Camera
from picamera import *
import sys
import cv2
import time
import atexit
from arduino import Arduino
import numpy as np


def main_loop():
    iterator = Camera.get_frame_iterator(capture_mode, cap, cam)
    h = Heuristics()
    a = Arduino()
    time.sleep(1)
    a.move_camera(170)
    a.drive_forward(10)
    for x in iterator:
        image = cv2.flip(Camera.read_frame(capture_mode, x, cap), -1)
        if image != None:
            h.refreshFrame(image)
            if True:#len(h.lines) == 0:
                print "No lines"
                #a.turn_servo(80)
            else:
                angle = h.threeDimensions()
                if angle < 0:
                    a.turn_servo(np.max([90-(90+angle)/2, 60]))
                else:
                    a.turn_servo(np.min([90+(90-angle)/2, 140]))
                print angle
        else:
            print "No image"

def exit_handler():
    cap.release()
    cv2.destroyAllWindows()

capture_mode = str(sys.argv[1])
cap, cam = Camera.camera_capture_instance(capture_mode)
atexit.register(exit_handler)
main_loop()
