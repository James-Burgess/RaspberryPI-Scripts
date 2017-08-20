#!/usr/bin/python

import RPi.GPIO as g
from time import sleep

sleepTime = 1
isOn = False

def setup(pin):
	g.setup(pin, g.OUT)
	g.output(pin, g.HIGH)

def dimmer(pin, percent):
	g.output(pin, g.LOW)
	sleep(percent)
	g.output(pin, g.HIGH)

def lightSwitch(pin):
	global isOn
	global sleepTime
	if isOn == False:
		g.output(pin, g.LOW)
		isOn = True
		sleep(sleepTime)
		print("isOn")
	elif isOn == True:
		g.output(pin, g.HIGH)
		isOn = False
		print("off")
		sleep(sleepTime)

g.cleanup()
g.setmode(g.BCM)
setup(17)

g.setup(11, g.IN, pull_up_down=g.PUD_UP)

#set button to trigger loop

while True:
	try:
		input_state = g.input(11)

		if input_state == False:
			lightSwitch(17)


	except KeyboardInterrupt:
		print("Outies")
		g.cleanup()
		
