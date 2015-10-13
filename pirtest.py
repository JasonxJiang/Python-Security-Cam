import RPi.GPIO as GPIO
import picamera
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.IN)
import time
camera = picamera.PiCamera()
prev_input = 0
picnum = 0;
while True:
	input = GPIO.input(25)
	if ((not prev_input) and input):
		print("MOTION")
		camera.capture('image' + str(picnum) + '.jpg')
		picnum += 1
	else:
		print("Prev: " + str( prev_input) + " Current: " + str( input))
	prev_input = input
	time.sleep(0.5)
