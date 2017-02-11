#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

# init list with pin numbers

pinList = [4, 5, 6, 7, 8, 9, 10, 11]

# loop through pins and set mode and state to 'low'

for i in pinList: 
    GPIO.setup(i, GPIO.OUT) 
    GPIO.output(i, GPIO.HIGH)

# time to sleep between operations in the main loop

SleepTimeL = 2

# main loop

try:
  GPIO.output(4, GPIO.LOW)
  print "ONE"
  time.sleep(SleepTimeL); 
  GPIO.output(5, GPIO.LOW)
  print "TWO"
  time.sleep(SleepTimeL);  
  GPIO.output(6, GPIO.LOW)
  print "THREE"
  time.sleep(SleepTimeL);
  GPIO.output(7, GPIO.LOW)
  print "FOUR"
  time.sleep(SleepTimeL);
  GPIO.output(8, GPIO.LOW)
  print "FIVE"
  time.sleep(SleepTimeL);
  GPIO.output(9, GPIO.LOW)
  print "SIX"
  time.sleep(SleepTimeL);
  GPIO.output(10, GPIO.LOW)
  print "SEVEN"
  time.sleep(SleepTimeL);
  GPIO.output(11, GPIO.LOW)
  print "EIGHT"
  time.sleep(SleepTimeL);
  GPIO.cleanup()
  print "Good bye!"

# End program cleanly with keyboard
except KeyboardInterrupt:
  print "  Quit"

  # Reset GPIO settings
  GPIO.cleanup()
