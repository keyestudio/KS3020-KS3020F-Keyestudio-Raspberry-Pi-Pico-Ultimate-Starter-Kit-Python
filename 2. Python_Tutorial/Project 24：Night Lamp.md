# Project 24：Night Lamp

### **Introduction**

Sensors or components are ubiquitous in our daily life. For example, some public street lights turn on automatically at night and turn off automatically during the day. 

Why? In fact, this make use of a photosensitive element that senses the intensity of external ambient light. When the outdoor brightness decreases at night, the street lights will automatically turn on. In the daytime, the street lights will automatically turn off. The principle of this is very simple. In this lesson we will use Raspberry Pi Pico to control LEDs to implement the function of this street light.

### **Components Required**

| ![img](media/wps250.png) | ![img](media/wps251.jpg)            | ![img](media/wps252.jpg) | ![img](media/wps253.jpg) | ![img](media/wps254.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ | ------------------------ | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | Photoresistor*1          | Red LED*1                | 10KΩResistor*1           |
| ![img](media/wps255.jpg) | ![img](media/wps256.jpg)            | ![img](media/wps257.jpg) | ![img](media/wps258.jpg) |                          |
| Breadboard*1             | 220ΩResistor*1                      | Jumper Wires             | USB Cable*1              |                          |

### **Component Knowledge**

![](/media/9e553e75b6f976f33438171eb2f2e775.png)

It is a photosensitive resistor, its principle is that the photoresistor surface receives brightness (light) to reduce the resistance. The resistance value will change with the detected intensity of the ambient light . With this property, we can use photoresistors to detect light intensity.  Photoresistors and other electronic symbols are as follows:


![](/media/7d575da675a2f6cb511d28b801e2abaa.png)

The following circuit is used to detect changes in resistance values of photoresistors:

![](/media/5a7f7e641eb78007760a94151c1d80a5.png)

In the circuit above, when the resistance of the photoresistor changes due to the change of light intensity, the voltage between the  photoresistor and resistance R2 will also change.  Thus, the intensity of light can be obtained by measuring this voltage.

### **Read the Analog Value**

We first use a simple code to read the value of the photoresistor, print it in the serial monitor. For wiring, please refer to the following wiring diagram.

![](/media/e3fde13b200927346e04b032373ce638.png)

![](/media/b97ff27ae10e3499c36312c8ee4881f8.png)

The code used in this project is saved in the file KS3020 Keyestudio Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.Python\_Tutorial\\2. Python Projects\\Project 24：Night Lamp. You can move the code to anywhere, for example, we can save the code in the Disk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project 24：Night Lamp”. And double left-click
the“Project\_24.1\_Read\_Photosensitive\_Analog\_Value.py”.

![](/media/bbda9735710eb80196f54a5096f16799.png)

```python
from machine import ADC, Pin
import time
# Initialize the photoresistance to pin 26 (ADC function)
adc = ADC(26)

# Read the current analog value of the photoresistance and return [0, 1023]
def get_value():
    return int(adc.read_u16() * 1024 / 65536)
 
# Print the current value of the photoresistance cyclically, value=[0, 1023]
while True:
    value = get_value()
    print(value)
    time.sleep(0.1)
```


Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](/media/8a0c37dff4793d4132a9c88e932f499b.png)

Click “Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the analog value read by the photoresistor. When the light intensity around the photoresistor is gradually reduced, the analog value will gradually increase. On the contrary, the analog value decreases gradually. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](/media/889383400283bc151486ce0bf5820a92.png)

![](/media/bbabb2d5c4a997c5024e6023cb272261.png)

### **Circuit Diagram and Wiring Diagram**

We made a little dimmer in the front, now let's make a light controlled lamp. The principle is the same, the Raspberry Pi Pico will be used to obtain the analog value of the sensor and then adjust the brightness of the LED.  

![](/media/b8e8d95bdc869bf76465fa73645db831.png)

![](/media/71f2886dc6fa97d02e2ecd0d429af71b.png)

### **Test Code**

The code used in this project is saved in the file KS3020 Keyestudio Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.Python\_Tutorial\\2. Python Projects\\Project 24：Night Lamp. You can move the code to anywhere, for example, we can save the code in the Disk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project 24：Night Lamp”. And double left-click
the“Project\_24.2\_Night\_Lamp.py”.

![](/media/c08014a9603cbf3b2411440b5e7d761e.png)

```python
from machine import Pin, ADC, PWM
import time

adc = ADC(26) # Initialize the potentiometer to pin 26 (ADC function)
pwm = PWM(Pin(16)) # Initialize the led's PWM to pin 16
pwm.freq(10000) # Define the PWM frequency as 1000
try:
    while True:
        adcValue = adc.read_u16() # read the ADC value of photoresistance
        pwm.duty_u16(adcValue) # map ADC value to the duty cycle of PWM to control led brightness
        time.sleep(0.1) # delay
except:
    pwm.deinit()
```

### **Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](/media/dcf4815ce265653df6759637b24087c0.png)

Click “Run current script”, the code starts executing, we will see that when the intensity of light around the photoresistor is reduced, the LED will be bright, on the contraty, the LED will be dim. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](/media/03dd68eab6f2579e15852f13c10ddc98.png)
