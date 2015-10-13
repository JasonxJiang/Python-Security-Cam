import os
import time
import smtplib
import RPi.GPIO as GPIO
import picamera
GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.IN)
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#setup pir and cam
camera = picamera.PiCamera()
prev_input = 0
picnum = 0;

#setup server
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login('mailserver12321@gmail.com', 'Alpha735')

def vid():
	os.system("rm video.mp4")
	camera.start_recording("video.h264")
	time.sleep(5)
	camera.stop_recording()
	os.system("MP4Box -add video.h264 video.mp4\nrm video.h264")

def setupmessage():
	msg = MIMEMultipart()
	msg['From'] = 'mailserver12321@gmail.com'
	receivers = ['dsyandrewdeng@gmail.com']
	msg['To'] = ', '.join(receivers)
	msg['Subject'] = 'Your camera has been alerted!!!'
	text = 'This is a message from your security system. Your camera has been triggered and video of the scene is attached. Please do not reply to this message.'
	plaintext = MIMEText(text, 'plain')
	msg.attach(plaintext)
	return msg

input = 0

while True:
	input = GPIO.input(25)
	if ((not prev_input) and input):
		vid()
		email = setupmessage()
		email.attach(MIMEImage(open(x, 'rb').read()))
		server.send_message(email)
server.quit()
#TODO
#1. Figure out how to get notifications to a phone
#2. Figure out how to receive a notification on a phone
#3. ???
#4. Profit!
