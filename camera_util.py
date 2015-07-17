import cv2
#from picamera import *


class Camera:
    @staticmethod
    def camera_capture_instance(capture_mode):
        cap = None
        cam = None
        if capture_mode == "opencv":
            cap = cv2.VideoCapture(0)
        elif capture_mode == "picamera":
            cam = PiCamera()
            cam.resolution = (640, 480)
            cap = PiRGBArray(cam, size=(640, 480))
        else:
            raise Exception("Unsupported camera type")
        return cap, cam

    @staticmethod
    def get_frame_iterator(capture_mode, cap, cam):
        if capture_mode == "opencv":
            return iter(int, 1)
        elif capture_mode == "picamera":
            return cam.capture_continuous(cap, format="bgr", use_video_port=True)

    @staticmethod
    def read_frame(capture_mode, iterated, cap):
        if capture_mode == "opencv":
            return cap.read()[1]
        elif capture_mode == "picamera":
            return iterated.array
