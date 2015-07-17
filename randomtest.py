from adaptiveThresh import Thresholding #static
from heuristics import Heuristics
from camerahelper import CameraHelper as ch
from camera_util import Camera
#from picamera import *
import sys
import cv2
import time
import atexit
import numpy as np

def main_loop():
    iterator = Camera.get_frame_iterator("opencv", cap, cam)
    h = Heuristics()
    for x in iterator:
        image = cv2.flip(Camera.read_frame("opencv", x, cap), -1)
        if image != None:
            #h.refreshFrame(image)
            cv2.imshow("hello", image)
            cv2.waitKey(1)
            print ch.colourCount(image, minColor = [200, 0, 0], maxColor=[255, 255, 255])

cap, cam = Camera.camera_capture_instance("opencv")
main_loop()
