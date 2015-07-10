from nanpy import ArduinoApi, SerialManager, Servo
import time

serial = SerialManager()
arduino = ArduinoApi(connection = serial)
arduino.pinMode(13, arduino.OUTPUT)
drive = Servo(12, connection = serial)
turn = Servo(9, connection = serial)
camera = Servo(11, connection = serial)

while True:
	action, speed = raw_input("gib acton pl0x\n> ").split()
	speed = int(speed)
	if action == "drive":
		drive.write(speed + 90)
	elif action == "turn":
		turn.write(speed)
	elif action == "stop":
		drive.write(90)
	elif action == "camera":
		camera.write(speed)
	else:
		break
