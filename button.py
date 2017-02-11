#!/usr/bin/python 

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(2,GPIO.OUT)
GPIO.output(2,GPIO.HIGH)

try:
  while True:
    input_state = GPIO.input(18)
    if input_state == False:
      print("you pressed a button")
      GPIO.output(2,GPIO.LOW)
      time.sleep(2)
      GPIO.output(2,GPIO.HIGH)
except KeyboardInterrupt:
  print ("quitting...")
  GPIO.cleanup()
