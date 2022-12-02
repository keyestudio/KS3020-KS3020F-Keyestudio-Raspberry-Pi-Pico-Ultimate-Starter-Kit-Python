# Project 13：Passive Buzzer

1.  **Introduction**

In a previous project, we have learned an active buzzer, which can only
produce one sound and may let you feel monotonous. In this project, we
will learn a passive buzzer and use the Raspberry Pi Pico to control the
passive buzzer to sound an alarm. Unlike the active buzzer, the passive
buzzer can emit sounds of different frequencies.

2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/b18fe281156b29c44796f72222718d58.jpeg" style="width:2.37431in;height:0.94514in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png" style="width:1.67014in;height:1.28472in" /></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td><blockquote>
<p>Raspberry Pi PicoExpansion Board*1</p>
</blockquote></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/d1ea1bb2b2749820cab389d5b85b838b.png" style="width:0.66181in;height:0.79444in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.69375in;height:1.70139in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/c801a7baee258ff7f5f28ac6e9a7097b.png" style="width:0.77778in;height:0.74792in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.05903in;height:0.56667in" /></td>
</tr>
<tr class="even">
<td>Passive Buzzer*1</td>
<td>Breadboard*1</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

**3. Component Knowledge**

![](/media/8d0020e53824072cbe9d4f7d2f8acb4f.png)

A passive buzzer is an integrated electronic buzzer with no internal
vibration source. It must be driven by 2K to 5K square wave, not a DC
signal. The two buzzers are very similar in appearance, but one buzzer
with a green circuit board is a passive buzzer, while the other with
black tape is an active buzzer. Passive buzzers cannot distinguish
between positive polarity while active buzzers can.

![](/media/fc42c5ed014609ff0b290ee5361bb2fd.png)

**4. Circuit Diagram and Wiring Diagram**

![](/media/e0da1ccdbff24d256db130816c55da74.png)

![](/media/e601e48f8deddb3e9e7734d0022106b3.png)

**5. Test Code**

The code used in this project is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects\\Project 13：Passive Buzzer. You can
move the code to anywhere, for example, we can save the code in the
Disk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project
13：Passive Buzzer”. And double left-click
the“Project\_13\_Passive\_Buzzer.py”.

![](/media/4e4cf166f1de082468ebf77ef6ba3d4d.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin</p>
<p>import time</p>
<p>#Initialize the passive buzzer</p>
<p>buzzer = Pin(16,Pin.OUT)</p>
<p>#Simulate two different frequencies</p>
<p>while True:</p>
<p>#Output 500HZ frequency sound</p>
<p>for i in range(80):</p>
<p>buzzer.value(1)</p>
<p>time.sleep(0.001)</p>
<p>buzzer.value(0)</p>
<p>time.sleep(0.001)</p>
<p>#Output 250HZ frequency sound</p>
<p>for i in range(100):</p>
<p>buzzer.value(1)</p>
<p>time.sleep(0.002)</p>
<p>buzzer.value(0)</p>
<p>time.sleep(0.002)</p></td>
</tr>
</tbody>
</table>

5.  **Test Result**
    
    Ensure that the Raspberry Pi Pico is connected to the
    computer，click“Stop/Restart backend”.
    
    ![](/media/699667c6aea0990e6a2fa408ef7ca3a1.png)
    
    Click“![](/media/da852227207616ccd9aff28f19e02690.png)Run current script”, the code starts
    executing, we will see that the the passive buzzer sounds the alarm.
    Press“Ctrl+C”or click“![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to
    exit the program.

![](/media/02d6cb5bd3d2cef4e669886b957544ed.png)
