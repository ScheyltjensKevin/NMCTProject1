import RPi.GPIO as GPIO
import time

class LCD_controll():
    def __init__(self, messageLine1, messageLine2):
        self.__delay = 0.002
        self.__line1 = 0x80
        self.__line2 = 0xC0
        self.__PIN_RS = 25
        # self.__PIN_RW = RW connected to ground
        self.__PIN_E  = 24
        self.__PIN_D4 = 21
        self.__PIN_D5 = 20
        self.__PIN_D6 = 16
        self.__PIN_D7 = 12

        self.__msgL1 = messageLine1
        self.__msgL2 = messageLine2
        self.__listAllPins = [self.__PIN_RS, self.__PIN_E, self.__PIN_D4, self.__PIN_D5, self.__PIN_D6, self.__PIN_D7]
        self.__listDataPins = [self.__PIN_D7, self.__PIN_D6, self.__PIN_D5, self.__PIN_D4]
        self.main(self.__msgL1, self.__msgL2)

    @property
    def listDataPins(self):
        return self.__listDataPins

    @property
    def listAllPins(self):
        return self.__listAllPins

    @property
    def msgL1(self):
        return self.__msgL1

    @msgL1.setter
    def msgL1(self, value):
        self.__msgL1 = value

    @property
    def msgL2(self):
        return self.__msgL2

    @msgL2.setter
    def msgL2(self,value):
        self.__msgL2 = value



    def main(self, msgL1, msgL2):
            try:
                self.init()
                time.sleep(self.__delay)
                self.initLCD4bit()
                time.sleep(self.__delay)
                self.write4bitmsg(msgL1, self.__line1)
                self.write4bitmsg(msgL2, self.__line2)
                time.sleep(self.__delay)
                while True:
                    pass
            except KeyboardInterrupt:
                self.initLCD4bit()
                time.sleep(self.__delay)
                self.reset()
                time.sleep(self.__delay)
                GPIO.cleanup()

    def init(self):
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        for i in range(len(self.__listAllPins)):
            GPIO.setup(self.__listAllPins[i], GPIO.OUT)

    def pulseE(self):
        GPIO.output(self.__PIN_E, GPIO.HIGH)
        time.sleep(self.__delay)
        GPIO.output(self.__PIN_E, GPIO.LOW)
        time.sleep(self.__delay)

    def reset(self):
        self.write4bitsTwice(0x3, GPIO.LOW, True)
        self.write4bitsTwice(0x3, GPIO.LOW, True)
        self.write4bitsTwice(0x3, GPIO.LOW, True)
        self.write4bitsTwice(0x2, GPIO.LOW, True)

    def initLCD4bit(self):
        self.reset()
        self.write4bitsTwice(0x2C, GPIO.LOW, False)
        self.write4bitsTwice(0x0F, GPIO.LOW, False)
        self.write4bitsTwice(0x01, GPIO.LOW, False)
        self.write4bitsTwice(0x0C, GPIO.LOW, False)

    def write4bitsTwice(self, value, rs_mode,reset):
        GPIO.output(self.__PIN_RS, rs_mode)
        time.sleep(self.__delay)

        if reset != 1:
            for i in range(4):
                GPIO.output(self.__listDataPins[i], GPIO.HIGH if ((value >> i) & 1) > 0 else GPIO.LOW)
            self.pulseE()

        for i in range(4):
            GPIO.output(self.__listDataPins[i], GPIO.HIGH if ((value >> i) & 1) > 0 else GPIO.LOW)
        self.pulseE()

    def write4bitmsg(self, msg,line):
        self.write4bitsTwice(line, GPIO.LOW,False) # determines the line to write on 0x80 l1, 0xC0 l2

        for l in msg:
            self.write4bitsTwice(ord(l), GPIO.HIGH,False)
