import picamera
import time
import io
import os
import sys
stream = io.BytesIO()
name = raw_input('Enter the name of your video file:')
temp = '.h264'
if name.endswith(temp):
	name = name[:5]
with picamera.PiCamera() as cam:
	os.system("rm " + name + ".h264\nrm " + name + ".mp4")
	cam.start_recording(name + '.h264')
	time.sleep(5)
	cam.stop_recording()
	os.system("MP4Box -add " + name + ".h264 " + name + ".mp4\nrm " + name + ".h264")
	time.sleep(5)
	os.system("omxplayer " + name + ".mp4")
	print('Script Concluded\n')
sys.exit()
