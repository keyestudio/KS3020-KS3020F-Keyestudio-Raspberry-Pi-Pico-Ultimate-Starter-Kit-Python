# Project 31：Temperature Instrument

1.  **Introduction**
    
    Thermistor is a kind of resistor whose resistance depends on
    temperature changes, which is widely used in gardening, home alarm
    system and other devices. Therefore, we can use this feature to make
    a temperature instrument.

2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><p><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/8f45d8141f23885af95f870ab64a859c.jpeg" style="width:1.76389in;height:0.70278in" /></p></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png" style="width:1.66944in;height:1.28472in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/b45bb81bb3763377c63accce606ac5f2.png" style="width:0.25in;height:1.11597in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/b395b1cd2678f87b3a34dec15659efbc.png" style="width:0.22431in;height:1.00556in" /></td>
<td></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Thermistor*1</td>
<td>10KΩResistor*1</td>
<td></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/74ca4fa6d49dbd04de6a603c6e55a9ee.png" style="width:1.15347in;height:0.9625in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.56736in;height:1.38958in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/9232141f8a3166a8a6cdd43b78edd4e3.png" style="width:1.29722in;height:0.625in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/e9a8d050105397bb183512fb4ffdd2f6.png" style="width:1.10139in;height:1.03472in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:0.99028in;height:0.52986in" /></td>
</tr>
<tr class="even">
<td>10CM M-F Dupont Wires</td>
<td>Breadboard*1</td>
<td>LCD 128X32 DOT*1</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**
    
    Thermistor: A thermistor is a temperature sensitive resistor. When
    it senses a change in temperature, the thermistor's resistance
    changes. We can use this feature to detect temperature intensity
    with thermistor. Thermistors and its electronic symbols are shown
    below:

![](/media/809b8634747fb295021f12e3b92b7894.png)

The relation between thermistor resistance and temperature is:

**[in](javascript:;) [the](javascript:;) [formula](javascript:;): **

Rt is the resistance of the thermistor at T2 temperature.

R is the nominal resistance value of the thermistor at T1 room
temperature.

EXP\[n\] is the nth power of e.

B is the temperature index

T1 and T2 refer to K degrees, that is, Kelvin temperature. Kelvin
temperature =273.15 + Celsius temperature. For thermistor parameters, we
use : B=3950, R=10KΩ，T1=25℃.The circuit connection method of thermistor
is similar to that the photoresistor, as shown below :

![](/media/ac0d68aac58bffa5c99e1d0ed3a8bc37.jpeg)

We can use the value measured by the ADC converter to get the resistance
value of the thermistor, and then use the formula to get the temperature
value. Therefore, the temperature formula can be deduced as:

4.  **Read the Values**
    
    First we will learn the thermistor to read the current ADC value,
    voltage value and temperature value and print them out . Please
    connect the wires according to the following wiring diagram.

![](/media/c143dc239ceaa5e65a63f47d6512630c.png)

![](/media/c0ad763fa1dda5ce55d03fe9b3d61bcd.png)

The code used in this project is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects\\Project 31：Temperature Instrument.
You can move the code anywhere. We save the code to the pi folder of the
Raspberry Pi system. The path:home/pi/2. Projects

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project
31：Temperature Instrument”. And double left-click
the“Project\_31.1\_Read\_the\_thermistor\_analog\_value.py”.

