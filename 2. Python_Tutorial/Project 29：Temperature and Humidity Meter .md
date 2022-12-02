# Project 29：Temperature and Humidity Meter 

1.  **Introduction**

In winter, the humidity in the air is very low, that is, the air is very
dry. Coupled with the cold, the human skin is prone to crack from
excessive dryness. Therefore, you need to use a humidifier to increase
the humidity of the air at home. But how do you know that the air is too
dry? Then you need equipment to detect air humidity. In this lesson, we
will learn how to use the temperature and humidity sensor. We use the
sensor to create a thermohygrometer and also combined with an
LCD\_128X32\_DOT to display the temperature and humidity values.

2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/b1265f71184b5d144248ea3e847a18c9.jpeg" style="width:2.16597in;height:0.8625in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/34bafe8113e2db36c8f0c8492b835474.png" style="width:1.27292in;height:0.96111in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/9232141f8a3166a8a6cdd43b78edd4e3.png" style="width:1.29722in;height:0.625in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Temperature and Humidity Sensor*1</td>
<td>LCD 128X32 DOT*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/f1aed48e2c02214415853ad2358f3744.png" style="width:0.97569in;height:0.82431in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/f1aed48e2c02214415853ad2358f3744.png" style="width:0.97569in;height:0.82431in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.275in;height:0.68264in" /></td>
</tr>
<tr class="even">
<td>20CM M-F Dupont Wires</td>
<td>10CM M-F Dupont Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**

![](/media/34bafe8113e2db36c8f0c8492b835474.png)

**Temperature and Humidity Sensor:** It is a temperature and humidity
composite sensor with calibrated digital signal output. Its accuracy
humidity is ±5%RH, temperature is ±2℃. Range humidity is 20 to 90%RH,
and temperature is 0 to 50℃. The temperature and humidity sensor applies
dedicated digital module acquisition technology and temperature and
humidity sensing technology to ensure extremely high reliability and
excellent long-term stability of the product. The temperature and
humidity sensor includes a resistive-type humidity measurement and an
NTC temperature measurement component, which is very suitable for
temperature and humidity measurement applications where accuracy and
real-time performance are not required.

The operating voltage is in the range of 3.3V to 5.5V.

XHT11 has three pins, which are VCC, GND, and S. S is the pin for data
output, using serial communication.

**Single bus format definition:**

<table>
<tbody>
<tr class="odd">
<td><strong>Description</strong></td>
<td><strong>Definition</strong></td>
</tr>
<tr class="even">
<td>Start signal</td>
<td>Microprocessor pulls data bus (SDA) down at least 18ms for a period of time(Maximum is 30ms), notifying the sensor to prepare data.</td>
</tr>
<tr class="odd">
<td>Response signal</td>
<td>The sensor pulls the data bus (SDA) low for 83µs, and then pulls up for 87µs to respond to the host's start signal.</td>
</tr>
<tr class="even">
<td>Humidity</td>
<td>The high humidity is an integer part of the humidity data, and the low humidity is a fractional part of the humidity data.</td>
</tr>
<tr class="odd">
<td>Temperature</td>
<td>The high temperature is the integer part of the temperature data, the low temperature is the fractional part of the temperature data. And the low temperature Bit8 is 1, indicating a negative temperature, otherwise, it is a positive temperature.</td>
</tr>
<tr class="even">
<td>Parity bit</td>
<td>Parity bit=Humidity high bit+ Humidity low bit+temperature high bit+temperature low bit</td>
</tr>
</tbody>
</table>

**Data sequence diagram:**

When MCU sends a start signal, XHT11 changes from the
low-power-consumption mode to the high-speed mode, waiting for MCU
completing the start signal. Once it is completed, XHT11 sends a
response signal of 40-bit data and triggers a signal acquisition. The
signal is sent as shown in the figure.

![](/media/933ac5e5a5e921d4b16c7c48091ba75a.png)

Combined with the code, you can understand better.

The XHT11 temperature and humidity sensor can easily add temperature and
humidity data to your DIY electronic projects. It is perfect for remote
weather stations, home environmental control systems, and farm or garden
monitoring systems.

**Specification:**

Working voltage: +5V

Temperature range: 0°C to 50°C, error of ± 2°C

Humidity range: 20% to 90% RH,± 5% RH error

Digital interface

**Schematic diagram:**

![](/media/53fa034cbbcec22579b2bdf8252c90cd.emf)

4.  **Read the Value**

![](/media/c3b585b4747d3ba04be7af544bbbe27c.png)

![](/media/751a9a67b2657cac8dfaddf451e7b74a.png)

The code used in this project is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects\\Project 29：Temperature Humidity
Meter. You can move the code to anywhere, for example, we can save the
code in the Disk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project
29：Temperature Humidity Meter”. Select“dht11.py”， right-click and
select“Upload to /”，waiting for the “dht11.py”to be uploaded to the
Raspberry Pi Pico. And double left-click
the“Project\_29.1\_Detect\_Temperature\_Humidity.py”.

