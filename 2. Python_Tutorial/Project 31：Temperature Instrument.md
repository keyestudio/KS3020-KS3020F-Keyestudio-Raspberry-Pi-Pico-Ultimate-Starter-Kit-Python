# Project 31：Temperature Instrument

### **Introduction**

Thermistor is a kind of resistor whose resistance depends on temperature changes, which is widely used in gardening, home alarm system and other devices. Therefore, we can use this feature to make a temperature instrument.

### **Components Required**

| ![img](media/wps312.png) | ![img](media/wps313.jpg)            | ![img](media/wps314.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | Thermistor*1             |
| ![img](media/wps315.jpg) | ![img](media/wps316.jpg)            | ![img](media/wps317.jpg) |
| 10CM M-F Dupont Wires    | Breadboard*1                        | LCD 128X32 DOT*1         |
| ![img](media/wps318.jpg) | ![img](media/wps319.jpg)            | ![img](media/wps320.jpg) |
| 10KΩResistor*1           | Jumper Wires                        | USB Cable*1              |

### **Component Knowledge**

Thermistor: A thermistor is a temperature sensitive resistor. When it senses a change in temperature, the thermistor's resistance changes. We can use this feature to detect temperature intensity with thermistor. Thermistors and its electronic symbols are shown below:

![](/media/809b8634747fb295021f12e3b92b7894.png)

The relation between thermistor resistance and temperature is:

![img](media/wps321.png)

**in the formula: **

Rt is the resistance of the thermistor at T2 temperature.

R is the nominal resistance value of the thermistor at T1 room temperature.

EXP\[n\] is the nth power of e.

B is the temperature index

T1 and T2 refer to K degrees, that is, Kelvin temperature. Kelvin temperature =273.15 + Celsius temperature. For thermistor parameters, we use : B=3950, R=10KΩ，T1=25℃.The circuit connection method of thermistor is similar to that the photoresistor, as shown below :

![](/media/ac0d68aac58bffa5c99e1d0ed3a8bc37.jpeg)

We can use the value measured by the ADC converter to get the resistance value of the thermistor, and then use the formula to get the temperature value. Therefore, the temperature formula can be deduced as:

![img](media/wps322.png)

### **Read the Values**

First we will learn the thermistor to read the current ADC value, voltage value and temperature value and print them out . Please connect the wires according to the following wiring diagram.

![](/media/c143dc239ceaa5e65a63f47d6512630c.png)

![](/media/c0ad763fa1dda5ce55d03fe9b3d61bcd.png)

The code used in this project is saved in the file KS3020 Keyestudio Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.Python\_Tutorial\\2. Python Projects\\Project 31：Temperature Instrument. You can move the code anywhere. We save the code to the pi folder of the Raspberry Pi system. The path:home/pi/2. Projects

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project 31：Temperature Instrument”. And double left-click
the“Project\_31.1\_Read\_the\_thermistor\_analog\_value.py”.

![](/media/ad5f606c570f0ae011d4a28e7a48d848.png)

```python
from machine import Pin, ADC
import time
import math

#Set ADC
adc=ADC(27)

try:
    while True:
        adcValue = adc.read_u16()
        voltage = adcValue / 65535.0 * 3.3
        Rt = 10 * voltage / (3.3-voltage)
        tempK = (1 / (1 / (273.15+25) + (math.log(Rt/10)) / 3950))
        tempC = int(tempK - 273.15)
        print("ADC value:", adcValue, "  Voltage: %0.2f"%voltage + "V",
              "  Temperature: " + str(tempC) + "C")
        time.sleep(1)
except:
    pass
```


Ensure that the Raspberry Pi Pico is connected to the computer，click“![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](/media/73a6c53febad0486b1286b38a0625f9d.png)

Click ![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will continuously display the thermistor's current ADC value, voltage value, and temperature value.  Try pinching the thermistor with your index finger and thumb (don't touch the wire) for a while, and you will see the temperature increase. Press“Ctrl+C”or click“![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](/media/fbf956504f3e5246fe465e789c10690d.png)

![](/media/0a035900fbc73a112eced64a926872ad.png)

### **Circuit Diagram and Wiring Diagram**

Note : LCD\_128X32\_DOT must be connected with a 10CM M-F Dupont wire, the LCD\_128X32\_DOT will display normally. Otherwise, using a 20CM M-F Dupont wire may cause the LCD\_128X32\_DOT display abnormally.  

![](/media/281774a4fbf4f7f2ca0fd1e60c89516c.png)

![](/media/91445212232765942d482b84da03f598.png)

### **Test Code**

The code used in this project is saved in the file KS3020 Keyestudio Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.Python\_Tutorial\\2. Python Projects\\Project 31：Temperature Instrument. You can move the code anywhere. We save the code to the pi folder of the Raspberry Pi system. The path:home/pi/2. Projects

Open “Thonny”, click “This computer” → “D:” → “2. Python Projects” → “Project 31：Temperature Instrument”. Select “lcd128\_32.py” and “lcd128\_32\_fonts.py”,  right-click and select “Upload to /”, waiting for the “lcd128\_32.py” and “lcd128\_32\_fonts.py” to be uploaded to the Raspberry Pi Pico. And double left-click the “Project\_31.2\_Temperature\_Instrument.py”.

![](/media/96328c28b0e82498218b114936fe7e78.png)

![](/media/c3542c1f9ccb781e566a7e2e0329089f.png)

![](/media/2d174fc09d012690cb2de6e12e6f0ba1.png)

```python
from machine import Pin, ADC, I2C
import time
import math
import lcd128_32_fonts
from lcd128_32 import lcd128_32

#Set ADC
adc=ADC(27)

#i2c config
clock_pin = 21
data_pin = 20
bus = 0
i2c_addr = 0x3f
use_i2c = True

def scan_for_devices():
    i2c = machine.I2C(bus,sda=machine.Pin(data_pin),scl=machine.Pin(clock_pin))
    devices = i2c.scan()
    if devices:
        for d in devices:
            print(hex(d))
    else:
        print('no i2c devices')

try:
    while True:
        adcValue = adc.read_u16()
        voltage = adcValue / 65535.0 * 3.3
        Rt = 10 * voltage / (3.3-voltage)
        tempK = (1 / (1 / (273.15+25) + (math.log(Rt/10)) / 3950))
        tempC = int(tempK - 273.15)
        
        if use_i2c:
            scan_for_devices()
            lcd = lcd128_32(data_pin, clock_pin, bus, i2c_addr)
            
        lcd.Clear()
        lcd.Cursor(0, 0)
        lcd.Display("Voltage:")
        lcd.Cursor(0, 8)
        lcd.Display(str(voltage))
        lcd.Cursor(0, 20)
        lcd.Display("V")
        lcd.Cursor(2, 0)
        lcd.Display("Temperature:")
        lcd.Cursor(2, 12)
        lcd.Display(str(tempC))
        lcd.Cursor(2, 15)
        lcd.Display("C")
        time.sleep(0.5)
except:
    pass
```

### **Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](/media/09d2a491dfb201b3b9c9cfd00ab8a8ac.png)

Click “Run current script”, the code starts executing, we will see that the LCD 128X32 DOT displays the voltage value of the thermistor and the temperature value in the current environment. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](/media/3b29267af1b5bb81abd99c53aee49e8f.png)
