import cv2 as cv
from thresholdhelper import ThresholdHelper
import time

capture = cv.VideoCapture(0)
threshold = ThresholdHelper.find_threshold(capture)

print "Found threshold %s" % threshold

time.sleep(100)

capture.release()
cv.destroyAllWindows()