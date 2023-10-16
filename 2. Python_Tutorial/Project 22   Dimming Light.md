# Project 22 : Dimming Light

### **Introduction**

A potentiometer is a three-terminal resistor with a sliding or rotating contact that forms an adjustable voltage divider. It works by varying the position of a sliding contact across a uniform resistance. In a potentiometer, the entire input voltage is applied across the whole length of the resistor, and the output voltage is the voltage drop between the fixed and sliding contact.

In this project, we are going to learn how to use Raspberry Pi Pico to read the values of the potentiometer, and make a dimming lamp with LEDs.

### **Components Required**

| ![img](media/wps232.png) | ![img](media/wps233.jpg)            | ![img](media/wps234.jpg) | ![img](media/wps235.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | Potentiometer*1          | Red LED*1                |
| ![img](media/wps236.jpg) | ![img](media/wps237.jpg)            | ![img](media/wps238.jpg) | ![img](media/wps239.jpg) |
| Breadboard*1             | 220ΩResistor*1                      | Jumper Wires             | USB Cable*1              |

### **Component Knowledge**

![](/media/03ab81e8b4f09287d2781ef0fd297f85.png)

**Adjustable potentiometer:** It is a kind of resistor and an analog electronic component, which has two states of 0 and 1(high level and low level). The analog quantity is different, its data state presents a linear state such as 1 \~ 1024.

### **Read the Potentiometer Value**

We connect the adjustable potentiometer to the analog IO of the Raspberry Pi Pico to read its value and voltage value . Please refer to the following wiring diagram for wiring.

![](/media/b8ee6320bce8729a4309857f257d30ec.png)

![](/media/cb970a340d830569e9ac4462a1318e44.png)

The code used in this project is saved in the file KS3020 Keyestudio Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.Python\_Tutorial\\2. Python Projects\\Project 22：Dimming Light. You can move the code to anywhere, for example, we can save the code in the Disk(D), the route is D:\\2. Python Projects.

Open“Thonny, click“This computer”→“D:”→“2. Python Projects”→“Project 22：Dimming Light”. And double left-click
the“Project\_22.1\_Read\_Potentiometer\_Analog\_Value.py”.

![](/media/d9cf3ce6c364675b7e787b625232e23a.png)

```python
from machine import ADC, Pin
import time
# Initialize the potentiometer to pin 26 (ADC function)
adc = ADC(26)

# Print the current adc value of the potentiometer cyclically 
# Print the current voltage value of the potentiometer cyclically
try:
    while True:
        adcValue = adc.read_u16() # read the ADC value of potentiometer
        voltage = adcValue / 65535.0 * 3.3
        print("ADC Value:", adcValue, "Voltage:", voltage, "V")
        time.sleep(0.1)
except:
    pass
```


Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](/media/463e789ae8824b5c724e8ff9a084a674.png)

Click “Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the ADC value and voltage value of the potentiomete, turn the potentiometer handle, the ADC value and voltage value will change. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](/media/00c8eafb82c2ade2b6efe03ff4c5d8ac.png)

![](/media/969b9de3cf505f05d6a9361286cef9c9.png)

### **Circuit Diagram and Wiring Diagram**

In the last step, we read the value of the potentiometer, and now we need to convert the value of the potentiometer into the brightness of the LED to make a lamp that can adjust the brightness. The wiring diagram is as follows:

![](/media/66f721b77035d40556c873e0c4577b4a.png)

![](/media/93b03f3cdc8af506d9035b748839ac33.png)

### **Test Result**

The code used in this project is saved in the file KS3020 Keyestudio Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.Python\_Tutorial\\2. Python Projects\\Project 22：Dimming Light. You can move the code to anywhere, for example, we can save the code in the Disk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project 22：Dimming Light”. And double left-click
the“Project\_22.2\_Dimming\_Light.py”.

![](/media/a9b04adef7ed5ed1429a923974241984.png)

```python
from machine import ADC, Pin, PWM
import time

adc = ADC(26) # Initialize the potentiometer to pin 26 (ADC function)
pwm = PWM(Pin(16)) # Initialize the led's PWM to pin 16
pwm.freq(1000) # Define the PWM frequency as 1000
try:
    while True:
        adcValue = adc.read_u16() # read the ADC value of potentiometer
        pwm.duty_u16(adcValue) #map it to the duty cycle of PWM to control led brightness 
        time.sleep(0.1)
except:
    pwm.deinit()
```

### **Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](/media/1d2b9866779f2f666fcf4a65e22a2173.png)

Click “Run current script”, the code starts executing, we will see that turn the potentiometer handle and the brightness of the LED will change accordingly. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](/media/a00b986be5645a89d8fbcfb235b79cb9.png)

![](/media/eca30dead3f4923afa0dcb0306db2319.jpeg)
