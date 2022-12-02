# Project 09：4-Digit Digital Tube

1.  **Introduction**
    
    The 4-digit 7-segment digital tube is a very practical display
    device, and it is used for devices such as electronic clocks and
    score counters. Due to the low price and it is easy to use, more and
    more projects will use 4-digit 7-segment digital tubes. In this
    project, we will use the Raspberry Pi Pico to control a 4-bit
    7-segment digital tube to create a manual counter.

<!-- end list -->

2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/b18fe281156b29c44796f72222718d58.jpeg" style="width:2.37431in;height:0.94514in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png" style="width:1.67014in;height:1.28472in" /></td>
<td></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/f65653a12f286475b4365035aa12c7c0.png" style="width:1.45208in;height:0.74653in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/ece3c38dc9a9e6428b122481d6bb0d4d.png" style="width:0.9625in;height:0.81319in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
</tr>
<tr class="even">
<td>4-Digit Digital Tube Module*1</td>
<td>M-F Dupont Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**

**TM1650 4-digit digital tube:** It is a 12-pin 4-digit tube display
module with clock dots. The driver chip is TM1650 which only needs 2
signal lines to enable the microcontroller to control the 4-digit
8-segment digital tube. The control interface level can be 5V or 3.3V.

**Specifications of 4-bit digital tube module:**

Working voltage: DC 3.3V-5V

Maximum current: 100MA

Maximum power: 0.5W

**Schematic diagram of 4-digit digital tube module:**

![](/media/5f400887c90fc00098a3e77beca656ef.png)

4.  **Circuit Diagram and Wiring Diagram**

# ![](/media/80f5738cf821288fff6ba0aba11fc453.png)

![](/media/39b708e69b2fb10057b71fe2321584b2.png)

5.  **Test Code**

The code used in this project is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects\\Project 09：4-Digit Digital Tube.
You can move the code to anywhere, for example, we can save the code in
the Disk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project
09：4-Digit Digital Tube”. Select“TM1650.py”，right-click and
select“Upload to /”， and wait for“TM1650.py to be uploaded to the
Raspberry Pi Pico. And double left-click
the“Project\_09\_Four\_Digit\_Digital\_Tube.py”.

![](/media/b4026879bc9491754fa118c103e86c5f.png)

![](/media/0c3fcafccf88e7e48fbaf712a94b367a.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin, I2C</p>
<p>from TM1650 import TM1650</p>
<p>import time</p>
<p># Define IIC interfaces and frequencies</p>
<p>i2c=I2C(0, scl=Pin(21),sda=Pin(20), freq=100000)</p>
<p>display = TM1650(i2c)</p>
<p># Display the numbers 1111-9999 circulately</p>
<p>while True:</p>
<p>display.display(1111)</p>
<p>time.sleep(1)</p>
<p>display.display(2222)</p>
<p>time.sleep(1)</p>
<p>display.display(3333)</p>
<p>time.sleep(1)</p>
<p>display.display(4444)</p>
<p>time.sleep(1)</p>
<p>display.display(5555)</p>
<p>time.sleep(1)</p>
<p>display.display(6666)</p>
<p>time.sleep(1)</p>
<p>display.display(7777)</p>
<p>time.sleep(1)</p>
<p>display.display(8888)</p>
<p>time.sleep(1)</p>
<p>display.display(9999)</p>
<p>time.sleep(1)</p></td>
</tr>
</tbody>
</table>

6.  **Test Result**
    
    Ensure that the Raspberry Pi Pico is connected to the
    computer，click“![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](/media/682029610c29b14122b37787bbd2ae53.png)

Click“![](/media/da852227207616ccd9aff28f19e02690.png)Run current script”, the code starts
executing, we will see that the 4-digit digital tube circularly displays
numbers from 0000 to 9999. Press“Ctrl+C”or
click“![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](/media/3ef28f4dda60e7c14e1ffd8aa5d823aa.png)
