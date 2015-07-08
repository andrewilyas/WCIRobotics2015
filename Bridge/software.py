from nanpy import ArduinoApi, SerialManager, Servo

class Pins():
    DRIVE = 12
    CAMERA = 11
    TURN = 9

class Constants():
    CAMERA_UP = 170
    CAMERA_DOWN = 180
    LEFT = 110
    RIGHT = 60

class Position():
    UP = 0
    DOWN = 1

class Direction():
    LEFT = 0
    RIGHT = 1
    FORWARD = 0
    BACKWARD = 1

class Arduino:
    def __init__(self):
        print "Initializing Arduino"
        self._serialManager = SerialManager()
        self._arduino = ArduinoApi(connection = self._serialManager)
        self._driveServo = Servo(Pins.DRIVE, connection = self._serialManager)
        self._cameraServo = Servo(Pins.CAMERA, connection = self._serialManager)
        self._turnServo = Servo(Pins.TURN, connection = self.serialManager)
        
    def moveCamera(self, position):
        if position == Position.UP:
            self._cameraServo.write(Constants.CAMERA_UP)
        elif position == Position.DOWN:
            self._cameraServo.write(Constants.CAMERA_DOWN)
        elif:
            raise Exception("Unknown camera position")

    def turn(self, direction):
        if position == Direction.LEFT:
            self._turnServo.write(Constants.LEFT)
        elif position == Direction.RIGHT:
            self._turnServo.write(Constants.RIGHT)
        elif:
            raise Exception("Unknown direction")

    def drive(self, direction, speed):
        if direction == Direction.FORWARD:
            speed = 90 + speed
        elif direction == Direction.BACKWARD:
            speed = 90 - speed
        else:
            raise Exception("Unknown direction")
        self._driveServo.write(speed)

    def stop(self):
        self._driveServo.write(0)

def printresults(l):
    for i in l:
        print "Got: " + str(i)

def main():
    arduino = Arduino()
    while True:
        x = int(input("Pin\n> "))
        arduino.toggleLed(x, callback=printresults)
    arduino.disconnect()

if __name__ == "__main__":
    main()
