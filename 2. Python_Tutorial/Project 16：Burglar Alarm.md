# Project 16：Burglar Alarm

1.  **Introduction**

PIR motion sensor measures the thermal infrared (IR) light emitted by
moving objects. The sensor can detect the movement of people, animals,
and cars to trigger safety alarms and lighting. They are used to detect
movement and ideal for security such as burglar alarms and security
lighting systems. In this project, we will use a Raspberry Pi Pico to
control PIR motion sensor, buzzers and LEDs to simulate burglar alarms.
 

2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/b1265f71184b5d144248ea3e847a18c9.jpeg" style="width:1.75486in;height:0.69861in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png" style="width:1.67014in;height:1.28472in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/99272d75b3f952a0c2dd770e2f6f5a7c.png" style="width:1.25347in;height:0.94097in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/4b4f653a76a82a3b413855493cc58fba.png" style="width:1.0125in;height:0.86667in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/ef77f5a64c382157fc2dea21ec373fef.png" style="width:0.29514in;height:1.25903in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>PIR Motion Sensor*1</td>
<td>Active Buzzer*1</td>
<td>Red LED*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.59028in;height:1.44583in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/c80f7e0e045c10576b3120eea281502f.png" style="width:0.85486in;height:0.72917in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/845d05a6108b1662b828610ba9dcb788.png" style="width:0.25833in;height:1.13681in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/e9a8d050105397bb183512fb4ffdd2f6.png" style="width:0.77222in;height:0.77986in" /></td>
</tr>
<tr class="even">
<td>Breadboard*1</td>
<td>F-F Dupont Wires</td>
<td>220ΩResistor*1</td>
<td>USB Cable*1</td>
<td>Jumper Wires</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**

**PIR motion sensor:** The principle is that when certain crystals, such
as lithium tantalate and triglyceride sulfate, are heated, the two ends
of the crystal will generate an equal number of charges with opposite
signs. These charges can be converted into voltage output by an
amplifier. And the human body will release infrared light, although
relatively weak, but still can be detected. When the PIR motion sensor
detects the movement of a nearby person, the sensor signal terminal
outputs a high level 1. Otherwise, it outputs a low level 0. Pay special
attention that this sensor can detect people, animals and cars in
motion. People, animals and cars at rest cannot be detected. The maximum
detection distance is about 7 meters.

**Note:** Since vulnerable to radio frequency radiation and temperature
changes, the PIR motion sensor should be kept away from heat sources
like radiators, heaters and air conditioners, as well as direct
irradiation of sunlight, headlights and incandescent light.

**Features:**

Maximum input voltage: DC 3.3 \~ 5V

Maximum operating current: 50MA

Maximum power: 0.3W

Operating temperature: -20 \~ 85℃

Output high level is 3V, low level is 0V.

Delay time: about 2.3 to 3 seconds

Detection Angle: about 100 degrees

Maximum detection distance: about 7 meters

Indicator light output (when the output is high, it will light up)

Pin limiting current: 50MA

**Schematic diagram:**

![](/media/9e1ec604aa6f9d4a3c1fe41d4bccd699.png)

4.  **Circuit Diagram and Wiring Diagram**
    
    ![](/media/8af6a40d69c138216548320abc46ed35.png)
    
    ![](/media/d028bb819eed7cf3a08af69a47ecfce6.png)

**5.Text Code**

The code used in this project is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects\\Project 16：Burglar Alarm. You can
move the code to anywhere, for example, we can save the code in the
Disk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project
16：Burglar Alarm”. And double left-click
the“Project\_16\_Burglar\_Alarm.py”.

![](/media/7f73cbbb7625a6a44b48265d65a3c61d.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin</p>
<p>import time</p>
<p>sensor_pir = machine.Pin(2, machine.Pin.IN)</p>
<p>led = machine.Pin(22, machine.Pin.OUT)</p>
<p>buzzer = machine.Pin(19, machine.Pin.OUT)</p>
<p>def pir_handler(pin):</p>
<p>print("ALARM! Motion detected!")</p>
<p>for i in range(50):</p>
<p>led.toggle()</p>
<p>buzzer.toggle()</p>
<p>time.sleep_ms(100)</p>
<p>sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)</p>
<p>while True:</p>
<p>led.toggle()</p>
<p>time.sleep(5)</p></td>
</tr>
</tbody>
</table>

6.  **Test Result**
    
    Ensure that the Raspberry Pi Pico is connected to the
    computer，click“![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](/media/e14873ab851f66c6e90699457100c992.png)

Click ![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts
executing, we will see that If the PIR motion sensor detects someone
nearby, the buzzer will give an alarm and the LEDs will flash
continuously. At the same time, the "Shell" window of the Thonny IDE
will print the string "ALARM\! Motion detected\!" Press“Ctrl+C”or
click“![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](/media/7883b057dfdf98de0af0bdc02012d93f.png)
