import pigpio
from classes import DHT22
import time
from classes import aLCD_class as lcd

l1 = lcd.LCD(24, 27, 25, 22, 13, 19, 26, 12, 16, 20, 21)

pi = pigpio.pi()

dht22 = DHT22.sensor(pi,18)
dht22.trigger()

sleepTime = 3

def readDHT22():
    dht22.trigger()

    humidity ='%.2f' %(dht22.humidity())
    temp ='%.2f' %(dht22.temperature())
    return (humidity,temp)


humidity, temperature = readDHT22()
counter = 0
try:
    l1.startDisplay()
    while True:
        humidity, temperature = readDHT22()
        print("humidity is: " + humidity + "%")
        print("temperature is: " + temperature + "°C")
        time.sleep(sleepTime)

        if counter == 10:
            l1.ShowText("Hum: " + humidity + "%")
            l1.ShowText("Temp: " + temperature + "C")

            counter = 0
        counter +=1
        print (counter)
except KeyboardInterrupt:
    l1.reset()
    pass