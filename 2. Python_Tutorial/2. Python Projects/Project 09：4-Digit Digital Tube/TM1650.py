# MicroPython TM1650 driver, I2C and SPI interfaces

import time

COMMAND_I2C_ADDRESS = 0x24
DISPLAY_I2C_ADDRESS = 0x34
SEG = [0x3F,0x06,0x5B,0x4F,0x66,0x6D,0x7D,0x07,0x7F,0x6F,]


class TM1650():
    def __init__(self, i2c):
        self.i2c = i2c
        self.cmd(3,8,1)
        time.sleep(0.01)

    # Digital tube display num
    def display_write(self, num,bit):
        self.i2c.writeto(DISPLAY_I2C_ADDRESS+bit, bytearray([SEG[num]]))
        
    def display(self, num):
        if num < 0:
            self.i2c.writeto(DISPLAY_I2C_ADDRESS, 0x40)
        num1 = int(num/1000)
        num2 = int(num%1000/100)
        num3 = int(num%100/10)
        num4 = int(num%10)
        if num > 999:
            self.display_write(num1,0)
        if num > 99:
            self.display_write(num2,1)
        if num > 9:
            self.display_write(num3,2)
        if num >= 0:
            self.display_write(num4,3)
        
    #  clear Digital tube display
    def display_clear(self):
        self.i2c.writeto(DISPLAY_I2C_ADDRESS, bytearray([0]))
        self.i2c.writeto(DISPLAY_I2C_ADDRESS+1, bytearray([0]))
        self.i2c.writeto(DISPLAY_I2C_ADDRESS+2, bytearray([0]))
        self.i2c.writeto(DISPLAY_I2C_ADDRESS+3, bytearray([0]))

    # set Digital tube light(0-7)/bit(7 or 8)/on or off(1 or 0)
    def cmd(self, light, bit, on):
        self.i2c.writeto(COMMAND_I2C_ADDRESS,bytearray([light*16+on+8*(8-bit)]))

