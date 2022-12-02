# Project 32：RFID

1.  **Introduction**
    
    Nowadays, many residential districts use this function to open the
    door by swiping the card, which is very convenient. In this lesson,
    we will learn how to use RFID(radio frequency identification)
    wireless communication technology and read and write the key chain
    card (white card) and control the steering gear rotation by
    RFID-MFRC522 module.

2.  **Components Required**

<table>
<tbody>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/8eeca2083cc744159c642a792b53eba2.jpeg" style="width:2.06806in;height:0.82361in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/bbed91c0b45fcafc7e7163bfeabf68f9.png" style="width:1.66944in;height:1.28472in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/dac05f32017287326cbdb88227a11366.png" style="width:1.63194in;height:0.80764in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/284218a1b5f1d347b1fd3c3119a34695.jpeg" style="width:0.8in;height:0.92361in" /></td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>RFID-MFRC522 Module*1</td>
<td>Key Chain*1</td>
</tr>
<tr class="odd">
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/1fbdfe0569327d9a42600a54336bf7b5.png" style="width:1.38819in;height:1.15833in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/cd0bc424e9916881a1a903793821a042.png" style="width:1.25417in;height:1.04792in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/284218a1b5f1d347b1fd3c3119a34695.jpeg" style="width:0.64792in;height:0.98681in" /></td>
<td><img src="https://raw.githubusercontent.com/keyestudio/KS3020-KS3020F-Keyestudio-Raspberry-Pi-Pico-Ultimate-Starter-Kit-Python/master/media/7dcbd02995be3c142b2f97df7f7c03ce.png" style="width:0.99028in;height:0.52986in" /></td>
</tr>
<tr class="even">
<td>F-F Dupont Wires</td>
<td>Servo*1</td>
<td>White Card*1</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.  **Component Knowledge**
    
    **RFID**：RFID (Radio Frequency Identification) is a wireless
    communication technology. A complete RFID system generally consists
    of a transponder and a reader. Usually we use tags as transponders,
    and each tag has a unique code attached to the object to identify
    the target object. The reader is a device that reads (or writes) tag
    information.
    
    Products derived from RFID technology can be divided into three
    categories: passive RFID products, active RFID products and
    semi-active RFID products. However, the passive RFID products are
    the earliest, most mature and most widely used products on the
    market, which can be seen everywhere in our daily life, such as bus
    card, meal card, bank card, hotel access card, etc., which are close
    contact identification. The main operating frequencies of the
    passive RFID products are 125KHZ(low frequency), 13.56mhz (high
    frequency), 433MHZ(UHF), and 915MHZ(UHF). The active and the
    semi-active RFID products operate at higher frequencies.
    
    The RFID module we use is a passive RFID product with a working
    frequency of 13.56MHz.  
    
    **RFID-RC522 Module：**The MFRC522 is a highly integrated
    reader/writer IC for 13.56MHz contactless communication. Its
    internal transmitter is capable of driving a read/write antenna ,
    which is designed to communicate with ISO/IEC 14443A /MIFARE cards
    and transponders without the need for additional active circuits
    . The receiving module provides an efficient implementation of
    demodulation and decoding of signals from ISO/IEC 14443 A /MIFARE
    compatible cards and transponders. The digital module manages
    complete ISO/IEC 14443A framing and error detection (parity and CRC)
    features.  
    
    The RFID module uses the MFRC522 as the control chip and adopts I2C
    (Inter-Integrated Circuit) interface.  
    
    ![](/media/5a19d0dd224c2cdc78871f11e8951045.png)
    
    Specifications:
    
    Operating voltage: DC 3.3V-5V
    
    Operating current: 13—100mA/DC 5V
    
    Idling current: 10-13mA/DC 5V
    
    Sleep current: \<80uA
    
    Peak current: \<100mA
    
    Operating frequency: 13.56MHz
    
    Maximum power: 0.5W
    
    Supported card types: mifare1 S50、mifare1 S70、mifare
    UltraLight、mifare Pro、mifare Desfire
    
    Environmental operating temperature: -20 to 80 degrees Celsius
    
    Environment storage temperature: -40 to 85 degrees Celsius
    
    Relative Humidity: 5% to 95%
    
    Data transfer rate: The maximum is 10Mbit/s.

