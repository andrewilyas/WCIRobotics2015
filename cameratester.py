#A PROGRAM BUILT TO TEST THINGS USING CAMERAHELPER.PY
import cv2
import matplotlib.pyplot as plt
from camerahelper import CameraHelper
from math import *
import numpy as np

ch = CameraHelper(bottomfov=11,middlefov=29,cameraheight=36,focallength=0.28, pixelheight = 1024)
image = cv2.imread('TestData/IMG_2156.JPG')
#print ch.realScreen(350, 0)
gray = ch.nonAdaptiveThreshold(ch.grayscaleImage(image))
gray = ch.resizeImage(gray, 4, 4)[-300:-100, :]
lines = ch.findLines(ch.grayToRGB(gray))
negatives = []
positives = []
for (x1, y1, x2, y2) in lines[0]:
    try:
        x = atan(float(y2-y1)/float(x2-x1))
        if x < 0:
            negatives += [abs(x)]
        else:
            positives += [x]
    except:
        pass
print "Left:", degrees(np.mean(negatives))
print "Right:", degrees(np.mean(positives))

cv2.imshow('color image', lines[1])
cv2.waitKey(0)                 # Waits forever for user to press any key
cv2.destroyAllWindows()        # Closes displayed windows
