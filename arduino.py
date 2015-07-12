from nanpy import ArduinoApi, SerialManager, Servo
import time

serial = SerialManager()
arduino = ArduinoApi(connection = serial)
arduino.pinMode(13, arduino.OUTPUT)
drive = Servo(12, connection = serial)
turn = Servo(9, connection = serial)
camera = Servo(11, connection = serial)

def drive (speed):
	drive.write(speed + 90)

def turn(speed):
	turn.write(speed)

def stop():
	drive.write(90)

def camera(speed):
	camera.write(speed)