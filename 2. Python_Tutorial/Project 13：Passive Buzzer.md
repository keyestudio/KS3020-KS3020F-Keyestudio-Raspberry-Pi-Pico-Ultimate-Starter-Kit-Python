# Project 13：Passive Buzzer

### **Introduction**

In a previous project, we have learned an active buzzer, which can only produce one sound and may let you feel monotonous. In this project, we will learn a passive buzzer and use the Raspberry Pi Pico to control the passive buzzer to sound an alarm. Unlike the active buzzer, the passive buzzer can emit sounds of different frequencies.

### **Components Required**

| ![img](media/wps175.png) | ![img](media/wps176.jpg)           | ![img](media/wps177.jpg) |
| ------------------------ | ---------------------------------- | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi PicoExpansion Board*1 | Passive Buzzer*1         |
| ![img](media/wps172.jpg) | ![img](media/wps173.jpg)           | ![img](media/wps174.jpg) |
| Breadboard*1             | Jumper Wires                       | USB Cable*1              |

### **Component Knowledge**

![](/media/8d0020e53824072cbe9d4f7d2f8acb4f.png)

A passive buzzer is an integrated electronic buzzer with no internal vibration source. It must be driven by 2K to 5K square wave, not a DC signal. The two buzzers are very similar in appearance, but one buzzer with a green circuit board is a passive buzzer, while the other with black tape is an active buzzer. Passive buzzers cannot distinguish between positive polarity while active buzzers can.

![](/media/fc42c5ed014609ff0b290ee5361bb2fd.png)

### **Circuit Diagram and Wiring Diagram**

![](/media/e0da1ccdbff24d256db130816c55da74.png)

![](/media/e601e48f8deddb3e9e7734d0022106b3.png)

### **Test Code**

The code used in this project is saved in the file KS3020 Keyestudio Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.Python\_Tutorial\\2. Python Projects\\Project 13：Passive Buzzer. You can move the code to anywhere, for example, we can save the code in the Disk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project 13：Passive Buzzer”. And double left-click
the“Project\_13\_Passive\_Buzzer.py”.

![](/media/4e4cf166f1de082468ebf77ef6ba3d4d.png)

```python
from machine import Pin
import time

#Initialize the passive buzzer
buzzer = Pin(16,Pin.OUT)

#Simulate two different frequencies
while True:
    #Output 500HZ frequency sound
    for i in range(80):
        buzzer.value(1)
        time.sleep(0.001)
        buzzer.value(0)
        time.sleep(0.001)
    #Output 250HZ frequency sound
    for i in range(100):
        buzzer.value(1)
        time.sleep(0.002)
        buzzer.value(0)
        time.sleep(0.002)
```

### **Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](/media/699667c6aea0990e6a2fa408ef7ca3a1.png)

Click “![](/media/da852227207616ccd9aff28f19e02690.png)Run current script”, the code starts executing, we will see that the the passive buzzer sounds the alarm. Press “Ctrl+C” or click “![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend” to exit the program.

![](/media/02d6cb5bd3d2cef4e669886b957544ed.png)
