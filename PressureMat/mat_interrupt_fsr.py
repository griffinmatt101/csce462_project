import time
import os
import RPi.GPIO as GPIO
'''
GPIO.setmode(GPIO.BCM)
DEBUG = 1

#set GPIO Pins
LED_ON = 26
BUTTON = 19
state = 0

GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_ON, GPIO.OUT)
lastTime = time.time()
GPIO.output(LED_ON, state)

#Port Numbers
CLK = 18
DIGITAL_OUT = 23
DIGITAL_IN = 24
CS = 25

FSR = 0

#Set up pins
GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(DIGITAL_OUT, GPIO.IN)
GPIO.setup(DIGITAL_IN, GPIO.OUT)
GPIO.setup(CS, GPIO.OUT)
'''
#read SPI data from MCP3008 chip, 8 possible adc's (0-7)
def read_adc(adcnum, clockpin, mosipin, misopin, cspin):
	if ((adcnum > 7) or (adcnum < 0)): 
		return -1
	GPIO.output(cspin, True)
	GPIO.output(clockpin, False)
	GPIO.output(cspin, False)

	commandout = adcnum
	commandout |= 0x18 	#start bit and single-ended bit
	commandout <<= 3 	#only need to send 5 bits
	for i in range(5):
		if (commandout & 0x80):
			GPIO.output(mosipin,  True)
		else:
			GPIO.output(mosipin, False)
		commandout <<= 1
		GPIO.output(clockpin, True)
		GPIO.output(clockpin, False)

	adcout = 0
	#read in one empty bit, one null bit and 10 ADC bits
	for i in range(12):
		GPIO.output(clockpin, True)
		GPIO.output(clockpin, False)
		adcout <<= 1
		if (GPIO.input(misopin)):
			adcout |= 0x1

	GPIO.output(cspin, True)
	adcout >>= 1
	return adcout
'''
def pressed(channel):
    currentTime = time.time()
    global lastTime
    global state
    if((currentTime-lastTime)<5):
        print (currentTime-lastTime)
    else:
        print(GPIO.input(BUTTON))
        if(GPIO.input(BUTTON) == 0):
            valueSum = 0
            newState = not state
            for i in range (0,5):
                value = read_adc(FSR, CLK, DIGITAL_IN, DIGITAL_OUT, CS)
                print(value)
                valueSum = valueSum + value
            print("Avg : {}".format(valueSum/5))
            if((valueSum/5) > 100):
                GPIO.output(LED_ON, newState)
                state=newState
    currentTime = time.time()
    lastTime = currentTime
    time.sleep(.1)
GPIO.add_event_detect(BUTTON, GPIO.RISING, pressed)
while(True):
	i=1
        time.sleep(0.1)
'''
