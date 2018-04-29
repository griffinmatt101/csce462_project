#Libraries
import RPi.GPIO as GPIO
import time

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
 
#set GPIO Pins
LED_ON = 26
BUTTON = 19
state = 0

GPIO.setup(BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_ON, GPIO.OUT)
lastTime = time.time()
GPIO.output(LED_ON, state)

def pressed(channel):
        currentTime = time.time()
        global lastTime
        global state
        if((currentTime-lastTime)<5):
            print (currentTime-lastTime)
        else:
            print(GPIO.input(BUTTON))
            if(GPIO.input(BUTTON) == 0):
                GPIO.output(LED_ON, not state)
                state=not state
        lastTime = currentTime
	time.sleep(.1)

GPIO.add_event_detect(BUTTON, GPIO.RISING, pressed)

while(True):
	i=1
