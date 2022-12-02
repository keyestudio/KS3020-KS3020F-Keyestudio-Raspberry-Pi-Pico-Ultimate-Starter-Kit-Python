# Project 26：Sound Control Fan

1.  **Introduction**

The sound sensor has a built-in capacitive electret microphone and power
amplifier. It can be used to detect the sound intensity of the
environment. In this project, we use a Raspberry Pi Pico to control a
sound sensor and a motor module to make a voice-activated fan.

2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><p><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/8eeca2083cc744159c642a792b53eba2.jpeg" style="width:2.06806in;height:0.82361in" /></p></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png" style="width:1.66944in;height:1.28472in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/2ea1614210807e59a5bc7223a6fa960b.png" style="width:1.46944in;height:1.09722in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:0.99028in;height:0.52986in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Sound Sensor*1</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/6f668af8a0ecdffb5e0b64b21c0fd392.png" style="width:1.34167in;height:1.27708in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/2f77153d70a7cea1d49a75550e38eacf.png" style="width:1.31042in;height:1.11806in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/1fbdfe0569327d9a42600a54336bf7b5.png" style="width:1.38819in;height:1.15833in" /></td>
<td></td>
</tr>
<tr class="even">
<td>130 Motor Module*1</td>
<td>F-F Dupont Wires</td>
<td>M-F Dupont Wires</td>
<td></td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**

# ![](/media/9271d5f7a7647d7a3c959e6c7b837b5b.png)

**Sound sensor** is usually used to detect the loudness of the sound in
the surroundings. Arduino can collect its output signal through the
analog input interface. The S pin is an analog output, which is the
real-time output of the microphone voltage signal. The sensor comes with
a potentiometer so you can adjust the signal strength. It also has two
fixing holes so that the sensor can be installed on any other equipment.
You can use it to make some interactive works, such as voice-operated
switches.

4.  **Read the Analog Value of the Sound Sensor**

We first use a simple code to read the analog value of the sound sensor
and print it to the serial monitor, please refer to the following wiring
diagram for the wiring.

![](/media/7bcfe48423953695c677c0c504d8f745.png)

![](/media/547329f9d46a7267798728d385b60912.png)

The code used in this project is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects\\Project 26：Sound Control Fan. You
can move the code to anywhere, for example, we can save the code in the
Disk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project
26：Sound Control Fan”. And double left-click
the“Project\_26.1\_Read\_Sound\_Sensor\_Analog\_Value.py”.

![](/media/dcb5c22ff7ba7c8f1ca0621b6d2edd8b.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import ADC, Pin</p>
<p>import time</p>
<p># Initialize the sound sensor to pin 28 (ADC function)</p>
<p>adc = ADC(28)</p>
<p># Read the current analog value of the sound sensor and return [0, 1023]</p>
<p>def get_value():</p>
<p>return int(adc.read_u16() * 1024 / 65536)</p>
<p># Print the current value of the sound sensor cyclically, value=[0, 1023]</p>
<p>while True:</p>
<p>value = get_value()</p>
<p>print(value)</p>
<p>time.sleep(0.1)</p></td>
</tr>
</tbody>
</table>

Ensure that the Raspberry Pi Pico is connected to the
computer，click“Stop/Restart backend”.

![](/media/cbb7fb1e59c8224034609e4672482714.png)

Click “Run current script”, the code starts executing, we will see that
the "Shell" window of Thonny IDE will print the analog values read by
the sound sensor. When you clap your hands to the sensor, the analog
value of the sound sensor will change significantly. Press“Ctrl+C”or
click“Stop/Restart backend”to exit the program.

![](/media/033a647d45e8b533d703af6c57bd503a.png)

![](/media/ebe92f3cc97f7d21b92d498c9f04f625.png)

5.  **Wiring Diagram**

Next, we use a sound sensor, a 130 motor module and a fan leaf to make a
voice-activated fan. The wiring diagram is as follows.

![](/media/631b461716fe53a2c1138f561acae5f7.png)

![](/media/340c224f0f71765f71d17afc623d595d.png)

6.  **Text Code**（Note：![](/media/c20911df19d11290cf099072fe250029.png)The threshold 600 in the
    code can be reset itself as needed）

The code used in this project is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects\\Project 26：Sound Control Fan. You
can move the code to anywhere, for example, we can save the code in the
Disk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project
26：Sound Control Fan”. And double left-click
the“Project\_26.2\_Sound\_Control\_Fan.py”.

![](/media/2fd3e5837ddbbe6883f558f9f3922a49.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import ADC, Pin</p>
<p>import time</p>
<p># Onboard LED light initialization</p>
<p>led = Pin(25, Pin.OUT)</p>
<p># Initialize the Sound sensor to pin 28 (ADC function)</p>
<p>adc = ADC(28)</p>
<p># Pin initialization</p>
<p>motor1a = Pin(17, Pin.OUT)</p>
<p>motor1b = Pin(16, Pin.OUT)</p>
<p># Read the current analog value of the Sound sensor and return [0, 1023]</p>
<p>def get_value():</p>
<p>return int(adc.read_u16() * 1024 / 65536)</p>
<p># If the Sound sensor detects Sounds, the built-in LED on the Pico board will blink</p>
<p># and the motor will rotate when the analog value is greater than 600</p>
<p># Otherwise, the motor does not rotate and the LED goes off</p>
<p>while True:</p>
<p>value = get_value()</p>
<p>if value &gt;600:</p>
<p>led.value(1) # Set led turn on</p>
<p>motor1a.high() # Set motor1a high</p>
<p>motor1b.low() # Set motor1b low</p>
<p>time.sleep(5) # delay time</p>
<p>else:</p>
<p>motor1a.low() # Set motor1a low</p>
<p>motor1b.low() # Set motor1b low</p>
<p>led.value(0) # Set led turn off</p></td>
</tr>
</tbody>
</table>

7.  **Text Result**
    
    Ensure that the Raspberry Pi Pico is connected to the
    computer，click“Stop/Restart backend”.

![](/media/4ef29066484fdc0818796ad3cffcfc61.png)

Click“Run current script”, the code starts executing, we will see that
clap your hands to the sound sensor, and when the sound intensity
exceeds a threshold, the small fan spins while the Raspberry Pi Pico's
built-in LED lights up.  Instead, the small fan doesn't rotate, and the
Raspberry Pi Pico's built-in LEDS don't light up. Press“Ctrl+C”or
click“Stop/Restart backend”to exit the program.

![](/media/ab4cfcab677950942adac1410e7e7e6e.png)
