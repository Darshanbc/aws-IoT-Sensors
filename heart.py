import RPi.GPIO as gpio
import time

def initpins():
	gpio.setmode(gpio.BOARD)
	gpio.setwarnings(0)	
	gpio.setup(8,gpio.OUT)
	gpio.setup(10,gpio.OUT)
	gpio.setup(12,gpio.OUT)
	
	gpio.setup(38,gpio.IN)
	
def readtemp():
    gpio.output(8,1)#channel for temp
    list=[]
    start=time.time()
    end=start
    i=0
    status=gpio.input(38)
    while(end-start<5):
	if((gpio.input(38))!=status):
		i=i+1
	status=gpio.input(38)
	end=time.time()
	time.sleep(.2)
    print i*12
    return i*8
