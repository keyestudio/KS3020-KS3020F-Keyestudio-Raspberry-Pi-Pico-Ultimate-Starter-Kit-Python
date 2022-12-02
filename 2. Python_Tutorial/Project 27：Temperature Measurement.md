# Project 27：Temperature Measurement

1.  **Introduction**

LM35 is a commonly used and easy-to-use temperature sensor. It does not
require other hardware, only needs an analog port. The difficulty lies
in compiling the code and converting the analog values to Celsius
temperature. In this project, we use a temperature sensor and 3 LEDs to
make a temperature tester. When the temperature sensor touches objects
with different temperature, the LEDs will show different colors.

2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/74a834bb65d3f86d643648f2fa26430f.jpeg" style="width:1.97153in;height:0.78542in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png" style="width:1.66944in;height:1.28472in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/0fded1cfe95575d0fa4aa03839d8e30d.png" style="width:1.35556in;height:1.00139in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:0.99028in;height:0.52986in" /></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>LM35Temperature Sensor*1</td>
<td>USB Cable*1</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/098a2730d0b0a2a4b2079e0fc87fd38b.png" style="width:1.09792in;height:0.44097in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/afa6edd3ff90b027a6f43995a6fb15a2.png" style="width:0.28333in;height:1.20972in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/0c1b0f91b4e56bcbc235d06b48809ac9.png" style="width:0.27986in;height:1.22222in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/6c688493b558ed5f3e90e7dab38cbd93.png" style="width:0.26736in;height:1.16389in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/2f77153d70a7cea1d49a75550e38eacf.png" style="width:1.31042in;height:1.11806in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/e65c16153d0ca27891c8c08092d96d5a.png" style="width:0.47292in;height:1.15833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/e9a8d050105397bb183512fb4ffdd2f6.png" style="width:0.8375in;height:0.83194in" /></td>
</tr>
<tr class="even">
<td>220Ω Resistor*3</td>
<td>Red LED*1</td>
<td>Yellow LED*1</td>
<td>Green LED*1</td>
<td>F-F Dupont Wires</td>
<td>Breadboard*1</td>
<td>Jumper Wires</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**

![](/media/0fded1cfe95575d0fa4aa03839d8e30d.png)

**Working principle of LM35 temperature sensor:** LM35 is a widely used
temperature sensor with many different package types. At room
temperature, it can achieve the accuracy of 1/4°C without additional
calibration processing. LM35 temperature sensor can produce different
voltage by different temperature. When the temperature is 0 ℃, it
outputs 0V. If increasing 1 ℃, the output voltage will increase 10mv.
The output temperature is 0℃ to 100℃, the conversion formula is as
follows.

![](/media/0dfa07fa69f2a98658a3822c2da93bf7.jpeg)

4.  **Read the Temperature Value**

We first use a simple code to read the value of the temperature sensor,
print it in the serial monitor. The wiring diagram is shown below.

![](/media/952016b1b69fcad9f4eea889de63106a.png)

![](/media/2c05b1929588977832c955526f519e89.png)

LM35 output is given to analog pin GP26 of theRaspberry Pi Pico. This
analog voltage is converted to its digital form and processed to get the
temperature reading.

The code used in this project is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects\\Project 27：Temperature
Measurement. You can move the code to anywhere, for example, we can save
the code in the Disk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project
27：Temperature Measurement”. And double left-click
the“Project\_27.1\_Read\_LM35\_Temperature\_Value.py”.

