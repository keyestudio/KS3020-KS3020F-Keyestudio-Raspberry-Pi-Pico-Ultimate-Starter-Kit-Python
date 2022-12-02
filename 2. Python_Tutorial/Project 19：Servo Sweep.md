# Project 19：Servo Sweep

1.  **Introduction**

Servo is a kind of motor that can rotate very precisely. It has been
widely used in toy cars, RC helicopters, airplanes, robots, etc. In this
project, we will use a Raspberry Pi Pico to control the rotation of the
servo.

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
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/cd0bc424e9916881a1a903793821a042.png" style="width:1.25417in;height:1.04792in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/c801a7baee258ff7f5f28ac6e9a7097b.png" style="width:0.84722in;height:0.81389in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
</tr>
<tr class="even">
<td>Servo*1</td>
<td><p>Jumper</p>
<p>Wires</p></td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**

**Servo:**

![](/media/99830768916233a9c5900ac399006c17.png)

The servo is a kind of position servo driver, which is mainly composed
of housing, circuit board, coreless motor, gear and position detector.
The working principle is that the receiver or microcontroller sends a
signal to the servo, which has an internal reference circuit that
generates a reference signal with a period of 20ms and a width of 1.5ms,
and compares the DC bias voltage with the voltage of the potentiometer
to output voltage difference. The IC on the circuit board determines the
direction of rotation, and then drives the coreless motor to start
rotation and transmits the power to the swing arm through the reduction
gear, while the position detector sends back a signal to determine
whether it has reached the positioning. It is suitable for those control
systems that require constant change of angle and can be maintained.
When the motor rotates at a certain speed, the potentiometer is driven
by the cascade reduction gear to rotate so that the voltage difference
is 0 and the motor stops rotating. The angle range of general servo
rotation is 0 to 180 degrees.

The pulse period for controlling the servo is 20ms, the pulse width is
0.5ms to 2.5ms, and the corresponding position is -90° to +90°. The
following is an example of a 180 degree servo.

![](/media/708316fde05c62113a3024e0efb0c237.jpeg)

Servo motors have many specifications, but they all have three
connecting wires, which are brown, red, and orange (different brands may
have different colors). The brown is GND, the red is the positive power
supply, and the orange is the signal line.

![](/media/3f5bc31305e64108bed3b3619d602891.jpeg)

4.  **Wiring Diagram**
    
    When supplying the servo, please note that the power supply voltage
    should be 3.3V-5V. Make sure there are no errors when connecting the
    servo to the power supply.

 

![](/media/64a80947d0cd45b50d4bd1d125509bbe.png)

**5.Text Code**

The code used in this project is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects\\Project 19：Servo Sweep. You can
move the code to anywhere, for example, we can save the code in the
Disk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project
19：Servo Sweep”. Select“myservo.py”，right-click and select“Upload to
/”, waiting for the“myservo.py”to be uploaded to the Raspberry Pi
Pico. And double left-click the“Project\_19\_Servo\_Sweep.py”.

![](/media/31cd81f84d6666bf9806abddbe0d1632.png)

![](/media/7167ad374cdf0aa592739e0aa9f0dcec.png)

<table>
<tbody>
<tr class="odd">
<td><p>from myservo import Servo</p>
<p>import time</p>
<p>servo=Servo(16)</p>
<p>servo.ServoAngle(0)</p>
<p>time.sleep_ms(1000)</p>
<p>try:</p>
<p>while True:</p>
<p>for i in range(0, 180, 1):</p>
<p>servo.ServoAngle(i)</p>
<p>time.sleep_ms(15)</p>
<p>for i in range(180, 0, -1):</p>
<p>servo.ServoAngle(i)</p>
<p>time.sleep_ms(15)</p>
<p>except:</p>
<p>servo.deinit()</p></td>
</tr>
</tbody>
</table>

6.  **Test Result**
    
    Ensure that the Raspberry Pi Pico is connected to the
    computer，click“Stop/Restart backend”.

![](/media/e04de0afec735a4f27700be0d990121d.png)

Click “Run current script”, the code starts executing, we will see that
the servo will rotate from 0° to 180°, then reverse direction to rotate
from 180° to 0°, and repeat these actions in an infinite
loop. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](/media/33bbece8b90ae027e1a8af54fcbac01e.png)

![](/media/c5250405a4290ecb2d758ff1097310c7.png)

#
