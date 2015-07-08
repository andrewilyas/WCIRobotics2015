#A PROGRAM BUILT TO TEST THINGS USING CAMERAHELPER.PY
import cv2
import matplotlib.pyplot as plt
from camerahelper import CameraHelper
from math import *
import numpy as np
from heuristics import Heuristics

h = Heuristics(cv2.imread())

# cap = cv2.VideoCapture(0)
# while True:
#     ret, frame = cap.read()
#     cv2.imshow('hello', frame)
#     if cv2.waitKey(100) and 0xFF == ord('q'):
#         break
#     #print frame.shape
#     h = Heuristics(frame)
#     print h.trafficLight()
#
# cap.release()
# cv2.destroyAllWindows()
#ch = CameraHelper(bottomfov=39,middlefov=99,cameraheight=76,focallength=0.29, #pixelheight = 2448, pixelwidth = 3264)
#print ch.realScreen(1770, 0)
# ch g CameraHelper(bottomfov=10,middlefov=19,cameraheight=10.4,focallength=0.36, pixelheight = 1944, pixelwidth = 2592)
# image = cv2.imread('TestData/IMG_2156.JPG')
# #print ch.realScreen(350, 0)
# print ch.realScreen(1210, 1551)
# gray = ch.nonAdaptiveThreshold(ch.grayscaleImage(image))
# gray = ch.resizeImage(gray, 4, 4)[-300:-100, :]
# lines = ch.findLines(ch.grayToRGB(gray))
# negatives = []
# positives = []
# for (x1, y1, x2, y2) in lines[0]:
#     try:
#         x = atan(float(y2-y1)/float(x2-x1))
#         if x < 0:
#             negatives += [abs(x)]
#         else:
#             positives += [x]
#     except:
#         pass
# print "Left:", degrees(np.mean(negatives))
# print "Right:", degrees(np.mean(positives))
#
# cv2.imshow('color image', lines[1])
# cv2.waitKey(0)                 # Waits forever for user to press any key
# cv2.destroyAllWindows()        # Closes displayed windows
