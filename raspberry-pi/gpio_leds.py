#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
for i in range(10):
    if i % 2 == 0:
        GPIO.setup(11, GPIO.OUT)
        print("LED is on: Green")
        time.sleep(1)
        GPIO.setup(11, True)
    else:
        GPIO.setup(12, GPIO.OUT)
        print("LED is on: RED")
        time.sleep(1)
        GPIO.setup(12, True)
GPIO.cleanup()
