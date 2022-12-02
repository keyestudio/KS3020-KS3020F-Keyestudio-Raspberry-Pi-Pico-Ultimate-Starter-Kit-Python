# Project 34：IR Control Sound and LED

1.  **Introduction**

Infrared remote control is a low-cost, easy-to-use wireless
communication technology. IR light is very similar to visible light,
except that it has a slightly longer wavelength. This means that
infrared rays cannot be detected by the human eye, which is perfect for
wireless communication. For example, when you press a button on the TV
remote control, an infrared LED will switch on and off repeatedly at a
frequency of 38,000 times per second, sending information (such as
volume or channel control) to the infrared sensor on the TV.

We will first explain how common IR communication protocols work. Then
we will start this project with a remote control and an IR receiving
component.

2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/17098ffd05750eb6b34eb75b82fbb37a.jpeg" style="width:1.62292in;height:0.64653in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/355118d2d21e57840d34a30ec500a900.png" style="width:1.59028in;height:1.22431in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/88e6b057fb4b0c576c9b2111d15b26e5.png" style="width:1.14861in;height:0.48403in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/f1a86fc81ab4b043263ce7e01e14d470.png" style="width:0.23056in;height:1.27847in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/098a2730d0b0a2a4b2079e0fc87fd38b.png" style="width:1.22639in;height:0.49236in" /></td>
<td></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td><blockquote>
<p>Raspberry Pi Pico Expansion Board*1</p>
</blockquote></td>
<td>IR Receiver *1</td>
<td>RGB LED*1</td>
<td>220ΩResistor*3</td>
<td></td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/8a6fb37dedef748e6c2609bff5c64906.png" style="width:0.69792in;height:1.45764in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/e380dd26e4825be9a768973802a55fe6.png" style="width:0.5625in;height:1.30903in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/d1ea1bb2b2749820cab389d5b85b838b.png" style="width:0.66181in;height:0.79444in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/a22dac8c5edbe90e867cbb04769d1816.png" style="width:0.23194in;height:1.04028in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/e9a8d050105397bb183512fb4ffdd2f6.png" style="width:0.90694in;height:0.90139in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:0.99028in;height:0.52986in" /></td>
</tr>
<tr class="even">
<td>IR Remote Controller*1</td>
<td>Breadboard*1</td>
<td>Passive Buzzer*1</td>
<td>10KΩResistor*1</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**

**IR Remote Controller**: It is a device that has a certain number of
buttons. Pressing different buttons causes the infrared transmitter
tubes at the front of the remote control to send infrared signals in
different codes. Infrared remote control technology is widely used, such
as TV, air conditioner and so on. Therefore, in today's technologically
advanced society, the infrared remote control technology makes it very
convenient for us to change TV programs and adjust the temperature of
the air conditioner.  

The remote control we used is as follows:

The infrared remote controller adopts NEC code and the signal cycle is
110ms.

![](/media/3c9d76cb0d24d9861811ce2cb0bb6ae4.png)

**IR Receiver:** It is a component that can receive infrared light,
which can be used to detect the infrared signal sent by the infrared
remote control. The infrared signal received by the infrared receiver
demodulation can be converted back to binary, then the information will
be passed to a microcontroller.

**Process Diagram：**

![](/media/3da1969e509f53706643c77d0534eb73.png)

**NEC Infrared communication protocol：**

**NEC Protocol**

To my knowledge the protocol I describe here was developed by NEC (Now
Renesas). I've seen very similar protocol descriptions on the internet,
and there the protocol is called Japanese Format.

I do admit that I don't know exactly who developed it. What I do know is
that it was used in my late VCR produced by Sanyo and was marketed under
the name of Fisher. NEC manufactured the remote control IC.

This description was taken from my VCR's service manual. Those were the
days, when service manuals were filled with useful information\!

**Features**

8 bit address and 8 bit command length.

Extended mode available, doubling the address size.

Address and command are transmitted twice for reliability.

Pulse distance modulation.

Carrier frequency of 38kHz.

Bit time of 1.125ms or 2.25ms.

**Modulation**

![](/media/da33571c6f0afb94b1ec1d91caba3edb.png)

The NEC protocol uses pulse distance encoding of the bits. Each pulse is
a 560µs long 38kHz carrier burst (about 21 cycles). A logical "1" takes
2.25ms to transmit, while a logical "0" is only half of that, being
1.125ms. The recommended carrier duty-cycle is 1/4 or 1/3

**Protocol**

![](/media/f970404e7bbfb5711fea5c776f689f3a.png)

The picture above shows a typical pulse train of the NEC protocol. With
this protocol the LSB is transmitted first. In this case Address $59 and
Command $16 is transmitted. A message is started by a 9ms AGC burst,
which was used to set the gain of the earlier IR receivers. This AGC
burst is then followed by a 4.5ms space, which is then followed by the
Address and Command. Address and Command are transmitted twice. The
second time all bits are inverted and can be used for verification of
the received message. The total transmission time is constant because
every bit is repeated with its inverted length. If you're not interested
in this reliability you can ignore the inverted values, or you can
expand the Address and Command to 16 bits each\!

