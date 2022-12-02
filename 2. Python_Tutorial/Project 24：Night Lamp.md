# Project 24：Night Lamp

1.  **Introduction**

Sensors or components are ubiquitous in our daily life. For example,
some public street lights turn on automatically at night and turn off
automatically during the day. Why? In fact, this make use of a
photosensitive element that senses the intensity of external ambient
light. When the outdoor brightness decreases at night, the street lights
will automatically turn on. In the daytime, the street lights will
automatically turn off. The principle of this is very simple. In this
lesson we will use Raspberry Pi Pico to control LEDs to implement the
function of this street light.

2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><p><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/f70a6a892505b1816d151452b9b995a7.jpeg" style="width:1.55417in;height:0.61875in" /></p></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png" style="width:1.66944in;height:1.28472in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/9e553e75b6f976f33438171eb2f2e775.png" style="width:0.19097in;height:1.26597in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/ef77f5a64c382157fc2dea21ec373fef.png" style="width:0.29514in;height:1.25903in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/b395b1cd2678f87b3a34dec15659efbc.png" style="width:0.22431in;height:1.00556in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Photoresistor*1</td>
<td>Red LED*1</td>
<td>10KΩResistor*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.59028in;height:1.44583in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/845d05a6108b1662b828610ba9dcb788.png" style="width:0.25833in;height:1.13681in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/e9a8d050105397bb183512fb4ffdd2f6.png" style="width:0.77222in;height:0.77986in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:0.99028in;height:0.52986in" /></td>
<td></td>
</tr>
<tr class="even">
<td>Breadboard*1</td>
<td>220ΩResistor*1</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
<td></td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**

![](/media/9e553e75b6f976f33438171eb2f2e775.png)

It is a photosensitive resistor, its principle is that the photoresistor
surface receives brightness (light) to reduce the resistance. The
resistance value will change with the detected intensity of the ambient
light . With this property, we can use photoresistors to detect light
intensity.  Photoresistors and other electronic symbols are as follows:
 

![](/media/7d575da675a2f6cb511d28b801e2abaa.png)

The following circuit is used to detect changes in resistance values of
photoresistors:

![](/media/5a7f7e641eb78007760a94151c1d80a5.png)

In the circuit above, when the resistance of the photoresistor changes
due to the change of light intensity, the voltage between the
photoresistor and resistance R2 will also change.  Thus, the intensity
of light can be obtained by measuring this voltage.

4.  **Read the Analog Value**

We first use a simple code to read the value of the photoresistor, print
it in the serial monitor. For wiring, please refer to the following
wiring diagram.

![](/media/e3fde13b200927346e04b032373ce638.png)

![](/media/b97ff27ae10e3499c36312c8ee4881f8.png)

The code used in this project is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects\\Project 24：Night Lamp. You can
move the code to anywhere, for example, we can save the code in the
Disk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project
24：Night Lamp”. And double left-click
the“Project\_24.1\_Read\_Photosensitive\_Analog\_Value.py”.

![](/media/bbda9735710eb80196f54a5096f16799.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import ADC, Pin</p>
<p>import time</p>
<p># Initialize the photoresistance to pin 26 (ADC function)</p>
<p>adc = ADC(26)</p>
<p># Read the current analog value of the photoresistance and return [0, 1023]</p>
<p>def get_value():</p>
<p>return int(adc.read_u16() * 1024 / 65536)</p>
<p># Print the current value of the photoresistance cyclically, value=[0, 1023]</p>
<p>while True:</p>
<p>value = get_value()</p>
<p>print(value)</p>
<p>time.sleep(0.1)</p></td>
</tr>
</tbody>
</table>

Ensure that the Raspberry Pi Pico is connected to the
computer，click“Stop/Restart backend”.

![](/media/8a0c37dff4793d4132a9c88e932f499b.png)

Click “Run current script”, the code starts executing, we will see that
the "Shell" window of Thonny IDE will print the analog value read by the
photoresistor. When the light intensity around the photoresistor is
gradually reduced, the analog value will gradually increase. On the
contrary, the analog value decreases gradually. Press“Ctrl+C”or
click“Stop/Restart backend”to exit the program.

![](/media/889383400283bc151486ce0bf5820a92.png)

![](/media/bbabb2d5c4a997c5024e6023cb272261.png)

5.  **Circuit Diagram and Wiring Diagram**

We made a little dimmer in the front, now let's make a light controlled
lamp. The principle is the same, the Raspberry Pi Pico will be used to
obtain the analog value of the sensor and then adjust the brightness of
the LED.  

![](/media/b8e8d95bdc869bf76465fa73645db831.png)

![](/media/71f2886dc6fa97d02e2ecd0d429af71b.png)

6.  **Text Code**

The code used in this project is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects\\Project 24：Night Lamp. You can
move the code to anywhere, for example, we can save the code in
theDisk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project
24：Night Lamp”. And double left-click
the“Project\_24.2\_Night\_Lamp.py”.

![](/media/c08014a9603cbf3b2411440b5e7d761e.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin, ADC, PWM</p>
<p>import time</p>
<p>adc = ADC(26) # Initialize the potentiometer to pin 26 (ADC function)</p>
<p>pwm = PWM(Pin(16)) # Initialize the led's PWM to pin 16</p>
<p>pwm.freq(10000) # Define the PWM frequency as 1000</p>
<p>try:</p>
<p>while True:</p>
<p>adcValue = adc.read_u16() # read the ADC value of photoresistance</p>
<p>pwm.duty_u16(adcValue) # map ADC value to the duty cycle of PWM to control led brightness</p>
<p>time.sleep(0.1) # delay</p>
<p>except:</p>
<p>pwm.deinit()</p></td>
</tr>
</tbody>
</table>

7.  **Text Result**
    
    Ensure that the Raspberry Pi Pico is connected to the
    computer，click“Stop/Restart backend”.

![](/media/dcf4815ce265653df6759637b24087c0.png)

Click “Run current script”, the code starts executing, we will see that
when the intensity of light around the photoresistor is reduced, the LED
will be bright, on the contraty, the LED will be dim. Press“Ctrl+C”or
click“Stop/Restart backend”to exit the program.

![](/media/03dd68eab6f2579e15852f13c10ddc98.png)
