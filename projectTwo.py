#!/usr/bin/env python

import explorerhat
import math
import time

lr = explorerhat.light.red
lb = explorerhat.light.blue
ly = explorerhat.light.yellow
lg = explorerhat.light.green

while True:
	lg.on()
	time.sleep(.5)
	lb.on()
	time.sleep(.5)
	ly.on()
	time.sleep(.5)
	lg.on()
	time.sleep(.5)

	lg.off()
	time.sleep(.5)
	lb.off()
	time.sleep(.5)
	ly.off()
	time.sleep(.5)
	lg.off()
	time.sleep(3)
