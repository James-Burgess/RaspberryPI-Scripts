import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
print("LED On")
GPIO.output(18,GPIO.HIGH)
time.sleep(1)
print("LED Off")
GPIO.output(18,GPIO.LOW)
count=0
while (count < 10):
	GPIO.output(17,GPIO.HIGH)
	time.sleep(1)
	GPIO.output(17,GPIO.LOW)
	time.sleep(1)
	count = count + 1

print("goodbye")

