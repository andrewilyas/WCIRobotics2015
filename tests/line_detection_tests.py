#!/usr/bin/python2

__package__ = "tests"
from lib import *
from cv2 import *

image = imread("test.jpg")
imwrite("detected_lines.jpg", line_detection.detectLines(image))