import RPi.GPIO as GPIO
import time
from classes import LCD_class as lcd
from classes import DHT22 as dht
from classes import DbClass as db

trans = 6
trans2 = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(trans,GPIO.OUT)
GPIO.setup(trans2,GPIO.OUT)

GPIO.PWM(trans,0)
GPIO.PWM(trans2,0)


try:
    while True:
        time.sleep(2)
        temperatuur = dht.returnTemp()
        luchtvochtigheid = dht.returnHumidity()

        lcd.LCD_controll("temp: " + temperatuur,"hum: " + luchtvochtigheid)
except KeyboardInterrupt:
    GPIO.cleanup()