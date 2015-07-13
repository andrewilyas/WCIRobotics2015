from nanpy import ArduinoApi, SerialManager, Servo
import time

def drive_forward(speed):
	drive.write(speed + 90)

def turn_servo(speed):
	turn.write(speed)

def stop_car():
	drive.write(90)

def move_camera(speed):
	camera.write(speed)

serial = SerialManager()
arduino = ArduinoApi(connection = serial)
arduino.pinMode(13, arduino.OUTPUT)
drive = Servo(12, connection = serial)
turn = Servo(9, connection = serial)
camera = Servo(11, connection = serial)

move_camera(170)
