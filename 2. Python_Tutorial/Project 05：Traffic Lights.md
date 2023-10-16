# Project 05：Traffic Lights

### **Introduction**

Traffic lights are closely related to people's daily lives, which generally show red, yellow, and green. Everyone should obey the traffic rules, which can avoid many traffic accidents. In this project, we will use Raspberry Pi Pico and some LEDs (red, green and yellow) to simulate the traffic lights.

### **Components Required**

| ![img](media/wps118.png) | ![img](media/wps119.jpg)            | ![img](media/wps120.jpg)                |
| ------------------------ | ----------------------------------- | --------------------------------------- |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | Red LED*1                               |
| ![img](media/wps121.jpg) | ![img](media/wps122.jpg)            | ![img](media/wps123-16971769965132.jpg) |
| Green LED*1              | USB Cable*1                         | 220ΩResistor*3                          |
| ![img](media/wps126.jpg) | ![img](media/wps124.jpg)            | ![img](media/wps125.jpg)                |
| Yellow LED*1             | Breadboard*1                        | Jumper Wires                            |

### **Circuit Diagram and Wiring Diagram**



![](/media/98f9db025163638c33095cbd16abe7e7.png)

Note:

How to connect an LED

![](/media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω 5-band resistor

![](/media/55c0199544e9819328f6d5778f10d7d0.png)

### **Test Code**

The code used in this project is saved in the file KS3020 Keyestudio Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows
System\\1.Python\_Tutorial\\2. Python Projects\\Project 05：Traffic Lights. You can move the code to anywhere, for example, we can save the code in the Disk(D), the route is D:\\2. Python Projects.)

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→”Project 05：Traffic Lights”and double left-click the“Project\_05\_Traffic\_Lights.py”.

![](/media/23e79112920bc111a9bc621dc75162a0.png)

```python
from machine import Pin
import time

led_red = machine.Pin(16, machine.Pin.OUT)  # create red led object from Pin 16, Set Pin 16 to output
led_yellow = machine.Pin(17, machine.Pin.OUT)  # create yellow led object from Pin 17, Set Pin 17 to output
led_green = machine.Pin(18, machine.Pin.OUT) # create green led object from Pin 18, Set Pin 18 to output

while True:
    led_red.value(1)  # Set red led turn on
    time.sleep(5)   # Sleep 5s
    led_red.value(0) # Set red led turn off 
    led_yellow.value(1)
    time.sleep(0.5)
    led_yellow.value(0)
    time.sleep(0.5)
    led_yellow.value(1)
    time.sleep(0.5)
    led_yellow.value(0)
    time.sleep(0.5)
    led_yellow.value(1)
    time.sleep(0.5)
    led_yellow.value(0)
    time.sleep(0.5)
    led_green.value(1)
    time.sleep(5) 
    led_green.value(0) 
```

### **Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer, click “![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](/media/914349b7c46f99b24beaada57db00815.png)

Click“![](/media/da852227207616ccd9aff28f19e02690.png)Run current script”, the code starts executing, what we will see are below:

1.  First, the green light will be on for 5 seconds and then off; 

2.  Next, the yellow light blinks three times and then goes off. 

3.  Then, the red light goes on for five seconds and then goes off. 
    

Repeat steps 1 to 3 above and press“Ctrl+C”or click“![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend” to exit the program.

![](/media/ff8674d60cc99a8c3bbef24bf65ae20c.png)