![](/media/4e72290107f42992138c883132081bac.png)

![](/media/109a99a8546fa851f4c62be307ec49df.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin</p>
<p>import time</p>
<p>import dht11</p>
<p>temperature = 0</p>
<p>humidity = 0</p>
<p>#Initialize temperature and humidity pins and library</p>
<p>dht = dht11.DHT11(22)</p>
<p>time.sleep(0.5)</p>
<p>while True:</p>
<p>if dht.measure() == 0:</p>
<p>print("DHT11 data error!")</p>
<p>break</p>
<p>time.sleep(1)</p>
<p>temperature = dht.temperature()</p>
<p>humidity = dht.humidity()</p>
<p>print("temperature: %dC humidity: %d"%(temperature, humidity) + "%")</p></td>
</tr>
</tbody>
</table>

Ensure that the Raspberry Pi Pico is connected to the
computer，click“Stop/Restart backend”.

![](/media/8e5cd9d0e407b4e254e8f098e73f0350.png)

Click “Run current script”, the code starts executing, we will see that
the "Shell" window of Thonny IDE will print the temperature and humidity
data in the current surroundings, as shown in the following figure.
Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](/media/1a81b6a62a73b13dcebd29e9f7ac4356.png)

![](/media/af350892cefaa74dae1740153a0c1626.png)

5.  **Circuit Diagram and Wiring Diagram**

Now we start printing the value of the XHT11 temperature and humidity
sensor with LCD screen. We will see the corresponding values on the LCD
screen. Let's get started with this project. Please follow the wiring
diagram below.

Note: LCD\_128X32\_DOT must be connected with 10CM M-F Dupont wires, the
LCD\_128X32\_DOT will display normally;  Otherwise, using a 20CM M-F
Dupont wire may cause the LCD\_128X32\_DOT display abnormally.  

![](/media/d78889590f1945eec0125ee7dc250d73.png)

![](/media/78cb8eb87aa36af901a7a839fbf7eb10.png)

6.  **Text Code**

The code used in this project is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects\\Project 29：Temperature Humidity
Meter. You can move the code to anywhere, for example, we can save the
code in the Disk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project
29：Temperature Humidity Meter”. Select“dht11.py”,“lcd128\_32.py”and
“lcd128\_32\_fonts.py”，right-click and select“Upload to /”，waiting for
the“dht11.py”，“lcd128\_32.py”and“lcd128\_32\_fonts.py”to be uploaded to
the Raspberry Pi Pico. And double left-click
the“Project\_29.2\_Temperature\_Humidity\_Meter.py”.

![](/media/4e72290107f42992138c883132081bac.png)

![](/media/1b547dfc772378fe450c185a3f72059c.png)

![](/media/a40e1d929304074a1c63354338ab82e6.png)

![](/media/340ac580344b9c6a94c51ec5824340f7.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin, I2C</p>
<p>import time</p>
<p>import lcd128_32_fonts</p>
<p>from lcd128_32 import lcd128_32</p>
<p>import dht11</p>
<p>temp = 0</p>
<p>humi = 0</p>
<p>#Initialize temperature and humidity pins and library</p>
<p>dht = dht11.DHT11(22)</p>
<p>time.sleep(0.5)</p>
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
<p>if dht.measure() == 0:</p>
<p>print("DHT11 data error")</p>
<p>break</p>
<p>temp = int(dht.temperature())</p>
<p>humi = int(dht.humidity())</p>
<p>if use_i2c:</p>
<p>scan_for_devices()</p>
<p>lcd = lcd128_32(data_pin, clock_pin, bus, i2c_addr)</p>
<p>lcd.Clear()</p>
<p>lcd.Cursor(0, 0)</p>
<p>lcd.Display("temper:")</p>
<p>lcd.Cursor(0, 8)</p>
<p>lcd.Display(str(temp))</p>
<p>lcd.Cursor(0, 11)</p>
<p>lcd.Display("C")</p>
<p>lcd.Cursor(2, 0)</p>
<p>lcd.Display("Humid:")</p>
<p>lcd.Cursor(2, 7)</p>
<p>lcd.Display(str(humi))</p>
<p>lcd.Cursor(2, 10)</p>
<p>lcd.Display("%")</p>
<p>time.sleep(1)</p>
<p>except:</p>
<p>pass</p></td>
</tr>
</tbody>
</table>

7.  **Text Result**
    
    Ensure that the Raspberry Pi Pico is connected to the
    computer，click“Stop/Restart backend”.
    
    ![](/media/3b865acac86da4d0e81dae45ee9117a9.png)
    
    Click “Run current script”, the code starts executing, we will see
    that the LCD\_128X32\_DOT will display temperature and humidity in
    the current environment. Press“Ctrl+C”or click“Stop/Restart
    backend”to exit the program.

![](/media/eb2a301072b2e37a0feb30b23c0098d5.png)
