from nanpy import ArduinoApi, SerialManager, Servo
import time

class Arduino:
	serial  = SerialManager()
	arduino = ArduinoApi(connection = serial)
	drive = None
	turn = None
	camera = None

	def __init__(self):
		self.arduino.pinMode(13, self.arduino.OUTPUT)
		self.drive = Servo(12, connection = self.serial)
		self.turn = Servo(9, connection = self.serial)
		self.camera = Servo(11, connection = self.serial)

	def drive_forward(self, speed):
		self.drive.write(speed + 90)

	def turn_servo(self, speed):
		self.turn.write(speed)

	def stop_car(self):
		self.drive.write(90)

	def move_camera(self, speed):
		self.camera.write(speed)
