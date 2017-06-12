import serial
import time

ser = serial.Serial('/dev/ttyACM0',9600)
t = [0]
while True:
    read_first_line= str(float (ser.readline()))
    t[0] = str(float (ser.readline()))
    print ("temperatuur: " + t[0])
    print ("luchtvochtigheid: " + read_first_line)

