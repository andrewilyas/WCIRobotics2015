from nanpy import ArduinoApi, SerialManager, Servo
import time

class Arduino:
	serial  = SerialManager()
	arduino = ArduinoApi(connection = serial)
	drive = None
	turn = None
	camera = None

	def __init__():
		arduino.pinMode(13, arduino.OUTPUT)
		self.drive = Servo(12, connection = serial)
		self.turn = Servo(9, connection = serial)
		self.camera = Servo(11, connection = serial)

	def drive_forward(self, speed):
		self.drive.write(speed + 90)

	def turn_servo(self, speed):
		self.turn.write(speed)

	def stop_car(self):
		self.drive.write(90)

	def move_camera(self, speed):
		self.camera.write(speed)
