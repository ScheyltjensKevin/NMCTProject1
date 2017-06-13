import RPi.GPIO as GPIO
import time
from classes.LCD_class import LCD_controll as lcd
from classes import DHT22 as dht
from classes import DbClass as db

trans = 6
trans2 = 5
GPIO.setmode(GPIO.BCM)
GPIO.setup(trans,GPIO.OUT)
GPIO.setup(trans2,GPIO.OUT)


try:

    l1 = lcd(24, 25, 0, 0, 0, 0, 12, 16, 20, 21, 'hello', 'world', 4)

    while True:
        pass
        # time.sleep(2)
        # temperatuur = dht.returnTemp()
        # luchtvochtigheid = dht.returnHumidity()
        # time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()