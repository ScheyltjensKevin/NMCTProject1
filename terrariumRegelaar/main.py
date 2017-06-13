import RPi.GPIO as GPIO
import time
from classes import twoDHT22 as dht
from classes import DbClass as db

sleepTime = 3
trans = 6
trans2 = 5
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(trans,GPIO.OUT)
GPIO.setup(trans2,GPIO.OUT)


try:
    while True:
        time.sleep(sleepTime)
        GPIO.output(trans,GPIO.LOW)
except KeyboardInterrupt:
    GPIO.cleanup()