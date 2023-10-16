# Project 06: RGB LED

### **Introduction**

![](/media/94bdff69e438989d8e0934e57f2e5c00.png)

RGB LEDS are made up of three colors (red, green, and blue) , which can emit different colors by mixing these three basic colors. In this project, we will introduce the RGB LED and show you how to use the Raspberry Pi Pico to control the RGB LED. Even though RGB LED is very basic, it is also a great way to learn the fundamentals of electronics and coding.

### **Components Required**

| ![img](media/wps127.png) | ![img](media/wps128.jpg)            | ![img](media/wps129.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | RGB LED*1                |
| ![img](media/wps130.jpg) | ![img](media/wps131.jpg)            | ![img](media/wps132.jpg) |
| 220ΩResistor*3           | Breadboard*1                        | Jumper Wires             |
| ![img](media/wps133.jpg) |                                     |                          |
| USB Cable*1              |                                     |                          |

### **Component Knowledge**

The monitors mostly adopt the RGB color standard, and all the colors on the computer screen are composed of the three colors of red, green and blue mixed in different proportions.

![](/media/8bf1339719a922f2fbc1e01a4347b4ab.png)

This RGB LED has 4 pins and a common cathode. To change its brightness, we can use the PWM of the Raspberry Pi Pico pins, which can give different duty cycle signals to the RGB LED to produce different colors.

If we use three 10-bit PWM to control the RGBLED, theoretically we can create 210\*210\*210= 1,073,741,824(1 billion) colors through different combinations.

### **Circuit Diagram and Wiring Diagram**

![](/media/f6950bc8498e6139cbb67db84cdd5a9a.png)

![](/media/fdab8c2fd2dfdd1670c09962e7b458ce.png)

**Note:**

RGB LED longest pin (common cathode) connected to GND.

![](/media/1584356c63bf99934ae0810ee02dced3.png)

How to identify the 220Ω 5-band resistor

![](/media/55c0199544e9819328f6d5778f10d7d0.png)

### **Test Code**

The code used in this project is saved in the file KS3020 Keyestudio Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.Python\_Tutorial\\2. Python Projects\\Project 06：RGB LED. You can move the code to anywhere, for example, we can save the code in the Disk(D, the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project 06：RGB LED”. And double left-click the“Project\_06\_RGB\_LED.py”.

![](/media/4d197d2ef390d93cbdcd6606fa754188.png)

```pyton
# import Pin, PWM and Random function modules.
from machine import Pin, PWM
from random import randint
import time

#configure ouput mode of GP18, GP17 and GP16 as PWM output and PWM frequency as 10000Hz.
pins = [18, 17, 16]
freq_num = 10000

pwm0 = PWM(Pin(pins[0]))  #set PWM
pwm1 = PWM(Pin(pins[1]))
pwm2 = PWM(Pin(pins[2]))
pwm0.freq(freq_num)
pwm1.freq(freq_num)
pwm2.freq(freq_num)

#define a function to set the color of RGBLED.
def setColor(r, g, b):
    pwm0.duty_u16(65535 - r)
    pwm1.duty_u16(65535 - g)
    pwm2.duty_u16(65535 - b)
    
try:
    while True:
        red   = randint(0, 65535) 
        green = randint(0, 65535)
        blue  = randint(0, 65535)
        setColor(red, green, blue)
        time.sleep_ms(200)
except:
    pwm0.deinit()
    pwm1.deinit()
    pwm2.deinit() 
```

### **Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](/media/a2b85aea8a2bd67ad184662be36a1c9e.png)

Click ![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts executing, we will see that RGB LED starts showing random colors. Press“Ctrl+C”or click“![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](/media/296bcab9a2eaccf483b8cb9e8b8a0e43.png)
