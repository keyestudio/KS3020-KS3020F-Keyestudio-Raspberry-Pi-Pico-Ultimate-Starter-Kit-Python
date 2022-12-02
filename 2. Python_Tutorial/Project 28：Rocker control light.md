# Project 28：Rocker control light

1.  **Introduction**

The joystick module is a component with two analog inputs and one
digital input. It is widely used in game operation, robot control, drone
control and other fields.

In this project, we will use a Raspberry Pi Pico and a joystick module
to control RGB. You can have a deeper understanding of the principle and
operation of the joystick module in practice.

2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/b18fe281156b29c44796f72222718d58.jpeg" style="width:2.37431in;height:0.94514in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png" style="width:1.67014in;height:1.28472in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/d087b123748cbfb8ed9f517150db71c5.png" style="width:1.71042in;height:0.95139in" /></td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td><blockquote>
<p>Raspberry Pi Pico Expansion Board*1</p>
</blockquote></td>
<td>Joystick Module*1</td>
<td></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/af749ecbde89c728a8c63e6527781cac.png" style="width:0.16806in;height:0.93194in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/098a2730d0b0a2a4b2079e0fc87fd38b.png" style="width:1.22639in;height:0.49236in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/c801a7baee258ff7f5f28ac6e9a7097b.png" style="width:0.92778in;height:0.89167in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.275in;height:0.68264in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/f1aed48e2c02214415853ad2358f3744.png" style="width:1.21875in;height:1.02986in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/e65c16153d0ca27891c8c08092d96d5a.png" style="width:0.47292in;height:1.15833in" /></td>
</tr>
<tr class="even">
<td>RGB LED*1</td>
<td>220ΩResistor*3</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
<td>M-F Dupont Wires</td>
<td>Breadboard*1</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**

![](/media/d087b123748cbfb8ed9f517150db71c5.png)

**Joystick module**: It mainly uses PS2 joystick components. In fact,
the joystick module has 3 signal terminal pins, which simulate a
three-dimensional space. The pins of the joystick module are GND, VCC,
and signal terminals (B, X, Y). The signal terminals X and Y simulate
the X-axis and Y-axis of the space. When controlling, the X and Y signal
terminals of the module are connected to the analog port of the
microcontroller. The signal terminal B simulates the Z axis of the
space, it is generally connected to the digital port and used as a
button.

VCC is connected to the microcontroller power output VCC (3.3V or 5V),
GND is connected to the microcontroller GND, the voltage in the original
state is about 1.65V or 2.5V. In the X-axis direction, when moving in
the direction of the arrow, the voltage value increases, and the maximum
voltage can be reached. Moving in the opposite direction of the arrow,
the voltage value gradually decreases to the minimum voltage. In the
Y-axis direction, the voltage value decreases gradually as it moves in
the direction of the arrow on the module, decreasing to the minimum
voltage. As the arrow is moved in the opposite direction, the voltage
value increases and can reach the maximum voltage. In the Z-axis
direction, the signal terminal B is connected to the digital port and
outputs 0 in the original state and outputs 1 when pressed. In this way,
we can read the two analog values and the high and low level conditions
of the digital port to determine the operating status of the joystick on
the module.

**Features:**

Input Voltage：DC 3.3V \~ 5V

Output Signal：X/Y dual axis analog value +Z axis digital signal

[Range](javascript:;) [of](javascript:;) [Application](javascript:;)：Suitable
for control point coordinate movement in plane as well as control of two
degrees of freedom steering gear, etc.  

[product](javascript:;) [feature](javascript:;)s：Exquisite appearance,
joystick feel superior, simple operation, sensitive response, long
service life.  

4.  **Read the Value**

We have to use analog Raspberry Pi Pico pin IO to read the data from X
or Y pins, and use digital IO port to read the values of the button.
Please follow the wiring diagram below for wiring.

![](/media/36004a41553a2f413ba05775e9b696eb.png)

![](/media/b843cdff62b3ccf3f3f028a834b468aa.png)

The code used in this project is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects\\Project 28：Rocker control light.
You can move the code to anywhere, for example, we can save the code in
the Disk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project
28：Rocker control light”. And double left-click
the“Project\_28.1\_Read\_Rocker\_Value.py”.