4.  **Read the Card Number Value**
    
    We will read the UNIQUE ID number (UID) of the RFID card and
    identify its type . And display relevant information through the
    "Shell" window of Thonny IDE. The wiring diagram is as follows:
    
    ![](/media/654c447a08c85a3b54c80aea24577ad7.png)
    
    The code used in this project is saved in the file KS3020 Keyestudio
    Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows
    System\\1. Python\_Tutorial\\2. Python Projects\\Project 32：RFID.
    You can move the code to anywhere, for example, we can save the code
    in the Disk(D), the route is D:\\2. Python Projects.
    
    Open Thonny, click“This computer”→“D:”→“2. Python Projects”→“Project
    32：RFID”.
    Select“mfrc522\_config.py”“mfrc522\_i2c.py”and“soft\_iic.py”，right-click
    and select“Upload to /”,waiting for
    the“mfrc522\_config.py”“mfrc522\_i2c.py”and“soft\_iic.py”to be
    uploaded to the Raspberry Pi Pico. And double left-click
    the“Project\_32.1\_RFID\_Read\_UID.py”.

![](/media/16a289ade8d67f22ec39faef236ea8b3.png)

![](/media/3ec54155e10e80dc2a8132a3cc22cf7d.png)

![](/media/dafb6349a78a115b7f3b13d62e81f0fe.png)

![](/media/a7c2cf9283e2dd36e232e5603dc82b48.png)

<table>
<tbody>
<tr class="odd">
<td><p>import machine</p>
<p>import time</p>
<p>from mfrc522_i2c import mfrc522</p>
<p>#i2c config</p>
<p>addr = 0x28</p>
<p>scl = 21</p>
<p>sda = 20</p>
<p>rc522 = mfrc522(scl, sda, addr)</p>
<p>rc522.PCD_Init()</p>
<p>rc522.ShowReaderDetails() # Show details of PCD - MFRC522 Card Reader details</p>
<p>while True:</p>
<p>if rc522.PICC_IsNewCardPresent():</p>
<p>#print("Is new card present!")</p>
<p>if rc522.PICC_ReadCardSerial() == True:</p>
<p>print("Card UID:")</p>
<p>print(rc522.uid.uidByte[0 : rc522.uid.size])</p>
<p>#time.sleep(1)</p></td>
</tr>
</tbody>
</table>

Ensure that the Raspberry Pi Pico is connected to the
computer，click“Stop/Restart backend”.

![](/media/1f6a9dec0c6e1ca3e8955e2b719ed377.png)

Click “Run current script”, the code starts executing, we will see that

place the door card and key chain close to the module sensor area
respectively, the "Shell" window of Thonny IDE will display the card
number and key chain value respectively, as shown below. Press“Ctrl+C”or
click“Stop/Restart backend”to exit the program.

![](/media/f756e0c4dc6360842d7c97d7fdd80a70.png)

![](/media/091b3f4fdd9b823b64487aec5d5834f8.png)

Note: the door card value and key chain value may be different for
different RRFID -RC522 door cards and key chains.  

5.  **Circuit Diagram and Wiring diagram of RFID-RC522 Controlling
    Steering gear Rotation**
    
    Now we use a RFID-RC522 module, door card/key chain and servo to
    simulate an intelligent access control system. When the door card is
    close to the RFID-RC522 module induction area, the servo rotates.
    Wiring according to the figure below:

![](/media/671a93cf112889c8c5245ac6ebeb2c4d.png)

6.  **Test Code**

The code used in this project is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2.
Python\_Tutorial\\Window System\\2. Projects\\Project 32：RFID. You can
move the code to anywhere, for example, we can save the code in the
Disk(D), the route is D:\\2. Python Projects.

