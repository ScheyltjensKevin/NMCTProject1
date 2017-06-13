import RPi.GPIO as GPIO
import time

class LCD_controll():
    def __init__(self, RS, E, D0, D1, D2, D3, D4, D5, D6, D7, messageLine1, messageLine2, bitMode):
        self.__delay = 0.002
        self.__line1 = 0x80
        self.__line2 = 0xC0
        self.__PIN_RS = RS
        # self.__PIN_RW = RW
        self.__PIN_E = E
        self.__PIN_D0 = D0
        self.__PIN_D1 = D1
        self.__PIN_D2 = D2
        self.__PIN_D3 = D3
        self.__PIN_D4 = D4
        self.__PIN_D5 = D5
        self.__PIN_D6 = D6
        self.__PIN_D7 = D7
        self.__bitmode = bitMode
        self.__msgL1 = messageLine1
        self.__msgL2 = messageLine2
        self.__listAllPins = [self.__PIN_RS, self.__PIN_E, self.__PIN_D0, self.__PIN_D1, self.__PIN_D2,
                              self.__PIN_D3, self.__PIN_D4, self.__PIN_D5, self.__PIN_D6, self.__PIN_D7]
        self.__listDataPins = [self.__PIN_D0, self.__PIN_D1, self.__PIN_D2, self.__PIN_D3, self.__PIN_D4, self.__PIN_D5,
                               self.__PIN_D6, self.__PIN_D7]
        self.main(self.__msgL1, self.__msgL2, self.__bitmode)

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

    @property
    def bitmode(self):
        return self.__bitmode

    @bitmode.setter
    def bitmode(self,value):
        self.__bitmode = value

    def main(self, msgL1, msgL2, bitmode):

        if bitmode == 4:
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

        elif bitmode == 8:
            try:
                self.init()
                self.reset8bits()
                self.initLcd()
                self.write8bitmsg(msgL1, self.__line1)
                self.write8bitmsg(msgL2, self.__line2)
                while True:
                    pass
            except KeyboardInterrupt:
                self.initLcd()
                self.reset8bits()
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
                GPIO.output(self.__listDataPins[i + 4], GPIO.HIGH if ((value >> i + 4) & 1) > 0 else GPIO.LOW)
            self.pulseE()

        for i in range(4):
            GPIO.output(self.__listDataPins[i + 4], GPIO.HIGH if ((value >> i) & 1) > 0 else GPIO.LOW)
        self.pulseE()

    def write4bitmsg(self, msg,line):
        self.write4bitsTwice(line, GPIO.LOW,False) # determines the line to write on 0x80 l1, 0xC0 l2

        for l in msg:
            self.write4bitsTwice(ord(l), GPIO.HIGH,False)

    #-------------------------------8 bit code beneath this ---------------------------------
    def instructie(self,hexaBit):
        self.eHoogInstructie()
        self.setGPIODataBits(hexaBit)
        self.eLaagInstructie()
        time.sleep(self.__delay)

    def initLcd(self):
        self.instructie(0x38)  # function set
        self.instructie(0x0f)  # display on or or
        self.instructie(0x01)  # clear display
        self.instructie(0x06)  # entry mode

    def reset8bits(self):
        self.instructie(0x30)  # functionset
        time.sleep(self.__delay)

        self.instructie(0x30)  # functionset
        time.sleep(self.__delay)

        self.instructie(0x30)  # functionset
        time.sleep(self.__delay)

    def eHoogInstructie(self,Ebit=1, RSbit=0):
        GPIO.output(self.__listAllPins[1], Ebit)
        GPIO.output(self.__listAllPins[0], RSbit)

    def eLaagInstructie(self,Ebit=0, RSbit=0):
        GPIO.output(self.__listAllPins[1], Ebit)
        GPIO.output(self.__listAllPins[0], RSbit)

    def eHoogData(self,Ebit=1, RSbit=1):
        GPIO.output(self.__listAllPins[1], Ebit)
        GPIO.output(self.__listAllPins[0], RSbit)

    def eLaagData(self,Ebit=0, RSbit=1):
        GPIO.output(self.__listAllPins[1], Ebit)
        GPIO.output(self.__listAllPins[0], RSbit)

    def setGPIODataBits(self,data):
        filter = 0x80
        for i in range(0, 8):
            bit = data & filter
            filter = filter >> 1
            GPIO.output(self.__listDataPins[(7-i)], bit)

    def write8bitmsg(self,value,line):
        self.eHoogInstructie()
        self.setGPIODataBits(line)
        self.eLaagInstructie()
        time.sleep(self.__delay)

        for letter in value:
            self.eHoogData()
            self.setGPIODataBits(ord(letter))
            self.eLaagData()
            time.sleep(self.__delay)