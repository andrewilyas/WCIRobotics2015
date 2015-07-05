import serial
import time
import traceback
import struct
from enum import Enum

class _command(Enum):
    SOFTWARE_CONNECT = '\xff';
    HARDWARE_ACKNOWLEDGE = '\xfe';

    TOGGLE_LED = '\x03'
    MOVE_CAMERA = '\x04'
    TURN = '\x05'
    DRIVE = '\x06'
    STOP = '\x07'
    READ_ULTRASONIC = '\x08'

class Position(Enum):
    UP = 0
    DOWN = 1

class Direction(Enum):
    LEFT = 0
    RIGHT = 1
    FORWARD = 0
    BACKWARD = 1

class Arduino:
    def __init__(self, port):
        print "Initializing Arduino on " + port
        self.port = port
        self.connect()

    def connect(self, baud=28800):
        if not hasattr(self, 'con'):
            print "Connecting to Arduino with baud " + str(baud)
            self.con = serial.Serial(self.port, baud)
            self.handshake()
            self.con.timeout = 0
            print "Connect to Arduino"
        else:
            raise Exception("Already Connected")

    def handshake(self):
        self.con.timeout = 0.1;
        self.con.write(_command.SOFTWARE_CONNECT.value)
        handshake = self.con.read(size=1)
        while len(handshake) != 1:
            self.con.write(_command.SOFTWARE_CONNECT.value)
            handshake = self.con.read(size=1)
        if handshake != _command.HARDWARE_ACKNOWLEDGE.value:
            raise Exception("Invalid response!")

    def awaitAcknowledgement(self, command, callback):
        while self.con.inWaiting() == 0:
            #print "WAAAAAAAAAITING"
            pass
        response = self.con.read(size=self.con.inWaiting())
        while ord(response[-1]) != 255:
            response = response + self.con.read(size=self.con.inWaiting())
        if response[0] == command:
            argslen = i[1]
            if argslen > 0:
                args = []
                for x in range(2, len(response) - 1):
                    args.append(ord(response[x]))
                self.invoke(callback, args)
            return True
        else:
            return False

    def sendCommand(self, command, data=[], callback=None):
        self.con.write(command.value)
        string = struct.pack('!B', len(data))
        for i in tuple(data):
            string += struct.pack('!B', i)
        self.con.write(string)
        if self.awaitAcknowledgement(command.value, callback):
            return True
        else:
            raise Exception("Could not send command " + command)

    def disconnect(self):
        self.con.close()
        print "Disconnected"

    def toggleLed(self, pin, callback=None):
        self.sendCommand(_command.TOGGLE_LED, data=[pin], callback=callback)

    def moveCamera(self, position):
        self.sendCommand(_command.MOVE_CAMERA, data=[position.value])

    def turn(self, direction, degrees):
        self.sendCommand(_command.TURN, data=[degrees.value])

    def drive(self, direction, speed):
        if direction == Direction.BACKWARD:
            speed = -1 * speed
        self.sendCommand(_command.DRIVE, data=[speed])

    def stop(self):
        self.sendCommand(_command.STOP)

    def readUltrasonic(self, callback):
        self.sendCommand(_command.READ_ULTRASONIC, callback=callback)

    def invoke(self, function, *args):
        if function != None:
            function(*args)

def printresults(l):
    for i in l:
        print "Got: " + str(i)

def main():
    arduino = Arduino("/dev/tty.usbmodem1411")
    while True:
        try:
            x = raw_input("Command\n> ")
            if x == "drive forward":
                arduino.toggleLed(13)
                #speed = int(input("Speed\n> "))
                #arduino.drive(Direction.FORWARD, speed)
            elif x == "drive backward":
                speed = int(input("Speed\n> "))
                arduino.drive(Direction.BACKWARD, speed)
            elif x == "stop":
                arduino.stop()
            else:
                break
        except Exception, e:
            print traceback.format_exc()
            break
    arduino.disconnect()

if __name__ == "__main__":
    main()