Keep in mind that one extra 560µs burst has to follow at the end of the
message in order to be able to determine the value of the last bit.

![](/media/63364daf21e5522c64eb8dfa82f2cef2.png)

A command is transmitted only once, even when the key on the remote
control remains pressed. Every 110ms a repeat code is transmitted for as
long as the key remains down. This repeat code is simply a 9ms AGC pulse
followed by a 2.25ms space and a 560µs burst.

![](/media/afea92a3b5cc1aa2457d2b118b157c84.png)

**Extended NEC protocol**

The NEC protocol is so widely used that soon all possible addresses were
used up. By sacrificing the address redundancy the address range was
extended from 256 possible values to approximately 65000 different
values. This way the address range was extended from 8 bits to 16 bits
without changing any other property of the protocol.

By extending the address range this way the total message time is no
longer constant. It now depends on the total number of 1's and 0's in
the message. If you want to keep the total message time constant you'll
have to make sure the number 1's in the address field is 8 (it
automatically means that the number of 0's is also 8). This will reduce
the maximum number of different addresses to just about 13000.

The command redundancy is still preserved. Therefore each address can
still handle 256 different commands.

![](/media/2f78d1ce7f001926f6b90ad966796e91.png)

Keep in mind that 256 address values of the extended protocol are
invalid because they are in fact normal NEC protocol addresses. Whenever
the low byte is the exact inverse of the high byte it is not a valid
extended address.

4.  **Decode Infrared Signal:**
    
    We connect the infrared receiving element to the Raspberry Pi Pico
    according to the wiring diagram below.  

![](/media/240a9b2efcdd0c0e7099ec5b69beaca6.png)

![](/media/a6a7f74730669dfa0272e9b5e88ac41e.png)

The code used in this project is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects\\Project 34：IR Control Sound and
LED. You can move the code to anywhere, for example, we can save the
code in the Disk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project
34：IR Control Sound and LED”. Select“irrecvdata.py”， right-click and
select“Upload to /”,waiting for the“irrecvdata.py”to be uploaded to the
Raspberry Pi Pico. And double left-click
the“Project\_34.1\_Decoded\_IR\_Signal.py”.

![](/media/0e559f2f7ce06f100f33f2aa562669b3.png)

![](/media/91b7122d9d7183692a5cd243a9f493e1.png)

<table>
<tbody>
<tr class="odd">
<td><p># Import the infrared decoder.</p>
<p>from irrecvdata import irGetCMD</p>
<p># Associate the infrared decoder with GP16.</p>
<p>recvPin = irGetCMD(16)</p>
<p>#When infrared key value is obtained, print it out in"Shell".</p>
<p>try:</p>
<p>while True:</p>
<p>irValue = recvPin.ir_read() #Call ir_read() to read the value of the pressed key and assign it to IRValue.</p>
<p>if irValue:</p>
<p>print(irValue)</p>
<p>except:</p>
<p>pass</p></td>
</tr>
</tbody>
</table>

Ensure that the Raspberry Pi Pico is connected to the
computer，click“Stop/Restart backend”.

![](/media/f74f668d149dbdab5ac8f19df19c1852.png)

Click “Run current script”, the code starts executing, we will see that
aim the infrared remote control transmitter at the infrared receiving
head, press the button on the infrared controller, and the "Shell"
window of Thonny IDE will print the current received key code values.
Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](/media/a75baa34fe256fdea2714b1b0c66cd66.png)

![](/media/623f8fa842b90a093d286954835483c6.png)

Write down the code associated with each button, because you will need
that information later.

![](/media/ebcf0cb2055f7784505f76ceeaef9f47.jpeg)

**5. Circuit Diagram and Wiring Diagram**

![](/media/6e2da9ed5d5bdc5b251348903a37e5c0.png)

![](/media/d170f9c106c16175d34f20fdaa0f8970.png)

**6. Text Code**

The code used in this project is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects\\Project 34：IR Control Sound and
LED. You can move the code to anywhere, for example, we can save the
code in the Disk(D), the route is D:\\2. Python Projects.

Open“Thonny”, click“This computer”→“D:”→“2. Python Projects”→“Project
34：IR Control Sound and LED”. Select“irrecvdata.py”，right-click and
select“Upload to /”,waiting for the“irrecvdata.py”to be uploaded to the
Raspberry Pi Pico. And double left-click
the“Project\_34.2\_IR\_Control\_Sound\_And\_LED.py”.

![](/media/0e559f2f7ce06f100f33f2aa562669b3.png)

