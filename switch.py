import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO16 = 16
GPIO20 = 20

GPIO.setup(GPIO16, GPIO.IN)
GPIO.setup(GPIO20, GPIO.IN)

try:
    while True:
        if GPIO.input(GPIO20) == GPIO.HIGH:
            print "high\n"
        else:
            print "low\n"
        sleep(0.01)

except KeyboardInterrupt:
        pass

GPIO.cleanup()