# Project 07: Flowing Water Light

### **Introduction**

In our daily life, we can see many billboards made up of different colors of LED. They constantly change the light to attract the attention of customers. In this project, we will use Raspberry Pi Pico to control 10 LEDs to achieve the effect of flowing water.

### **Components Required**

| ![img](media/wps134.png) | ![img](media/wps135.jpg)            | ![img](media/wps136.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | Red LED*10               |
| ![img](media/wps137.jpg) | ![img](media/wps138.jpg)            | ![img](media/wps139.jpg) |
| 220ΩResistor*10          | Breadboard*1                        | Jumper Wires             |
| ![img](media/wps140.jpg) |                                     |                          |
| USB Cable*1              |                                     |                          |

### **Circuit Diagram and Wiring Diagram**

![](/media/fc6e73a6664012c9a33262b50d6e256f.png)

**Note:**

How to connect the LED

![](/media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω 5-band resistor

![](/media/55c0199544e9819328f6d5778f10d7d0.png)

### **Test Code**

This project is to design and manufacture a flowing water light.  Here are the steps: first , turn on LED \#1, then turn it off.  Second, turn on LED \#2, then turn off... . Do the same for the 10 LEDs until the last one is turned off.  Repeating the process to achieve the "movement" of the water.

The code used in this project is saved in the file KS3020 Keyestudio Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.Python\_Tutorial\\2. Python Projects\\Project 07：Flowing Water Light.You can move the code to anywhere, for example, we can save the code in the Disk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project 07：Flowing Water Light”. And double left-click
the“Project\_07\_Flowing\_Water\_Light.py”.

![](/media/a923fafe77f629ea8288ec40b52a6059.png)

```python
from machine import Pin
import time

#Use an array to define 10 GPIO ports connected to LED Bar Graph for easier operation.
pins = [16, 17, 18, 19, 20, 21, 22, 26, 27, 28]
#Use two for loops to turn on LEDs separately from left to right and then back from right to left
def showLed():
    for pin in pins:
        print(pin)
        led = Pin(pin, Pin.OUT)
        led.value(1)
        time.sleep_ms(100)
        led.value(0)
        time.sleep_ms(100)        
    for pin in reversed(pins):
        print(pin)
        led = Pin(pin, Pin.OUT)
        led.value(1)
        time.sleep_ms(100)
        led.value(0)
        time.sleep_ms(100)
          
while True:
    showLed()
```

### **Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](/media/b908750521d4d2b64c55751825916a7e.png)

Click ![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts executing, we will see that the 10 LEDs will light up from left to right and then return from right to left. Press“Ctrl+C”or click“![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](/media/c9814fae261b7f8c9d2b33938d8e6144.png)

![image-20231013142059620](media/image-20231013142059620.png)
