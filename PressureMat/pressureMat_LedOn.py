#Libraries
import RPi.GPIO as GPIO
import time
import os
 
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)


#set GPIO Pins for pressure mat
LED_ON = 26
MAT = 19
#Port Numbers for FSR
CLK = 18
DIGITAL_OUT = 23
DIGITAL_IN = 24
CS = 25
FSR = 0

#Mat GPIO setups
GPIO.setup(MAT, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(LED_ON, GPIO.OUT)

#FSR GPIO set up pins
GPIO.setup(CLK, GPIO.OUT)
GPIO.setup(DIGITAL_OUT, GPIO.IN)
GPIO.setup(DIGITAL_IN, GPIO.OUT)
GPIO.setup(CS, GPIO.OUT)

#read SPI data from MCP3008 chip, 8 possible adc's (0-7)
def read_adc(adcnum, clockpin, mosipin, misopin, cspin):
	if ((adcnum >7) or (adcnum < 0)): 
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

def pressed(channel):
    print("Edge detected! Need to know if falling or rising...")
    print(not GPIO.input(MAT))
    # if input(MAT) == 0 => someone may be ON the board
    # if input(MAT) == 1 => someone may be OFF the board
    if(GPIO.input(MAT) == 0):
        print("rising?")
        while(True):
            value_sum = 0
            for i in range(0,5):
                fsr_read = read_adc(FSR, CLK, DIGITAL_IN, DIGITAL_OUT, CS)
                print(fsr_read)
                value_sum = value_sum + fsr_read
                time.sleep(.02)
            if((value_sum/5) < 50):
                print("no one there")
                GPIO.output(LED_ON, 0)
                break
            elif ((value_sum/5) > 200):
                print("hellllloooooo")
                GPIO.output(LED_ON, 1)
                break
            else:
                continue
    
    else:
        print("falling?")
        while(True):
            value_sum = 0
            for i in range(0,5):
                fsr_read = read_adc(FSR, CLK, DIGITAL_IN, DIGITAL_OUT, CS)
                print(fsr_read)
                value_sum = value_sum + fsr_read
                time.sleep(.02)
            if((value_sum/5) < 100):
                print("no one there")
                GPIO.output(LED_ON, 0)
                break
            elif ((value_sum/5) > 150):
                print("someone is still there")
                GPIO.output(LED_ON, 1)
                break
            else:
                print("not sure")
                continue
        

GPIO.add_event_detect(MAT, GPIO.BOTH, pressed)


def main():
    while(True):
        i=1
main()