Open Thonny, click“This computer”→“D:”→“2. Python Projects”→“Project
32：RFID”.
Select“mfrc522\_config.py”“mfrc522\_i2c.py”and“soft\_iic.py”，right-click
and select“Upload to /”,waiting for
the“mfrc522\_config.py”“mfrc522\_i2c.py”and“soft\_iic.py”to be
uploaded to the Raspberry Pi Pico. And double left-click
the“Project\_32.2\_RFID\_Control\_Servo.py”.

![](/media/16a289ade8d67f22ec39faef236ea8b3.png)

![](/media/3ec54155e10e80dc2a8132a3cc22cf7d.png)

![](/media/dafb6349a78a115b7f3b13d62e81f0fe.png)

![](/media/e8c3b1f0e1f2d3c168eaed26ee239e95.png)

<table>
<tbody>
<tr class="odd">
<td><p>from machine import Pin, PWM</p>
<p>import time</p>
<p>from mfrc522_i2c import mfrc522</p>
<p>#Define GPIO2’s output frequency as 50Hz and assign them to PWM.</p>
<p>pwm = PWM(Pin(2))</p>
<p>pwm.freq(50)</p>
<p>'''</p>
<p>#Duty cycle corresponding to steering gear Angle</p>
<p>0°----2.5%----1638</p>
<p>45°----5%----3276</p>
<p>90°----7.5%----4915</p>
<p>135°----10%----6553</p>
<p>180°----12.5%----8192</p>
<p>'''</p>
<p>#steering gear Angle are fit to its duty cycle.</p>
<p>angle_0 = 1638</p>
<p>angle_45 = 3276</p>
<p>angle_90 = 4915</p>
<p>angle_135 = 6553</p>
<p>angle_180 = 8192</p>
<p>#i2c config</p>
<p>addr = 0x28</p>
<p>scl = 21</p>
<p>sda = 20</p>
<p>rc522 = mfrc522(scl, sda, addr)</p>
<p>rc522.PCD_Init()</p>
<p>rc522.ShowReaderDetails() # Show details of PCD - MFRC522 Card Reader details</p>
<p>uid1 = [147, 173, 247, 32]</p>
<p>uid2 = [57, 182, 70, 194]</p>
<p>pwm.duty_u16(angle_180)</p>
<p>time.sleep(1)</p>
<p>while True:</p>
<p>if rc522.PICC_IsNewCardPresent():</p>
<p>#print("Is new card present!")</p>
<p>if rc522.PICC_ReadCardSerial() == True:</p>
<p>print("Card UID:", end=' ')</p>
<p>print(rc522.uid.uidByte[0 : rc522.uid.size])</p>
<p>if rc522.uid.uidByte[0 : rc522.uid.size] == uid1 or rc522.uid.uidByte[0 : rc522.uid.size] == uid2:</p>
<p>pwm.duty_u16(angle_0)</p>
<p>else :</p>
<p>pwm.duty_u16(angle_180)</p>
<p>time.sleep(500)</p></td>
</tr>
</tbody>
</table>

Note: For different RFID-RC522 modules, white cards and key chains, its
RFID-RC522 modules may read different UID1 and UID2 values. You should
replace the uID1 and UID2 values of the white cards and key chains read
by your RRFID -RC522 module with the corresponding values in the program
code, otherwise, click "Run current script" to run the code may cause
your swipe cards and key chains can not control the servo.

For example, you replace the ![](/media/54b4d282380bd68468de99bbda6bd3ad.png) UID1 and UID2
values in the program code with the white card and key chain values read
by your rFID-RC522 module.

7.  **Text Result**
    
    Ensure that the Raspberry Pi Pico is connected to the
    computer，click“Stop/Restart backend”.
    
    ![](/media/52511e1772f5d695c42ddb1dd7d67eeb.png)
    
    Click “Run current script”, the code starts executing, we will see
    that when using the white card or a key card swiping, the "Shell"
    window of Thonny IDE will display the card number value
    respectively, and at the same time, the servo will rotate to the
    corresponding angle to simulate opening the door. Press“Ctrl+C”or
    click“Stop/Restart backend”to exit the program.

![](/media/77cf190202d54f9ab93e2379c8d2a29f.png)
