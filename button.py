#!/usr/bin/python 

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)


GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)


try:
  while True:

    input_state = GPIO.input(18)
    if input_state == False:
      print("you pressed a button")





except KeyboardInterrupt:
  print ("quitting...")
  GPIO.cleanup()
