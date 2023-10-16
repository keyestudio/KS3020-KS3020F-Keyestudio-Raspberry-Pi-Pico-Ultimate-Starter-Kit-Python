# Project 21：Relay

### **Introduction**

In daily life, we generally use AC to drive electrical equipment, and sometimes we use switches to control electrical appliances. If the switch is directly connected to the AC circuit, once electricity leakage occurs, people are in danger. From a safety point of view, we specially designed this relay module with NO (normally open) and NC (normally closed) terminals. In this lesson we will learn a special and easy-to-use switch, which is the relay module.

### **Components Required**

| ![img](media/wps227.png) | ![img](media/wps228.jpg)            | ![img](media/wps229.jpg) | ![img](media/wps230.jpg) | ![img](media/wps231.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ | ------------------------ | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | Relay Module*1           | M-F Dupont Wires         | USB Cable*1              |

### **Component Knowledge**

**Relay:** It is an "automatic switch" that uses a small current to control the operation of a large current.

Input voltage：3.3V-5V

Rated load：5A 250VAC (NO/NC) 5A 24VDC (NO/NC)

The rated load means that devices with dc voltage of 24V or AC voltage of 250V can be controlled using 3.3V-5V microcontrollers.  

**Schematic diagram of the Relay:**

![image-20231013145356951](media/image-20231013145356951.png)

### **Wiring Diagram**

![](/media/0e76ea13b2034301be2ecdfde7f21f1e.png)

### **Test Code**

The code used in this project is saved in the file KS3020 Keyestudio Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.Python\_Tutorial\\2. Python Projects\\Project 21：Relay. You can move the code to anywhere, for example, we can save the code in the Disk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project 21：Relay”. And double left-click the“Project\_21\_Relay.py”.

![](/media/6b610e7e5081befcea5305663f426d38.png)

```python
from machine import Pin
import time

# create relay from Pin 16, Set Pin 16 to output 
relay = Pin(16, Pin.OUT)
 
# The relay is opened, COM and NO are connected on the relay, and COM and NC are disconnected.
def relay_on():
    relay(1)
 
# The relay is closed, the COM and NO on the relay are disconnected, and the COM and NC are connected.
def relay_off():
    relay(0)
 
# Loop, the relay is on for one second and off for one second
while True:
    relay_on()
    time.sleep(1)
    relay_off()
    time.sleep(1)
```

### **Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](/media/e9e38c240d8278f282fd2912cc73d331.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts executing, we will see that the relay will cycle on and off, on for 1 second, off for 1 second.  At the same time, you can hear the sound of the relay on and off, and you can also see the change of the indicator light on the relay. Press“Ctrl+C”or click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to exit the program.

![](/media/be6f35e062c5656930fffa6dce839777.png)
