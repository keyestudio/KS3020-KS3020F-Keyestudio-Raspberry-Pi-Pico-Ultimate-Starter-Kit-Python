from machine import Pin,PWM
import utime
from irrecvdata import irGetCMD

#Set RGB light interface and frequency
rgb_r = PWM(Pin(19))
rgb_g = PWM(Pin(18))
rgb_b = PWM(Pin(17))
rgb_r.freq(1000)
rgb_g.freq(1000)
rgb_b.freq(1000)

# Initialize the buzzer pin to PWM function
buzzer=PWM(Pin(15, Pin.OUT))
buzzer.freq(262)
buzzer.duty_u16(0)

# Play the frequency of midrange tones 1-7
freq = [262, 294, 330, 350, 393, 441, 495]

#Configure infrared receiving pin and library
recvPin = irGetCMD(16)

# Set the buzzer to emit different tones.
# index=[0-7], where 0 is closed, and 1-7 respectively represent middle C, middle D, middle E, middle F, middle G, middle A, middle B.
# time represents the function delay time (a positive integer), in milliseconds.
# auto_off indicates whether the buzzer will be turned off automatically after the delay time.
def tone(index, time=0, auto_off=False):
    if index == 0:
        buzzer.duty_u16(0)
        utime.sleep_ms(time)
    elif index >= 1 and index <= 7:
        tone_freq = freq[int(index - 1)]
        buzzer.freq(tone_freq)
        buzzer.duty_u16(32768)
        utime.sleep_ms(time)
        if auto_off == True:
            buzzer.duty_u16(0)
        # print("----freq:", index, tone_freq)
    else:
        print("Tones must be 0-7")
 
delay = 0
 
tone(1, 100, True)

while True:
    irValue = recvPin.ir_read() # Read remote control data
# Determine whether there is a button that meets the needs 
    if irValue:
        print(irValue)
        if irValue == '0xff6897':   #1
           rgb_r.duty_u16(65535)
           rgb_g.duty_u16(0)
           rgb_b.duty_u16(0)
           tone(1, delay)
        elif irValue == '0xff9867': #2
            rgb_r.duty_u16(0)
            rgb_g.duty_u16(65535)
            rgb_b.duty_u16(0)
            tone(2, delay)
        elif irValue == '0xffb04f': #3
            rgb_r.duty_u16(0)
            rgb_g.duty_u16(0)
            rgb_b.duty_u16(65535)
            tone(3, delay)
        elif irValue == '0xff30cf': #4
            rgb_r.duty_u16(65535)
            rgb_g.duty_u16(65535)
            rgb_b.duty_u16(0)
            tone(4, delay)
        elif irValue == '0xff18e7': #5
            rgb_r.duty_u16(65535)
            rgb_g.duty_u16(0)
            rgb_b.duty_u16(65535)
            tone(5, delay)
        elif irValue == '0xff7a85': #6
            rgb_r.duty_u16(0)
            rgb_g.duty_u16(65535)
            rgb_b.duty_u16(65535)
            tone(6, delay)
        elif irValue == '0xff10ef': #7
            rgb_r.duty_u16(65535)
            rgb_g.duty_u16(65535)
            rgb_b.duty_u16(65535)
            tone(7, delay) 
        else:
            rgb_r.duty_u16(0)
            rgb_g.duty_u16(0)
            rgb_b.duty_u16(0)
            tone(0)