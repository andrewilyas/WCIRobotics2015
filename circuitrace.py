__author__ = 'nulldev'

#Python imports
import math
import numpy
import JBridge

MAX_SPEED = 1 # TODO: bug hardware and find this value
# Author: nulldev (Git: null-dev)

# DON'T EXECUTE THIS, YOU WILL GET A VERY COOL INFINITE LOOP :P

def main():
    while(True):
        System.out.println("ITER");
        # Line is an array of arrays of tuples
        lines = getDetectedLines()
        x1 = (lines[0][0][0]+lines[1][0][0])/2
        y1 = (lines[0][0][1]+lines[1][0][1])/2
        x2 = (lines[0][1][0]+lines[1][1][0])/2
        y2 = (lines[0][1][1]+lines[1][1][1])/2
        slope = (x1-x2)/(y2-y1)
        degrees = numpy.arctan(slope)
        speed = MAX_SPEED
        sendToServo(degrees, speed) #HELP ME HARDWARE
        
def getDetectedLines():
    System.out.println("Getting detected lines...")
    lines = dragRace.getDetectedLines(test1.jpg)