import cv2 as cv
from adaptiveThresh import Thresholding
import time

capture = cv.VideoCapture(0)
threshold = Thresholding.find_threshold(capture)

print "Found threshold %s" % threshold

time.sleep(100)

capture.release()
cv.destroyAllWindows()