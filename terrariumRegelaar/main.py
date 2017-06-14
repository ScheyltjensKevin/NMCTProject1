import RPi.GPIO as GPIO
import time
from classes import twoDHT22 as dht
from classes import DbClass as db
from classes import aLCD_class as lcd

l1 = lcd.LCD(24, 27, 25, 22, 13, 19, 26, 12, 16, 20, 21)
counter = 0

sleepTime = 3
trans = 6
trans2 = 5
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(trans,GPIO.OUT)
GPIO.setup(trans2,GPIO.OUT)


try:
    l1.startDisplay()
    while True:
        time.sleep(sleepTime)
        GPIO.output(trans,GPIO.LOW)

        humidity, temperature = dht.readDHT22()

        if counter == 3:
            l1.ShowText("Hum: " + humidity + "%")
            l1.ShowText("Temp: " + temperature + "C")

            counter = 0
        counter +=1
        print (counter)
except KeyboardInterrupt:
    l1.reset()

    GPIO.cleanup()