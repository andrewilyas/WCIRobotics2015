__author__ = 'nulldev'
import math
import numpy
import JBridge

#JAVA IMPORTS
java = JBridge.java
Boolean = java.lang.Boolean
Byte = java.lang.Byte
Character = java.lang.Character
Class = java.lang.Class
ClassLoader = java.lang.ClassLoader
ClassValue = java.lang.ClassValue
Compiler = java.lang.Compiler
Double = java.lang.Double
Enum = java.lang.Enum
Float = java.lang.Float
InheritableThreadLocal = java.lang.InheritableThreadLocal
Integer = java.lang.Integer
Long = java.lang.Long
Math = java.lang.Math
Number = java.lang.Number
Object = java.lang.Object
Package = java.lang.Package
Process = java.lang.Process
ProcessBuilder = java.lang.ProcessBuilder
Runtime = java.lang.Runtime
RuntimePermissions = java.lang.RuntimePermissions
SecurityManager = java.lang.SecurityManager
Short = java.lang.Short
StackTraceElement = java.lang.StackTraceElement
StrictMath = java.lang.StrictMath
String = java.lang.String
StringBuffer = java.lang.StringBuffer
StringBuilder = java.lang.StringBuilder
System = java.lang.System
Thread = java.lang.Thread
ThreadGroup = java.lang.ThreadGroup
ThreadLocal = java.lang.ThreadLocal
Throwable = java.lang.Throwable
Void = java.lang.Void

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