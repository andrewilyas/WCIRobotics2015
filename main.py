import cv2 as cv
from thresholdhelper import ThresholdHelper
from heuristichelper import HeuristicHelper
from camerahelper import CameraHelper
import time
from matplotlib import pyplot as plt

# capture = cv.VideoCapture(0)
#
# threshold = ThresholdHelper.find_threshold(capture)
# print "Found threshold %s" % threshold
#
# while True:
#     ret, img = cv.read()
#     lines, i, e = HeuristicHelper.parse_frame(img, threshold)
#     pers = HeuristicHelper.adjust_perspective(lines)
#     print pers
#
# time.sleep(100)
#
# capture.release()
# cv.destroyAllWindows()

CameraHelper.real_screen(10, 4)