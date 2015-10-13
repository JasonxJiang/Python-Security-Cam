import picamera
import sys
import time
name = 'default'
if len(sys.argv) > 1:
	name = sys.argv[1]
else if len(sys.argv) > 1
camera = picamera.PiCamera()
camera.start_preview()
time.sleep(5)
camera.capture(name + '.jpg')
camera.stop_preview()
