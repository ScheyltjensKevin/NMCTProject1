import serial
import time

ser = serial.Serial('/dev/ttyACM0',9600)
t = [0]


def returnTemp():
    return t

def returnHumidity():
    return read_first_line


while True:
    read_first_line= str(float (ser.readline()))
    t[0] = str(float (ser.readline()))


