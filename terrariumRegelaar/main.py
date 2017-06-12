import RPi.GPIO as GPIO
import time



trans = 6
trans2 = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(trans,GPIO.OUT)
GPIO.setup(trans2,GPIO.OUT)

try:
    while True:

        GPIO.output(trans2,GPIO.HIGH)

except KeyboardInterrupt:
    GPIO.cleanup()


