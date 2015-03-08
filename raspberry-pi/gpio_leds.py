#!/usr/bin/python
import RPi.GPIO as GPIO
import time

print("initializing...")
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)
print("initializing...done")
time.sleep(3)

for i in range(10):
    if i % 2 == 0:
        print("LED is on: Green")
        GPIO.output(11, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(11, GPIO.LOW)
    else:
        print("LED is on: RED")
        GPIO.output(12, GPIO.HIGH)
        time.sleep(1)
        GPIO.output(12, GPIO.LOW)
GPIO.cleanup()