![](/media/6b333ee03c3f9fb71860c83c1bcae81b.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin, ADC</p>
<p>import time</p>
<p># Initialize the joystick module (ADC function)</p>
<p>rocker_x = ADC(27)</p>
<p>rocker_y = ADC(26)</p>
<p>button = Pin(28, Pin.IN, Pin.PULL_UP)</p>
<p># Read the value of the X axis and return [0, 1023]</p>
<p>def read_x():</p>
<p>value = int(rocker_x.read_u16() * 1024 / 65536)</p>
<p>return value</p>
<p># Read the value of Y axis and return [0, 1023]</p>
<p>def read_y():</p>
<p>value = int(rocker_y.read_u16() * 1024 / 65536)</p>
<p>return value</p>
<p># Read the state of the button, press to return to True, release to return to False</p>
<p>def btn_state():</p>
<p>press = False</p>
<p>if button.value() == 0:</p>
<p>press = True</p>
<p>return press</p>
<p># Print the current value of the X axis,Y axis,Z axis cyclically.</p>
<p>while True:</p>
<p>value_x = read_x()</p>
<p>value_y = read_y()</p>
<p>state = btn_state()</p>
<p>print("x:%d, y:%d, press:%s" % (value_x, value_y, state))</p>
<p>time.sleep(0.1)</p></td>
</tr>
</tbody>
</table>

Ensure that the Raspberry Pi Pico is connected to the
computer，click“Stop/Restart backend”.

![](/media/3981469747a51ddd09a4c177e9b56adf.png)

Click “Run current script”, the code starts executing, we will see that
the "Shell" window of Thonny IDE will print the analog and digital
values of the current joystick. Moving the joystick or pressing it will
change the analog and digital values in "Shell". Press“Ctrl+C”or
click“Stop/Restart backend”to exit the program.

![](/media/7e4012f9f4e55f14361b0db5b443f78d.png)

![](/media/c8097bd115d4c564192c19a08df2702a.jpeg)

![](/media/20904cf7c75d3dd861da3b3575670a0e.png)

5.  **Circuit Diagram and Wiring Diagram**

We just read the value of the joystick module. Now we need to do
something with the joystick module and RGB, connecting according to the
following diagram.

![](/media/000ec2c5dae0b0d5368569abbd026f35.png)

![](/media/68601044f75ee6840f0b97cad9bea891.png)

6.  **Text Code**

The code used in this project is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects\\Project 28：Rocker control light.
You can move the code to anywhere, for example, we can save the code in
the Disk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project
28：Rocker control light”. And double left-click
the“Project\_28.2\_Rocker\_Control\_Light.py”.

![](/media/ffadbdf940cf18a81dd2c7b618dc0159.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin, PWM</p>
<p>import time</p>
<p>#Set RGB light interface and frequency</p>
<p>rgb_r = PWM(Pin(18))</p>
<p>rgb_g = PWM(Pin(17))</p>
<p>rgb_b = PWM(Pin(16))</p>
<p>rgb_b.freq(1000)</p>
<p>rgb_r.freq(1000)</p>
<p>rgb_g.freq(1000)</p>
<p>#Set rocker pin</p>
<p>rocker_y = machine.ADC(26)</p>
<p>rocker_x = machine.ADC(27)</p>
<p>y=500</p>
<p>x=500</p>
<p>while True:</p>
<p>y = rocker_y.read_u16()#Get Y value of rocker</p>
<p>x = rocker_x.read_u16()#Get X value of rocker</p>
<p>if x &lt; 6400: #left</p>
<p> rgb_b.duty_u16(0)</p>
<p>rgb_r.duty_u16(65535)</p>
<p>rgb_g.duty_u16(0)</p>
<p>elif x &gt; 38400: #right</p>
<p>rgb_b.duty_u16(0)</p>
<p>rgb_r.duty_u16(0)</p>
<p>rgb_g.duty_u16(65535)</p>
<p>elif y &lt; 6400: #down</p>
<p>rgb_b.duty_u16(65535)</p>
<p>rgb_r.duty_u16(0)</p>
<p>rgb_g.duty_u16(0)</p>
<p>elif y &gt; 38400: #up</p>
<p>rgb_b.duty_u16(65535)</p>
<p>rgb_r.duty_u16(65535)</p>
<p>rgb_g.duty_u16(65535)</p>
<p>time.sleep(0.01)</p></td>
</tr>
</tbody>
</table>

7.  **Test Result**
    
    Ensure that the Raspberry Pi Pico is connected to the
    computer，click“Stop/Restart backend”.

![](/media/79afea801b881d4c848bb295da1ee833.png)

Click“Run current script”, the code starts executing, we will see that①

If the joystick is moved to the far left in the X direction, the RGB
light turns red. ② If the joystick is moved to the far right in the X
direction, the RGB light turns green. ③If the joystick is moved to the
top in the Y direction, the RGB light turns white. ④If the joystick is
moved to the bottom in the Y direction, the RGB light turns blue.
Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](/media/e93935d3790240b04176f479f1981313.png)

![](/media/9c2d0d8777200827b16c49b752d45c4c.jpeg)
