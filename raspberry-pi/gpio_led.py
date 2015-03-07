#!/usr/bin/python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.OUT)
print("LED is on: Green")
time.sleep(3)
GPIO.cleanup()
