#!/usr/bin/env python


import explorerhat
import time

count = 0

def flash(channel, event):
	explorerhat.light.red.on()
	time.sleep(1)
	explorerhat.light.green.on()
	time.sleep(1)
	explorerhat.light.blue.on()
	time.sleep(1)
	explorerhat.light.yellow.on()

	explorerhat.light.red.off()
	time.sleep(1)
	explorerhat.light.green.off()
	time.sleep(1)
	explorerhat.light.blue.off()
	time.sleep(1)
	explorerhat.light.yellow.off()

def disco(channel, event):
	while (count < 20):
		explorerhat.light.red.on()
		time.sleep(.1)
		explorerhat.light.red.off()
		time.sleep(.1)
		count = count + 1

while True:	
	explorerhat.touch.one.pressed(flash)
	explorerhat.touch.two.pressed(disco)