![](/media/cdbe2c4d1e154cfa7983588113189876.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin,PWM</p>
<p>import utime</p>
<p>from irrecvdata import irGetCMD</p>
<p>#Set RGB light interface and frequency</p>
<p>rgb_r = PWM(Pin(19))</p>
<p>rgb_g = PWM(Pin(18))</p>
<p>rgb_b = PWM(Pin(17))</p>
<p>rgb_r.freq(1000)</p>
<p>rgb_g.freq(1000)</p>
<p>rgb_b.freq(1000)</p>
<p># Initialize the buzzer pin to PWM function</p>
<p>buzzer=PWM(Pin(15, Pin.OUT))</p>
<p>buzzer.freq(262)</p>
<p>buzzer.duty_u16(0)</p>
<p># Play the frequency of midrange tones 1-7</p>
<p>freq = [262, 294, 330, 350, 393, 441, 495]</p>
<p>#Configure infrared receiving pin and library</p>
<p>recvPin = irGetCMD(16)</p>
<p># Set the buzzer to emit different tones.</p>
<p># index=[0-7], where 0 is closed, and 1-7 respectively represent middle C, middle D, middle E, middle F, middle G, middle A, middle B.</p>
<p># time represents the function delay time (a positive integer), in milliseconds.</p>
<p># auto_off indicates whether the buzzer will be turned off automatically after the delay time.</p>
<p>def tone(index, time=0, auto_off=False):</p>
<p>if index == 0:</p>
<p>buzzer.duty_u16(0)</p>
<p>utime.sleep_ms(time)</p>
<p>elif index &gt;= 1 and index &lt;= 7:</p>
<p>tone_freq = freq[int(index - 1)]</p>
<p>buzzer.freq(tone_freq)</p>
<p>buzzer.duty_u16(32768)</p>
<p>utime.sleep_ms(time)</p>
<p>if auto_off == True:</p>
<p>buzzer.duty_u16(0)</p>
<p># print("----freq:", index, tone_freq)</p>
<p>else:</p>
<p>print("Tones must be 0-7")</p>
<p>delay = 0</p>
<p>tone(1, 100, True)</p>
<p>while True:</p>
<p>irValue = recvPin.ir_read() # Read remote control data</p>
<p># Determine whether there is a button that meets the needs</p>
<p>if irValue:</p>
<p>print(irValue)</p>
<p>if irValue == '0xff6897': #1</p>
<p>rgb_r.duty_u16(65535)</p>
<p>rgb_g.duty_u16(0)</p>
<p>rgb_b.duty_u16(0)</p>
<p>tone(1, delay)</p>
<p>elif irValue == '0xff9867': #2</p>
<p>rgb_r.duty_u16(0)</p>
<p>rgb_g.duty_u16(65535)</p>
<p>rgb_b.duty_u16(0)</p>
<p>tone(2, delay)</p>
<p>elif irValue == '0xffb04f': #3</p>
<p>rgb_r.duty_u16(0)</p>
<p>rgb_g.duty_u16(0)</p>
<p>rgb_b.duty_u16(65535)</p>
<p>tone(3, delay)</p>
<p>elif irValue == '0xff30cf': #4</p>
<p>rgb_r.duty_u16(65535)</p>
<p>rgb_g.duty_u16(65535)</p>
<p>rgb_b.duty_u16(0)</p>
<p>tone(4, delay)</p>
<p>elif irValue == '0xff18e7': #5</p>
<p>rgb_r.duty_u16(65535)</p>
<p>rgb_g.duty_u16(0)</p>
<p>rgb_b.duty_u16(65535)</p>
<p>tone(5, delay)</p>
<p>elif irValue == '0xff7a85': #6</p>
<p>rgb_r.duty_u16(0)</p>
<p>rgb_g.duty_u16(65535)</p>
<p>rgb_b.duty_u16(65535)</p>
<p>tone(6, delay)</p>
<p>elif irValue == '0xff10ef': #7</p>
<p>rgb_r.duty_u16(65535)</p>
<p>rgb_g.duty_u16(65535)</p>
<p>rgb_b.duty_u16(65535)</p>
<p>tone(7, delay)</p>
<p>else:</p>
<p>rgb_r.duty_u16(0)</p>
<p>rgb_g.duty_u16(0)</p>
<p>rgb_b.duty_u16(0)</p>
<p>tone(0)</p></td>
</tr>
</tbody>
</table>

7.  **Test Result**
    
    Ensure that the Raspberry Pi Pico is connected to the
    computer，click“Stop/Restart backend”.

![](/media/91f4a1a976aa6dc5e3008f1c1e6ea864.png)

Click “Run current script”, the code starts executing, we will see
that press buttons 1 to 7 on the infrared remote controller, we
can hear buzzers such as do、re、mi、fa、sol、la、si ,etc. At the same time,
the RGB will be red , green , blue , yellow , [magenta](javascript:;),
blue and green, white respectively. However, if we press other buttons
(except 1-7), the buzzer stops playing and the RGB goes off
.  Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](/media/6b00ce3539b5537d80fd0a614b70902c.png)

**Note**：When the code is running, the following prompt appears, you
just need to click![](/media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”，then
click![](/media/da852227207616ccd9aff28f19e02690.png)“Run current script”to make the code run
again.

![](/media/3f425db5cda9eb56bc1f29c27fa6696d.png)

(Note: Before use, we need to remove the plastic sheet from the bottom
of the infrared remote controller.)
