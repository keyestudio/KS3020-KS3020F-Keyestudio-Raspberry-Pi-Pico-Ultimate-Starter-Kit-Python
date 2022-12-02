# Project 10：8×8 Dot-matrix Display

1.  **Introduction**

The dot-matrix display is an electronic digital display device that can
show information on machines, clocks and many other devices. In this
project, we will use the Raspberry Pi Pico to control the 8x8 LED dot
matrix to make a“❤”pattern.

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
<td><blockquote>
<p>Raspberry Pi Pico Expansion Board*1</p>
</blockquote></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/fa4eb4c55bbbb4ae7fcde8298a903b5a.png" style="width:1.90486in;height:0.94931in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/b1991d0d88442db1d6b2f4189530397b.png" style="width:1.08958in;height:0.92014in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
</tr>
<tr class="even">
<td>8*8 Dot-matrix Display *1</td>
<td>M-F Dupont Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**

**8\*8 Dot-matrix display module:**

The 8\*8 dot matrix is composed of 64 LEDs, and each LED is placed at
the intersection of a row and a column. When using a single-chip
microcomputer to drive an 8\*8 dot matrix, we need to use a total of 16
digital ports, which greatly wastes the data of the single-chip
microcomputer. For this reason, we specially designed this module, using
the HT16K33 chip to drive an 8\*8 dot matrix, and only need to use the
I2C communication port of the single-chip microcomputer to control the
dot matrix, which greatly saves the microcontroller resources.

**Specifications:**

Working voltage: DC 5V

Current: 200MA

Maximum power: 1W

**4. Schematic diagram:**

# ![](/media/b04fe5e60695365a23644395aaef5085.png)

Some modules have three DIP switches that you can flip at will. These
switches are used to set the I2C communication address. The setting
method is as follows. The module has fixed the communication address.
A0, A1 and A2 are connected to GND, and the address is 0x70.  

<table>
<tbody>
<tr class="odd">
<td>A0（1）</td>
<td>A1（2）</td>
<td>A2（3）</td>
<td>A0（1）</td>
<td>A1（2）</td>
<td>A2（3）</td>
<td>A0（1）</td>
<td>A1（2）</td>
<td>A2（3）</td>
</tr>
<tr class="even">
<td>0（OFF）</td>
<td>0（OFF）</td>
<td>0（OFF）</td>
<td>1（ON）</td>
<td>0（OFF）</td>
<td>0（OFF）</td>
<td>0（OFF）</td>
<td>1（ON）</td>
<td>0（OFF）</td>
</tr>
<tr class="odd">
<td>0X70</td>
<td>0X71</td>
<td>0X72</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>A0（1）</td>
<td>A1（2）</td>
<td>A2（3）</td>
<td>A0（1）</td>
<td>A1（2）</td>
<td>A2（3）</td>
<td>A0（1）</td>
<td>A1（2）</td>
<td>A2（3）</td>
</tr>
<tr class="odd">
<td>1（ON）</td>
<td>1（ON）</td>
<td>0（OFF）</td>
<td>0（OFF）</td>
<td>0（OFF）</td>
<td>1（ON）</td>
<td>1（ON）</td>
<td>0（OFF）</td>
<td>1（ON）</td>
</tr>
<tr class="even">
<td>0X73</td>
<td>0X74</td>
<td>0X75</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>A0（1）</td>
<td>A1（2）</td>
<td>A2（3）</td>
<td>A0（1）</td>
<td>A1（2）</td>
<td>A2（3）</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>0（OFF）</td>
<td>1（ON）</td>
<td>1（ON）</td>
<td>1（ON）</td>
<td>1（ON）</td>
<td>1（ON）</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td>0X76</td>
<td>0X77</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
</tr>
</tbody>
</table>

4.  **Circuit Diagram and Wiring Diagram**

![](/media/f4fc6111c35b571928d0f0a4a4bf45b3.png)

![](/media/ad529b82657cd9c7ddcd4b8828a0b1e8.png)

5.  **Text Code**

The code used in this project is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects\\Project 10：8×8 Dot-matrix Display.
You can move the code to anywhere, for example, we can save the code in
the Disk(D), the route is D:\\2. Python Projects.

