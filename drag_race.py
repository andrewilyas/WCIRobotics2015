from adaptiveThresh import Thresholding #static
from heuristics import Heuristics
from camerahelper import CameraHelper as ch
from camera_util import Camera
#from picamera import PiCamera, PiRGBArray
import sys
import cv2
import time

def main_loop():
    capture_mode = str(sys.argv[1])
    cap, cam = Camera.camera_capture_instance(capture_mode)
    iterator = Camera.get_frame_iterator(capture_mode, cap, cam)
    h = Heuristics()
    for x in iterator:
        if Thresholding.checkThresh():
            image = Camera.read_frame(capture_mode, x, cap)
            cv2.imshow("Frame", image)
            cv2.waitKey(1)
        else:
            #TODO: Find a way to integrate thresholding into the loop
            break





cap.release()
cv2.destroyAllWindows()

time.sleep(0.1)
