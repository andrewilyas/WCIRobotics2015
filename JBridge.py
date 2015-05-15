__author__ = 'nulldev'

#Simple program to manage JVMs in Python...

import jpype
import atexit

java = jpype.java

def close():
    if jpype.isJVMStarted() == True:
        jpype.java.lang.System.out.println ('Shutting down JVM...')
        jpype.shutdownJVM() 
        print('JBridge closed!')
    else:
        print('JBridge not open!')

print('Checking if JVM is started...')
if jpype.isJVMStarted() == False:
    print('Getting default JVM path...')
    jvmPath = jpype.getDefaultJVMPath() 
    print('Starting JVM...')
    jpype.startJVM(jvmPath)
    jpype.java.lang.System.out.println ('JVM Started!')
    jpype.java.lang.System.out.println ('Registering shutdown hook...')
    atexit.register(close)
else:
    jpype.java.lang.System.out.println ('JVM is already running, not starting!')