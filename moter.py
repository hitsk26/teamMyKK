#!/usr/bin/python
def rotate(flavor):
  import time
  import os
  import RPi.GPIO as GPIO

  GPIO.setmode(GPIO.BCM)
  DEBUG = 0
  GPIO18 = 18
  GPIO23 = 23
  GPIO24 = 24

  GPIO.setup(GPIO18,GPIO.OUT)
  GPIO.setup(GPIO23,GPIO.OUT)
  GPIO.setup(GPIO24,GPIO.OUT)

  if flavor==1:
    GPIO.output(GPIO23,True)
    GPIO.output(GPIO24,False)
    time.sleep(3)
    GPIO.output(GPIO23,False)
    GPIO.output(GPIO24,False)
  elif flavor==2:
    GPIO.output(GPIO23,True)
    GPIO.output(GPIO24,False)
    time.sleep(3)
    GPIO.output(GPIO23,False)
    GPIO.output(GPIO24,False)

  GPIO.cleanup()

"""

p18 = GPIO.PWM(GPIO18, 50)
p18.ChangeDutyCycle(100)
p18.start(0)
p18.ChangeDutyCycle(50)

GPIO.output(GPIO23,True)
GPIO.output(GPIO24,False)
print GPIO.input(GPIO23)
print GPIO.input(GPIO24)
time.sleep(3)


p18.ChangeDutyCycle(10)
GPIO.output(GPIO23,False)
print GPIO.input(GPIO23)
print GPIO.input(GPIO24)
time.sleep(3)

p18.ChangeDutyCycle(100)
GPIO.output(GPIO24,True)
print GPIO.input(GPIO23)
print GPIO.input(GPIO24)
time.sleep(3)

GPIO.cleanup()a
"""
