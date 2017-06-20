import pigpio
from classes import DHT22

pi = pigpio.pi()
dht22 = DHT22.sensor(pi,12)
dht22.trigger()

def readDHT22():
    dht22.trigger()

    humidity ='%.2f' %(dht22.humidity())
    temp ='%.2f' %(dht22.temperature())
    return (humidity,temp)
