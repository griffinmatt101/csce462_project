import picamera
import time
import cv2
import numpy

from picamera.array import PiRGBArray
from PIL import Image
from matplotlib import pyplot as plt
from pprint import pprint
from PlotData import plotData

camera = picamera.PiCamera()
camera.resolution = (256,256)
rgbFrame = PiRGBArray(camera, size = camera.resolution)

minData = []
maxData = []

prevMin = -1
prevMax = -1
SLOPE_SET = 12  # Number of points to take the slope of
MIN_SLOPE = 8   # Slope of data set that determines a gesture
GESTURE = None

print("Readying...")
time.sleep(1)

# Capture and Process Frame
camera.capture(rgbFrame, format="bgr", use_video_port=True)
rawFrame1 = rgbFrame.array
grayFrame1 = cv2.cvtColor(rawFrame1, cv2.COLOR_BGR2GRAY)
blurFrame1 = cv2.GaussianBlur(grayFrame1, (5, 5), 0)
frame1 = blurFrame1

rgbFrame.truncate(0)

while True:
    time.sleep(0.01)

    # Capture frame
    camera.capture(rgbFrame, format="bgr", use_video_port=True)
    
    # Process frame
    rawFrame2 = rgbFrame.array
    grayFrame2 = cv2.cvtColor(rawFrame2, cv2.COLOR_BGR2GRAY)
    blurFrame2 = cv2.GaussianBlur(grayFrame2, (5, 5), 0)
    frame2 = blurFrame2

    rgbFrame.truncate(0)

    # Create difference image, enhance result
    diffImg = cv2.absdiff(frame1, frame2)
    threshImg = cv2.threshold(diffImg, 50, 255, cv2.THRESH_BINARY)[1]

    frame1 = frame2

    # Process white points
    whitePixels = cv2.findNonZero(threshImg)
    if whitePixels is not None:
        whitePixelsList = whitePixels.tolist()
    else:
        continue

    whitePixelX = []
    for whitePixels in whitePixelsList:
        for vals in whitePixels:
            whitePixelX.append(vals[0])

    xMin = min(whitePixelX)

    if len(minData) is SLOPE_SET:
        del minData[0]
    minData.append(xMin)

    if prevMin < 0:
        pass

    prevMin = xMin

    if len(minData) == SLOPE_SET:
        axis = range(1, len(minData)+1)
        slope = numpy.polyfit(axis, minData, 1)[0]
        if GESTURE is None:
            if slope > MIN_SLOPE:
                GESTURE = "Right Gesture\n"
            elif slope < -MIN_SLOPE:
                GESTURE = "Left Gesture\n"
            if GESTURE is not None:
                print GESTURE
        else:
            if slope < MIN_SLOPE and slope > -MIN_SLOPE:
                GESTURE = None

plotData(minData, maxData=None)
