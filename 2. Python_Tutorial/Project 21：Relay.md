# Project 21：Relay

1.  **Introduction**
    
    In daily life, we generally use AC to drive electrical equipment,
    and sometimes we use switches to control electrical appliances. If
    the switch is directly connected to the AC circuit, once electricity
    leakage occurs, people are in danger. From a safety point of view,
    we specially designed this relay module with NO (normally open) and
    NC (normally closed) terminals. In this lesson we will learn a
    special and easy-to-use switch, which is the relay module.

2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><p><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/5207588df3059cf385957664d41e9ac6.jpeg" style="width:1.41806in;height:0.56458in" /></p></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/bc08dc3772fc1fef6fa1e07bd81f6680.png" style="width:1.66806in;height:1.28403in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/1ea87894c6aa8d475203e447ad5e930a.png" style="width:1.27083in;height:0.68056in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/1fbdfe0569327d9a42600a54336bf7b5.png" style="width:1.38819in;height:1.15833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:1.11528in;height:0.59722in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Relay Module*1</td>
<td>M-F Dupont Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**
    
    **Relay:** It is an "automatic switch" that uses a small current to
    control the operation of a large current.
    
    Input voltage：3.3V-5V
    
    Rated load：5A 250VAC (NO/NC) 5A 24VDC (NO/NC)
    
    The rated load means that devices with dc voltage of 24V or AC
    voltage of 250V can be controlled using 3.3V-5V microcontrollers.  
    
    **Schematic diagram of the Relay:**

![](/media/be1c90d2b52fc2489590e3f702a087bf.emf)

4.  **Wiring Diagram**

# ![](/media/bfe4e5e68d12e715c50f8aa5797a689c.png)

![](/media/0e76ea13b2034301be2ecdfde7f21f1e.png)

5.  **Test Code**

The code used in this project is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects\\Project 21：Relay. You can move the
code to anywhere, for example, we can save the code in the Disk(D), the
route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project
21：Relay”. And double left-click the“Project\_21\_Relay.py”.

![](/media/6b610e7e5081befcea5305663f426d38.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin</p>
<p>import time</p>
<p># create relay from Pin 16, Set Pin 16 to output</p>
<p>relay = Pin(16, Pin.OUT)</p>
<p># The relay is opened, COM and NO are connected on the relay, and COM and NC are disconnected.</p>
<p>def relay_on():</p>
<p>relay(1)</p>
<p># The relay is closed, the COM and NO on the relay are disconnected, and the COM and NC are connected.</p>
<p>def relay_off():</p>
<p>relay(0)</p>
<p># Loop, the relay is on for one second and off for one second</p>
<p>while True:</p>
<p>relay_on()</p>
<p>time.sleep(1)</p>
<p>relay_off()</p>
<p>time.sleep(1)</p></td>
</tr>
</tbody>
</table>

6.  **Test Result**
    
    Ensure that the Raspberry Pi Pico is connected to the
    computer，click“![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](/media/e9e38c240d8278f282fd2912cc73d331.png)

Click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts
executing, we will see that the relay will cycle on and off, on for 1
second, off for 1 second.  At the same time, you can hear the sound of
the relay on and off, and you can also see the change of the indicator
light on the relay. Press“Ctrl+C”or
click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to exit the program.

![](/media/be6f35e062c5656930fffa6dce839777.png)
