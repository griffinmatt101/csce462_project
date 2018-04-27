import picamera
import time
import cv2
import numpy

from picamera.array import PiRGBArray
from PIL import Image
from matplotlib import pyplot as plt
from pprint import pprint
from PlotData import plotData

class DetectMotion:
	def __init__(self):
		self.camera = picamera.PiCamera()
		self.camera.resolution = (256,256)
		self.rgbFrame = PiRGBArray(self.camera, size = self.camera.resolution)

		self.minData = []
		self.maxData = []

		self.prevMin = -1
		self.prevMax = -1
		self.SLOPE_SET = 12  # Number of points to take the slope of
		self.MIN_SLOPE = 8   # Slope of data set that determines a gesture
		self.GESTURE = None

		# print("Readying...")
		time.sleep(1)

		# Capture and Process Frame
		self.camera.capture(self.rgbFrame, format="bgr", use_video_port=True)
		rawFrame1 = self.rgbFrame.array
		grayFrame1 = cv2.cvtColor(rawFrame1, cv2.COLOR_BGR2GRAY)
		blurFrame1 = cv2.GaussianBlur(grayFrame1, (5, 5), 0)
		self.frame1 = blurFrame1

		self.rgbFrame.truncate(0)
		
		print "Initialization complete"

	def detectMotion(self):
		time.sleep(0.01)

		# Capture frame
		self.camera.capture(self.rgbFrame, format="bgr", use_video_port=True)
		
		# Process frame
		rawFrame2 = self.rgbFrame.array
		grayFrame2 = cv2.cvtColor(rawFrame2, cv2.COLOR_BGR2GRAY)
		blurFrame2 = cv2.GaussianBlur(grayFrame2, (5, 5), 0)
		self.frame2 = blurFrame2

		self.rgbFrame.truncate(0)

		# Create difference image, enhance result
		diffImg = cv2.absdiff(self.frame1, self.frame2)
		threshImg = cv2.threshold(diffImg, 50, 255, cv2.THRESH_BINARY)[1]

		self.frame1 = self.frame2

		# Process white points
		whitePixels = cv2.findNonZero(threshImg)
		if whitePixels is not None:
			whitePixelsList = whitePixels.tolist()
		else:
			return None

		whitePixelX = []
		for whitePixels in whitePixelsList:
			for vals in whitePixels:
				whitePixelX.append(vals[0])

		xMin = min(whitePixelX)

		if len(self.minData) is self.SLOPE_SET:
			del self.minData[0]
		self.minData.append(xMin)

		if self.prevMin < 0:
			pass

		self.prevMin = xMin

		if len(self.minData) == self.SLOPE_SET:
			axis = range(1, len(self.minData)+1)
			slope = numpy.polyfit(axis, self.minData, 1)[0]
			if self.GESTURE is None:
				if slope > self.MIN_SLOPE:
					self.GESTURE = "Right Gesture\n"
				elif slope < -self.MIN_SLOPE:
					self.GESTURE = "Left Gesture\n"
				if self.GESTURE is not None:
					print(self.GESTURE)
			else:
				if slope < self.MIN_SLOPE and slope > -self.MIN_SLOPE:
					self.GESTURE = None
		
		plotData(minData=self.minData, maxData=None)
		
		return self.GESTURE

	