![](/media/e2cf3b46ed80db641574699f08923ee8.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import ADC, Pin</p>
<p>import time</p>
<p># Initialize the Sound sensor to pin 26 (ADC function)</p>
<p># Select ADC input 0 (GPIO26)</p>
<p>sensor_temp = ADC(26)</p>
<p>conversion_factor = 3.3 / (65535)</p>
<p>while True:</p>
<p>reading = sensor_temp.read_u16() * conversion_factor</p>
<p>temperature = reading * 102.4</p>
<p>print(temperature)</p>
<p>time.sleep(1)</p></td>
</tr>
</tbody>
</table>

6.  **Text Result**
    
    Ensure that the Raspberry Pi Pico is connected to the
    computer，click“Stop/Restart backend”.

![](/media/03e9ea412789d6560b11e25e2fbe48dc.png)

Click “Run current script”, the code starts executing, we will see that
The "Shell" window of Thonny IDE will print the temperature values read
by the LM35 temperature sensor. Hold the LM35 element by hand, the
temperature value read by the LM35 temperature sensor will change.
Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](/media/de9286949268fb2f1202ba91ff143b13.png)

![](/media/9c2c52dbee8a37315075178f167ba342.png)

5.  **Circuit Diagram and Wiring Diagram**

Now we use a LM35 temperature sensor and three LED lights to do a
temperature test. When the LM35 temperature sensor senses different
temperatures, different LED lights will light up. Follow the diagram
below for wiring.

![](/media/65b5f44e3a73ff102a40f6c90bdf6d4c.png)

![](/media/fa3eddc7bda77c7c8420d0f3a0b0d2eb.png)

6.  **Text Code**

The code used in this project is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects\\Project 27：Temperature
Measurement. You can move the code to anywhere, for example, we can save
the code in theDisk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project
27：Temperature Measurement”. And double left-click
the“Project\_27.2\_Temperature\_Measurement.py”.

Note: The temperature threshold in the code can be reset itself as
required.  

![](/media/0496bf3b0c767e809c6ecd8b7bdc9ba3.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import ADC, Pin</p>
<p>import time</p>
<p># Initialize the Sound sensor to pin 26 (ADC function)</p>
<p># Select ADC input 0 (GPIO26)</p>
<p>sensor_temp = ADC(26)</p>
<p>conversion_factor = 3.3 / (65535)</p>
<p># create red led object from Pin 19, Set Pin 19 to output</p>
<p>led_red = machine.Pin(19, machine.Pin.OUT)</p>
<p># create yellow led object from Pin 21, Set Pin 21 to output</p>
<p>led_yellow = machine.Pin(21, machine.Pin.OUT)</p>
<p># create green led object from Pin 22, Set Pin 22 to output</p>
<p>led_green = machine.Pin(22, machine.Pin.OUT)</p>
<p>while True:</p>
<p>reading = sensor_temp.read_u16() * conversion_factor</p>
<p>temperature = reading * 102.4</p>
<p>print(temperature)</p>
<p>time.sleep(1)</p>
<p>if temperature &lt;28:</p>
<p>led_red.value(1) # Set red led turn on</p>
<p>led_yellow.value(0) # Set yellow led turn off</p>
<p>led_green.value(0) # Set green led turn off</p>
<p>elif temperature &gt;28 and temperature &lt;31:</p>
<p>led_red.value(0) # Set red led turn off</p>
<p>led_yellow.value(1) # Set yellow led turn on</p>
<p>led_green.value(0) # Set green led turn off</p>
<p>else:</p>
<p>led_red.value(0) # Set red led turn off</p>
<p>led_yellow.value(0) # Set yellow led turn off</p>
<p>led_green.value(1) # Set green led turn on</p></td>
</tr>
</tbody>
</table>

7.  **Text Result**
    
    Ensure that the Raspberry Pi Pico is connected to the
    computer，click“Stop/Restart backend”.

![](/media/25cd2e58ae326217ffbe622a282b0b8b.png)

Click “Run current script”, the code starts executing, we will see that
the "Shell" window of Thonny IDE will print the temperature values read
by the LM35 temperature sensor. When the LM35 temperature sensor senses
different temperatures, different LEDS will light up. Press“Ctrl+C”or
click“Stop/Restart backend”to exit the program.

![](/media/bbe1ee004d2a3daeb041da650c1768f6.png)
