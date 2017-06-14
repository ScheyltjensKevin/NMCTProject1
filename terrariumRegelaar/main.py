import RPi.GPIO as GPIO
import time
from classes import DHT22_datareader as dht
from classes import DbClass as db
from classes import aLCD_class as lcd


l1 = lcd.LCD(24, 27, 25, 22, 13, 19, 26, 12, 16, 20, 21)

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

        # db.DbClass.setSensorDataToDatabase(db.DbClass(),1,temperature,time.time())
        # db.DbClass.setSensorDataToDatabase(db.DbClass(),2,humidity,time.time())

        l1.ShowText("Hum: " + humidity + "%")
        l1.ShowText("Temp: " + temperature + "C")

        if (float(temperature) > 28.50):
            GPIO.output(vent,GPIO.HIGH)
            GPIO.output(vent2,GPIO.HIGH)
            timestart=time.time()
        elif(float(temperature) < 27.50):
            GPIO.output(vent,GPIO.LOW)
            GPIO.output(vent2,GPIO.LOW)
            timestop=time.time()
            # db.DbClass.setfansDataToDatabase(db.DbClass(),timestart,timestop,(timestop-timestart))



except KeyboardInterrupt:
    l1.reset()
    GPIO.cleanup()