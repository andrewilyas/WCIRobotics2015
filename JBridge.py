__author__ = 'nulldev'

#Simple program to manage JVMs in Python...
#By: nulldev
#Specifically created to tick Andrew off.

import jpype
import atexit
import __builtin__
from jnius import autoclass

#def close():
#    if jpype.isJVMStarted() == True:
#        jpype.java.lang.System.out.println ('Shutting down JVM...')
#        jpype.shutdownJVM() 
#        print('JBridge closed!')
#    else:
#        print('JBridge not open!')

#Import classes
#def JImport(jclass):
#    if jpype.isJVMStarted() == False:
#        print('JVM not started! Cannot import class!')
#    else:
#        System.out.println("Importing " + jclass)
#        eval("__builtin__." + " = java.lang.Boolean")

#print('Checking if JVM is started...')
#if jpype.isJVMStarted() == False:
#    print('Getting default JVM path...')
#    jvmPath = jpype.getDefaultJVMPath() 
#    print('Starting JVM...')
#    jpype.startJVM(jvmPath)
#    jpype.java.lang.System.out.println ('JVM Started!')
#    jpype.java.lang.System.out.println ('Registering shutdown hook...')
#    atexit.register(close)
#else:
#    jpype.java.lang.System.out.println ('JVM is already running, not starting!')

print('Importing java.lang package...')
#For other programs to reference
#__builtin__.java = jpype.java
#__builtin__.jpype = jpype
#java = jpype.java

#Default Java imports
'''
__builtin__.Boolean = java.lang.Boolean
__builtin__.Byte = java.lang.Byte
__builtin__.Character = java.lang.Character
__builtin__.Class = java.lang.Class
__builtin__.ClassLoader = java.lang.ClassLoader
__builtin__.ClassValue = java.lang.ClassValue
__builtin__.Compiler = java.lang.Compiler
__builtin__.Double = java.lang.Double
__builtin__.Enum = java.lang.Enum
__builtin__.Float = java.lang.Float
__builtin__.InheritableThreadLocal = java.lang.InheritableThreadLocal
__builtin__.Integer = java.lang.Integer
__builtin__.Long = java.lang.Long
__builtin__.Math = java.lang.Math
__builtin__.Number = java.lang.Number
__builtin__.Object = java.lang.Object
__builtin__.Package = java.lang.Package
__builtin__.Process = java.lang.Process
__builtin__.ProcessBuilder = java.lang.ProcessBuilder
__builtin__.Runtime = java.lang.Runtime
__builtin__.RuntimePermissions = java.lang.RuntimePermissions
__builtin__.SecurityManager = java.lang.SecurityManager
__builtin__.Short = java.lang.Short
__builtin__.StackTraceElement = java.lang.StackTraceElement
__builtin__.StrictMath = java.lang.StrictMath
__builtin__.String = java.lang.String
__builtin__.StringBuffer = java.lang.StringBuffer
__builtin__.StringBuilder = java.lang.StringBuilder
__builtin__.System = java.lang.System
__builtin__.Thread = java.lang.Thread
__builtin__.ThreadGroup = java.lang.ThreadGroup
__builtin__.ThreadLocal = java.lang.ThreadLocal
__builtin__.Throwable = java.lang.Throwable
__builtin__.Void = java.lang.Void
'''
__builtin__.Boolean = autoclass('java.lang.Boolean')
__builtin__.Byte = autoclass('java.lang.Byte')
__builtin__.Character = autoclass('java.lang.Character')
__builtin__.Class = autoclass('java.lang.Class')
__builtin__.ClassLoader = autoclass('java.lang.ClassLoader')
__builtin__.ClassValue = autoclass('java.lang.ClassValue')
__builtin__.Compiler = autoclass('java.lang.Compiler')
__builtin__.Double = autoclass('java.lang.Double')
__builtin__.Enum = autoclass('java.lang.Enum')
__builtin__.Float = autoclass('java.lang.Float')
__builtin__.InheritableThreadLocal = autoclass('java.lang.InheritableThreadLocal')
__builtin__.Integer = autoclass('java.lang.Integer')
__builtin__.Long = autoclass('java.lang.Long')
__builtin__.Math = autoclass('java.lang.Math')
__builtin__.Number = autoclass('java.lang.Number')
__builtin__.Object = autoclass('java.lang.Object')
__builtin__.Package = autoclass('java.lang.Package')
__builtin__.Process = autoclass('java.lang.Process')
__builtin__.ProcessBuilder = autoclass('java.lang.ProcessBuilder')
__builtin__.Runtime = autoclass('java.lang.Runtime')
#__builtin__.RuntimePermissions = autoclass('java.lang.RuntimePermissions')
#__builtin__.SecurityManager = autoclass('java.lang.SecurityManager')
__builtin__.Short = autoclass('java.lang.Short')
__builtin__.StackTraceElement = autoclass('java.lang.StackTraceElement')
__builtin__.StrictMath = autoclass('java.lang.StrictMath')
__builtin__.String = autoclass('java.lang.String')
__builtin__.StringBuffer = autoclass('java.lang.StringBuffer')
__builtin__.StringBuilder = autoclass('java.lang.StringBuilder')
__builtin__.System = autoclass('java.lang.System')
__builtin__.Thread = autoclass('java.lang.Thread')
__builtin__.ThreadGroup = autoclass('java.lang.ThreadGroup')
__builtin__.ThreadLocal = autoclass('java.lang.ThreadLocal')
__builtin__.Throwable = autoclass('java.lang.Throwable')
__builtin__.Void = autoclass('java.lang.Void')

System.out.println("JBridge intialized!");