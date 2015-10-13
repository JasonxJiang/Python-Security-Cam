import socket
import picamera
import time
import sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.1.190', 10006))
sock.listen(1)

connection = sock.accept()[0].makefile('wb')

try:
	with picamera.PiCamera() as cam:
		cam.resolution = (640, 480)
		cam.framerate = 24
		cam.start_preview()
		time.sleep(2)
		cam.stop_preview()
		cam.start_recording(connection, format='h264')
		cam.wait_recording(60)
		cam.stop_recording()
finally:
	connection.close()
	sock.close()

sys.exit()