![](/media/ad5f606c570f0ae011d4a28e7a48d848.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin, ADC</p>
<p>import time</p>
<p>import math</p>
<p>#Set ADC</p>
<p>adc=ADC(27)</p>
<p>try:</p>
<p>while True:</p>
<p>adcValue = adc.read_u16()</p>
<p>voltage = adcValue / 65535.0 * 3.3</p>
<p>Rt = 10 * voltage / (3.3-voltage)</p>
<p>tempK = (1 / (1 / (273.15+25) + (math.log(Rt/10)) / 3950))</p>
<p>tempC = int(tempK - 273.15)</p>
<p>print("ADC value:", adcValue, " Voltage: %0.2f"%voltage + "V",</p>
<p>" Temperature: " + str(tempC) + "C")</p>
<p>time.sleep(1)</p>
<p>except:</p>
<p>pass</p></td>
</tr>
</tbody>
</table>

Ensure that the Raspberry Pi Pico is connected to the
computer，click“![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](/media/73a6c53febad0486b1286b38a0625f9d.png)

Click ![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts
executing, we will see that the "Shell" window of Thonny IDE will
continuously display the thermistor's current ADC value, voltage value,
and temperature value.  Try pinching the thermistor with your index
finger and thumb (don't touch the wire) for a while, and you will see
the temperature increase. Press“Ctrl+C”or
click“![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](/media/fbf956504f3e5246fe465e789c10690d.png)

![](/media/0a035900fbc73a112eced64a926872ad.png)

5.  **Circuit Diagram and Wiring Diagram**

Note : LCD\_128X32\_DOT must be connected with a 10CM M-F Dupont wire,
the LCD\_128X32\_DOT will display normally. Otherwise, using a 20CM M-F
Dupont wire may cause the LCD\_128X32\_DOT display abnormally.  

![](/media/281774a4fbf4f7f2ca0fd1e60c89516c.png)

![](/media/91445212232765942d482b84da03f598.png)

6.  **Test Code**

The code used in this project is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects\\Project 31：Temperature Instrument.
You can move the code anywhere. We save the code to the pi folder of the
Raspberry Pi system. The path:home/pi/2. Projects

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project
31：Temperature Instrument”.
Select“lcd128\_32.py”and“lcd128\_32\_fonts.py”， right-click and
select“Upload to /”，waiting for the
“lcd128\_32.py”and“lcd128\_32\_fonts.py”to be uploaded to the
Raspberry Pi Pico. And double left-click
the“Project\_31.2\_Temperature\_Instrument.py”.

![](/media/96328c28b0e82498218b114936fe7e78.png)

![](/media/c3542c1f9ccb781e566a7e2e0329089f.png)

![](/media/2d174fc09d012690cb2de6e12e6f0ba1.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin, ADC, I2C</p>
<p>import time</p>
<p>import math</p>
<p>import lcd128_32_fonts</p>
<p>from lcd128_32 import lcd128_32</p>
<p>#Set ADC</p>
<p>adc=ADC(27)</p>
<p>#i2c config</p>
<p>clock_pin = 21</p>
<p>data_pin = 20</p>
<p>bus = 0</p>
<p>i2c_addr = 0x3f</p>
<p>use_i2c = True</p>
<p>def scan_for_devices():</p>
<p>i2c = machine.I2C(bus,sda=machine.Pin(data_pin),scl=machine.Pin(clock_pin))</p>
<p>devices = i2c.scan()</p>
<p>if devices:</p>
<p>for d in devices:</p>
<p>print(hex(d))</p>
<p>else:</p>
<p>print('no i2c devices')</p>
<p>try:</p>
<p>while True:</p>
<p>adcValue = adc.read_u16()</p>
<p>voltage = adcValue / 65535.0 * 3.3</p>
<p>Rt = 10 * voltage / (3.3-voltage)</p>
<p>tempK = (1 / (1 / (273.15+25) + (math.log(Rt/10)) / 3950))</p>
<p>tempC = int(tempK - 273.15)</p>
<p>if use_i2c:</p>
<p>scan_for_devices()</p>
<p>lcd = lcd128_32(data_pin, clock_pin, bus, i2c_addr)</p>
<p>lcd.Clear()</p>
<p>lcd.Cursor(0, 0)</p>
<p>lcd.Display("Voltage:")</p>
<p>lcd.Cursor(0, 8)</p>
<p>lcd.Display(str(voltage))</p>
<p>lcd.Cursor(0, 20)</p>
<p>lcd.Display("V")</p>
<p>lcd.Cursor(2, 0)</p>
<p>lcd.Display("Temperature:")</p>
<p>lcd.Cursor(2, 12)</p>
<p>lcd.Display(str(tempC))</p>
<p>lcd.Cursor(2, 15)</p>
<p>lcd.Display("C")</p>
<p>time.sleep(0.5)</p>
<p>except:</p>
<p>pass</p></td>
</tr>
</tbody>
</table>

7.  **Test Result**
    
    Ensure that the Raspberry Pi Pico is connected to the
    computer，click“![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.
    
    ![](/media/09d2a491dfb201b3b9c9cfd00ab8a8ac.png)
    
    Click “Run current script”, the code starts executing, we will see
    that the LCD 128X32 DOT displays the voltage value of the thermistor
    and the temperature value in the current environment.
    Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](/media/3b29267af1b5bb81abd99c53aee49e8f.png)
