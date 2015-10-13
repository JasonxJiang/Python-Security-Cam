import cv2, platform
import numpy as np
import urllib
import os

localCam = 0 

class VideoCamera(object):
	def __init__(self):
		#Using OpenCv apture fro mdevice 0 (local cam)
		self.video = cv2.VideoCapture(0)

	def __del__(self):
		self.video.release()

	def get_frame(self):
		success, iage = self.video.read()
		ret, jpeg = cv2.imencode('.jpg',image)
		return jpeg.tobytes() 


