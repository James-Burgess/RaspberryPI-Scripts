#!/usr/bin/env python


import explorerhat
import time

def ohai(channel, event):
	print("Hey you pressed my buttons, number: ()".format(channel))

while True:
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



	explorerhat.touch.one.pressed(ohai)
