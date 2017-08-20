import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(4,GPIO.OUT)
GPIO.output(4,GPIO.LOW)

print("LED On")
GPIO.output(4,GPIO.HIGH)
time.sleep(10)
print("LED Off")
GPIO.output(4,GPIO.LOW)

GPIO.cleanup()
print("goodbye")