Open“Thonny, click“This computer”→“D:”→“2. Python Projects”→“Project
10：8×8 Dot-matrix Display”.
Select“ht16k33\_matrix.py”and“matrix\_fonts.py”，right-click and
select“Upload to /”and wait
for“ht16k33\_matrix.py”and“matrix\_fonts.py”to be uploaded to
the Raspberry Pi Pico. And double left-click
the“Project\_10\_8×8\_Dot\_Matrix\_Display.py”.

![](/media/487405e5443d1dcba1706351ffea6d11.png)

![](/media/7a3a8ed25fcc739a74453588dfe3abd5.png)

![](/media/0e9ede0023678e49711608cf3845505a.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin,I2C</p>
<p>import time</p>
<p>import json</p>
<p>import matrix_fonts</p>
<p>from ht16k33_matrix import ht16k33_matrix</p>
<p>## Tool To Make Sprites https://gurgleapps.com/tools/matrix</p>
<p>#i2c config</p>
<p>clock_pin = 21</p>
<p>data_pin = 20</p>
<p>bus = 0</p>
<p>i2c_addr_left = 0x70</p>
<p>use_i2c = True</p>
<p>def scan_for_devices():</p>
<p>i2c = machine.I2C(bus,sda=machine.Pin(data_pin),scl=machine.Pin(clock_pin))</p>
<p>devices = i2c.scan()</p>
<p>if devices:</p>
<p>for d in devices:</p>
<p>print(hex(d))</p>
<p>else:</p>
<p>print('no i2c devices')</p>
<p>if use_i2c:</p>
<p>scan_for_devices()</p>
<p>left_eye = ht16k33_matrix(data_pin, clock_pin, bus, i2c_addr_left)</p>
<p>def show_char(left):</p>
<p>if use_i2c:</p>
<p>left_eye.show_char(left)</p>
<p>def scroll_message(font,message='hello',delay=0.05): #Scrolling display</p>
<p>left_message = ' ' + message</p>
<p>right_message = message + ' '</p>
<p>length=len(right_message)</p>
<p>char_range=range(length-1)</p>
<p>for char_pos in char_range:</p>
<p>right_left_char=font[right_message[char_pos]]</p>
<p>right_right_char=font[right_message[char_pos+1]]</p>
<p>left_left_char=font[left_message[char_pos]]</p>
<p>left_right_char=font[left_message[char_pos+1]]</p>
<p>for shift in range(8):</p>
<p>left_bytes=[0,0,0,0,0,0,0,0]</p>
<p>right_bytes=[0,0,0,0,0,0,0,0]</p>
<p>for col in range(8):</p>
<p>left_bytes[col]=left_bytes[col]|left_left_char[col]&lt;&lt;shift</p>
<p>left_bytes[col]=left_bytes[col]|left_right_char[col]&gt;&gt;8-shift;</p>
<p>right_bytes[col]=right_bytes[col]|right_left_char[col]&lt;&lt;shift</p>
<p>right_bytes[col]=right_bytes[col]|right_right_char[col]&gt;&gt;8-shift;</p>
<p>if use_i2c:</p>
<p>left_eye.show_char(left_bytes)</p>
<p>time.sleep(delay)</p>
<p>while True:</p>
<p>show_char(matrix_fonts.textFont1['A']) #Show the letter A</p>
<p>time.sleep(1)</p>
<p>show_char(matrix_fonts.textFont1['B'])</p>
<p>time.sleep(1)</p>
<p>show_char(matrix_fonts.textFont1['C'])</p>
<p>time.sleep(1)</p>
<p>scroll_message(matrix_fonts.textFont1, ' Hello World ')</p></td>
</tr>
</tbody>
</table>

6.  **Text Result**
    
    Ensure that the Raspberry Pi Pico is connected to the
    computer，click“Stop/Restart backend”.

![](/media/d195d37e4eb32c656c741c8c6c391572.png)

Click“Run current script”, the code starts executing, we will see that
the 8 x 8 dot matrix displays the character "A" 1S, "B" 1S, and "C" 1S.
Then scroll to display the string "Hello
World”repeatedly. Press“Ctrl+C”or click“Stop/Restart backend”to
exit the program.

![](/media/476f84b2194fc6ef6e9d2df0cbd787d4.png)
