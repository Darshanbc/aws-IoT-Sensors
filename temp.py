

import RPi.GPIO as gpio
import time

def initpins():
	gpio.setmode(gpio.BOARD)
	gpio.setwarnings(0)	
	gpio.setup(8,gpio.OUT)
	gpio.setup(10,gpio.OUT)
	gpio.setup(12,gpio.OUT)
	
	gpio.setup(16,gpio.IN)
	
	gpio.setup(37,gpio.IN)
	gpio.setup(35,gpio.IN)
	gpio.setup(33,gpio.IN)
	gpio.setup(31,gpio.IN)
	gpio.setup(29,gpio.IN)
	gpio.setup(23,gpio.IN)
	gpio.setup(21,gpio.IN)
	gpio.setup(19,gpio.IN)

def readtemp():
#	gpio.output(8,1)#channel for temp
	gpio.output(10,1)#Ale high
	gpio.output(12,1)#start conversion
	gpio.output(10,0)#ale low
	gpio.output(12,0)#start low
	
	while(gpio.input(16)==0):
		pass
#	time.sleep(0.6)
	if(gpio.input(16)==1):
		bit7=gpio.input(37)
		bit6=gpio.input(35)
		bit5=gpio.input(33)
		bit4=gpio.input(31)
		bit3=gpio.input(29)
		bit2=gpio.input(23)
		bit1=gpio.input(21)
		bit0=gpio.input(19)
	
		temperature=(bit7*128)+(bit6*64)+(bit5*32)+(bit4*16)+(bit3*8)+(bit2*4)+(bit1*2)+bit0
	
		temperature=temperature*500/255
	else:
		temperature=1000
	print temperature
	return temperature
	
#initpins()
#readtemp()
