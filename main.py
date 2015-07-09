import cv2 as cv
from thresholdhelper import ThresholdHelper
from heuristichelper import HeuristicHelper
import time

capture = cv.VideoCapture(0)

while True:
    ret, frame = capture.read()
    cv.imshow('frame', frame)
    x = HeuristicHelper.get_light_info(frame)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

#threshold = ThresholdHelper.find_threshold(capture)
#print "Found threshold %s" % threshold



time.sleep(100)

capture.release()
cv.destroyAllWindows()