import pigpio
from classes import DHT22
import time

pi = pigpio.pi()

dht22 = DHT22.sensor(pi,18)
dht22.trigger()

sleepTime = 3

def readDHT22():
    dht22.trigger()

    humidity ='%.2f' %(dht22.humidity())
    temp ='%.2f' %(dht22.temperature())
    return (humidity,temp)


# humidity, temperature = readDHT22()

# try:
#
#     while True:
#         humidity, temperature = readDHT22()
#         print("humidity is: " + humidity + "%")
#         print("temperature is: " + temperature + "°C")
#         time.sleep(sleepTime)
#
#
# except KeyboardInterrupt:
#     pass