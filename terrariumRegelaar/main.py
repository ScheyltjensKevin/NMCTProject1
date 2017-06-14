import RPi.GPIO as GPIO
import time
from classes import DHT22_datareader as dht
from classes import DbClass as db
from classes import aLCD_class as lcd

l1 = lcd.LCD(24, 27, 25, 22, 13, 19, 26, 12, 16, 20, 21)
counter = 0
sleepTime = 3

GPIO.setmode(GPIO.BCM)
vent = 5
vent2 = 6
GPIO.setup(vent,GPIO.OUT)
GPIO.setup(vent2,GPIO.OUT)


try:
    GPIO.output(vent,GPIO.LOW)
    GPIO.output(vent2,GPIO.LOW)
    l1.startDisplay()
    while True:
        time.sleep(sleepTime)
        humidity, temperature = dht.readDHT22()
        # if counter == 3:
        l1.ShowText("Hum: " + humidity + "%")
        l1.ShowText("Temp: " + temperature + "C")
        #     counter = 0
        # counter +=1

        if (float(temperature) > 28.00):
            GPIO.output(vent,GPIO.HIGH)
            GPIO.output(vent2,GPIO.HIGH)
        elif(float(temperature) < 28.00):
            GPIO.output(vent,GPIO.LOW)
            GPIO.output(vent2,GPIO.LOW)
except KeyboardInterrupt:
    l1.reset()
    GPIO.cleanup()