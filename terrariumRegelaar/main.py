import RPi.GPIO as GPIO
import time
from classes import DHT22_datareader as dht
from classes import DbClass as db
from classes import aLCD_class as lcd
import datetime

l1 = lcd.LCD(17, 27, 22, 18, 23, 24, 25, 5, 6, 13, 19)

sleepTime = 3

GPIO.setmode(GPIO.BCM)
vent = 21
vent2 = 26
lampDag = 16
lampNacht=20

GPIO.setup(vent,GPIO.OUT)
GPIO.setup(vent2,GPIO.OUT)
GPIO.setup(lampDag,GPIO.OUT)
GPIO.setup(lampNacht,GPIO.OUT)

GPIO.output(lampNacht, GPIO.HIGH)
GPIO.output(lampDag, GPIO.HIGH)

counter=0
areFansOn = 0
dataTransferer = db.DbClass()
start = 0

try:

    GPIO.output(vent,GPIO.LOW)
    GPIO.output(vent2,GPIO.LOW)
    l1.startDisplay()
    while True:
        dt= datetime.datetime.now()

        time.sleep(sleepTime)
        humidity, temperature = dht.readDHT22()

        l1.ShowText("Hum: " + humidity + "%")
        l1.ShowText("Temp: " + temperature + "C")

        if float(temperature) > 28.50:
            GPIO.output(vent,GPIO.HIGH)
            GPIO.output(vent2,GPIO.HIGH)
            areFansOn = 1
        elif float(temperature) < 27.50:
            GPIO.output(vent,GPIO.LOW)
            GPIO.output(vent2,GPIO.LOW)
            areFansOn = 0

        if dt.hour == 6:
            GPIO.output(lampDag,GPIO.LOW)
            GPIO.output(lampNacht,GPIO.HIGH)
        if dt.hour == 21:
            GPIO.output(lampDag,GPIO.HIGH)
            GPIO.output(lampNacht,GPIO.LOW)

        if counter == 0 and (dt.hour > 6 or dt.hour < 21):
            GPIO.output(lampDag,GPIO.LOW)
            counter =1
        elif counter == 0 and (dt.hour < 6 or dt.hour > 21):
            GPIO.output(lampNacht,GPIO.LOW)
            counter =1

        start += 1
        if start == 60:
            moment = datetime.datetime.now()
            dataTransferer.setTempDataToDatabase(temperature,moment,areFansOn)
            dataTransferer.setHumDataToDatabase(humidity,moment)
            start = 0



except KeyboardInterrupt:
    l1.reset()
    GPIO.cleanup()