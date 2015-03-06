from numpy.linalg import lstsq
from numpy.ma import vstack, ones

__author__ = 'nulldev'
#Author: nulldev (Git: null-dev)

import numpy

#Makes decisions from images

#TODO: Finish this
#THIS IS INCOMPLETE, DO NOT CALL IT
#Determines if an image is processable from a line array
def isSuitable(lines, tkImage):
    lineList = []
    for rho,theta in lines:
        a = numpy.cos(theta)
        b = numpy.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        lineList.append((x1,y1,x2,y2))

#Find the lines associated with the road...
def getRoadLines(lines, tkImage):
    lineList = []
    for rho,theta in lines:
        a = numpy.cos(theta)
        b = numpy.sin(theta)
        x0 = a*rho
        y0 = b*rho
        x1 = int(x0 + 1000*(-b))
        y1 = int(y0 + 1000*(a))
        x2 = int(x0 - 1000*(-b))
        y2 = int(y0 - 1000*(a))
        lineList.append((x1,y1,x2,y2))
        slope,yintercept = getLineEquation(x1,y1,x2,y2)

#Get the equation of a line (slope and y-intercept)
def getLineEquation(x1,y1,x2,y2):
    points = [(x1,y1),(x2,y2)]
    x_coords, y_coords = zip(*points)
    A = vstack([x_coords,ones(len(x_coords))]).T
    slope, yintercept = lstsq(A, y_coords)[0]
    return slope,yintercept