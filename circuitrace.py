__author__ = 'nulldev'
# Author: nulldev (Git: null-dev)
def main():
    while(True):
        print "ITER"
        # Line is an array of arrays of tuples
        lines = getDetectedLines()
        x1 = (lines[0][0][0]+lines[1][0][0])/2
        y1 = (lines[0][0][1]+lines[1][0][1])/2
        x2 = (lines[0][1][0]+lines[1][1][0])/2
        y2 = (lines[0][1][1]+lines[1][1][1])/2
        slope = 