# Python_Tutorial(Raspberry-Pi)

## 1. Preparation before class for Python

Raspberry Pi is a card computer whose official system is Raspberry Pi OS, and can be installed on the Raspberry Pi, such as: ubuntu, Windows IoT. Raspberry Pi can be used as a personal server, performing camera monitoring and recognition, as well as voice interaction by connecting a camera and a voice interactive assistant. 

Also, Raspberry Pi leads out 40Pin pins that can be connected to various sensors and control LEDs, motors, etc. This can be used to make a robot with a Raspberry Pi.

### 1.1. Tools needed for the Raspberry Pi system

#### 1.1.1. Hardware Tool:

- Raspberry Pi 4B/3B/2B

- Above 16G TFT Memory Card

- Card Reader

- Computer and other parts

#### 1.1.2. Install Software Tools(Windows System):

##### (1) Putty

Download link:

[https://www.chiark.greenend.org.uk/\~sgtatham/putty/](https://www.chiark.greenend.org.uk/~sgtatham/putty/)

![](./media/c26be4cd1f5543f20f275556ce5892c0.png)

![](./media/d888918aa7bf9e5ea94597aad1ee4224.png)

1). After downloading the package file ![](./media/e597704d7033c7c3c5da06d4f561822c.png), double-click it and tap “Next”.
    
![](./media/01f1b2d98915be2be9c0c2a3d330dde2.png)
    
2). Click “Next”.
    
![](./media/bd698753a8eea7a2ff5c5e0e598cbd94.png)

3). Choose “Install PuTTY files” and click “Install”.
    
![](./media/071a0acc98bb2dc5cd45d85dec72d111.png)

4). After a few seconds, click "Finish".

![](./media/ec368c3a549c09edd70f9786456d5430.png)

##### (2) SSH Remote Login software -WinSCP

Download Link: [https://winscp.net/eng/download.php](https://winscp.net/eng/download.php)

1). After downloading the package file ![](./media/1719daa1002d7477ad4700e1df85d2df.png), click ![](./media/e09e48a32781d08aabb06156efe1de49.png).
    
![](./media/5ee80ade909fe3eb73dc9535704b4c0b.png)
    
2). Click “Accept”.

![](./media/9c652f54f6a7d53f6b2aedba40104a00.png)

3). Follow the below steps to finish the installation.

![](./media/f32891714d5966037d59d1812aa15686.png)

![](./media/57d6139ba0aac9ca996bcbe6f6fd218f.png)

![](./media/49ffed878ee84546b156af3a0bf5556e.png)

![](./media/14ffa1e11243835d30ffb933219dcef5.png)

##### (3) SD Card Formatter

Format TFT card tool, download SD Card Formatter :

[http://www.canadiancontent.net/tech/download/SD\_Card\_Formatter.html](http://www.canadiancontent.net/tech/download/SD_Card_Formatter.html)

![](./media/fa229f4e063572ce1c59574c308bf452.png)

![](./media/ac5d5eb9463805484b9239b99faf04eb.png)

1). Unzip the SDCardFormatterv5\_WinEN package, double-click![](./media/8c6f8da97bf702080a8e302db2e9f982.png) to run it.
    
![](./media/046c67e4072093ee3dad27e8088fcf9f.png)
    

2). Click“Next”and choose ![Img](./media/img-20231114152827.png) , then tap“Next” .

![](./media/384203e0b54ddfe37f18b65f70e786e5.png)

![](./media/cf4e91eac0c0573cff282256a915a01a.png)
    
3). Click “Next” and “Install”.
    
![](./media/0af58ee3afb14005a884ca2dc941157f.png)
    
![](./media/807623ddeea20c8b61503845d8aec9bc.png)

4). After a few seconds, click "Finish".
    
![](./media/df2deb7e04c25ee207e994f0d2808194.png)

##### (4) Burn Win32DiskImager 

Download Link：[https://sourceforge.net/projects/win32diskimager/](https://sourceforge.net/projects/win32diskimager/)

![Img](./media/img-20231114152921.png)

a. After the download, double-click and tap“Run”.

![Img](./media/img-20231114152940.png)

b. Select ![Img](./media/img-20231114152953.png) and tap“Next”.

![Img](./media/img-20231114153002.png)

![Img](./media/img-20231114153007.png)

c. Click “Browse...”and find out the folder where the Win32DiskImager is located, tap “Next”. 

![Img](./media/img-20231114153026.png)

d. Tick ![Img](./media/img-20231114153042.png) , click “Next” and “Install”.

![Img](./media/img-20231114153057.png)

![Img](./media/img-20231114153104.png)

e. After a few seconds, click“Finish”. The installation is finished. 

![Img](./media/img-20231114153141.png)

##### (5) Scan for IP address software tool---WNetWatcher
    
Download Link：[http://www.nirsoft.net/utils/wnetwatcher.zip](http://www.nirsoft.net/utils/wnetwatcher.zip)
        
##### (6) Raspberry Pi Imager

Download link for **the latest version**:

[https://www.raspberrypi.org/downloads/raspberry-pi-os/](https://www.raspberrypi.org/downloads/raspberry-pi-os/)

**Old version**：

Raspbian：[https://downloads.raspberrypi.org/raspbian/images/](https://downloads.raspberrypi.org/raspbian/images/)

Raspbian full：[https://downloads.raspberrypi.org/raspbian_full/images/](https://downloads.raspberrypi.org/raspbian_full/images/)

Raspbian lite：[https://downloads.raspberrypi.org/raspbian_lite/images/](https://downloads.raspberrypi.org/raspbian_lite/images/)

We use the 2020.05.28 version in the tutorial and recommend you to use this version

(Please download this version as shown in the picture below.)

[https://downloads.raspberrypi.org/raspios_full_armhf/images/raspios_full_armhf-2021-05-28/](https://downloads.raspberrypi.org/raspios_full_armhf/images/raspios_full_armhf-2021-05-28/)

![](./media/857946c171dd1f5617a0cbbdd2608baf.png)

### 1.2. Install Raspberry Pi OS on Raspberry Pi 4B

#### 1.2.1. Connect the TFT memory card to a card reader, then plug the card reader into a computer’s USB port.

![Img](./media/img-20231011080903.jpg)

#### 1.2.2. Use the SD Card Formatter to format a TFT memory card, as illustrated below：

![](./media/79d747e6f00f857a593b3327397cc44f.png)

![](./media/cbc55902de71ce984d873ca2cb67fffa.png)

![](./media/82031b5354cc4edeccf2bfa7465b7c6c.png)

#### 1.2.3. Burn System:

（1）Use **Win32DiskImager** to burn the official **Raspberry Pi OS** mirror to the TFT memory card.

![](./media/80d236cae8bdf63d80dc65048ffb52b3.png)

![](./media/243d1ef34211eafe1a92b67fc0ee85a2.png)

![](./media/ea854c476e9a8d4f82dd4a7c714cd5af.png)

（2）After the mirror system is burned, don’t pull out the card reader, use a notepad to create a file named **SSH** and delete **.txt** , then copy it to the boot directory of the TFT card, so that you can open the SSH login function, as shown in the following figure:

![](./media/ffb73310322accd671da373bb2e71945.png)

（3） Pull out the card reader.

#### 1.2.4. Log in system:

（<span style="color: rgb(255, 76, 65);">The following operations require raspberry to share the same LOCAL area network with the PC</span>）

A. Insert the burned TFT memory card into the Raspberry Pi, connect internet cables and plug in power. If there is a screen and a HDMI cable of Raspberry Pi, connect the screen, and you can see the Raspberry Pi OS startup screen. If there is not a HDMI cable of Raspberry Pi, you can enter the desktop of Raspberry Pi via SSH remote login software---WinSCP and xrdp.

![Img](./media/img-20231011100454.png)

B. Use the WNetWatcher software to find the IP address of the Raspberry Pi.
![Img](./media/img-20231011114034.png)

C. If there is no IP address as shown in the figure above, follow the following steps to set it.

![Img](./media/img-20231011114043.png)

![Img](./media/img-20231011114047.png)

D. Once the setup is complete, record the IP and MAC addresses of the Raspberry Pi. As shown in the red box below, the MAC address of the Raspberry Pi is **b8:27:eb:17:16:01**, and the ip address is **192.168.0.57**. 

![Img](./media/img-20231011114112.png)

E. If you do not know the mac address and the ip address of the Raspberry Pi, then unplug the network cable of the Raspberry PI first, open the **WNetWatcher** query, and the detection times will be displayed on the right side of the interface. Connect the Raspberry Pi cable and query it once using **WNetWatcher**, and the Raspberry Pi address is detected one less time than the other addresses. Then write down the ip and mac addresses.

#### 1.2.5. Remote login

Enter default user name, password and host name on WinSCP to log in. Only a Raspberry Pi is connected in the same network.

![](./media/0a41d5c629ec98afbc31dc47ff5c18ec.png)

![](./media/ff64e71b9e30df60d0b099dbc2532587.png)

![Img](./media/img-20231011114258.png)

![Img](./media/img-20231011114428.png)

#### 1.2.6. View the ip address and mac address

![](./media/a4285a452978026c9e60c31d35974315.png)

Click to open terminal and input the password: <span style="color: rgb(255, 76, 65);">raspberry</span>, and tap“**Enter**”on keyboard.

![](./media/a433a9ee584c821a702d0250937e2ba8.png)

![](./media/7fb10d842cc7fd824a325d30fc3ecdc7.png)

After successfully login, open the terminal, input <span style="color: rgb(255, 76, 65);">ip a</span> and tap“**Enter**”keyboard to view the ip address and mac address.

![Img](./media/img-20231011115928.png)


#### 1.2.7. Fix the IP address of Raspberry Pi

IP address is changeable, therefore, we need to make IP address fixed for convenient use.

Follow the below steps:

Switch to root user

If without root user’s password

① Set root password

Input password in the terminal: **sudo passwd root** to set password.

② Switch to root user

Input **su root**

③ Fix the configuration file of IP address

Firstly change IP address of the following configuration file.

（<span style="color: rgb(255, 76, 65);">\#New IP address:：address 192.168.0.57</span>）

Copy the above new address to terminal and tap“**Enter**”keyboard.

**Configuration File:**

```
echo -e '

auto eth0

iface eth0 inet static

\#Change IP address

address 192.168.0.57

netmask 255.255.255.0

gateway 192.168.1.1

network 192.168.1.0

broadcast 192.168.1.255

dns-domain 119.29.29.29

dns-nameservers 119.29.29.29

metric 0

mtu 1492

'\>/etc/network/interfaces.d/eth0
```
Example operation diagram, as follows：

![Img](./media/img-20231012084519.png)


④ Reboot the system to activate the configuration file.

Input the restart command in the terminal: **sudo reboot**

You could log in via fixed IP afterwards.

⑤ Check IP to ensure IP address fixed well.

![Img](./media/img-20231011120412.png)

#### 1.2.8. Log in desktop on Raspberry Pi wirelessly

If we don't have an HDMI cable to connect to the display, can we wirelessly log in to the Raspberry Pi desktop from the Windows desktop? Yes, there are many methods, VNC and Xrdp are commonly used to log in desktop of Raspberry Pi wirelessly.

Let’s take an example of Xrdp.

①Install Xrdp Service in the terminal

Installation commands:

Switch to root User: <span style="color: rgb(255, 76, 65);">su root</span>

Installation commands: <span style="color: rgb(255, 76, 65);">apt-get install xrdp</span>

Enter y and tap“**Enter**”keyboard.

As shown below:

![](./media/aa59941ff4c1e582e8183c1dc3767fce.png)

Open the remote desktop connection on Windows

Press **WIN+R** on keyboard and enter **mstsc.exe**.

As shown below:

![](./media/e5a66a3a1c998f8feb1c21c7a457ec4e.png)

Enter the IP address of the Raspberry Pi, as shown below. Click “Connect” and then click “Connect”again.**192.168.0.57** is the ip address we use, you could change it into your IP address.

![Img](./media/img-20231011120551.png)

A prompt will appear and you can click “Yes”.

![](./media/297813f1370ce5c158fac61511f61295.png)

Then enter the user name: <span style="color: rgb(255, 76, 65);">pi</span> ,and the default password: <span style="color: rgb(255, 76, 65);">raspberry</span>, as shown below:

![Img](./media/img-20231011120636.png)

Click“OK”or tap“Enter”keyboard, you will view the desktop of Raspberry Pi OS, as shown below:

![](./media/56bd5693edd484c4433dc438b58c6130.png)

Now, we finish the basic configuration of the Raspberry Pi OS system.

### 1.3. Preparations for Python

Python is a programming language that lets you work more quickly and integrate your systems more effectively.

Python is an interpreted, high-level and general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.

Next to pick up Python to control 40 pin of Raspberry Pi.

#### 1.3.1. Hardware：

| **Raspberry Pi 4B**     | **Raspberry Pi 4B Model** |
| :---------------------: | :-----------------------: |
| ![image-20230425081935044](media/image-20230425081935044.png) |![image-20230425081939356](media/image-20230425081939356.png)|

**Hardware Interfaces：**

![](./media/d232a87d73f7426894a6cafed80521a0.png)

**40-Pin GPIO Header Description：**

GPIO pins are divided into BCM GPIO number, physics number and WiringPi GPIO number.

We usually use WiringPi GPIO when using C language and BCM GPIO and physics number are used to Python, as shown below;

In these lessons, we use Python, so BCM GPIO number is adopted.

![](./media/ca74a57f9eb9086f102688bf043e49fd.png)

Note: pin(3.3 V) on the left hand is square, but other pins are round. Turn Raspberry Pi over, there is a square GPIO on the back.(you could tell from pin(3.3V).

![](./media/86a686aad06cfe7563e7a01456e2cb7a.jpeg)

<span style="color: rgb(255, 76, 65);">Note:</span> the largest current of each pin on Raspberry Pi 4B is 16mA and the aggregate current of all pins is not less than 51mA.

#### 1.3.2. Copy Example Code Folder to Raspberry Pi：

Place example code folder to the pi folder of Raspberry Pi. and extract the example code from “<span style="color: rgb(255, 76, 65);">**Python_Codes(Raspberry-Pi).zip**</span>” file, as shown below:

![](./media/e7b577a013d27250449f6a6062f2a692.png)

![](./media/5f4f542cedf657c9cdf83c8fcc9b4b91.png)

![](./media/6721cea2e1524674a8732217b3f998ac.png)

Double-click “<span style="color: rgb(255, 76, 65);">**Python_Codes(Raspberry-Pi)**</span>” to check <span style="color: rgb(255, 76, 65);">.py</span> files.

![](./media/fbf63c5b42b99c080e5be93603e1facb.png)


####  1.3.3. Micropython firmware and Thonny

##### (1) Update the firmware of Micropython

If you want to run the MicroPython on the Pi Pico board, you need to upload a firmware to the pico board.

You can program via C language or MicroPython on the pico board. But you need to download the MicroPython firmware.

<span style="color: rgb(255, 76, 65);">Note: </span>

MicroPython firmware is required to be downloaded once. You don’t need to download it again when programming with MicroPython. 

If you have downloaded the .uf2 program firmware written in C language, the MicroPython firmware will be overwritten, so next time you use MicroPython, you need to follow the steps below to update the Raspberry Pi Pico's firmware.

**Download the firmward of Micropython**

<span style="color: rgb(255, 76, 65);">Method 1:</span> 

Click ![](./media/e1e5a14737d3f99726202e22e731d506.png)to enter the website：[https://www.raspberrypi.com/documentation/microcontrollers/](https://www.raspberrypi.com/documentation/microcontrollers/)

![](./media/3b3e6a639416b76c44f2a0854dc451cc.png)

![](./media/5d04d67506852588d126ce760739a3c5.png)

Click “**MicroPython(**Getting started MicroPython**)**” to go to the firmware download page.

![](./media/137e21851df02502fb989d8541fa0da8.png)

<span style="color: rgb(255, 76, 65);">Method 2:</span>

Click![](./media/e1e5a14737d3f99726202e22e731d506.png)to open the browser，click [https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2](https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2) to download the firmware.

<span style="color: rgb(255, 76, 65);">**Note：** transfer the firmware（rp2-pico-20210902-v1.17.uf2）to the desktop of Raspberry pi imager.</span>


##### (2) Program the firmware of MicroPython

Hold down **BOOTSEL** , connect a microUSB cable to the USB port of the pico board.

![](./media/33c91d51b2aeb2c943691706354aaad1.png)

Release the button, then there pops up a page.

Enter “**raspberry**” in the Password box, click “**OK**”.

![](./media/57aa727673e02ed5cc889c8669c587f2.png)

The drive **RPI-RP2** will appear on the desktop of the Raspberry Pi imager.

![](./media/6e6c11ffed92c2ae8307044bb19ef4dc.png)

<span style="color: rgb(255, 76, 65);">Note：</span>

The latest Raspberry Pi mirroring system will not display the above dialog box, but the old version will display the above dialog box.

<br>
<br>

Click “**OK**” and open “**drive(RPI-RP2)**”. Copy or drag the file（**rp2-pico-20210902-v1.17.uf2**）to the RPI-RP2.

![](./media/9cc833c1f1a30f7dc03dbf3704bb8078.png)

![](./media/39b8a265056f4a28d55ba3aba3bbae33.png)

After the firmware is programmed, the Pico board will reboot. Then you can run Micropython.

**Serial Ports**

The MicroPython firmware is equipped with a virtual USB serial port which is accessed through the micro USB connector on Raspberry Pi Pico.

Your computer should notice this serial port and list it as a character device, most likely **/dev/ttyACM0**.

You can run **ls /dev/tty\*** to list your serial ports. There may be quite a few, but MicroPython’s USB serial will start with **/dev/ttyACM**. If in doubt, unplug the micro USB connector and see which one disappears. If you don’t see anything, you can try rebooting your Raspberry Pi.

Enter the following command to install minicom:

<span style="color: rgb(0, 209, 0);">sudo apt install minicom</span>

<br>
<br>

![](./media/76bae15ef182b33d6a7b4d8b03d65475.png)

Select **Y** .

![](./media/b3d8daaf8399339b323c84b3c56f9306.png)

Enter the following commander, press **Enter** and open minicom

<span style="color: rgb(0, 209, 0);">minicom -o -D /dev/ttyACM0</span>

<br>
<br>

![](./media/69b6047c7ba379310c76fcd52985d73f.png)

![](./media/0477b4ed6ddd221558d39de98d232f9d.png)

Press **Ctrl + B** .

![](./media/eedefa717220824a6ef39d944aaf8e5e.png)

Enter print("Hello World") at the terminal and press **Enter**，then **Hello World** will be displayed.

![](./media/fc41b356fd7081524dccb490ce9a3259.png)

##### (3) Install Thonny

The Raspberry Pi Imager that we downloaded comes with some commonly used software, and Thonny is among them.

![](./media/0d1bd2cf2c99d19959684424c425c6ce.png)

If the Raspberry Pi Imager does not have Thonny, you need to manually download it yourself. Enter the following command in the terminal to download and install Thonny.

<span style="color: rgb(255, 169, 0);">sudo apt install thonny</span>

<br>
<br>

![](./media/abf9b407362422678af8eb0fd1b49684.png)

Open Thonny, click“**Switch to regular mode**”to switch modes, and click OK to reopen the Thonny.

![](./media/08a1b220328ad8b9c071741ea46fdb25.png)

![](./media/31139bbd6173717bb10421de36cf1334.png)

**Connect the Raspberry Pi Pico on the Thonny**

Click “**Python3.9.2**” and select “**MicroPython(Raspberry Pi Pico)**”.

![](./media/00ae7e7e6e18b5610b71e4186311c84a.png)

![](./media/3bfbbdcd940252fbdf399ff0de47dea2.png)

Click “**Tools**” → “**Options...**”.

![](./media/c98465fe869c72654adb035aceaaf83e.png)

Select “**Micropython (generic)**” or “**Micropython (Raspberry Pi Pico)**”. How to choose Micropython(Raspberry Pi Pico)? As shown below;

![](./media/2a698bf071942ac19ccb5eaa9fada66e.png)

Click “**Port**” to **select corresponding port** and click "**OK**".

![](./media/e72a434210946d6f9c981128e7f1195e.png)

![](./media/bb18e9e6d072469b230a06926dd5a3cc.png)

Click “**View**” → “**Files**”, then “**This computer**” and “**Raspberry Pi Pico**” will appear.

![](./media/69e6ee6703f190b059bf8eb4902ee637.png)

![](./media/9388fd552f625574f9a77c1c855867c2.png)

![](./media/5ef0b1e392c2e8f1ffc375bc966da812.png)

![](./media/7f98556c0fa277c215058ec2c4a14b3a.png)

### 1.4. Test Code

<span style="color: rgb(255, 169, 0);">Test the Shell commander</span>

<br>
<br>

Enter “**print(Hello World\!)**” in the Shell and press “**Enter**”.

![](./media/77c268003ff676b5d6c3baab9b2ebef3.png)

#### Online running：

To run Raspberry Pi Pico online, we need to connect the Raspberry Pi Pico to our computer, which allows us to compile or debug programs using Thonny software.  

**Advantages**: you can compile or debug programs using Thonny software.  

Through the "**Shell**" window, we can view the error information and output results generated during the operation of the program, and query related function information online to help improve the program.  

**Disadvantages**: To run Raspberry Pi Pico online, you must connect Raspberry Pi Pico to a computer and run it with Thonny software.  

If the Raspberry Pi Pico is disconnected from the computer, when they reconnect, the program won't run again.  

<span style="color: rgb(255, 76, 65);">basic operation:</span>

<br>

Open Thonny and click ![](./media/e776b2c874ac9c5d852212383b3cec27.png)“**Open...**”.

![](./media/d275ff88709c9e660a68545cdf1a1b4a.png)

Click“**This computer**”.

![](./media/f419da64013966003b63315c70bd88ad.png)

Enter "<span style="color: rgb(255, 76, 65);">.../home/pi/Python_Codes(Raspberry-Pi)/Project 01: Hello World</span>" to select **Project\_01\_HelloWorld.py** and click **OK**.

![](./media/03b115c1a39fcde581112f86a47fdb87.png)

Click ![](./media/0e4d02d37292e9d2c208b6b8bcde4f21.png)“Run current script to program **Hello World\!**, "**Welcome Keyestudio**" will be displayed on the **Shell**.

![](./media/e1aafe9ff0bfa4214e56f682d653ff07.png)

**Exit online**

When running online, click “![](./media/92a50d0579b5d50ea659a6b8930da44a.png)**Stop /Restart Backend**” on Thonny to exit the program.  

![](./media/5d0aa92074c5aebbcb37c0638ab308f0.png)

#### Offline running:

When running offline, the Raspberry Pi Pico doesn't need to connect to a computer and Thonny. Once powered up, it can run the main.pyprogram stored in the Raspberry Pi Pico.  

**Pros**: We don't need to connect a computer to Thonny's software to run the program.  

**Cons**: The program stops automatically when an error occurs or the Raspberry Pi Pico runs out of power, and the code is hard to change.

**Basic Operation:**

Once powered up, the Raspberry Pi Pico will  check for the presence of main\.py on the device automatically. If so, run the program in main\.py and go to the shell command system. (If we want the code to run offline, we can save it as main\.py); If the main\.py does not exist, go directly to the shell command system.   

Click “**File**” → “**New**”, create and write code.

![](./media/7a6988dfff80ecb0479e3e878ccde171.png)

Enter the code in the newly opened file. Here we use the Project\_02\_Onboard\_LED\_Flashing. Py code as an example.  

![](./media/9a7d7e35504c9f750e4a58eccd38e094.png)

Click “**Save**” on the menu bar, we can save the code in This computer or MicroPython device.

![](./media/3f7945cc8586bb85aa7bc24c480fd012.png)

Select “**MicroPython device**”，enter “**main\.py**”in the new pop-up window and click “**OK**”.

![](./media/0f5f516143bdb28bdcb62bad6784729d.png)

![](./media/c789c476ad5d517082b9c992ea365080.png)

![](./media/78a529ec66e2726b93dee1434e790554.png)

Disconnect the microUSB cable to the Raspberry Pi Pico and reconnect, and the LEDs on the Raspberry Pi Pico will  flash repeatedly. 

![Img](./media/img-20231114160904.png)

**Exit from Offline operation**

Connect Raspberry Pi Pico to the computer，click ![](./media/92a50d0579b5d50ea659a6b8930da44a.png) “Stop/Restart backend”on Thonny to end the offline operation.  

![](./media/1de7ccf1eee2c1acc908a70fa151774d.png)

If it does’t work, click ![](./media/92a50d0579b5d50ea659a6b8930da44a.png) “Stop/Restart backend” on Thonny several times or reconnect to the Raspberry Pi Pico.

![](./media/3abb1b4a1e2e600d06f76735cfe1c522.png)

We provide a main\.py file to run offline.  The code added to main\.py is the bootstrap that executes the user code file. We just need to upload the offline project's code file (<span style="color: rgb(255, 76, 65);">.py</span>) to the "<span style="color: rgb(255, 76, 65);">MicroPython Device</span>".

Move the folder <span style="color: rgb(255, 76, 65);">**Python_Codes(Raspberry-Pi)**</span> to the folder home/pi of Raspberry Pi system and open Thonny.

![](./media/aa2f0b276daa0dbffb031744c3083747.png)

Expand Project 00 : main in <span style="color: rgb(255, 169, 0);">.../home/pi/Python_Codes(Raspberry-Pi)</span> directory . Double-click "**main\.py**" to make the code in "**MicroPython Device**" run offline.  

![](./media/476b7d201f06b4f2a8d6479677e389bc.png)

Here, we use project 00 and Project 02 cases as examples.  

The results are displayed using an LED(GP25 pin) on a Raspberry Pi Pico.  If we have modified the Project\_02\_Onboard\_LED\_Flashing. Py file, then we need to modify it accordingly. 

Right-click the Project\_02\_Onboard\_LED\_Flashing. Py file and select '**Upload to/**' to upload the code to Raspberry Pi Pico, as shown below.  

![](./media/2d1b1056c12d938570df999d8136b74b.png)

Upload the **main\.py** in the same way.

![](./media/bf2c18b6154ce77b2c449b9b9cdb5a76.png)

Disconnect and reconnect the microUSB cable to the Raspberry Pi Pico, and the LEDs will flash repeatedly .

![Img](./media/img-20231114160947.png)

<span style="color: rgb(255, 76, 65);">**Note:**</span>

The code here runs offline. If we want to stop running offline and go to "Shell", simply click "![](./media/0b9cf6411531d005d760df16819813e3.png)Stop/Restart Backend" on Thonny software.

![](./media/c3dab4ada7b2e618d6278c570b9b1955.png)



### 1.5. Thonny common operations

#### (1) Upload the code to Raspberry Pi Pico

In the Project 01：Hello World file, right-click and select Project\_01\_HelloWorld.py，select “**Upload to /**”and upload the code to the root directory of the Raspberry Pi Pico.

![](./media/77c723c6c821dce154aecf2d7b5f1581.png)

#### (2) Download the code to the computer

In the “**MicroPython device**”, right-click and select Project\_01\_HelloWorld.py，select “**Download to ...**” to download the code to our computer.

![](./media/f0ed82cf3717041f02d12958c6209171.png)

#### (3) Delete the files in the Raspberry Pi Pico root directory

In the “**MicroPython device**”，right-click and select Project\_01\_HelloWorld.py，select “**Delete**”，delete the Project\_01\_HelloWorld.py from the Raspberry Pi Pico root directory.

![](./media/82158486bd8db01e825cfe907c60204b.png)

#### (4) Delete files from the computer's directory

In the Project\_01 : Hello World file, right-click and select Project\_01\_HelloWorld.py，select “**Move to Recycle Bin**”，then it can be deleted from the Project\_01\_HelloWorld file.

![](./media/7fc1a7b93f57fe8994e3ab0d429ffc1f.png)

#### (5) Create and Save Code

Click “**File**” → “**New**” to create and compile code.

![](./media/373922a344188cda87b797b0ad639522.png)

Enter code in the newly opened file, here we use Project\_02\_Onboard\_LED\_Flashing.py code as an example.

![](./media/9a7d7e35504c9f750e4a58eccd38e094.png)

Click “**Save**”，and we can save the code to our computer or the Raspberry Pi Pico.

![](./media/3f7945cc8586bb85aa7bc24c480fd012.png)

Select “**MicroPython device**”，enter “**main\.py**” in the new pop-up window and click“**OK**”.

![](./media/0f5f516143bdb28bdcb62bad6784729d.png)

![](./media/c789c476ad5d517082b9c992ea365080.png)

We can see the code has been uploaded to the Raspberry Pi Pico.

![](./media/78a529ec66e2726b93dee1434e790554.png)

Click “**Run current script**”, the LED on the Raspberry Pi Pico will flash periodically.

![](./media/88c2dc64c5f38600d8ef7180ea8a7b30.png)

![Img](./media/img-20231114160947.png)


## Projects

### Project 01: Hello World

1.**Introduction**
    
For Raspberry Pi Pico beginners, we will start with some simple things. In this project, you only need a Raspberry Pi Pico and a USB cable to complete the "Hello World\!" project, which is a test of communication between Raspberry Pi Pico and the PC as well as a primary project.
    
2.**Components**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/img-20231010153539.png)</td>
<td>![Img](./media/3bdcc62cfa661d2b860a76e28537e21e.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.**Wiring Up**
    
In this project, we use a USB cable to connect the Raspberry Pi Pico to Raspberry Pi.
![Img](./media/img-20231010153654.png)

    
4.**Test Code**
    
Connect the pico board to the Raspberry Pi, then the Thonny can compile or debug.
    
Advantages：
    
1)\. You can use Thonny software to compile or debug programs.
    
2)\. In the "Shell" window, you can view the error information and output results generated during the running of the program, and you can query related functional information online to help improve the program.
    
    
    
Disadvantages：

You have to connect the pico board with the Raspberry Pi then run the Thonny.
    
If disconnecting pico board and the Raspberry Pi and rebooting them, programming may fail.
    
  
Open "Thonny" and click![](./media/aedf8b88905c3cbb3c9c7015f14d3c74.png)“Open...”
    
![](./media/0da7962f717a49547b37a223f78bd4c6.png)
    
Then click“This computer”.
    
![](./media/5bdbc66ef89b41a53e46696c07b2c282.png)
    
Select“Project\_01\_HelloWorld.py”and click“OK”.

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>
 
![](./media/d2395e9b262a28bd14ae7727e4e1f8c4.png)

Click ![](./media/bb4d9305714a178069d277b20e0934b7.png)to run the code Hello World\!. Then Welcome Keyestudio will be displayed on the Shell.

![](./media/0e8e900658e71b157e1f5b41f224a93c.png)

**Exit online running**

When running online，click![](./media/32e03e9d4211e9ef97c1d2b18f05c902.png)“Stop /Restart backend”to exit.

![](./media/92ea345930ed8be1b8e04b341f20f2b6.png)

5.**Test Code：**

```Python
print("Hello World!")
print("Welcome Keyestudio")
```
### Project 02: Onboard LED flashing

1.**Description：**

There is an onboard LED in Raspberry Pi Pico,which is a GP25 pin attached to the Raspberry Pi Pico. In this project, we will learn the effect of making the onboard LED blink.

2.**Components**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/img-20231010153844.png)
</td>
<td>![Img](./media/3bdcc62cfa661d2b860a76e28537e21e.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.**Wiring Up**
    
In this project, we use a USB cable to connect the Raspberry Pi Pico to Raspberry Pi.

![Img](./media/img-20231010153923.png)


4.**Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

**Online running**

Open“Thonny”, click “This computer”→“home”→“pi”→“2. Projects”→“Project 02：Onboard LED flashing”

![](./media/7132fc82461f7395cfbd63fd62268984.png)

Go to the folder Project 02：Onboard LED flashing\<double-click “Project\_02\_Onboard\_LED\_flashing.py”, as shown below;

![](./media/dca3b825e4f9fb5f7090dbefadc441d1.png)

```Python
from machine import Pin
import time

led = Pin(25, Pin.OUT)   # create LED object from Pin 25, Set Pin 25 to output

try:
    while True:
        led.value(1)    # Set led turn on
        time.sleep(0.5) # Sleep 0.5s
        led.value(0)    # Set led turn off
        time.sleep(0.5) # Sleep 0.5s
except:
    pass
```

Connect the pico board to the Raspberry Pi. Click ![](./media/32e03e9d4211e9ef97c1d2b18f05c902.png)to check the Shell

![](./media/a8313a26331800f383c84ffa64b4e225.png)

Click ![](./media/bb4d9305714a178069d277b20e0934b7.png) to run the code. Then the LED on the pico board will flash; click ![](./media/32e03e9d4211e9ef97c1d2b18f05c902.png)to exit the program.

![](./media/6dbd11e5159b47b0061c2ed199bdd75e.png)

![Img](./media/img-20231114160947.png)

<span style="color: rgb(255, 76, 65);">Note:</span> This is the code that runs online.  If you disconnect the USB cable and restart Raspberry Pi Pico, the LEDS on Raspberry Pi Pico stop flashing. The following information will be displayed in the "Shell" window of Thonny software:  

<br>
<br>

![](./media/b7d8c524956cb140d5d04eefff0d9f9f.png)

**Code to run offline** (upload code to Raspberry Pi Pico) :

Ensure that the Raspberry Pi Pico is connected to the computer and click ![](./media/32e03e9d4211e9ef97c1d2b18f05c902.png).  

![](./media/3c1df575aecb6514c127558c7b70dfae.png)

As shown in the following figure, right-click the file“Project\_02\_Onboard\_LED\_Flashing. py”and choose“**Upload to/**”to upload the code to Raspberry Pi Pico.  

![](./media/8958426b1b043cd82eab3eb6891a9113.png)

Upload **main\.py** in the same way.

![](./media/ce2c0761a54621a4d363fae29cf0369f.png)

Disconnect the USB cable from the Raspberry Pi Pico and reconnect, and the Raspberry Pi Pico's LED flashes repeatedly.  

![Img](./media/img-20231114160947.png)

Note: The code here runs offline.  If you want to Stop running offline and display the information in the “Shell” window, simply click![](./media/32e03e9d4211e9ef97c1d2b18f05c902.png)in Thonny software.

![](./media/a416597bf07fbb471cc82a1c355065af.png)


### Project 03：External LED flashing 

1.**Introduction**
    
In this project, we are going to show you the external LED flashing effect.  We will use the Raspberry Pi Pico's digital pins to turn on the LED and make it flash.
    
2.**Components**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/19a8d68dfaf5224addb911f981c31ffc.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/c801a7baee258ff7f5f28ac6e9a7097b.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Jumper Wire*2</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/7eb361d680dfa351f07f8527aeb37abd.png)</td>
<td>![Img](./media/098a2730d0b0a2a4b2079e0fc87fd38b.png)</td>
<td>![Img](./media/e380dd26e4825be9a768973802a55fe6.png)</td>
<td></td>
</tr>
<tr class="even">
<td>Red LED*1</td>
<td>220Ω Resistor*1</td>
<td>Breadboard*1</td>
<td></td>
</tr>
</tbody>
</table>


3.**Knowledge**

**（1）LED:**

![Img](./media/img-20231010153407.png)

The LED is a kind of semiconductor called “light-emitting diode”, which is an electronic device made from semiconducting materials (silicon, selenium, germanium, etc.).  It has a anode and a cathode.  The short lead is cathode, which connects to GND, the long lead is anode , which connects to3.3V or 5V.

![](./media/f70404aa49540fd7aecae944c7c01f83.jpeg)

**（2）5-band Resistor**

A resistor is an electronic component in a circuit that restricts or regulates the flow current flow. On the left is the appearance of
the resistor and on the right is the symbol for the resistance in the circuit . Its unit is(Ω). 1 mΩ= 1000 kΩ，1kΩ= 1000Ω.

![](./media/8a86f65cf820d08e8956daa70d1c4195.jpeg)
![](./media/f6079fe22518f0fc1b0c3a3b93a516a1.png)

We can use resistors to protect sensitive components, such as LEDs. The strength of the resistance is marked on the body of the resistor with an electronic color code. Each color code represents a number, and you can refer to it in a resistance card.

\-Color 1 – 1st Digit

\-Color 2 – 2nd Digit

\-Color 3 – 3rd Digit

\-Color 4 – Multiplier

\-Color 5 – Tolerance

![](./media/c3df005312cd9f6d4cdae6abf3cddb83.png)

In this kit, we provide three 5-band resistors with different resistance values. Take three 5-band resistors as an example.

220Ω resistor\*10

![](./media/55c0199544e9819328f6d5778f10d7d0.png)

10KΩ resistor\*10

![](./media/246cf3885dc837c458a28123885c9f7b.png)

1KΩ resistor\*10

![](./media/19f5dfc51adfd79b04c3b164529767ed.png)

In the same voltage, there will be less current and more resistance. The connection between current, voltage, and resistance can be expressed by the formula: I=U/R. In the figure below, if the voltage is 3V, the current through R1 is: I = U / R = 3 V / 10 KΩ= 0.0003A=0.3mA.![](./media/b3eec552e4dfad361833730698621776.png)

Do not directly connect resistors with very low resistance to the two poles of the power supply, as this will cause excessive current to damage the electronic components. Resistors do not have positive and negative poles.

** (3) Breadboard**

A breadboard is used to build and test circuits quickly before finalizing any circuit design. The breadboard has many holes , into
which circuit components like integrated circuits and resistors can be inserted. A typical breadboard is as follows.

![](./media/612c1381811b2d780d5f6ed6a7ec3701.png)

The bread board has strips of metal , which run underneath the board and connect the holes on the top of the board. The metal strips are laid out as shown below. Note that the top and bottom rows of holes are connected horizontally while the remaining holes are connected vertically.

![](./media/b45e70b961537035c85878b73d371725.png)

The first two rows (top) and the last two rows (bottom) of the breadboard are used for the positive (+) and negative (-) terminals of the power supply, respectively. The conductive layout of the breadboard is shown in the following diagram.

![](./media/d5478bd5eac558252cbc235479d979eb.png)

When we connect DIP (Dual In-line Packages) components, such as integrated circuits, microcontrollers, chips and so on, we can see that a groove in the middle isolates the middle part, so the top and bottom of the groove is not connected. DIP components can be connected as shown in the figure below:

![](./media/50caf14e911c4244779e99445c658db6.png)

![](./media/9b66ae2199e77fbc99b7b278dac0b567.png)

4.**How to use the keyestudio raspberry pico expansion board.**

Stack the Raspberry Pi Pico on the expansionboardto use, as shown below:


![](./media/fae969ca3b1a4592a83a4e05f5795a5b.png)

5.**Power Supply:**

In this project, we use a USB to connect the Raspberry Pi Pico to the computer. Please refer to the documentation for connection methods: Preparation for Python

![](./media/8ea81d60b8e2132c358041235490b7d5.jpeg)

6.**Circuit Diagram and Wiring Diagram**

First, cut all power to the Raspberry Pi Pico.  Then build the circuit according to the circuit diagram and wiring diagram.  After the circuits are set up and verified, using a USB cable to connect the Raspberry Pi Pico to a computer .

**Note:** Avoid any possible short circuits(especially connecting 3.3V and GND)\!

**Warning:** A short circuit may cause a large current in the circuit, causing components to overheat and permanent damage to the hardware.

![](./media/cb069d7553d861e3293d8bdbe85bbd05.png)

![](./media/898285da10fa9b39e52a02bc68758d27.png)

7.**Wiring Diagram**

Note:

How to connect a LED

![](./media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω five-band resistor

![](./media/55c0199544e9819328f6d5778f10d7d0.png)

8.**Test Code**

According to the circuit diagram, when the GP16 output of the Pico is high, the LED will light up;  When the output power is low, the LED will light off.Therefore, we can make the LED flash repeatedly by controlling the GP16 to repeatedly output high and low levels.  

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

**Code running online:**

Open “Thonny”, clickThis computer”→“home”→“pi”→“2. Projects”→“Project 03：External LED flashing”.

Enter the file“Project 03：External LED flashing”, double left-click“Project\_03\_External\_LED\_flashing.py”,open it, as shown below:

![](./media/8b4bad2c707397cc37c542c03d7c349f.png)

![](./media/41dbfef0bb4a9e876293a090afc41637.png)

```Python
from machine import Pin
import time

led = Pin(16, Pin.OUT)   # create LED object from Pin 16, Set Pin 16 to output

try:
    while True:
        led.value(1)    # Set led turn on
        time.sleep(0.5) # Sleep 0.5s
        led.value(0)    # Set led turn off
        time.sleep(0.5) # Sleep 0.5s
except:
    pass
```

Connect the pico board to the Raspberry Pi. Click ![](./media/32e03e9d4211e9ef97c1d2b18f05c902.png)to check the Shell

![](./media/de1565c576c4233dfbe6d143404f03ac.png)

Click ![](./media/bb4d9305714a178069d277b20e0934b7.png) to run the code. Then the LED on the pico board will flash; click ![](./media/32e03e9d4211e9ef97c1d2b18f05c902.png)to exit the program.

![](./media/bb35d00ea60c7905ab81c4f36b528be6.png)

![Img](./media/img-20231116151553.png)

<span style="color: rgb(255, 76, 65);">Note:</span> This is the code that runs online, if we disconnect the USB cable, then restart the“Raspberry Pi Pico”, the LED will stop flashing. The following information will be displayed in the "Shell" window of Thonny software:
 
<br>
<br>

![](./media/e9abb644348e7adcdeddcee76b992755.png)

**Code running offline** （Upload the code to the Raspberry Pi Pico）：

Ensure that the Raspberry Pi Pico is connected to the computer, click“![](./media/32e03e9d4211e9ef97c1d2b18f05c902.png)Stop/Restart backend”

![](./media/2a48bcd6f59f1e11f127f9faa50cad92.png)

As shown below, right-click the file“Project\_03\_External\_LED\_flashing.py”，select**Upload to/**”to upload the code to the Raspberry Pi Pico.

![](./media/d73c9e4598ed1888447561693be920ca.png)

Upload main.py in the same way

![Img](./media/img-20231116151545.png)

Disconnect the USB from the Raspberry Pi Pico and reconnect, the LED in the circuit will flash repeatedly.

![](./media/2dcc6a55b77b4175b5175f717eb196c3.png)

**Note:** The code here runs offline. If you want to stop and display the information in the Shell window, simply click“![](./media/32e03e9d4211e9ef97c1d2b18f05c902.png)Stop/Restart backend” in Thonny software.


![](./media/a400b9db13988d0762d991a2cb7abaec.png)



### Project 04: Breathing Led

1.**Introduction**
    
In previous studies, we know that LEDS have on/off state, so how to enter the intermediate state?  How to output an intermediate state to make the LED "half bright"?  That's what we're going to learn.  Breathing lights, or LEDS turn on and off again, which are like "breathing".  So, how to control the brightness of LEDS?  We will use the Raspberry Pi Pico PWM to achieve this goal.  
    
2.**Components**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/19a8d68dfaf5224addb911f981c31ffc.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/c801a7baee258ff7f5f28ac6e9a7097b.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Jumper Wire*2</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/7eb361d680dfa351f07f8527aeb37abd.png)</td>
<td>![Img](./media/098a2730d0b0a2a4b2079e0fc87fd38b.png)</td>
<td>![Img](./media/e380dd26e4825be9a768973802a55fe6.png)</td>
<td></td>
</tr>
<tr class="even">
<td>Red LED*1</td>
<td>220ΩResistance*1</td>
<td>Breadboard*1</td>
<td></td>
</tr>
</tbody>
</table>

3.**Knowledge**

![](./media/6549bdbfd4e7b6b2b341012105d655e8.png)

**Analog & Digital**

Analog signals are continuous signals in both time and value.  In contrast, a digital or discrete time signal is a time series consisting of a series of numbers.  Most signals in life are analog signals.  A familiar example of an analog signal is how temperatures change continuously throughout the day, rather than suddenly changing from 0 to 10 in a flash.  However, the value of a digital signal can change instantaneously. This change is represented numerically as 1 and 0(the basis of binary code).  It's easier to see the difference, as shown below:

![](./media/4bdf6127e563b453a1fd8953b4ebb277.png)

In practical applications, we often use a binary as a digital signal, which are a series of 0 and 1. Since binary signals have only two values(0 or 1), they have great stability and reliability.  Finally, analog and digital signals can be converted to each other. 

**PWM：**

Pulse Width Modulation (PWM) is an effective method to control analog circuit by digital signal.  Ordinary processors cannot directly output analog signals.  The PWM makes this conversion (convert digital signal to analog signal) very convenient, which uses digital pins to send square waves at a certain frequency, which is high and low output to alternate for a period of time.  The total time of each set of high and low levels is generally fixed, which is called the period (Note: the reciprocal of the period is the frequency). The time of the high level output is usually called pulse width, and the duty cycle is the percentage of the pulse width (PW) to the total period (T) of the waveform. 

The longer the duration of the high level output as well as the duty cycle is, the higher the corresponding voltage in the analog
signal will be. The figure below shows the variation of analog signal voltage from 0V to 3.3V(high level is 3.3V) corresponding to pulse width of 0% to 100%.  

![](./media/a439e1bd8a4578b43b7188c821d58594.jpeg)

We all know that the longer the PWM duty cycle is, the higher the output power will be. Therefore, we can use PWM to control the brightness of LEDS or the speed of dc motors and so on.  As can be seen from the above, the PWM is not a real analog signal, and the effective value of the voltage is equal to the corresponding analog signal.  Therefore, we can control the output power of LEDS and other output modules to achieve different effects.

**Raspberry Pi Pico and PWM**

The Raspberry Pi Pico has 16 PWM channels, each of which can control frequency and duty cycle independently. The clock frequency ranges from 7Hz to 125MHz.  Each pin on the Raspberry Pi Pico can be configured for PWM output.  

4.**Circuit Diagram and Wiring Diagram**

![](./media/cb069d7553d861e3293d8bdbe85bbd05.png)

![](./media/898285da10fa9b39e52a02bc68758d27.png)

Note:

How to connect the LED

![](./media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω 5-band resistor

![](./media/55c0199544e9819328f6d5778f10d7d0.png)

5.**Test Code**

The design of this project makes the GP16 output PWM, and the pulse width gradually increases from 0% to 100%, and then gradually decreases from 100% to 0%.  

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→”Project 04：Breathing Led”. And double-click “Project\_04\_Breathing\_Led.py”.

![](./media/fb732f2603ea6f808c2fda117dd865f8.png)

```Python
#MicroPython implementation of raspberry PI Pico board LED breathing lamp program example
import time
from machine import Pin,PWM
PWM_PulseWidth=0
#Using external LED, build PWM object PWM LED
pwm_LED=PWM(Pin(16))
#Set the PWM LED frequency
pwm_LED.freq(500)
while True:
    while PWM_PulseWidth<65535:
        PWM_PulseWidth=PWM_PulseWidth+50
        time.sleep_ms(1)   #Delay 1 ms 
        pwm_LED.duty_u16(PWM_PulseWidth)
    while PWM_PulseWidth>0:
        PWM_PulseWidth=PWM_PulseWidth-50
        time.sleep_ms(1)
        pwm_LED.duty_u16(PWM_PulseWidth)
```

6.**Test Result：**

Connect the pico board to the Raspberry Pi. Click ![](./media/32e03e9d4211e9ef97c1d2b18f05c902.png)to check the Shell

![](./media/ac7c042fd7d45662f04395de18f19019.png)

Click ![](./media/bb4d9305714a178069d277b20e0934b7.png) to run the code. Then the LED on the pico board will flash; click ![](./media/32e03e9d4211e9ef97c1d2b18f05c902.png)to exit the program.

![](./media/9e8a8c744f9d22c8821016ea4b0491ba.png)

![](./media/3673c95868f245ee28365de8e51d2ced.png)

### Project 05: Traffic Lights

1.**Introduction**

Traffic lights are closely related to people's daily lives, which generally show red, yellow, and green. Everyone should obey the traffic rules, which can avoid many traffic accidents. In this project, we will use Raspberry Pi Pico and some LEDs (red, green and yellow) to simulate the traffic lights.

2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/b18fe281156b29c44796f72222718d58.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/afa6edd3ff90b027a6f43995a6fb15a2.png)</td>
<td>![Img](./media/0c1b0f91b4e56bcbc235d06b48809ac9.png)</td>
<td>![Img](./media/c801a7baee258ff7f5f28ac6e9a7097b.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Red LED*1</td>
<td>Yellow LED*1</td>
<td>Jumper Wires</td>
</tr>
<tr class="odd">
<td>![Img](./media/6c688493b558ed5f3e90e7dab38cbd93.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
<td>![Img](./media/098a2730d0b0a2a4b2079e0fc87fd38b.png)</td>
<td>![Img](./media/b57b4057770f0bcc43f037c0ab8e1c41.png)</td>
<td></td>
</tr>
<tr class="even">
<td>Green LED*1</td>
<td>USB Cable*1</td>
<td>220ΩResistor*3</td>
<td>Breadboard*1</td>
<td></td>
</tr>
</tbody>
</table>

3.**Circuit Diagram and Wiring Diagram**

![](./media/4cf2ad735b0df82d62a5fcdb19ebf3c0.png)

![](./media/98f9db025163638c33095cbd16abe7e7.png)

Note:

How to connect an LED

![](./media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω 5-band resistor

![](./media/55c0199544e9819328f6d5778f10d7d0.png)

4.**Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→"Project 05: Traffic Lights”. And double-click“Project\_05\_Traffic\_Lights.py”.

![](./media/bb44b31699957a99ec3e33f7a887e1be.png)

```Python
from machine import Pin
import time

led_red = machine.Pin(16, machine.Pin.OUT)  # create red led object from Pin 16, Set Pin 16 to output
led_yellow = machine.Pin(17, machine.Pin.OUT)  # create yellow led object from Pin 17, Set Pin 17 to output
led_green = machine.Pin(18, machine.Pin.OUT) # create green led object from Pin 18, Set Pin 18 to output

while True:
    led_red.value(1)  # Set red led turn on
    time.sleep(5)   # Sleep 5s
    led_red.value(0) # Set red led turn off 
    led_yellow.value(1)
    time.sleep(0.5)
    led_yellow.value(0)
    time.sleep(0.5)
    led_yellow.value(1)
    time.sleep(0.5)
    led_yellow.value(0)
    time.sleep(0.5)
    led_yellow.value(1)
    time.sleep(0.5)
    led_yellow.value(0)
    time.sleep(0.5)
    led_green.value(1)
    time.sleep(5) 
    led_green.value(0) 
```

5.**Test Result：**

Connect the pico board to the Raspberry Pi. Click ![](./media/32e03e9d4211e9ef97c1d2b18f05c902.png)to check the Shell

![](./media/3691a51f61750b1dc918de0f771a5482.png)

Click“![](./media/bb4d9305714a178069d277b20e0934b7.png)”, the code starts executing, what we will see are below:

1). First, the green light will be on for 5 seconds and then off; 

2). Next, the yellow light blinks three times and then goes off. 

3). Then, the red light goes on for five seconds and then goes off. 
    
Repeat steps 1 to 3 above and press“Ctrl+C”or click“![](./media/ec00367ea605788eab454cd176b94c7b.png)” to exit the program.

![](./media/5da95e477cc75ec61a63e001cd7e6a58.png)

### Project 06: RGB LED

1.**Introduction**

![](./media/94bdff69e438989d8e0934e57f2e5c00.png)

RGB LEDS are made up of three colors (red, green, and blue) , which can emit different colors by mixing these three basic colors. In this project, we will introduce the RGB LED and show you how to use the Raspberry Pi Pico to control the RGB LED. Even though RGB LED is very basic, it is also a great way to learn the fundamentals of electronics and coding.

2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/b18fe281156b29c44796f72222718d58.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/f1a86fc81ab4b043263ce7e01e14d470.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>RGB LED*1</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/098a2730d0b0a2a4b2079e0fc87fd38b.png)</td>
<td>![Img](./media/e380dd26e4825be9a768973802a55fe6.png)</td>
<td>![Img](./media/c801a7baee258ff7f5f28ac6e9a7097b.png)</td>
<td></td>
</tr>
<tr class="even">
<td>220ΩResistor*3</td>
<td>Breadboard*1</td>
<td>Jumper Wires</td>
<td></td>
</tr>
</tbody>
</table>

3.**Component Knowledge**

The monitors mostly adopt the RGB color standard, and all the colors on the computer screen are composed of the three colors of red, green and blue mixed in different proportions.

![](./media/8bf1339719a922f2fbc1e01a4347b4ab.png)

This RGB LED has 4 pins and a common cathode. To change its brightness, we can use the PWM of the Raspberry Pi Pico pins, which can give different duty cycle signals to the RGB LED to produce different colors.

If we use three 10-bit PWM to control the RGBLED, theoretically we can create ![Img](./media/img-20231117083005.png) = 1,073,741,824(1 billion) colors through different combinations.

4.**Circuit Diagram and Wiring Diagram**

![](./media/f6950bc8498e6139cbb67db84cdd5a9a.png)

![](./media/fdab8c2fd2dfdd1670c09962e7b458ce.png)

**Note:**

RGB LED longest pin (common cathode) connected to GND.

![](./media/1584356c63bf99934ae0810ee02dced3.png)

How to identify the 220Ω 5-band resistor

![](./media/55c0199544e9819328f6d5778f10d7d0.png)

5.**Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 06：RGB LED”and double left-click the“Project\_06\_RGB\_LED.py”.

![](./media/fa2c2f91ec4700ce6c73e4acb045df45.png)

```Python
# import Pin, PWM and Random function modules.
from machine import Pin, PWM
from random import randint
import time

#configure ouput mode of GP18, GP17 and GP16 as PWM output and PWM frequency as 10000Hz.
pins = [18, 17, 16]
freq_num = 10000

pwm0 = PWM(Pin(pins[0]))  #set PWM
pwm1 = PWM(Pin(pins[1]))
pwm2 = PWM(Pin(pins[2]))
pwm0.freq(freq_num)
pwm1.freq(freq_num)
pwm2.freq(freq_num)

#define a function to set the color of RGBLED.
def setColor(r, g, b):
    pwm0.duty_u16(65535 - r)
    pwm1.duty_u16(65535 - g)
    pwm2.duty_u16(65535 - b)
    
try:
    while True:
        red   = randint(0, 65535) 
        green = randint(0, 65535)
        blue  = randint(0, 65535)
        setColor(red, green, blue)
        time.sleep_ms(200)
except:
    pwm0.deinit()
    pwm1.deinit()
    pwm2.deinit()
```

6.**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer, click ![](./media/ec00367ea605788eab454cd176b94c7b.png)“Stop/Restart backend”.

![](./media/c338d727e51749fcf4e331cc729207ae.png)

Click “![](./media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that RGB LED starts showing random colors. Press“Ctrl+C”or click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/b6f35a993624aa56b058ca411d43e096.png)

### Project 07: Flowing Water Light

**Project 07: Flowing Water Light**

1.**Introduction**

In our daily life, we can see many billboards made up of different colors of LED. They constantly change the light to attract the attention of customers. In this project, we will use Raspberry Pi Pico to control 10 LEDs to achieve the effect of flowing water.

2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/b18fe281156b29c44796f72222718d58.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/3ec5906fad2172708d449390140f55e6.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Red LED*10</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/098a2730d0b0a2a4b2079e0fc87fd38b.png)</td>
<td>![Img](./media/e380dd26e4825be9a768973802a55fe6.png)</td>
<td>![Img](./media/c801a7baee258ff7f5f28ac6e9a7097b.png)</td>
<td></td>
</tr>
<tr class="even">
<td>220ΩResistor*10</td>
<td>Breadboard*1</td>
<td>Jumper Wires</td>
<td></td>
</tr>
</tbody>
</table>

3.**Circuit Diagram and Wiring Diagram**

![](./media/e6f92039d131685369db2d1ac2c30267.png)

![](./media/fc6e73a6664012c9a33262b50d6e256f.png)

**Note:**

How to connect the LED

![](./media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω 5-band resistor

![](./media/55c0199544e9819328f6d5778f10d7d0.png)

4.**Test Code**

This project is to design and manufacture a flowing water light.Here are the steps: first , turn on LED \#1, then turn it off.Second, turn on LED \#2, then turn off... . Do the same for the 10 LEDs until the last one is turned off.  Repeating the process to achieve the "movement" of the water.

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→”Project 07：Flowing Water Light”and double-click“Project\_07\_Flowing\_Water\_Light.py”

![](./media/7b5bf98a689171d60a3601f16e0ad283.png)

```Python
from machine import Pin
import time

#Use an array to define 10 GPIO ports connected to LED Bar Graph for easier operation.
pins = [16, 17, 18, 19, 20, 21, 22, 26, 27, 28]
#Use two for loops to turn on LEDs separately from left to right and then back from right to left
def showLed():
    for pin in pins:
        print(pin)
        led = Pin(pin, Pin.OUT)
        led.value(1)
        time.sleep_ms(100)
        led.value(0)
        time.sleep_ms(100)        
    for pin in reversed(pins):
        print(pin)
        led = Pin(pin, Pin.OUT)
        led.value(1)
        time.sleep_ms(100)
        led.value(0)
        time.sleep_ms(100)
          
while True:
    showLed()
```

5.**Test Result：**

Connect the pico board to the Raspberry Pi. Click![](./media/32e03e9d4211e9ef97c1d2b18f05c902.png)to check the Shell.

![](./media/909f8976896d54a32d84d7ac1f0537c1.png)

Click ![](./media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that the 10 LEDs will light up like a flowing light. Click ![](./media/ec00367ea605788eab454cd176b94c7b.png)“Stop/Restart backend”to exit the program.

![](./media/723dd7931ac070cf30719700f47f6850.png)

![](./media/912e2c3f88b522b89b9935548bae3bd9.png)

### Project 08: 1-Digit Digital Tube

1.**Introduction**

The seven-segment digital tube is an electronic display device that displays decimal numbers. It is widely used in digital clocks,
electronic meters, basic calculators and other electronic devices that display digital information. The tubes are an alternative to more complex dot-matrix displays that are easy to use in both limited light conditions and strong sunlight. In this project, we will use the Raspberry Pi Pico to control 1-digit digital tube to display numbers.

2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/b18fe281156b29c44796f72222718d58.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/75e38d601750a4707369bc73d8028063.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>1-digit Digital Tube*1</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/098a2730d0b0a2a4b2079e0fc87fd38b.png)</td>
<td>![Img](./media/e380dd26e4825be9a768973802a55fe6.png)</td>
<td>![Img](./media/c801a7baee258ff7f5f28ac6e9a7097b.png)</td>
<td></td>
</tr>
<tr class="even">
<td>220ΩResistor*8</td>
<td>Breadboard*1</td>
<td><p>Breadboard</p>
<p>Wires</p></td>
<td></td>
</tr>
</tbody>
</table>

3.**Component Knowledge**

![](./media/e44a0f27beec739ee13e68c04865989f.png)

**Display principle:** The digital tube display is a semiconductor light-emitting device. Its basic unit is a light-emitting diode (LED).
The digital tube display can be divided into 7-segment digital tube and 8-segment digital tube according to the number of segments. The 8-segment digital tube has one more LED unit than the 7-segment digital tube (used for decimal point display). Each segment of the 7-segment LED display is a separate LED. According to the connection mode of the LED unit, the digital tube can be divided into a common anode digital tube and a common cathode digital tube.

In the common cathode 7-segment digital tube, all the cathodes (or negative electrodes) of the segmented LEDs are connected together, so you should connect the common cathode to GND. To light up a segmented LED, you can set its associated pin to “HIGH”.

In the common anode 7-segment digital tube, the LED anodes (positive electrodes) of all segments are connected together, so you should connect the common anode to “+5V”. To light up a segmented LED, you can set its associated pin to “LOW”.

![](./media/28fd057848fbe0e8c8e3362768e7aa44.png)

Each part of the digital tube is composed of an LED. So when you use it, you also need to use a current limiting resistor. Otherwise, the LED will be damaged. In this experiment, we use an ordinary common cathode one-bit digital tube. As we mentioned above, you should connect the common cathode to GND. To light up a segmented LED, you can set its associated pin to “HIGH”.

4.**Circuit Diagram and Wiring Diagram**

![](./media/84e67e0ce2d7627a96b83156324d92d5.png)

**Note:** The direction of the 7-segment digital tube inserted into the breadboard is the same as the wiring diagram, and there is one more point in the lower right corner.

![](./media/66da2f88234019c4a712494174ea4426.png)

![](./media/d99daa4165cf32b2283aae82466981bd.png)

5.**Test Code**

The digital display is divided into 7 segments, and the decimal point display is divided into 1 segment. When certain numbers are displayed, the corresponding segment will be illuminated. For example, when the number 1 is displayed, segments b and c will be opened.

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→”Project 08：1-Digit Digital Tube”and double-click “Project\_08\_One\_Digit\_Digital\_Tube.py”.

![](./media/bd6201a70a81db2c1ed338e6c901b0c0.png)

```Python
from machine import Pin
import time

a = machine.Pin(17, machine.Pin.OUT)
b = machine.Pin(16, machine.Pin.OUT)
c = machine.Pin(14, machine.Pin.OUT)
d = machine.Pin(13, machine.Pin.OUT)
e = machine.Pin(12, machine.Pin.OUT)
f = machine.Pin(18, machine.Pin.OUT)
g = machine.Pin(19, machine.Pin.OUT)
dp = machine.Pin(15, machine.Pin.OUT)

pins = [machine.Pin(id,machine.Pin.OUT) for id in [17, 16, 14, 13, 12, 18, 19, 15]]

def show(code):
    for i in range(0, 8):
        pins[i].value(~code & 1)
        code = code >> 1

#Select code from 0 to 9
mask_digits = [0xc0, 0xf9, 0xa4, 0xb0, 0x99, 0x92, 0x82, 0xf8,0x80, 0x90]
for code in reversed(mask_digits):
    show(code)
    time.sleep(1)
```

6.**Test Result：**

Connect the pico board to the Raspberry Pi. Click![](./media/32e03e9d4211e9ef97c1d2b18f05c902.png)to check the Shell

![](./media/e4500855559da9a38a02bfcb915f605d.png)

Click ![](./media/bb4d9305714a178069d277b20e0934b7.png) to run the code. Then we will see that the 1-digit digital tube will display numbers from 9 to 0; click![](./media/32e03e9d4211e9ef97c1d2b18f05c902.png)to exit the program.

![](./media/d43aa47d0a7ea776daa925653ea3511b.png)


### Project 09：4-Digit Digital Tube

1.**Introduction**
    
The 4-digit 7-segment digital tube is a very practical display device, and it is used for devices such as electronic clocks and score counters. Due to the low price and it is easy to use, more and more projects will use 4-digit 7-segment digital tubes. In this project, we will use the Raspberry Pi Pico to control a 4-bit 7-segment digital tube to create a manual counter.



2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/b18fe281156b29c44796f72222718d58.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/f65653a12f286475b4365035aa12c7c0.png)</td>
<td>![Img](./media/ece3c38dc9a9e6428b122481d6bb0d4d.png)</td>
<td></td>
</tr>
<tr class="even">
<td>4-Digit Digital Tube Module*1</td>
<td>M-F Dupont Wires</td>
<td></td>
</tr>
</tbody>
</table>

3.**Component Knowledge**

**TM1650 4-digit digital tube:** It is a 12-pin 4-digit tube display module with clock dots. The driver chip is TM1650 which only needs 2 signal lines to enable the microcontroller to control the 4-digit 8-segment digital tube. The control interface level can be 5V or 3.3V.

**Specifications of 4-bit digital tube module:**

Working voltage: DC 3.3V-5V

Maximum current: 100MA

Maximum power: 0.5W

**Schematic diagram of 4-digit digital tube module:**

![](./media/5f400887c90fc00098a3e77beca656ef.png)

4.**Circuit Diagram and Wiring Diagram**

![](./media/80f5738cf821288fff6ba0aba11fc453.png)

![](./media/39b708e69b2fb10057b71fe2321584b2.png)

5.**Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 09：4-Digit Digital Tube”. Select“TM1650\.py”，right-click and select“**Upload to /**”， and wait for“TM1650\.py to be uploaded to the Raspberry Pi Pico. And double-click the“Project\_09\_Four\_Digit\_Digital\_Tube.py”.

![](./media/b6b6e85a9064a5b0bfcc601a07d6fede.png)

![](./media/026f71bc46b2210cda1d47d540466428.png)

```Python
from machine import Pin, I2C
from TM1650 import TM1650
import time

# Define IIC interfaces and frequencies
i2c=I2C(0, scl=Pin(21),sda=Pin(20), freq=100000)

display = TM1650(i2c)

# Display the numbers 1111-9999 circulately
while True:
    display.display(1111)
    time.sleep(1)
    display.display(2222)
    time.sleep(1)
    display.display(3333)
    time.sleep(1)
    display.display(4444)
    time.sleep(1)
    display.display(5555)
    time.sleep(1)
    display.display(6666)
    time.sleep(1)
    display.display(7777)
    time.sleep(1)
    display.display(8888)
    time.sleep(1)
    display.display(9999)
    time.sleep(1)
```

6.**Test Result：**

Connect the pico board to the Raspberry Pi. Click ![](./media/32e03e9d4211e9ef97c1d2b18f05c902.png)to check the Shell

![](./media/775183cf9ecb501ac6775a88ecc57422.png)

Click “![](./media/bb4d9305714a178069d277b20e0934b7.png)”, the code starts executing, we will see that the 4-digit digital tube circularly displays numbers from 0000 to 9999.

Click“![](./media/ec00367ea605788eab454cd176b94c7b.png)”to exit the program.

![](./media/0795b62b6194c8296eb4a0b570083df3.png)


### Project 10：8×8 Dot-matrix Display

1.**Introduction**

The dot-matrix display is an electronic digital display device that can show information on machines, clocks and many other devices. In this project, we will use the Raspberry Pi Pico to control the 8x8 LED dot matrix to make a“❤”pattern.

2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/b18fe281156b29c44796f72222718d58.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/fa4eb4c55bbbb4ae7fcde8298a903b5a.png)</td>
<td>![Img](./media/b1991d0d88442db1d6b2f4189530397b.png)</td>
<td></td>
</tr>
<tr class="even">
<td>8*8 Dot-matrix Display *1</td>
<td>M-F Dupont Wires</td>
<td></td>
</tr>
</tbody>
</table>

3.**Component Knowledge**

**8\*8 Dot-matrix display module:**

The 8\*8 dot matrix is composed of 64 LEDs, and each LED is placed at the intersection of a row and a column. When using a single-chip microcomputer to drive an 8\*8 dot matrix, we need to use a total of 16 digital ports, which greatly wastes the data of the single-chip microcomputer. For this reason, we specially designed this module, using the HT16K33 chip to drive an 8\*8 dot matrix, and only need to use the I2C communication port of the single-chip microcomputer to control the dot matrix, which greatly saves the microcontroller resources.

**Specifications:**

Working voltage: DC 5V

Current: 200MA

Maximum power: 1W

**Schematic diagram:**

![](./media/b04fe5e60695365a23644395aaef5085.png)

Some modules have three DIP switches that you can flip at will. These switches are used to set the I2C communication address. The setting method is as follows. The module has fixed the communication address. A0, A1 and A2 are connected to GND, and the address is 0x70.  

![Img](./media/img-20231116152427.png)

4.**Circuit Diagram and Wiring Diagram**
    
![](./media/f4fc6111c35b571928d0f0a4a4bf45b3.png)
    
![](./media/ad529b82657cd9c7ddcd4b8828a0b1e8.png)
    
5.**Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 10：8×8 Dot-matrix Display”. Select“ht16k33\_matrix.py”and“matrix\_fonts.py”，right-click and select“**Upload to /**”and wait for “ht16k33\_matrix.py”and“matrix\_fonts.py”to be uploaded to the Raspberry Pi Pico. And double-click the“Project\_10\_8×8\_Dot\_Matrix\_Display.py”.

![](./media/ac77180c40e309315873031716174110.png)

![](./media/b52cec77d49dc2e88355e07e763e0163.png)

![](./media/ed3c85cbc2970294032ed044b333191a.png)

```Python
from machine import Pin,I2C
import time
import json
import matrix_fonts
from ht16k33_matrix import ht16k33_matrix
## Tool To Make Sprites https://gurgleapps.com/tools/matrix
#i2c config
clock_pin = 21
data_pin = 20
bus = 0
i2c_addr_left = 0x70
use_i2c = True

def scan_for_devices():
    i2c = machine.I2C(bus,sda=machine.Pin(data_pin),scl=machine.Pin(clock_pin))
    devices = i2c.scan()
    if devices:
        for d in devices:
            print(hex(d))
    else:
        print('no i2c devices')

if use_i2c:
    scan_for_devices()
    left_eye = ht16k33_matrix(data_pin, clock_pin, bus, i2c_addr_left)

def show_char(left):
    if use_i2c:
        left_eye.show_char(left)
        
def scroll_message(font,message='hello',delay=0.05): #Scrolling display
    left_message = '   ' + message
    right_message = message + '   '
    length=len(right_message)
    char_range=range(length-1)
    for char_pos in char_range:
      right_left_char=font[right_message[char_pos]]
      right_right_char=font[right_message[char_pos+1]]
      left_left_char=font[left_message[char_pos]]
      left_right_char=font[left_message[char_pos+1]]
      for shift in range(8):
        left_bytes=[0,0,0,0,0,0,0,0]
        right_bytes=[0,0,0,0,0,0,0,0]
        for col in range(8):
          left_bytes[col]=left_bytes[col]|left_left_char[col]<<shift
          left_bytes[col]=left_bytes[col]|left_right_char[col]>>8-shift;
          right_bytes[col]=right_bytes[col]|right_left_char[col]<<shift
          right_bytes[col]=right_bytes[col]|right_right_char[col]>>8-shift;
        if use_i2c:
                left_eye.show_char(left_bytes)
        time.sleep(delay)


while True:
    show_char(matrix_fonts.textFont1['A']) #Show the letter A
    time.sleep(1)
    show_char(matrix_fonts.textFont1['B'])
    time.sleep(1)
    show_char(matrix_fonts.textFont1['C'])
    time.sleep(1)
    scroll_message(matrix_fonts.textFont1, ' Hello World ')
```

6.**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer, click ![](./media/ec00367ea605788eab454cd176b94c7b.png)“Stop/Restart backend”.

![](./media/e322767bf299432a383821d873aa3d5b.png)

Click ![](./media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that the 8 x 8 dot matrix displays the character "A" 1S, "B" 1S, and "C" 1S. Then scroll to display the string "Hello World”repeatedly. Click![](./media/ec00367ea605788eab454cd176b94c7b.png)“Stop/Restart backend”to exit the program.

![](./media/85c98d8f0f151318b93e299bada82147.png)


### Project 11：74HC595N Control 8 LEDs 

1.**Introduction**
    
In previous projects, we have learned how to light an LED. However, how to light up a lot of LEDs with only 26 I/O ports on the Raspberry Pi Pico? Sometimes we may run out of pins , at that time, we need to extend it with the shift register. You can use a 74HC595N chip to control up to eight outputs at a time, using only a few pins on your microcontroller. In addition, You can also connect multiple registers together to further expand the output. In this project, we will use a Raspberry Pi Pico, a 74HC595 chip and LEDs to make a flowing water light to understand the function of the chip.  
    
2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/b18fe281156b29c44796f72222718d58.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/f97e58ab51ec0a274ff3e72e08a7d55d.png)</td>
<td>![Img](./media/3ec5906fad2172708d449390140f55e6.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>74HC595N Chip*1</td>
<td>Red LED*8</td>
</tr>
<tr class="odd">
<td>![Img](./media/098a2730d0b0a2a4b2079e0fc87fd38b.png)</td>
<td>![Img](./media/e380dd26e4825be9a768973802a55fe6.png)</td>
<td>![Img](./media/c801a7baee258ff7f5f28ac6e9a7097b.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>220ΩResistor*8</td>
<td>Breadboard*1</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.**Component Knowledge**
    
![](./media/6921c6d60135e072ed4bd24564ec4a6d.png)

**74HC595N Chip:** To put it simply, 74HC595N chip is a combination of 8-digit shifting register, memorizer and equipped with tri-state output. The shift register and the memorizer are synchronized to different clocks, and the data is input on the rising edge of the shift register clock SCK and goes into the memory register on the rising edge of the memory register clock RCK. If the two clocks are connected together, the shift register is always one pulse earlier than the storage register.

The shift register has a serial shift input (SI) and a serial output(SQH) for cascading. The 8-bit shift register can be reset
asynchronously (low-level reset), and the storage register has an 8-bit Three-state parallel bus output, when the output enable (OE) is enabled(active low), the storage register is output to the 74HC595N pin (bus).

![](./media/858b189f06ad68afe051b15043b2affd.png)

**Pins**：

<table>
<tbody>
<tr class="odd">
<td>Pin13 OE</td>
<td>It is an output enable pin to ensure that the data of the latch is input to the Q0 to Q7 pins or not. When it is low, no high level is output. In this experiment, we directly connect to GND and keep the data output low.</td>
</tr>
<tr class="even">
<td>Pin14 SI</td>
<td>This is the pin for 74HC595 to receive data, i.e. serial data input, only one bit can be input at a time, then 8 times in a row, it can form a byte.</td>
</tr>
<tr class="odd">
<td>Pin10 SCLR</td>
<td>A pin to initialize the storage register pins. It initializes the internal storage registers at a low level. In this experiment, we connect VCC to maintain a high level.</td>
</tr>
<tr class="even">
<td>Pin11 SCK</td>
<td>The clock pin of the shift register. At the rising edge, the data in the shift register is shifted backward as a whole, and new data input is received.</td>
</tr>
<tr class="odd">
<td>Pin12 RCK</td>
<td>The clock input pin of the storage register . At the rising edge, the data is transferred from the shift register to the storage register. At this time, the data is output in parallel from the Q0 to Q7 ports.</td>
</tr>
<tr class="even">
<td>Pin9 SQH</td>
<td>It is a serial output pin dedicated for chip cascading to the SI terminal of the next 74HC595.</td>
</tr>
<tr class="odd">
<td>Q0--Q7(Pin 15,Pin1-7)</td>
<td>Eight-bit parallel output, can directly control the 8 segments of the digital tube.</td>
</tr>
</tbody>
</table>

4.**Circuit Diagram and Wiring Diagram**

![](./media/1738cecf584c83b55370153ebc1688b7.png)

Note: Pay attention to the direction in which the 74HC595N chip is inserted.

![](./media/a6d03617539b70d6d69fa7e9acb25be9.png)

![](./media/91833532723f4ee623902c0252092741.png)

5.**Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 11：74HC595N Control 8 LEDs”. Select“my74HC595\.py”, right-click and select“**Upload to /**”，wait for“my74HC595\.py”to be uploaded to the Raspberry Pi Pico. And double-click the“Project\_11\_74HC595N\_Controls\_8\_LEDs.py”.

![](./media/2ac6ee416569798a1c50a9d0f3da0cb2.png)

![](./media/48a039f4961237761acbaa6cbbeacba7.png)

```Python
#Import time and my74HC595 modules.
from my74HC595 import Chip74HC595
import time

#Create a Chip74HC595 object and configure pins
chip = Chip74HC595(18, 20, 21)
#Chip74HC595() == Chip74HC595(18, 20, 21)

#The first for loop makes LED Bar display separately from left to right
#while the second for loop make it display separately from right to left.
while True:
    x = 0x01
    for count in range(8):
        chip.shiftOut(1, x)
        x = x<<1;
        time.sleep_ms(300)
    x = 0x01
    for count in range(8):
        chip.shiftOut(0, x)
        x = x<<1
        time.sleep_ms(300)
```

6.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/c1b73a6a1a33fc7af94b5487703125d7.png)

Click ![](./media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that the 8 LEDs start flashing in flowing water mode. Press“Ctrl+C”or click![](./media/ec00367ea605788eab454cd176b94c7b.png)“Stop/Restart backend”to exit the program.

![](./media/a8284225cd537ee03f3c8ae031f4213b.png)


### Project 12：Active Buzzer

1.**Introduction**

Active buzzer is a sound making element, which is widely used on computers, printers, alarms, electronic toys, telephones, timers, etc. It has an inner vibration source. In this project, we will use a Raspberry Pi Pico to control the active buzzer to buzz.

2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/b18fe281156b29c44796f72222718d58.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/4b4f653a76a82a3b413855493cc58fba.png)</td>
<td>![Img](./media/e380dd26e4825be9a768973802a55fe6.png)</td>
<td>![Img](./media/c801a7baee258ff7f5f28ac6e9a7097b.png)</td>
</tr>
<tr class="even">
<td>Active Buzzer*1</td>
<td>Breadboard*1</td>
<td>Jumper Wires</td>
</tr>
</tbody>
</table>


3.**Component Knowledge**

![image-20230525152733045](media/image-20230525152733045.png)

The active buzzer inside has a simple oscillator circuit , which can convert constant direct current into a certain frequency pulse signal. Once active buzzer receives a high level, it will sound. The passive buzzer is an integrated electronic buzzer with no internal vibration source. It must be driven by 2K to 5K square wave instead of a DC signal. The appearance of the two buzzers is very similar, but passive buzzers come with a green circuit board, and active buzzers come with a black tape. Passive buzzers don't have positive pole, but active buzzers have. As shown below:

![image-20230525152754153](media/image-20230525152754153.png)

**4. Circuit Diagram and Wiring Diagram**



![](./media/48e73ef2d6090fe7cda58c385bad2ab2.png)

![](./media/56df73f7ac711e510b30164c5759615f.png)

Note:

1\. The buzzer power supply in this circuit is 5V.  On a 3.3V power supply, the buzzer will work, but it will reduce the loudness.  

2\. The VUSB should connect to the positive terminal of the USB cable, if it connects to GND, it could burn out the computer or Raspberry Pi Pico.  Similarly, the Raspberry Pi Pico's 36-40 pins need to be connected carefully to avoid short circuits. 

3\. The positive terminal ("+"/long pin) of the active buzzer is connected to pin 16, and the negative terminal (short pin) is connected to GND.

**5. Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 12: Active Buzzer”. And double-click the Project\_12\_Active\_Buzzer.py”.

![](./media/ea2bb3dcb76907238d836020d837a605.png)

```Python
from machine import Pin
import time

buzzer = Pin(16, Pin.OUT)   # create buzzer object from Pin 16, Set Pin 16 to output

try:
    while True:
        buzzer.value(1)    # Set buzzer turn on
        time.sleep(0.5) # Sleep 0.5s
        buzzer.value(0)    # Set buzzer turn off
        time.sleep(0.5) # Sleep 0.5s
except:
    pass
```

6.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.
    
![](./media/8166e15e1eeff8fe85a176be7cd6c9c2.png)
    
Click ![](./media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that the the active buzzer starts to buzz. Click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.
    
![](./media/95dc4875728d03ac8c4c48b62afb48fa.png)


### Project 13：Passive Buzzer

**1. Introduction**

In a previous project, we have learned an active buzzer, which can only produce one sound and may let you feel monotonous. In this project, we will learn a passive buzzer and use the Raspberry Pi Pico to control the passive buzzer to sound an alarm. Unlike the active buzzer, the passive buzzer can emit sounds of different frequencies.

2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/b18fe281156b29c44796f72222718d58.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi PicoExpansion Board*1</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/d1ea1bb2b2749820cab389d5b85b838b.png)</td>
<td>![Img](./media/e380dd26e4825be9a768973802a55fe6.png)</td>
<td>![Img](./media/c801a7baee258ff7f5f28ac6e9a7097b.png)</td>
</tr>
<tr class="even">
<td>Passive Buzzer*1</td>
<td>Breadboard*1</td>
<td>Jumper Wires</td>
</tr>
</tbody>
</table>

**3.Component Knowledge**

![](./media/8d0020e53824072cbe9d4f7d2f8acb4f.png)

A passive buzzer is an integrated electronic buzzer with no internal vibration source. It must be driven by 2K to 5K square wave, not a DC signal. The two buzzers are very similar in appearance, but one buzzer with a green circuit board is a passive buzzer, while the other with black tape is an active buzzer. Passive buzzers cannot distinguish between positive polarity while active buzzers can.

![](./media/fc42c5ed014609ff0b290ee5361bb2fd.png)

**4. Circuit Diagram and Wiring Diagram**

![](./media/e0da1ccdbff24d256db130816c55da74.png)

![](./media/e601e48f8deddb3e9e7734d0022106b3.png)

5.**Test Code**
    
Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 13：Passive Buzzer”. And double left-click the“Project\_13\_Passive\_Buzzer.py”.

![](./media/0ae6aecf5d0df477745a223e743a1362.png)

```Python
from machine import Pin
import time

#Initialize the passive buzzer
buzzer = Pin(16,Pin.OUT)

#Simulate two different frequencies
while True:
    #Output 500HZ frequency sound
    for i in range(80):
        buzzer.value(1)
        time.sleep(0.001)
        buzzer.value(0)
        time.sleep(0.001)
    #Output 250HZ frequency sound
    for i in range(100):
        buzzer.value(1)
        time.sleep(0.002)
        buzzer.value(0)
        time.sleep(0.002)
```

6.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.
    
![](./media/768c2e41ce5b5cc212a79538d77fc815.png)
    
Click ![](./media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that the the passive buzzer sounds the alarm. Click ![](./media/ec00367ea605788eab454cd176b94c7b.png)“Stop/Restart backend”to exit the program.
    
![](./media/6d7aeb45a390b49d5852638137dff2b4.png)


### Project 14 : Mini Table Lamp

1.**Introduction**

Did you know that a Raspberry Pi Pico can light up an LED when you press a button? In this project, we will use the Raspberry Pi Pico, a key switch and an LED to make a Mini Table lamp.

2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/222aee34a428755aaf97b711ded3f09a.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/5b8fea4657b47510d199f740fdcaaa9d.png)</td>
<td>![Img](./media/ef77f5a64c382157fc2dea21ec373fef.png)</td>
<td>![Img](./media/da8a2a9d15baf7280966f3fdbb025a8c.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Button*1</td>
<td>Red LED*1</td>
<td>10KΩResistor*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/e380dd26e4825be9a768973802a55fe6.png)</td>
<td>![Img](./media/845d05a6108b1662b828610ba9dcb788.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
<td>![Img](./media/e9a8d050105397bb183512fb4ffdd2f6.png)</td>
<td>![Img](./media/9cab81f7da18c7b0c245ec2a2f614f3a.png)</td>
</tr>
<tr class="even">
<td>Breadboard*1</td>
<td>220ΩResistor*1</td>
<td>USB Cable*1</td>
<td><p>Jumper</p>
<p>Wires</p></td>
<td>Button Cap*1</td>
</tr>
</tbody>
</table>

3.**Component Knowledge**

![](./media/5b8fea4657b47510d199f740fdcaaa9d.png)

**Button:** The button can control the circuit on and off. The circuit is disconnected when the button is not pressed. But it breaks when you release it. Why does it only work when you press it? It starts from the internal structure of the button, which is shown in the figure:![](./media/d2a204e61c768f18924150db58aee093.png). Before the button is pressed, 1 and 2 are on, 3 and 4 are also on, but 1, 3 or 1, 4 or 2, 3 or 2, 4 are off(not working). Only when the button is pressed, 1, 3 or 1, 4 or 2, 3 or 2, 4 are on. The key switch is one of the most commonly used components in circuit design.

**Schematic diagram of the button:**

![](./media/5e42fde9876f9be810d85a7fb8b331f7.png)
![](./media/8677548f9e756281629430d66ba3a460.png)

**What is button jitter?**

We think of the switch circuit as "press the button and turn it on immediately", "press it again and turn it off immediately". In fact,
this is not the case.

The button usually uses a mechanical elastic switch, and the mechanical elastic switch will produce a series of jitter due to the elastic action at the moment when the mechanical contact is opened and closed (usually about 10ms). As a result, the button switch will not immediately and stably turn on the circuit when it is closed, and it will not be completely and instantaneously disconnected when it is turned off.

![](./media/7e7ac82db8bb810a7ee1de4181ceaa2d.jpeg)

**How to eliminate the jitter?**

There are two common methods, namely fix jitter in the software and hardware. We only discuss the jitter removal in the software.

We already know that the jitter time generated by elasticity is about 10ms, and the delay command can be used to delay the execution time of the command to achieve the effect of jitter removal.

Therefore, we delay 0.02s in the code to achieve the key anti-shake function.

![](./media/c0d68d1134b0b4097e8983ed2cac07fc.jpeg)

**4.** **Circuit Diagram and Wiring Diagram**

![](./media/0753a2a452e0292b31f79f9b6dabb0cc.png)

![](./media/a03a6553dc194ab61fb7b4d914740f90.png)

**Note:**

How to connect the LED

![](./media/f70404aa49540fd7aecae944c7c01f83.jpeg)

How to identify the 220Ω 5-band resistor and 10KΩ 5-band resistor

![](./media/55c0199544e9819328f6d5778f10d7d0.png)

![](./media/246cf3885dc837c458a28123885c9f7b.png)

**5.Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 14：Mini Table Lamp”. And double-click the “Project\_14\_Mini\_Table\_Lamp.py”.

![](./media/275a3c4efc6794dc8fac059a2aa7f9e1.png)

```Python
from machine import Pin
import time

led = Pin(19, Pin.OUT) # create LED object from Pin 19,Set Pin 19 to output                   
button = Pin(22, Pin.IN, Pin.PULL_UP) #Create button object from Pin22,Set GP22 to input

#Customize a function and name it reverseGPIO(),which reverses the output level of the LED
def reverseGPIO():
    if led.value():
        led.value(0)     #Set led turn off
    else:
        led.value(1)     #Set led turn on

try:
    while True:
        if not button.value():
            time.sleep_ms(20)
            if not button.value():
                reverseGPIO()
                while not button.value():
                    time.sleep_ms(20)
except:
    pass
```

6.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/a85c858067d3c56ab6f35bc4cc631e5d.png)

Click“![](./media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that press the button, the LED lights up;  when the button is released, the LED remains lit. Press the button again, the LED goes off;  When the button is released, the LED remains off. Doesn't it look like a little lamp? Click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/4228655348a81a57813174e42b167955.png)


### Project 15：Tilt And LED

1.**Introduction**

The ancients without electronic clocks, so the hourglass are invented to measure time.  The hourglass has a large capacity on both sides, and which is filled with fine sand on one side. What’s more, there is a small channel in the middle, which can make the hourglass stand upright , the side with fine sand is on the top. 

However, due to the action of gravity, the fine sand will flow down through the channel to the other side of the hourglass. When the sand reaches the bottom, turn it upside down and record the number of times it has gone through the hourglass, therefore, the next day we can know the approximate time of the day by it. In this project, we will use a Raspberry Pi Pico to control the tilt switch and LED lights to simulate an hourglass and make an electronic hourglass. 

2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/222aee34a428755aaf97b711ded3f09a.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/36f15610f430e5d5138f4e4fb721c40f.png)</td>
<td>![Img](./media/ef77f5a64c382157fc2dea21ec373fef.png)</td>
<td>![Img](./media/da8a2a9d15baf7280966f3fdbb025a8c.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Tilt Switch*1</td>
<td>Red LED*4</td>
<td>10KΩResistor*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/e380dd26e4825be9a768973802a55fe6.png)</td>
<td>![Img](./media/845d05a6108b1662b828610ba9dcb788.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
<td>![Img](./media/e9a8d050105397bb183512fb4ffdd2f6.png)</td>
<td></td>
</tr>
<tr class="even">
<td>Breadboard*1</td>
<td>220ΩResistor*4</td>
<td>USB Cable*1</td>
<td>Jumper Wires</td>
<td></td>
</tr>
</tbody>
</table>

3.**Component Knowledge**

![](./media/8c40739f8e05f753f145420b421a0f47.png)

Tilt switch is also called digital switch. Inside is a metal ball that can roll. The principle of rolling the metal ball to contact with the conductive plate at the bottom, which is used to control the on and off of the circuit. When it is a rolling ball tilt sensing switch with single directional trigger, the tilt sensor is tilted toward the trigger end (two gold-plated pin ends), the tilt switch is in a closed circuit and the voltage at the analog port is about 5V (binary number is 1023).

In this way, the LED will light up. When the tilt switch is in a horizontal position or tilted to the other end, it is open and the
voltage of the analog port is about 0V (binary number is 0), the LED will turn off. In the program, we judge the state of the switch based on whether the voltage value of the analog port is greater than 2.5V(binary number is 512).

As shown in the figure, use the internal structure of the tilt switch to illustrate how it works.

![](./media/bf8b10ad248ac939ac4ef96d02ed87c7.png)

4.**Circuit Diagram and Wiring Diagram**

![](./media/8735f9531646b77c35932404a681b76d.png)

![](./media/9127e65ff0d7b3d5e579263fd06ec674.png)

Note:

How to connect the LED

![](./media/f70404aa49540fd7aecae944c7c01f83.jpeg)

How to identify the 220Ω 5-band resistor and 10KΩ 5-band resistor

![](./media/55c0199544e9819328f6d5778f10d7d0.png)

![](./media/246cf3885dc837c458a28123885c9f7b.png)

5.**Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 15：Tilt And LED. And double-click the“Project\_15\_Tilt\_And\_LED.py”.

![](./media/330c9af9def412421038a3906b330043.png)

```Python
from machine import Pin
import time

led1 = Pin(19, Pin.OUT) # create LED object from Pin 19,Set Pin 19 to output
led2 = Pin(18, Pin.OUT) # create LED object from Pin 18,Set Pin 18 to output
led3 = Pin(17, Pin.OUT) # create LED object from Pin 17,Set Pin 17 to output
led4 = Pin(16, Pin.OUT) # create LED object from Pin 16,Set Pin 16 to output
Tilt_Sensor = Pin(22,Pin.IN) #Create tilt object from Pin22,Set GP22 to input

while True:
    if(Tilt_Sensor.value() == 0) : #when the value of tilt sensor is 0
        led1.value(1) # led1 turn on
        time.sleep_ms(200)#delay
        led2.value(1) # led2 turn on
        time.sleep_ms(200)#delay
        led3.value(1) # led3 turn on
        time.sleep_ms(200)#delay
        led4.value(1) # led4 turn on
        time.sleep_ms(200)#delay 
    else :           #when the value of tilt sensor is 1
        led4.value(0) # led4 turn off
        time.sleep_ms(200)#delay
        led3.value(0) # led3 turn off
        time.sleep_ms(200)#delay
        led2.value(0) # led2 turn off
        time.sleep_ms(200)#delay
        led1.value(0) # led1 turn off
        time.sleep_ms(200)#delay
```

6.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/5b7274a01646a14b7bf7b0cbdb6fe5d7.png)

Click“![](./media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that when you tilt the breadboard to an angle, the LEDs will light up one by one. When you turn the breadboard to the original angle, the LEDs will turn off one by one. Like the hourglass, the sand will leak out over time.

Click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/4dd22f89da91bfae3943271e9b7fc6f8.png)


### Project 16：Burglar Alarm

1.**Introduction**

PIR motion sensor measures the thermal infrared (IR) light emitted by moving objects. The sensor can detect the movement of people, animals, and cars to trigger safety alarms and lighting. They are used to detect movement and ideal for security such as burglar alarms and security lighting systems. In this project, we will use a Raspberry Pi Pico to control PIR motion sensor, buzzers and LEDs to simulate burglar alarms.


2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/b1265f71184b5d144248ea3e847a18c9.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/99272d75b3f952a0c2dd770e2f6f5a7c.png)</td>
<td>![Img](./media/4b4f653a76a82a3b413855493cc58fba.png)</td>
<td>![Img](./media/ef77f5a64c382157fc2dea21ec373fef.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>PIR Motion Sensor*1</td>
<td>Active Buzzer*1</td>
<td>Red LED*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/e380dd26e4825be9a768973802a55fe6.png)</td>
<td>![Img](./media/c80f7e0e045c10576b3120eea281502f.png)</td>
<td>![Img](./media/845d05a6108b1662b828610ba9dcb788.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
<td>![Img](./media/e9a8d050105397bb183512fb4ffdd2f6.png)</td>
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

3.**Component Knowledge**

**PIR motion sensor:** The principle is that when certain crystals, such as lithium tantalate and triglyceride sulfate, are heated, the two ends of the crystal will generate an equal number of charges with opposite signs. These charges can be converted into voltage output by an amplifier. And the human body will release infrared light, although relatively weak, but still can be detected. When the PIR motion sensor detects the movement of a nearby person, the sensor signal terminal outputs a high level 1. 

Otherwise, it outputs a low level 0. Pay special attention that this sensor can detect people, animals and cars in motion. People, animals and cars at rest cannot be detected. The maximum detection distance is about 7 meters.

**Note:** Since vulnerable to radio frequency radiation and temperature changes, the PIR motion sensor should be kept away from heat sources like radiators, heaters and air conditioners, as well as direct irradiation of sunlight, headlights and incandescent light.

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

![](./media/9e1ec604aa6f9d4a3c1fe41d4bccd699.png)

4.**Circuit Diagram and Wiring Diagram**

![](./media/8af6a40d69c138216548320abc46ed35.png)

![](./media/d028bb819eed7cf3a08af69a47ecfce6.png)

**5.Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→”Project 16：Burglar Alarm”. And double-click the“Project\_16\_Burglar\_Alarm.py”.

![](./media/ef69b0bc87b5396d733f1aa683e78e88.png)

```Python
from machine import Pin
import time

sensor_pir = machine.Pin(2, machine.Pin.IN)
led = machine.Pin(22, machine.Pin.OUT)
buzzer = machine.Pin(19, machine.Pin.OUT)

def pir_handler(pin): 
    print("ALARM! Motion detected!") 
    for i in range(50): 
        led.toggle() 
        buzzer.toggle() 
        time.sleep_ms(100)

sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)

while True: 
    led.toggle() 
    time.sleep(5)
```

6.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/a17b9a7d214b754cd44ef1d229c3dbcd.png)

Click “![](./media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that If the PIR motion sensor detects someone nearby, the buzzer will give an alarm and the LEDs will flash continuously. At the same time, the "Shell" window of the Thonny IDE will print the string "ALARM\! Motion detected\!" .

Click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/55455ba8a2c83481fc922dfcec868f3d.png)


### Project 17： I2C 128×32 LCD

1.**Introduction**
    
We can use modules such as monitors to do various experiments in life. You can also DIY a variety of small objects. For example, you can make a temperature meter with a temperature sensor and display, or make a distance meter with an ultrasonic module and display.
    
In this project, we will use the LCD\_128X32\_DOT module as a display and connect it to a Raspberry Pi Pico, which will be used to control the LCD\_128X32\_DOT display to show various English characters, common symbols and numbers.
    
2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/b1265f71184b5d144248ea3e847a18c9.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/2c2645e94a00867ac23e8a022f0a631a.png)</td>
<td>![Img](./media/bb8cfe198d6a21b2dcaa7965992c76c4.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>LCD_128X32_DOT*1</td>
<td>10CM M-F Dupont Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.**Component Knowledge**
    
![](./media/2c2645e94a00867ac23e8a022f0a631a.png)

**LCD\_128X32\_DOT:** It is an LCD module with 128\*32 pixels and its driver chip is ST7567A. The module uses the IIC communication mode, while the code contains a library of all alphabets and common symbols that can be called directly. When using, we can also set it in the code so that the English letters and symbols show different text sizes. To make it easy to set up the pattern display, we also provide a mold capture software that converts a specific pattern into control code and then copies it directly into the test code for use.

**Schematic diagram:**

![](./media/5451aed32bc5b7b30fbd5613ad09a65b.png)

**Features:**

Pixel：128\*32 character

Operating voltage(chip)：4.5V to 5.5V

Operating current：100mA (5.0V)

Optimal operating voltage(module):5.0V

4.**Circuit Diagram and Wiring Diagram**
    
Note: The LCD\_128X32\_DOT must be connected with 10CM M-F Dupont wires, which can make the LCD\_128X32\_DOT display normally. Otherwise, using 20CM M-F Dupont wires may cause the LCD\_128X32\_DOT display abnormally.  

![](./media/82aae0a70e5628c53d7f81f7730cf79a.png)

5.**Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 17： I2C 128×32 LCD”. Select “lcd128\_32.py”and“lcd128\_32\_fonts.py”，right-click and select“**Upload to /**”，wait for the“lcd128\_32.py”and the “lcd128\_32\_fonts.py”to be uploaded to the Raspberry Pi Pico. And double--click the“Project\_17\_I2C\_128\_32\_LCD.py”.

![](./media/cf6da403bb3a70da064a800abfcdf3e8.png)

![](./media/34cb4f230ecef649b2c7282576cff27c.png)

![](./media/d6d36ab4b42ff3bcf4b354c8adabf90e.png)

```Python
import machine
import time
import lcd128_32_fonts
from lcd128_32 import lcd128_32

#i2c config
clock_pin = 21
data_pin = 20
bus = 0
i2c_addr = 0x3f
use_i2c = True

def scan_for_devices():
    i2c = machine.I2C(bus,sda=machine.Pin(data_pin),scl=machine.Pin(clock_pin))
    devices = i2c.scan()
    if devices:
        for d in devices:
            print(hex(d))
    else:
        print('no i2c devices')
```

6.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/e47d31acdd5429afcd63acfb0fd0a039.png)

Click “![](./media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that the LCD module display will show "KEYESTUDIO" at the first line. "ABCDEFGHIJKLMNOPQR" will be displayed at the second line. "123456789 + - \* / \<\> = $ @ " will be shown at the third line and "% ^ & () {} :; '|?,. \~ \\\\ \[\] " will be displayed at the fourth line. 

Press“Ctrl+C”or click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/ffc4f1df389a52a9b016f4fae9a7b703.png)


### Project 18：Small Fan

1.**Introduction**

In the hot summer, we need an electric fan to cool us down, so in this project, we will use a Raspberry Pi Pico to control 130 motor module and small blade to make a small fan.

2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/b18fe281156b29c44796f72222718d58.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/a572bcde7a5e3bf01d273b3d9a024701.png)</td>
<td>![Img](./media/70ceedcda00dab3b484e5eddbd0382de.png)</td>
<td></td>
</tr>
<tr class="even">
<td>130 Motor Module*1</td>
<td>M-F Dupont Wires</td>
<td></td>
</tr>
</tbody>
</table>

3.**Component Knowledge**

![](./media/a572bcde7a5e3bf01d273b3d9a024701.png)

130 motor module: The motor control module uses the HR1124S motor control chip, which is a single-channel H-bridge driver chip for DC motor. The H-bridge driving part of the HR1124S features low on-resistance PMOS and NMOS power tube. The low on-resistance ensures low power loss of the chip, making the chip work safely for a longer time. In addition, HR1124S has low standby current and low quiescent current, which makes HR1124S easy to be used in toy scheme.

Features:

Working voltage: 5V

Working current: 200MA

Working power: 2W

Working temperature: -10℃\~ +50℃

**Schematic diagram:**

![](./media/ee2deb2ed7ae310b953ff178aff3d6c1.emf)

4.**Circuit Diagram and Wiring Diagram**

![](./media/98c9335e5ef2e5304e2cddde04e6e168.png)

![](./media/aad9f071a4d7a6a9a62c2899c78822b8.png)

5.**Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 18: Small Fan”. And double-click the“Project\_18\_ Small\_Fan.py”.

![](./media/3ae6011fd277fd283c51a2edc38f5af6.png)

```Python
from machine import Pin
import time

motor1a = Pin(17, Pin.OUT) # create motor1a object from Pin 17, Set Pin 17 to output
motor1b = Pin(16, Pin.OUT) # create motor1b object from Pin 16, Set Pin 16 to output

def forward():
    motor1a.high() # Set motor1a high
    motor1b.low() # Set motor1b low
def backward():
    motor1a.low()
    motor1b.high()
def stop():
    motor1a.low()
    motor1b.low()

def test():
    forward() # motor forward
    time.sleep(5) #delay
    stop() # motor stop
    time.sleep(2)
    backward()# motor backward 
    time.sleep(5)
    stop()
    time.sleep(2)
    
for i in range(5):
    test() 
```

6.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/b8719ff8af67a604c56bb0d2ca526d1b.png)

Click “![](./media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that The small fan turns counterclockwise for 5 seconds and stops for 2 seconds, and then turns clockwise for 5 seconds and stops for 2 seconds. Repeat this rule for 5 times and then the small fan stops. Click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/67a1f00e73daef1dc40651d871597b74.png)



### Project 19：Servo Sweep

1.**Introduction**

Servo is a kind of motor that can rotate very precisely. It has been widely used in toy cars, RC helicopters, airplanes, robots, etc. In this project, we will use a Raspberry Pi Pico to control the rotation of the servo.

2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/b18fe281156b29c44796f72222718d58.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/cd0bc424e9916881a1a903793821a042.png)</td>
<td>![Img](./media/c801a7baee258ff7f5f28ac6e9a7097b.png)</td>
<td></td>
</tr>
<tr class="even">
<td>Servo*1</td>
<td><p>Jumper</p>
<p>Wires</p></td>
<td></td>
</tr>
</tbody>
</table>

3.**Component Knowledge**

**Servo:**

![](./media/99830768916233a9c5900ac399006c17.png)

The servo is a kind of position servo driver, which is mainly composed of housing, circuit board, coreless motor, gear and position detector. The working principle is that the receiver or microcontroller sends a signal to the servo, which has an internal reference circuit that generates a reference signal with a period of 20ms and a width of 1.5ms, and compares the DC bias voltage with the voltage of the potentiometer to output voltage difference. 

The IC on the circuit board determines the direction of rotation, and then drives the coreless motor to start rotation and transmits the power to the swing arm through the reduction gear, while the position detector sends back a signal to determine whether it has reached the positioning. It is suitable for those control systems that require constant change of angle and can be maintained. When the motor rotates at a certain speed, the potentiometer is driven by the cascade reduction gear to rotate so that the voltage difference is 0 and the motor stops rotating. The angle range of general servo rotation is 0 to 180 degrees.

The pulse period for controlling the servo is 20ms, the pulse width is 0.5ms to 2.5ms, and the corresponding position is -90° to +90°. The following is an example of a 180 degree servo.

![](./media/708316fde05c62113a3024e0efb0c237.jpeg)

Servo motors have many specifications, but they all have three connecting wires, which are brown, red, and orange (different brands may have different colors). The brown is GND, the red is the positive power supply, and the orange is the signal line.

![](./media/3f5bc31305e64108bed3b3619d602891.jpeg)

4.**Wiring Diagram**
    
When supplying the servo, please note that the power supply voltage should be 3.3V-5V. Make sure there are no errors when connecting the servo to the power supply.

![](./media/64a80947d0cd45b50d4bd1d125509bbe.png)

**5.Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 19：Servo Sweep”. Select“myservo\.py”，right-click and select“**Upload to/**”, waiting for the“myservo\.py”to be uploaded to the Raspberry Pi Pico. And double-click the “Project\_19\_Servo\_Sweep.py”.

![](./media/19500404b4592580e637218a8302e048.png)

![](./media/b73dea82f7b22b16b1db0449e8383d10.png)

```Python
from myservo import Servo
import time

servo=Servo(16)
servo.ServoAngle(0)
time.sleep_ms(1000)

try:
    while True:       
        for i in range(0, 180, 1):
            servo.ServoAngle(i)
            time.sleep_ms(15)
        for i in range(180, 0, -1):
            servo.ServoAngle(i)
            time.sleep_ms(15)        
except:
    servo.deinit()
```

6.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/0ac752d69e93df3280606c598df08b5a.png)

Click ![](./media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that the servo will rotate from 0° to 180°, then reverse direction to rotate from 180° to 0°in a loop. Press“Ctrl+C”or click![](./media/ec00367ea605788eab454cd176b94c7b.png)“Stop/Restart backend”to exit the program.

![](./media/fa2eefbf0876ed0fe8010741e05b29a2.png)

![](./media/c5250405a4290ecb2d758ff1097310c7.png)


### Project 20：Stepping Motor

1.**Introduction**

Stepping motors are accurately positioned and are the most important components in industrial robots, 3D printers, large lathes, and other mechanical devices. In this project, we will use a Raspberry Pi Pico to control the ULN2003 stepper motor drive board to make the motors rotate.

2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/e4d763773ba5bc91a3df128e040f491e.jpeg)</td>
<td>![Img](./media/e0c3777cc7b4a2c6e400c07ef05c70dd.png)</td>
<td>![Img](./media/6c9c142fb9187aeb8337493ca5dd5ee7.jpeg)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>ULN2003 Stepper Motor Drive Board*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/8ebb14a35091dc8d02d95cb6748dd1e9.png)</td>
<td>![Img](./media/70ceedcda00dab3b484e5eddbd0382de.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>Stepper Motor *1</td>
<td>M-F Dupont Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.**Component Knowledge**
    
![](./media/8ebb14a35091dc8d02d95cb6748dd1e9.png)

**Stepper motor:** It is a motor controlled by a series of electromagnetic coils. It can rotate by the exact number of degrees (or steps) needed, allowing you to move it to a precise position and keep it there. It does this by supplying power to the coil inside the motor in a very short time, but you must always supply power to the motor to keep it in the position you want. There are two basic types of stepping motors, namely unipolar stepping motor and bipolar stepping motor. In this project, we use a 28-BYJ48 unipolar stepper motor.

![](./media/bea0e202b7bfe23d1fdcdbbe996aa6da.jpeg)

**Working Principle:**

The stepper motor is mainly composed of a stator and a rotor. The stator is fixed. As shown in the figure below, the part of the coil group A, B, C, and D will generate a magnetic field when the coil group is energized. The rotor is the rotating part. As follows, the middle part of the stator, two poles are permanent magnets.

![](./media/32748e0804b1fff434181cb228b23242.png)

Single -phase four beat: At the beginning, the coils of group A are turned on, and the poles of the rotor point at A coil. Next, the group A coil are disconnected, and the group B coils are turned on. The rotor will turn clockwise to the group B. Then, group B is disconnected, group C is turned on, and the rotor is turned to group C. After that, group C is disconnected, and group D is turned on, and the rotor is turned to group D. Finally, group D is disconnected, group A is turned on, and the rotor is turned to group A coils. Therefore, rotor turns 180° and continuously rotates B-C-D-A, which means it runs a circle (eight phase). As shown below, he rotation principle of stepper motor is A - B C - D - A.

You make order inverse(D - C - B - A - D .....) if you want to make stepper motor rotate anticlockwise.

![](./media/b8ae50bbdee2dd5bc683e8c450baee6a.png)

Half-phase and eight beat: 8 beat adopts single and dual beat way，A - AB B - BC - C - CD - D - DA - A ...... ，rotor will rotate half phase in this order. For example, when A coil is electrified，rotor faces to A coil , then A and B coil are connected, on this condition, the strongest magnetic field produced lies in the central part of AB coil, which means rotating half-phase clockwise.

**Stepper Motor Parameters:**

The rotor rotates one circle when the stepper motor we provide rotates 32 phases and with the output shaft driven by 1:64 reduction geared set. Therefore the rotation (a circle) of output shaft requires 32 \* 64 = 2048 phases.

The step angle of 4-beat mode of 5V and 4-phase stepper motor is 11.25. And the step angle of 8-beat mode is 5.625, the reduction ratio is 1:64.

**ULN2003Stepper Motor Drive Board:** It is a stepper motor driver, which converts the weak signal into a stronger control signal to drive the stepper motor. 

The following schematic diagram shows how to use the ULN2003 stepper motor driver board interface to connect a unipolar stepper motor to the pins of the Raspberry Pi Pico, and shows how to use four TIP120 interfaces.

![](./media/6fa632d2b70e97dd55565d23ec15d245.png)

4.**Schematic Diagram and Wiring Diagram:**
    
![](./media/ba02656bb1cb44ce8edb187a10dc7bef.png)

![](./media/6f72f7b5f6a520099d7714236372a9fe.png)

**5.Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→”Project 20：Stepping Motor”. And double-click the “Project\_20\_Stepping\_Motor.py”.

![](./media/c7c8462a4f2a88008201f51104f12ba5.png)

```Python
from machine import Pin
import time
 
# Pin initialization
in1 = Pin(21, Pin.OUT)
in2 = Pin(20, Pin.OUT)
in3 = Pin(19, Pin.OUT)
in4 = Pin(18, Pin.OUT)
 
# Delay time
delay = 1
 
# The number of steps required for the motor to rotate one revolution, (about 360°), with a slight deviation
ROUND_VALUE = 509
 
# The sequence value of the four-phase eight-beat stepper motor: A-AB-B-BC-C-CD-D-DA-A。
STEP_VALUE = [
    [1, 0, 0, 0],
    [1, 1, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 0, 0, 1],
    [1, 0, 0, 1],
]
 
# Pin output low level
def reset():
    in1(0)
    in2(0)
    in3(0)
    in4(0)
 
# If count is positive integers turn clockwise, if count is negative integers turn counterclockwise
def step_run(count):
    direction = 1     # turn clockwise
    if count < 0:
        direction = -1  # turn counterclockwise
        count = -count
    for x in range(count):
        for bit in STEP_VALUE[::direction]:
            in1(bit[0])
            in2(bit[1])
            in3(bit[2])
            in4(bit[3])
            time.sleep_ms(delay)
    reset()
 
# If a is positive integers turn clockwise, if a is negative integers turn counterclockwise
def step_angle(a):
    step_run(int(ROUND_VALUE * a / 360))
 
# Cycle: turn clockwise one circle, then counterclockwise one circle.
while True:
    step_run(509)
    step_run(-509)
    step_angle(360)
    step_angle(-360)
```

6.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/25f6339ca30f946b54fb1f6702f113f1.png)

Click“![](./media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that the four LEDS ( D1,D2,D3 ,D4) on the ULN2003 drive module will light up. The stepper motor rotates clockwise first, then counterclockwise, and keeps this state circulating.

Click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/7e557dab9aaafac28b4e91f5308b35ab.png)

![](./media/8dc4a0547390e0108c3960c31d330ee7.png)


### Project 21：Relay

1.**Introduction**
    
In daily life, we generally use AC to drive electrical equipment, and sometimes we use switches to control electrical appliances. If the switch is directly connected to the AC circuit, once electricity leakage occurs, people are in danger. From a safety point of view, we specially designed this relay module with NO (normally open) and NC (normally closed) terminals. In this lesson we will learn a special and easy-to-use switch, which is the relay module.
    
2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/5207588df3059cf385957664d41e9ac6.jpeg)</td>
<td>![Img](./media/bc08dc3772fc1fef6fa1e07bd81f6680.png)</td>
<td>![Img](./media/1ea87894c6aa8d475203e447ad5e930a.png)</td>
<td>![Img](./media/1fbdfe0569327d9a42600a54336bf7b5.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
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

3.**Component Knowledge**
    
**Relay:** It is an "automatic switch" that uses a small current to control the operation of a large current.
    
Input voltage：3.3V-5V
    
Rated load：5A 250VAC (NO/NC) 5A 24VDC (NO/NC)
    
The rated load means that devices with dc voltage of 24V or AC voltage of 250V can be controlled using 3.3V-5V microcontrollers.  
    
**Schematic diagram of the Relay:**

![](./media/be1c90d2b52fc2489590e3f702a087bf.emf)

4.**Wiring Diagram**

![](./media/bfe4e5e68d12e715c50f8aa5797a689c.png)

![](./media/0e76ea13b2034301be2ecdfde7f21f1e.png)

5.**Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 21：Relay”. And double-click the“Project\_21\_Relay.py”.

![](./media/57310f17327299cc49eeca50bcd8b7c1.png)

```Python
from machine import Pin
import time

# create relay from Pin 16, Set Pin 16 to output 
relay = Pin(16, Pin.OUT)
 
# The relay is opened, COM and NO are connected on the relay, and COM and NC are disconnected.
def relay_on():
    relay(1)
 
# The relay is closed, the COM and NO on the relay are disconnected, and the COM and NC are connected.
def relay_off():
    relay(0)
 
# Loop, the relay is on for one second and off for one second
while True:
    relay_on()
    time.sleep(1)
    relay_off()
    time.sleep(1)
```

6.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/d7abc767223f8f73b7d9996316439607.png)

Click“![](./media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that the relay will cycle on and off, on for 1 second, off for 1 second.  At the same time, you can hear the sound of the relay on and off, and you can also see the change of the indicator light on the relay. Press“![](./media/ec00367ea605788eab454cd176b94c7b.png)Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/61481c566efa37002db8b70970a81a5b.png)


### Project 22 : Dimming Light

1.**Introduction**

A potentiometer is a three-terminal resistor with a sliding or rotating contact that forms an adjustable voltage divider. It works by varying the position of a sliding contact across a uniform resistance. In a potentiometer, the entire input voltage is applied across the whole length of the resistor, and the output voltage is the voltage drop between the fixed and sliding contact.

In this project, we are going to learn how to use Raspberry Pi Pico to read the values of the potentiometer, and make a dimming lamp with LEDs.

2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/b1265f71184b5d144248ea3e847a18c9.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/03ab81e8b4f09287d2781ef0fd297f85.png)</td>
<td>![Img](./media/ef77f5a64c382157fc2dea21ec373fef.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Potentiometer*1</td>
<td>Red LED*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/e380dd26e4825be9a768973802a55fe6.png)</td>
<td>![Img](./media/845d05a6108b1662b828610ba9dcb788.png)</td>
<td>![Img](./media/e9a8d050105397bb183512fb4ffdd2f6.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>Breadboard*1</td>
<td>220ΩResistor*1</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.**Component Knowledge**
    
![](./media/03ab81e8b4f09287d2781ef0fd297f85.png)

**Adjustable potentiometer:** It is a kind of resistor and an analog electronic component, which has two states of 0 and 1(high level and low level). The analog quantity is different, its data state presents a linear state such as 1 \~ 1024.

4.**Read the Potentiometer Value**
    
We connect the adjustable potentiometer to the analog IO of the Raspberry Pi Pico to read its value and voltage value . Please refer to the following wiring diagram for wiring.

![](./media/b8ee6320bce8729a4309857f257d30ec.png)

![](./media/cb970a340d830569e9ac4462a1318e44.png)

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 22：Dimming Light”. And double-click the “Project\_22.1\_Read\_Potentiometer\_Analog\_Value.py”.

![](./media/a15ac026d4ffddcfa4092a73ec94db62.png)

```Python
from machine import ADC, Pin
import time
# Initialize the potentiometer to pin 26 (ADC function)
adc = ADC(26)

# Print the current adc value of the potentiometer cyclically 
# Print the current voltage value of the potentiometer cyclically
try:
    while True:
        adcValue = adc.read_u16() # read the ADC value of potentiometer
        voltage = adcValue / 65535.0 * 3.3
        print("ADC Value:", adcValue, "Voltage:", voltage, "V")
        time.sleep(0.1)
except:
    pass
```

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/24576fd319aa242673e032410c3a4274.png)

Click“![](./media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the ADC value and voltage value of the potentiomete, turn the potentiometer handle, the ADC value and voltage value will change. Click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/e48bc2d7a4b4c78f615a38b15b4028c2.png)

![](./media/969b9de3cf505f05d6a9361286cef9c9.png)

5.**Circuit Diagram and Wiring Diagram**

In the last step, we read the value of the potentiometer, and now we need to convert the value of the potentiometer into the brightness of the LED to make a lamp that can adjust the brightness. The wiring diagram is as follows:

![](./media/66f721b77035d40556c873e0c4577b4a.png)

![](./media/93b03f3cdc8af506d9035b748839ac33.png)

6.**Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 22：Dimming Light”. And double left-click the “Project\_22.2\_Dimming\_Light.py”.

![](./media/5721f7690258b3da3e3ca26f9b2a16af.png)

```Python
from machine import ADC, Pin, PWM
import time

adc = ADC(26) # Initialize the potentiometer to pin 26 (ADC function)
pwm = PWM(Pin(16)) # Initialize the led's PWM to pin 16
pwm.freq(1000) # Define the PWM frequency as 1000
try:
    while True:
        adcValue = adc.read_u16() # read the ADC value of potentiometer
        pwm.duty_u16(adcValue) #map it to the duty cycle of PWM to control led brightness 
        time.sleep(0.1)
except:
    pwm.deinit()
```

7.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/d335fc1670c6c486420472d4435092e8.png)

Click ![](./media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that turn the potentiometer handle and the brightness of the LED will change accordingly.

Click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/56349a69c557c5302c5d0721bfac0048.png)

![](./media/eca30dead3f4923afa0dcb0306db2319.jpeg)



### Project 23：Flame Alarm

1.**Introduction**
    
Fire is a terrible thing and fire alarm systems are very useful in houses, commercial buildings and factories. In this project, we will use a Raspberry Pi Pico to control a flame sensor , a buzzer and LEDs to make fire alarm devices, which is a meaningful maker activity.
    
2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/f70a6a892505b1816d151452b9b995a7.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/a50ec3e38adf10643eafac8cb62bec8a.png)</td>
<td>![Img](./media/ef77f5a64c382157fc2dea21ec373fef.png)</td>
<td>![Img](./media/4b4f653a76a82a3b413855493cc58fba.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Flame Sensor*1</td>
<td>Red LED*1</td>
<td>Active Buzzer*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/e380dd26e4825be9a768973802a55fe6.png)</td>
<td>![Img](./media/845d05a6108b1662b828610ba9dcb788.png)</td>
<td>![Img](./media/b395b1cd2678f87b3a34dec15659efbc.png)</td>
<td>![Img](./media/e9a8d050105397bb183512fb4ffdd2f6.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>Breadboard</td>
<td>220ΩResistor*1</td>
<td>10KΩResistor*1</td>
<td>Jumper Wires</td>
<td>USBCable*1</td>
</tr>
</tbody>
</table>

3.**Component Knowledge**
    
![](./media/a50ec3e38adf10643eafac8cb62bec8a.png)

**Flame Sensor**：The flame emits a certain degree of IR light, which is invisible to the human eye, but our flame sensor can detect it and alert the microcontroller. If the Raspberry Pi Pico has detected a fire, it has a specially designed infrared receiver to detect the flame, and then convert the flame brightness into a fluctuating level signal. The short pin of the receiving triode is negative pole and the other long pin is positive pole. We should connect the short pin (negative pole) to 5V and the long pin (positive pole) to the analog pin, a resistor and GND. As shown in the figure below.

![](./media/87bd204db523c602c80745266c1ee452.png)

Note: Since vulnerable to radio frequency radiation and temperature changes, the flame sensor should be kept away from heat sources like radiators, heaters and air conditioners, as well as direct irradiation of sunlight, headlights and incandescent light.

4.**Read the Simulation Value**

We start with a simple code to read the value of the flame sensor and print it on the serial monitor. For wiring, please refer to the
following wiring diagram.

![](./media/85531078db041bba05599b3a1118a7bc.png)

![](./media/1e3c424f7cc7ac797ab0b8ae4a00f4f1.png)

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 23：Flame Alarm. And double left-click the “Project\_23.1\_Read\_Analog\_Value\_Of\_Flame\_Sensor.py”.

![](./media/28dc15cd9bfe7a12b52940a8457e868e.png)

```Python
from machine import ADC, Pin
import time
# Initialize the flame sensor to pin 26 (ADC function)
adc = ADC(26)

# Read the current analog value of the flame sensor and return [0, 1023]
def get_value():
    return int(adc.read_u16() * 1024 / 65536)
 
# Print the current value of the flame sensor cyclically, value=[0, 1023]
while True:
    value = get_value()
    print(value)
    time.sleep(0.1)
```

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/c65e3ead39bbbf9254fe41ee174e34e8.png)

Click ![](./media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the simulation value read by the flame sensor. When the flame is close to the sensor, the simulation value increases. On the contrary, the simulated value decreases. Press“![](./media/ec00367ea605788eab454cd176b94c7b.png)Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/b8c396cf3296859e2027508e18505ce4.png)

![](./media/7c04b9dd8c4a10e7b9788ecd95eeeeaa.png)

5.**Circuit Diagram and Wiring Diagram**

Next, we will use flame sensor and buzzer, an RGB LED to make an interesting project, that is flame alarm. When flame is detected, RGB LED is red and buzzer alarms.

![](./media/c2b7feb8039e618ba070a9714ef06554.png)

![](./media/0cd1ee17a6f8de81464817090c5832eb.png)

6.**Test Code**
    
Note：![](./media/40a3ea572836945268b22dfc0cce29c3.png) The threshold of 500 in the code can be reset itself as required.

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 23：Flame Alarm”. And double left-click the “Project\_23.2\_Flame\_Alarm.py”.

![](./media/608f781d005a926db2382e4c748a1657.png)

```Python
from machine import ADC, Pin
import time

# Initialize the flame sensor to pin 26 (ADC function)
adc = ADC(26)
# create LED object from Pin 16,Set Pin 16 to output
led = Pin(16, Pin.OUT) 
# create buzzer object from Pin 17, Set Pin 17 to output
buzzer = Pin(17, Pin.OUT)   

# Read the current analog value of the flame sensor and return [0, 1023]
def get_value():
    return int(adc.read_u16() * 1024 / 65536)
 
# If the flame sensor detects a flame, the buzzer will beep
# and the LED will blink when the analog value is greater than 500
# Otherwise, the buzzer does not sound and the LED goes off 
while True:
    value = get_value()
    if value >500:
        buzzer.value(1)    # Set buzzer turn on
        led.value(1)    # Set led turn on
        time.sleep(0.5) # Sleep 0.5s
        led.value(0)    # Set led turn off
        time.sleep(0.5) # Sleep 0.5s
    else:
        buzzer.value(0)    # Set buzzer turn off
        led.value(0)    # Set led turn off
```

**7. Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/80f0b43ab61fa479b5b7762d114fcbb0.png)

Click“![](./media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that when the flame sensor detects the flame, the LED flashes and the buzzer alarms. Otherwise, the LED does not light, the buzzer does not sound. Click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/e8ff1eba81201d39a49e4f2828d57c10.png)


### Project 24：Night Lamp

1.**Introduction**

Sensors or components are ubiquitous in our daily life. For example, some public street lights turn on automatically at night and turn off automatically during the day. Why? In fact, this make use of a photosensitive element that senses the intensity of external ambient light. When the outdoor brightness decreases at night, the street lights will automatically turn on. In the daytime, the street lights will automatically turn off. The principle of this is very simple. In this lesson we will use Raspberry Pi Pico to control LEDs to implement the function of this street light.

2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/f70a6a892505b1816d151452b9b995a7.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/9e553e75b6f976f33438171eb2f2e775.png)</td>
<td>![Img](./media/ef77f5a64c382157fc2dea21ec373fef.png)</td>
<td>![Img](./media/b395b1cd2678f87b3a34dec15659efbc.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Photoresistor*1</td>
<td>Red LED*1</td>
<td>10KΩResistor*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/e380dd26e4825be9a768973802a55fe6.png)</td>
<td>![Img](./media/845d05a6108b1662b828610ba9dcb788.png)</td>
<td>![Img](./media/e9a8d050105397bb183512fb4ffdd2f6.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
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

3.**Component Knowledge**

![](./media/9e553e75b6f976f33438171eb2f2e775.png)

It is a photosensitive resistor, its principle is that the photoresistor surface receives brightness (light) to reduce the resistance. The resistance value will change with the detected intensity of the ambient light . With this property, we can use photoresistors to detect light intensity. Photoresistors and other electronic symbols are as follows:


![](./media/7d575da675a2f6cb511d28b801e2abaa.png)

The following circuit is used to detect changes in resistance values of photoresistors:

![](./media/5a7f7e641eb78007760a94151c1d80a5.png)

In the circuit above, when the resistance of the photoresistor changes due to the change of light intensity, the voltage between the photoresistor and resistance R2 will also change.  Thus, the intensity of light can be obtained by measuring this voltage.

4.**Read the Analog Value**

We first use a simple code to read the value of the photoresistor, print it in the serial monitor. For wiring, please refer to the following wiring diagram.

![](./media/e3fde13b200927346e04b032373ce638.png)

![](./media/b97ff27ae10e3499c36312c8ee4881f8.png)

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 24：Night Lamp”. And double left-click the “Project\_24.1\_Read\_Photosensitive\_Analog\_Value.py”.

![](./media/d97ee01c83aa9cd39da8fe42580614b5.png)

```Python
from machine import ADC, Pin
import time
# Initialize the photoresistance to pin 26 (ADC function)
adc = ADC(26)

# Read the current analog value of the photoresistance and return [0, 1023]
def get_value():
    return int(adc.read_u16() * 1024 / 65536)
 
# Print the current value of the photoresistance cyclically, value=[0, 1023]
while True:
    value = get_value()
    print(value)
    time.sleep(0.1)
```

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/96ed707533887ade4a65e0df7b460eae.png)

Click ![](./media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the analog value read by the photoresistor. When the light intensity around the photoresistor is gradually reduced, the analog value will gradually increase. On the contrary, the analog value decreases gradually. Click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/6df70dafea54c3d7a73e18c8e03f86d4.png)

![](./media/bbabb2d5c4a997c5024e6023cb272261.png)

5.**Circuit Diagram and Wiring Diagram**

We made a little dimmer in the front, now let's make a light controlled lamp. The principle is the same, the Raspberry Pi Pico will be used to obtain the analog value of the sensor and then adjust the brightness of the LED.  

![](./media/b8e8d95bdc869bf76465fa73645db831.png)

![](./media/71f2886dc6fa97d02e2ecd0d429af71b.png)

6.**Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 24：Night Lamp”. And double left-click the“Project\_24.2\_Night\_Lamp.py”.

![](./media/ae27830403a2f741aa9b725e5324c215.png)

![](./media/b636cdb16d60ae75729e44508e647044.png)

```Python
from machine import Pin, ADC, PWM
import time

adc = ADC(26) # Initialize the potentiometer to pin 26 (ADC function)
pwm = PWM(Pin(16)) # Initialize the led's PWM to pin 16
pwm.freq(10000) # Define the PWM frequency as 1000
try:
    while True:
        adcValue = adc.read_u16() # read the ADC value of photoresistance
        pwm.duty_u16(adcValue) # map ADC value to the duty cycle of PWM to control led brightness
        time.sleep(0.1) # delay
except:
    pwm.deinit()
```

7.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.
    
![](./media/8ee7742359fdbb9f8ea9d47aaccf4abd.png)
    
Click ![](./media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that when the intensity of light around the photoresistor is reduced, the LED will be bright, on the contraty, the LED will be dim. Click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/6b71892be4c0326147cf47bcbe84340a.png)


### Project 25：Human Induction Lamp

1.**Introduction**
    
With the development of science and technology, the use of human induction lamp that usually used in the dark corridor area is very common in our real life, such as the corridor of the community, the bedroom of the room, the garage of the dungeon, the bathroom and so on. The human induction lamp are generally composed of a PIR Motion Sensor, a lamp, a photoresistor sensor and so on. In this project, we will learn how to use a PIR Motion Sensor, LEDs, and a photoresistor to make a human induction lamp .
    
2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/f70a6a892505b1816d151452b9b995a7.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/82b6a0e286b6ca25c06c6353397bad79.png)</td>
<td>![Img](./media/7eb361d680dfa351f07f8527aeb37abd.png)</td>
<td>![Img](./media/img-20231116163617.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Photoresistor*1</td>
<td>Red LED*1</td>
<td>10KΩResistor*1</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/e380dd26e4825be9a768973802a55fe6.png)</td>
<td>![Img](./media/99272d75b3f952a0c2dd770e2f6f5a7c.png)</td>
<td>![Img](./media/img-20231116163652.png)</td>
<td>![Img](./media/c80f7e0e045c10576b3120eea281502f.png)</td>
<td>![Img](./media/e9a8d050105397bb183512fb4ffdd2f6.png)</td>
<td></td>
</tr>
<tr class="even">
<td>Breadboard*1</td>
<td>PIR Motion Sensor*1</td>
<td>220ΩResistor*1</td>
<td>F-F Dupont Wires</td>
<td>Jumper Wires</td>
<td></td>
</tr>
</tbody>
</table>

3.**Circuit Diagram and Wiring Diagram**
    
![](./media/79c069794eed2b3eb611f4aee7952862.png)
    
![](./media/643c9552a922ed3ddde80be42481481d.png)

4.**Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 25：Human Induction Lamp”. And double left-click the “Project\_25\_Human\_ Induction\_Lamp.py”.

![](./media/f0b469934c60f65bb9c4f318551fd03b.png)

```Python
from machine import Pin, ADC
import time
 
# Human infrared sensor pin
human = Pin(2, Pin.IN)
 
# Initialize the photosensitive sensor pin to GP26 (ADC function)
light = ADC(26)
#create the External LED object from Pin 16, Set Pin 16 to output 
led1 = Pin(16, Pin.OUT)
#create the built-in LED on the Pico board from Pin 25, Set Pin 25 to output 
led2 = Pin(25, Pin.OUT) 
 
# Turn off the External LED
def led1_off():
    led1.value(0)
 
# Turn on the External LED
def led1_on():
    led1.value(1)
    
# Open the built-in LED on the Pico board
def led2_on():
    led2.value(1)
 
# Close the built-in LED on the Pico board
def led2_off():
    led2.value(0)
 
# Read the current analog value of the photosensitive sensor, range [0, 1023]
# The stronger the light intensity, the smaller the value.
def get_value():
    return int(light.read_u16() * 1024 / 65536)
 
 
def detect_someone():
    if human.value() == 1:
        return True
    return False
 
abc = 0
 
while True:
    val = get_value()
#     print('val=', val)
 
    if val >= 500:
        led2_on()
        if detect_someone() == True:
            abc += 1
            led1_on()
            print("value=", abc)
            time.sleep(1)
        else:
            if abc != 0:
                abc = 0
                led1_off()
    else:
        led2_off()
        led1_off()
 
    time.sleep(0.1)
```

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/99cc13c8fe7576e631c0cf9147a324a7.png)

Click ![](./media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that When your hand covers the light-sensitive part of the photoresistor to simulate darkness, the Raspberry Pi Pico's built-in LED will light up. Then shake it in front of the PIR motion sensor with your other hand, the external LED will light up, too, and after a delay of a few seconds, the external LED will automatically turn off.  

At the same time, the "Shell" window of Thonny IDE will print the delay time when the external LED lights up . If the sensitive part of the photoresistor is not covered, you can see that the the Raspberry Pi Pico's built-in LED lights go out , at this time, shake in front of the PIR motion sensor with your hand, the external LED is off.

Click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/1e713643e34dad2e48541a9ec20afbb9.png)

![](./media/af94ad9d2f008956592ee64e207aa8b5.png)


### Project 26：Sound Control Fan

1.**Introduction**

The sound sensor has a built-in capacitive electret microphone and power amplifier. It can be used to detect the sound intensity of the environment. In this project, we use a Raspberry Pi Pico to control a sound sensor and a motor module to make a voice-activated fan.

2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/8eeca2083cc744159c642a792b53eba2.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/2ea1614210807e59a5bc7223a6fa960b.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Sound Sensor*1</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/6f668af8a0ecdffb5e0b64b21c0fd392.png)</td>
<td>![Img](./media/2f77153d70a7cea1d49a75550e38eacf.png)</td>
<td>![Img](./media/1fbdfe0569327d9a42600a54336bf7b5.png)</td>
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

3.**Component Knowledge**

**Sound sensor** is usually used to detect the loudness of the sound in the surroundings. Arduino can collect its output signal through the analog input interface. The S pin is an analog output, which is the real-time output of the microphone voltage signal. The sensor comes with a potentiometer so you can adjust the signal strength. It also has two fixing holes so that the sensor can be installed on any other equipment. You can use it to make some interactive works, such as voice-operated switches.

4.**Read the Analog Value of the Sound Sensor**

We first use a simple code to read the analog value of the sound sensor and print it to the serial monitor, please refer to the following wiring diagram for the wiring.

![](./media/7bcfe48423953695c677c0c504d8f745.png)

![](./media/547329f9d46a7267798728d385b60912.png)

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 26：Sound Control Fan”. And double left-click the “Project\_26.1\_Read\_Sound\_Sensor\_Analog\_Value.py”.

![](./media/27eac64857f25c481f3dd5d6df9b18c7.png)

```Python
from machine import ADC, Pin
import time
# Initialize the sound sensor to pin 28 (ADC function)
adc = ADC(28)

# Read the current analog value of the sound sensor and return [0, 1023]
def get_value():
    return int(adc.read_u16() * 1024 / 65536)
 
# Print the current value of the sound sensor cyclically, value=[0, 1023]
while True:
    value = get_value()
    print(value)
    time.sleep(0.1)
```

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/1be0ecb86d1263ba7693b7058376b7ab.png)

Click “![](./media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the analog values read by the sound sensor. When you clap your hands to the sensor, the analog value of the sound sensor will change significantly. Click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/27e036453fd9c7f22800cb540f4c500b.png)

![](./media/ebe92f3cc97f7d21b92d498c9f04f625.png)

5.**Wiring Diagram**

Next, we use a sound sensor, a 130 motor module and a fan leaf to make a voice-activated fan. The wiring diagram is as follows.

![](./media/631b461716fe53a2c1138f561acae5f7.png)

![](./media/340c224f0f71765f71d17afc623d595d.png)

6.**Test Code**（Note：![](./media/c20911df19d11290cf099072fe250029.png)The threshold 600 in the code can be reset itself as needed)

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 26：Sound Control Fan”. And double left-click the “Project\_26.2\_Sound\_Control\_Fan.py”.

![](./media/e78dce78ed1df268479f97584ccbcd8d.png)

```Python
from machine import ADC, Pin
import time
 
# Onboard LED light initialization
led = Pin(25, Pin.OUT)
 
# Initialize the Sound sensor to pin 28 (ADC function)
adc = ADC(28)
 
# Pin initialization
motor1a = Pin(17, Pin.OUT) 
motor1b = Pin(16, Pin.OUT) 

# Read the current analog value of the Sound sensor and return [0, 1023]
def get_value():
    return int(adc.read_u16() * 1024 / 65536)
 
# If the Sound sensor detects Sounds, the built-in LED on the Pico board will blink
# and the motor will rotate when the analog value is greater than 600
# Otherwise, the motor does not rotate and the LED goes off    
while True:
    value = get_value()
    if value >600:
        led.value(1)    # Set led turn on 
        motor1a.high()  # Set motor1a high
        motor1b.low()   # Set motor1b low
        time.sleep(5)   # delay time 
    else:
        motor1a.low()  # Set motor1a low
        motor1b.low()  # Set motor1b low 
        led.value(0)    # Set led turn off
```

7.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/cf0f619d87a3dd56bd74304634468227.png)

Click ![](./media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that clap your hands to the sound sensor, and when the sound intensity exceeds a threshold, the small fan spins while
the Raspberry Pi Pico's built-in LED lights up.  Instead, the small fan doesn't rotate, and the Raspberry Pi Pico's built-in LEDS don't light up. Press“Ctrl+C”or click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/9080ca52a8f37114bae5edc03c23d6ae.png)


### Project 27：Temperature Measurement

1.**Introduction**

LM35 is a commonly used and easy-to-use temperature sensor. It does not require other hardware, only needs an analog port. The difficulty lies in compiling the code and converting the analog values to Celsius temperature. In this project, we use a temperature sensor and 3 LEDs to make a temperature tester. When the temperature sensor touches objects with different temperature, the LEDs will show different colors.

2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/74a834bb65d3f86d643648f2fa26430f.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/0fded1cfe95575d0fa4aa03839d8e30d.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
<td>![Img](./media/img-20231116163917.png)</td>
<td>![Img](./media/e9a8d050105397bb183512fb4ffdd2f6.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>LM35Temperature Sensor*1</td>
<td>USB Cable*1</td>
<td>Breadboard*1</td>
<td>Jumper Wires</td>
</tr>
<tr class="odd">
<td>![Img](./media/098a2730d0b0a2a4b2079e0fc87fd38b.png)</td>
<td>![Img](./media/afa6edd3ff90b027a6f43995a6fb15a2.png)</td>
<td>![Img](./media/0c1b0f91b4e56bcbc235d06b48809ac9.png)</td>
<td>![Img](./media/6c688493b558ed5f3e90e7dab38cbd93.png)</td>
<td>![Img](./media/2f77153d70a7cea1d49a75550e38eacf.png)</td>
<td></td>
</tr>
<tr class="even">
<td>220Ω Resistor*3</td>
<td>Red LED*1</td>
<td>Yellow LED*1</td>
<td>Green LED*1</td>
<td>F-F Dupont Wires</td>
<td></td>
</tr>
</tbody>
</table>

3.**Component Knowledge**

![](./media/0fded1cfe95575d0fa4aa03839d8e30d.png)

**Working principle of LM35 temperature sensor:** LM35 is a widely used temperature sensor with many different package types. At room temperature, it can achieve the accuracy of 1/4°C without additional calibration processing. LM35 temperature sensor can produce different voltage by different temperature. When the temperature is 0 ℃, it outputs 0V. If increasing 1 ℃, the output voltage will increase 10mv. The output temperature is 0℃ to 100℃, the conversion formula is as follows.

![](./media/0dfa07fa69f2a98658a3822c2da93bf7.jpeg)

4.**Read the Temperature Value**

We first use a simple code to read the value of the temperature sensor, print it in the serial monitor. The wiring diagram is shown below.

![](./media/952016b1b69fcad9f4eea889de63106a.png)

![](./media/2c05b1929588977832c955526f519e89.png)

LM35 output is given to analog pin GP26 of the Raspberry Pi Pico. This analog voltage is converted to its digital form and processed to get the temperature reading.

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 27：Temperature Measurement”. And double left-click the “Project\_27.1\_Read\_LM35\_Temperature\_Value.py”.

![](./media/9be9a19832db166fbcb2a8618a813cfc.png)

```Python
from machine import ADC, Pin
import time

# Initialize the Sound sensor to pin 26 (ADC function)
# Select ADC input 0 (GPIO26)
sensor_temp = ADC(26)
conversion_factor = 3.3 / (65535)

while True:
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = reading * 102.4 
    print(temperature)
    time.sleep(1)
```

**5. Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend.

![](./media/8381fdb5db551ce91677b1ada5e05140.png)

Click“![](./media/da852227207616ccd9aff28f19e02690.png)Run current script”, the code starts executing, we will see that The "Shell" window of Thonny IDE will print the temperature values read by the LM35 temperature sensor. Hold the LM35 element by hand, the temperature value read by the LM35 temperature sensor will change. Press“Ctrl+C”or click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](./media/16fe92748af1c5cc9dafdb2f2c2b8a84.png)

![](./media/9c2c52dbee8a37315075178f167ba342.png)

**6. Circuit Diagram and Wiring Diagram**

Now we use a LM35 temperature sensor and three LED lights to do a temperature test. When the LM35 temperature sensor senses different temperatures, different LED lights will light up. Follow the diagram below for wiring.

![](./media/65b5f44e3a73ff102a40f6c90bdf6d4c.png)

![](./media/fa3eddc7bda77c7c8420d0f3a0b0d2eb.png)

**7. Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 27：Temperature Measurement”. And double left-click
the “Project\_27.2\_Temperature\_Measurement.py”.

Note: The temperature threshold in the code can be reset itself as required.  

![](./media/3c045c0f5b0f63d0948bcc7ab5699321.png)

```Python
from machine import ADC, Pin
import time

# Initialize the Sound sensor to pin 26 (ADC function)
# Select ADC input 0 (GPIO26)
sensor_temp = ADC(26)
conversion_factor = 3.3 / (65535)

# create red led object from Pin 19, Set Pin 19 to output
led_red = machine.Pin(19, machine.Pin.OUT)  
# create yellow led object from Pin 21, Set Pin 21 to output
led_yellow = machine.Pin(21, machine.Pin.OUT)
# create green led object from Pin 22, Set Pin 22 to output
led_green = machine.Pin(22, machine.Pin.OUT) 

while True:
    reading = sensor_temp.read_u16() * conversion_factor 
    temperature = reading * 102.4
    print(temperature)
    time.sleep(0.2)
    if temperature <28:
        led_red.value(1)  # Set red led turn on
        led_yellow.value(0) # Set yellow led turn off 
        led_green.value(0)  # Set green led turn off
    elif temperature >28 and temperature <31:
        led_red.value(0)  # Set red led turn off
        led_yellow.value(1) # Set yellow led turn on 
        led_green.value(0)  # Set green led turn off
    else:
        led_red.value(0)  # Set red led turn off
        led_yellow.value(0) # Set yellow led turn off 
        led_green.value(1)  # Set green led turn on
```

7.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](./media/8a55812323a1c8158bdb60e4bd496b28.png)

Click ![](./media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the temperature values read by the LM35 temperature sensor. When the LM35 temperature sensor senses different temperatures, different LEDS will light up. Press“Ctrl+C”or click![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to exit the program.

![](./media/20daf7e277e6321706feec4119ab7f2c.png)


### Project 28：Rocker control light

1.**Introduction**

The joystick module is a component with two analog inputs and one digital input. It is widely used in game operation, robot control, drone control and other fields.

In this project, we will use a Raspberry Pi Pico and a joystick module to control RGB. You can have a deeper understanding of the principle and operation of the joystick module in practice.

2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/b18fe281156b29c44796f72222718d58.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/d087b123748cbfb8ed9f517150db71c5.png)</td>
<td>![Img](./media/f1aed48e2c02214415853ad2358f3744.png)</td>
<td>![Img](./media/img-20231116164058.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td><blockquote>
<p>Raspberry Pi Pico Expansion Board*1</p>
</blockquote></td>
<td>Joystick Module*1</td>
<td>M-F Dupont Wires</td>
<td>Breadboard*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/af749ecbde89c728a8c63e6527781cac.png)</td>
<td>![Img](./media/098a2730d0b0a2a4b2079e0fc87fd38b.png)</td>
<td>![Img](./media/c801a7baee258ff7f5f28ac6e9a7097b.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
<td></td>
</tr>
<tr class="even">
<td>RGB LED*1</td>
<td>220ΩResistor*3</td>
<td>Jumper Wires</td>
<td>USB Cable*1</td>
<td></td>
</tr>
</tbody>
</table>

3.**Component Knowledge**

![](./media/d087b123748cbfb8ed9f517150db71c5.png)

**Joystick module**: It mainly uses PS2 joystick components. In fact, the joystick module has 3 signal terminal pins, which simulate a three-dimensional space. The pins of the joystick module are GND, VCC, and signal terminals (B, X, Y). The signal terminals X and Y simulate the X-axis and Y-axis of the space. When controlling, the X and Y signal terminals of the module are connected to the analog port of the microcontroller. The signal terminal B simulates the Z axis of the space, it is generally connected to the digital port and used as a button.

VCC is connected to the microcontroller power output VCC (3.3V or 5V), GND is connected to the microcontroller GND, the voltage in the original state is about 1.65V or 2.5V. In the X-axis direction, when moving in the direction of the arrow, the voltage value increases, and the maximum voltage can be reached. Moving in the opposite direction of the arrow, the voltage value gradually decreases to the minimum voltage. In the Y-axis direction, the voltage value decreases gradually as it moves in the direction of the arrow on the module, decreasing to the minimum voltage. 

As the arrow is moved in the opposite direction, the voltage value increases and can reach the maximum voltage. In the Z-axis
direction, the signal terminal B is connected to the digital port and outputs 0 in the original state and outputs 1 when pressed. In this way, we can read the two analog values and the high and low level conditions of the digital port to determine the operating status of the joystick on the module.

**Features:**

Input Voltage：DC 3.3V \~ 5V

Output Signal：X/Y dual axis analog value +Z axis digital signal

[Range](javascript:;) [of](javascript:;) [Application](javascript:;)：Suitable for control point coordinate movement in plane as well as control of two degrees of freedom steering gear, etc.  

[Product](javascript:;) [feature](javascript:;)s：Exquisite appearance, joystick feel superior, simple operation, sensitive response, long service life.  

4.**Read the Value**

We have to use analog Raspberry Pi Pico pin IO to read the data from X or Y pins, and use digital IO port to read the values of the button. Please follow the wiring diagram below for wiring.

![](./media/36004a41553a2f413ba05775e9b696eb.png)

![](./media/b843cdff62b3ccf3f3f028a834b468aa.png)

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 28：Rocker control light”. And double left-click the “Project\_28.1\_Read\_Rocker\_Value.py”.

![](./media/8a76bb8e2c4b5e146f39241dc0c2d64a.png)

```Python
from machine import Pin, ADC
import time
# Initialize the joystick module (ADC function)
rocker_x = ADC(27)
rocker_y = ADC(26)
button = Pin(28, Pin.IN, Pin.PULL_UP)
 
# Read the value of the X axis and return [0, 1023]
def read_x():
    value = int(rocker_x.read_u16() * 1024 / 65536)
    return value
 
# Read the value of Y axis and return [0, 1023]
def read_y():
    value = int(rocker_y.read_u16() * 1024 / 65536)
    return value
 
# Read the state of the button, press to return to True, release to return to False
def btn_state():
    press = False
    if button.value() == 0:
        press = True
    return press
 
# Print the current value of the X axis,Y axis,Z axis cyclically.
while True:
    value_x = read_x()
    value_y = read_y()
    state = btn_state()
    print("x:%d, y:%d, press:%s" % (value_x, value_y, state))
    time.sleep(0.1)
```

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/e42d431beb8c38c1d9edfc8dd4835497.png)

Click ![](./media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the analog and digital values of the current joystick. Moving the joystick or pressing it will change the analog and digital values in "Shell". Click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/6310b5d15613eca68f193ff996e0fc48.png)

![](./media/c8097bd115d4c564192c19a08df2702a.jpeg)

![](./media/20904cf7c75d3dd861da3b3575670a0e.png)

5.**Circuit Diagram and Wiring Diagram**

We just read the value of the joystick module. Now we need to do something with the joystick module and RGB, connecting according to the following diagram.

![](./media/000ec2c5dae0b0d5368569abbd026f35.png)

![](./media/68601044f75ee6840f0b97cad9bea891.png)

6.**Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 28：Rocker control light”. And double left-click the “Project\_28.2\_Rocker\_Control\_Light.py”.

![](./media/a8d0765b4b6499868b8c135962e70fda.png)

```Python
from machine import Pin, PWM
import time
#Set RGB light interface and frequency
rgb_r = PWM(Pin(18))
rgb_g = PWM(Pin(17))
rgb_b = PWM(Pin(16))
rgb_b.freq(1000)
rgb_r.freq(1000)
rgb_g.freq(1000)
#Set rocker pin
rocker_y = machine.ADC(26)
rocker_x = machine.ADC(27)
y=500
x=500
while True:
    y = rocker_y.read_u16()#Get Y value of rocker
    x = rocker_x.read_u16()#Get X value of rocker
    if x < 6400:    #left
        rgb_b.duty_u16(0)
        rgb_r.duty_u16(65535)
        rgb_g.duty_u16(0)
    elif x > 38400:    #right
        rgb_b.duty_u16(0)
        rgb_r.duty_u16(0)
        rgb_g.duty_u16(65535)
    elif y < 6400:    #down
        rgb_b.duty_u16(65535)
        rgb_r.duty_u16(0)
        rgb_g.duty_u16(0)
    elif y > 38400:    #up
        rgb_b.duty_u16(65535)
        rgb_r.duty_u16(65535)
        rgb_g.duty_u16(65535)
    time.sleep(0.01)
```

7.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/4bce4d98a3b7e171a0e93b5b27c18be6.png)

Click ![](./media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that①If the joystick is moved to the far left in the X direction, the RGB light turns red. ② If the joystick is moved to the far right in the X direction, the RGB light turns green. ③If the joystick is moved to the top in the Y direction, the RGB light turns white. ④If the joystick is moved to the bottom in the Y direction, the RGB light turns blue. Press“Ctrl+C”or click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/67825ce03c80a9d2111608b8676181a4.png)

![](./media/9c2d0d8777200827b16c49b752d45c4c.jpeg)


### Project 29：Temperature and Humidity Meter 

1.**Introduction**

In winter, the humidity in the air is very low, that is, the air is very dry. Coupled with the cold, the human skin is prone to crack from excessive dryness. Therefore, you need to use a humidifier to increase the humidity of the air at home. But how do you know that the air is too dry? Then you need equipment to detect air humidity. In this lesson, we will learn how to use the temperature and humidity sensor. We use the sensor to create a thermohygrometer and also combined with an LCD\_128X32\_DOT to display the temperature and humidity values.

2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/b1265f71184b5d144248ea3e847a18c9.jpeg)</td>
<td>![Img](./media/34bafe8113e2db36c8f0c8492b835474.png)</td>
<td>![Img](./media/9232141f8a3166a8a6cdd43b78edd4e3.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Temperature and Humidity Sensor*1</td>
<td>LCD 128X32 DOT*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/f1aed48e2c02214415853ad2358f3744.png)</td>
<td>![Img](./media/f1aed48e2c02214415853ad2358f3744.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>20CM M-F Dupont Wires</td>
<td>10CM M-F Dupont Wires</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.**Component Knowledge**

![](./media/34bafe8113e2db36c8f0c8492b835474.png)

**Temperature and Humidity Sensor:** It is a temperature and humidity composite sensor with calibrated digital signal output. Its accuracy humidity is ±5%RH, temperature is ±2℃. Range humidity is 20 to 90%RH, and temperature is 0 to 50℃. The temperature and humidity sensor applies dedicated digital module acquisition technology and temperature and humidity sensing technology to ensure extremely high reliability and excellent long-term stability of the product. 

It includes a resistive-type humidity measurement and an NTC temperature measurement component, which is very suitable for
temperature and humidity measurement applications where accuracy and real-time performance are not required.The operating voltage is in the range of 3.3V to 5.5V.

XHT11 has three pins, which are VCC, GND, and S. S is the pin for data output, using serial communication.

**Single bus format definition:**

<table>
<tbody>
<tr class="odd">
<td><strong>Description</strong></td>
<td><strong>Definition</strong></td>
</tr>
<tr class="even">
<td>Start signal</td>
<td>Microprocessor pulls data bus (SDA) down at least 18ms for a period of time(Maximum is 30ms), notifying the sensor to prepare data.</td>
</tr>
<tr class="odd">
<td>Response signal</td>
<td>The sensor pulls the data bus (SDA) low for 83µs, and then pulls up for 87µs to respond to the host's start signal.</td>
</tr>
<tr class="even">
<td>Humidity</td>
<td>The high humidity is an integer part of the humidity data, and the low humidity is a fractional part of the humidity data.</td>
</tr>
<tr class="odd">
<td>Temperature</td>
<td>The high temperature is the integer part of the temperature data, the low temperature is the fractional part of the temperature data. And the low temperature Bit8 is 1, indicating a negative temperature, otherwise, it is a positive temperature.</td>
</tr>
<tr class="even">
<td>Parity bit</td>
<td>Parity bit=Humidity high bit+ Humidity low bit+temperature high bit+temperature low bit</td>
</tr>
</tbody>
</table>

**Data sequence diagram:**

When MCU sends a start signal, XHT11 changes from the low-power-consumption mode to the high-speed mode, waiting for MCU completing the start signal. Once it is completed, XHT11 sends a response signal of 40-bit data and triggers a signal acquisition. The signal is sent as shown in the figure.

![](./media/933ac5e5a5e921d4b16c7c48091ba75a.png)

Combined with the code, you can understand better.

The XHT11 temperature and humidity sensor can easily add temperature and humidity data to your DIY electronic projects. It is perfect for remote weather stations, home environmental control systems, and farm or garden monitoring systems.

**Specification:**

Working voltage: +5V

Temperature range: 0°C to 50°C, error of ± 2°C

Humidity range: 20% to 90% RH,± 5% RH error

Digital interface

**Schematic diagram:**

![](./media/53fa034cbbcec22579b2bdf8252c90cd.emf)

4.**Read the Value**

![](./media/c3b585b4747d3ba04be7af544bbbe27c.png)

![](./media/751a9a67b2657cac8dfaddf451e7b74a.png)

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 29：Temperature Humidity Meter”. Select“dht11\.py”,  right-click and select“**Upload to /**”，waiting for the “dht11\.py”to be uploaded to the Raspberry Pi Pico. And double left-click the“Project\_29.1\_Detect\_Temperature\_Humidity.py”.

![](./media/c2d8ca3682cb897d2aa15b04f50cdc45.png)

![](./media/c29c0e0af79a671d39ffdb24c0f36d23.png)

```Python
from machine import Pin
import time
import dht11

temperature = 0
humidity = 0
#Initialize temperature and humidity pins and library
dht = dht11.DHT11(22)
time.sleep(0.5)

while True:
    if dht.measure() == 0:
        print("DHT11 data error!")
        break
    time.sleep(1)
    temperature = dht.temperature()
    humidity = dht.humidity()
    print("temperature: %dC  humidity: %d"%(temperature, humidity) + "%")
```

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/92a50d0579b5d50ea659a6b8930da44a.png)Stop/Restart backend”.

![](./media/243f41963cd6da4339b772684900e8da.png)

Click ![](./media/03500869d5be2aa603b774b1f01a4af1.png)“Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the temperature and humidity data in the current surroundings, as shown in the following figure. Click“![](./media/92a50d0579b5d50ea659a6b8930da44a.png)Stop/Restart backend”to exit the program.

![](./media/639dff079a7290d05b8bcb775e237723.png)

![](./media/af350892cefaa74dae1740153a0c1626.png)

5.**Circuit Diagram and Wiring Diagram**

Now we start printing the value of the XHT11 temperature and humidity sensor with LCD screen. We will see the corresponding values on the LCD screen. Let's get started with this project. Please follow the wiring diagram below.

Note: LCD\_128X32\_DOT must be connected with 10CM M-F Dupont wires, the LCD\_128X32\_DOT will display normally;  Otherwise, using a 20CM M-F Dupont wire may cause the LCD\_128X32\_DOT display abnormally.  

![](./media/d78889590f1945eec0125ee7dc250d73.png)

![](./media/78cb8eb87aa36af901a7a839fbf7eb10.png)

6.**Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 29：Temperature Humidity Meter”. Select“dht11\.py”,“lcd128\_32.py”and “lcd128\_32\_fonts.py”，right-click and select“**Upload to /**”，waiting for the “dht11\.py”，“lcd128\_32.py”and“lcd128\_32\_fonts.py”to be uploaded to the Raspberry Pi Pico. And double left-click the“Project\_29.2\_Temperature\_Humidity\_Meter.py”.

![](./media/4c3c3bab0ea827089355b1412d9ce699.png)

![](./media/ce783ae8700ca7d2b3240f8574cb9c72.png)

![](./media/b17870d95491e8ec75e9757b7596acf7.png)

![](./media/6257809b84210220e9d431b819105832.png)

```Python
from machine import Pin, I2C
import time
import lcd128_32_fonts
from lcd128_32 import lcd128_32
import dht11

temp = 0
humi = 0
#Initialize temperature and humidity pins and library
dht = dht11.DHT11(22)
time.sleep(0.5)
#i2c config
clock_pin = 21
data_pin = 20
bus = 0
i2c_addr = 0x3f
use_i2c = True

def scan_for_devices():
    i2c = machine.I2C(bus,sda=machine.Pin(data_pin),scl=machine.Pin(clock_pin))
    devices = i2c.scan()
    if devices:
        for d in devices:
            print(hex(d))
    else:
        print('no i2c devices')

try:
    while True:
        if dht.measure() == 0:
            print("DHT11 data error")
            break
        temp = int(dht.temperature())
        humi = int(dht.humidity())

        if use_i2c:
            scan_for_devices()
            lcd = lcd128_32(data_pin, clock_pin, bus, i2c_addr)
            
        lcd.Clear()
        lcd.Cursor(0, 0)
        lcd.Display("temper:")
        lcd.Cursor(0, 8)
        lcd.Display(str(temp))
        lcd.Cursor(0, 11)
        lcd.Display("C")
        lcd.Cursor(2, 0)
        lcd.Display("Humid:")
        lcd.Cursor(2, 7)
        lcd.Display(str(humi))
        lcd.Cursor(2, 10)
        lcd.Display("%")
        time.sleep(1)
except:
    pass
```

7.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/92a50d0579b5d50ea659a6b8930da44a.png)Stop/Restart backend”.
    
![](./media/120f207ec952db8d3b0e37fadc58b95e.png)
    
Click ![](./media/03500869d5be2aa603b774b1f01a4af1.png)“Run current script”, the code starts executing, we will see that the LCD\_128X32\_DOT will display temperature and humidity in the current environment. Press“Ctrl+C”or click“![](./media/92a50d0579b5d50ea659a6b8930da44a.png)Stop/Restart backend”to exit the program.

![](./media/0be8cbc9c3da870f87555497a5d6f64b.png)



### Project 30：Ultrasonic Ranger

**1. Introduction**

The HC-SR04 ultrasonic sensor is a very affordable distance sensor, mainly used for obstacle avoidance in various robotic projects. It is also used for water level sensing and even as a parking sensor. We treat the ultrasonic sensors as bat's eyes. In the dark, bats can still identify objects in front of them and directions through ultrasound. In this project, we will use a Raspberry Pi Pico to control the ultrasonic sensor and an LED analog ultrasonic ranger.  

**2. Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/ea74681ffd2116a2434692d34c25e829.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/85df6831220dec7d43a68bfc9b7382cb.png)</td>
<td>![Img](./media/7eb361d680dfa351f07f8527aeb37abd.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Ultrasonic Sensor*1</td>
<td>Red LED*4</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/1fbdfe0569327d9a42600a54336bf7b5.png)</td>
<td>![Img](./media/098a2730d0b0a2a4b2079e0fc87fd38b.png)</td>
<td>![Img](./media/e9a8d050105397bb183512fb4ffdd2f6.png)</td>
<td>![Img](./media/e380dd26e4825be9a768973802a55fe6.png)</td>
<td></td>
</tr>
<tr class="even">
<td>M-F Dupont Wires</td>
<td>220ΩResistor*4</td>
<td>Jumper Wires</td>
<td>Breadboard*1</td>
<td></td>
</tr>
</tbody>
</table>

**3. Component Knowledge**

**HC-SR04 Ultrasonic Sensor:** Like bats, sonar is used to determine the distance to an object. It provides accurate non-contact range detection, high-precision and stable readings. Its operation is not affected by sunlight or black materials, just like a precision camera (acoustically softer materials like cloth are difficult to detect). It has an ultrasonic transmitter and receiver.

![](./media/e6f6037071e434febf7090b56ac35802.png)

In front of the ultrasonic sensor are two metal cylinders, these are the converters. The converters convert the mechanical energy into an electrical signal. In the ultrasonic sensor, there are transmitting converters and receiving converters. The transmitting converter converts the electric signal into an ultrasonic pulse, and the receiving converter converts the reflected ultrasonic pulse back to an electric signal.

If you look at the back of the ultrasonic sensor, you will see an IC behind the transmitting converter, which controls the transmitting converter. There is also an IC behind the receiving converter, which is a quad operational amplifier that amplifies the signal generated by the receiving converter into a signal large enough to be transmitted to the Raspberry Pi Pico.

**Sequence diagrams:**

The figure shows the sequence diagram of the HC-SR04. To start the measurement, the Trig of SR04 must receive at least 10us high pulse(5V), which will activate the sensor to emit 8 cycles of 40kHz ultrasonic pulses, and wait for the reflected ultrasonic pulses. When the sensor detects ultrasound from the receiver, it sets the Echo pin to high (5V) and delays it by one cycle (width), proportional to the distance. To get the distance, measure the width of the Echo pin.

![](./media/4114885ac4b6214953e3224d8c1d52c4.png)

Time = Echo pulse width, its unit is “us” (microseconds)

Distance in centimeters = time / 58

Distance in inches = time / 148

4.**Read the Distance Value**
    
We will start with a simple ultrasonic distance measurement and print the measured distance on the serial monitor.
    
![](./media/db430baa07e2e4d9ac9efca1950b953a.jpeg)
    
The HC-SR04 ultrasonic sensor has four pins, they are Vcc, Trig, Echo and GND. The Vcc pin provides the power source for generating ultrasonic pulses and is connected to Vcc (+5V). The GND pin is grounded. The Trig pin is where the Arduino sends a signal to start the ultrasonic pulse. The Echo pin is where the ultrasonic sensor sends information about the duration of the ultrasonic pulse to the Plus control board. Wiring as shown below.
    
![](./media/2e5a5d288a21bc75933876f223a278e4.png)
    
![](./media/92213eb45109991180d9eeadbba009b1.png)

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 30：Ultrasonic Ranger”. And double left-click the“Project 30.1\_Ultrasonic\_Ranging.py”.

![](./media/a75c7f3680cd7389a63575772fd7c0df.png)

```Python
from machine import Pin
import time

#Define the control pins of the ultrasonic ranging module. 
Trig = Pin(27, Pin.OUT, 0)
Echo = Pin(26, Pin.IN, 0)

distance = 0 # Define the initial distance to be 0.
soundVelocity = 340 #Set the speed of sound.

# The getDistance() function is used to drive the ultrasonic module to measure distance,
# the Trig pin keeps at high level for 10us to start the ultrasonic module.
# Echo.value() is used to read the status of ultrasonic module’s Echo pin,
# and then use timestamp function of the time module to calculate the duration of Echo
# pin’s high level,calculate the measured distance based on time and return the value.
def getDistance():
    Trig.value(1)
    time.sleep_us(10)
    Trig.value(0)
    while not Echo.value():
        pass
    pingStart = time.ticks_us()
    while Echo.value():
        pass
    pingStop = time.ticks_us()
    distanceTime = time.ticks_diff(pingStop, pingStart) // 2
    distance = int(soundVelocity * distanceTime // 10000)
    return distance

# Delay for 2 seconds and wait for the ultrasonic module to stabilize,
# Print data obtained from ultrasonic module every 500 milliseconds. 
time.sleep(2)
while True:
    time.sleep_ms(500)
    distance = getDistance()
    print("Distance: ", distance, "cm")
```

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/83c7d02ecca7f023bc81f2b0c3ea72ee.png)

Click“![](./media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the distance value between the ultrasonic sensor and the object. Press“Ctrl+C”or click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/902f8522d5c8ada95737a616730e4fe4.png)

![](./media/ce873cf513307a15f9aa58078c8dd7d6.png)

5.**Circuit Diagram and Wiring Diagram**
    
Next, we will make a simple ultrasonic ranger using a Raspberry Pi Pico to control an ultrasonic sensor and 4 LED lights. Connect the wires as shown below.

![](./media/fde13d356d164fa9bf4e2f01253a3523.png)

![](./media/1d9e98a0287beea858503dacd289a809.png)

6.**Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 30：Ultrasonic Ranger”. And double left-click the“Project\_30.2\_Ultrasonic\_Ranger.py”.

![](./media/79996541604e3b51fb85ac82739e1305.png)

```Python
from machine import Pin
import time

#Define the pins of four leds.
led1 = Pin(16, Pin.OUT)
led2 = Pin(17, Pin.OUT)
led3 = Pin(18, Pin.OUT)
led4 = Pin(19, Pin.OUT)

#Define the control pins of the ultrasonic ranging module. 
Trig = Pin(27, Pin.OUT, 0)
Echo = Pin(26, Pin.IN, 0)

distance = 0 # Define the initial distance to be 0.
soundVelocity = 340 #Set the speed of sound.

# The getDistance() function is used to drive the ultrasonic module to measure distance,
# the Trig pin keeps at high level for 10us to start the ultrasonic module.
# Echo.value() is used to read the status of ultrasonic module’s Echo pin,
# and then use timestamp function of the time module to calculate the duration of Echo
# pin’s high level,calculate the measured distance based on time and return the value.
def getDistance():
    Trig.value(1)
    time.sleep_us(10)
    Trig.value(0)
    while not Echo.value():
        pass
    pingStart = time.ticks_us()
    while Echo.value():
        pass
    pingStop = time.ticks_us()
    distanceTime = time.ticks_diff(pingStop, pingStart) // 2
    distance = int(soundVelocity * distanceTime // 10000)
    return distance

# Delay for 2 seconds and wait for the ultrasonic module to stabilize,
# Print data obtained from ultrasonic module every 500 milliseconds. 
time.sleep(2)
while True:
    time.sleep_ms(500)
    distance = getDistance()
    print("Distance: ", distance, "cm")
    if distance <= 5:
       led1.value(1)
    else:
       led1.value(0)
    if distance <= 10:
       led2.value(1)
    else:
       led2.value(0)
    if distance <= 15:
       led3.value(1)
    else:
       led3.value(0)
    if distance <= 20:
       led4.value(1)
    else:
       led4.value(0)
```

7.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.
    
![](./media/2ead14b66cb346f7de86141ffb9ef80f.png)
    
Click ![](./media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the distance between the ultrasonic sensor and the object, and the corresponding LED will light up when we move our hand in front of the ultrasonic sensor. Press“![](./media/ec00367ea605788eab454cd176b94c7b.png)Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/e77a016d25df567933b91c5fe30eb8d6.png)


### Project 31：Temperature Instrument

1.**Introduction**
    
Thermistor is a kind of resistor whose resistance depends on temperature changes, which is widely used in gardening, home alarm system and other devices. Therefore, we can use this feature to make a temperature instrument.
    
2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/8f45d8141f23885af95f870ab64a859c.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/b45bb81bb3763377c63accce606ac5f2.png)</td>
<td>![Img](./media/b395b1cd2678f87b3a34dec15659efbc.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Thermistor*1</td>
<td>10KΩResistor*1</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/74ca4fa6d49dbd04de6a603c6e55a9ee.png)</td>
<td>![Img](./media/e380dd26e4825be9a768973802a55fe6.png)</td>
<td>![Img](./media/9232141f8a3166a8a6cdd43b78edd4e3.png)</td>
<td>![Img](./media/e9a8d050105397bb183512fb4ffdd2f6.png)</td>
<td></td>
</tr>
<tr class="even">
<td>10CM M-F Dupont Wires</td>
<td>Breadboard*1</td>
<td>LCD 128X32 DOT*1</td>
<td>Jumper Wires</td>
<td></td>
</tr>
</tbody>
</table>

3.**Component Knowledge**
    
Thermistor: A thermistor is a temperature sensitive resistor. When it senses a change in temperature, the thermistor's resistance changes. We can use this feature to detect temperature intensity with thermistor. Thermistors and its electronic symbols are shown below:

![](./media/809b8634747fb295021f12e3b92b7894.png)

The relation between thermistor resistance and temperature is:

**in the formula:**

Rt is the resistance of the thermistor at T2 temperature.

R is the nominal resistance value of the thermistor at T1 room temperature.

EXP\[n\] is the nth power of e.

B is the temperature index

T1 and T2 refer to K degrees, that is, Kelvin temperature. Kelvin temperature =273.15 + Celsius temperature. For thermistor parameters, we use : B=3950, R=10KΩ，T1=25℃.The circuit connection method of thermistor is similar to that the photoresistor, as shown below :

![](./media/ac0d68aac58bffa5c99e1d0ed3a8bc37.jpeg)

We can use the value measured by the ADC converter to get the resistance value of the thermistor, and then use the formula to get the temperature value. Therefore, the temperature formula can be deduced as:

4.**Read the Values**
    
First we will learn the thermistor to read the current ADC value, voltage value and temperature value and print them out . Please connect the wires according to the following wiring diagram.

![](./media/c143dc239ceaa5e65a63f47d6512630c.png)

![](./media/c0ad763fa1dda5ce55d03fe9b3d61bcd.png)

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 31: Temperature Instrument”. And double left-click the “Project\_31.1\_Read\_the\_thermistor\_analog\_value.py”.

![](./media/dfba50f255a7ff5b0bd327fa210cf6b2.png)

```Python
from machine import Pin, ADC
import time
import math

#Set ADC
adc=ADC(27)

try:
    while True:
        adcValue = adc.read_u16()
        voltage = adcValue / 65535.0 * 3.3
        Rt = 10 * voltage / (3.3-voltage)
        tempK = (1 / (1 / (273.15+25) + (math.log(Rt/10)) / 3950))
        tempC = int(tempK - 273.15)
        print("ADC value:", adcValue, "  Voltage: %0.2f"%voltage + "V",
              "  Temperature: " + str(tempC) + "C")
        time.sleep(1)
except:
    pass
```

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/92a50d0579b5d50ea659a6b8930da44a.png)Stop/Restart backend”.

![](./media/685166e5ad7c715f87a71fd1e353d475.png)

Click “![](./media/b8c516557596c51f73780a628fc6a933.png)Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will continuously display the thermistor's current ADC value, voltage value, and temperature value.  Try pinching the thermistor with your index finger and thumb (don't touch the wire) for a while, and you will see the temperature increase. Press“Ctrl+C”or click“![](./media/92a50d0579b5d50ea659a6b8930da44a.png)Stop/Restart backend”to exit the program.

![](./media/d6a85395a98b16456b424d1757fb48e2.png)

![](./media/0a035900fbc73a112eced64a926872ad.png)

5.**Circuit Diagram and Wiring Diagram**

Note : LCD\_128X32\_DOT must be connected with a 10CM M-F Dupont wire, the LCD\_128X32\_DOT will display normally. Otherwise, using a 20CM M-F Dupont wire may cause the LCD\_128X32\_DOT display abnormally.  

![](./media/281774a4fbf4f7f2ca0fd1e60c89516c.png)

![](./media/91445212232765942d482b84da03f598.png)

6.**Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 31：Temperature Instrument”.
Select“lcd128\_32.py”and“lcd128\_32\_fonts.py”， right-click and select“**Upload to /**”，waiting for the “lcd128\_32.py”and“lcd128\_32\_fonts.py”to be uploaded to the Raspberry Pi Pico. And double left-click the “Project\_31.2\_Temperature\_Instrument.py”.

![](./media/51899f245e06b3e3cb9067edc15ac9db.png)

![](./media/e26b49223d077b1be42d67f7a6199568.png)

![](./media/6a1943fd6792b528c49d7fb82531b88a.png)

```Python
from machine import Pin, ADC, I2C
import time
import math
import lcd128_32_fonts
from lcd128_32 import lcd128_32

#Set ADC
adc=ADC(27)

#i2c config
clock_pin = 21
data_pin = 20
bus = 0
i2c_addr = 0x3f
use_i2c = True

def scan_for_devices():
    i2c = machine.I2C(bus,sda=machine.Pin(data_pin),scl=machine.Pin(clock_pin))
    devices = i2c.scan()
    if devices:
        for d in devices:
            print(hex(d))
    else:
        print('no i2c devices')

try:
    while True:
        adcValue = adc.read_u16()
        voltage = adcValue / 65535.0 * 3.3
        Rt = 10 * voltage / (3.3-voltage)
        tempK = (1 / (1 / (273.15+25) + (math.log(Rt/10)) / 3950))
        tempC = int(tempK - 273.15)
        
        if use_i2c:
            scan_for_devices()
            lcd = lcd128_32(data_pin, clock_pin, bus, i2c_addr)
            
        lcd.Clear()
        lcd.Cursor(0, 0)
        lcd.Display("Voltage:")
        lcd.Cursor(0, 8)
        lcd.Display(str(voltage))
        lcd.Cursor(0, 20)
        lcd.Display("V")
        lcd.Cursor(2, 0)
        lcd.Display("Temperature:")
        lcd.Cursor(2, 12)
        lcd.Display(str(tempC))
        lcd.Cursor(2, 15)
        lcd.Display("C")
        time.sleep(0.5)
except:
    pass

```

7.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/92a50d0579b5d50ea659a6b8930da44a.png)Stop/Restart backend”.
    
![](./media/5dca0b0bfa2a91ecb44acd93352c7fae.png)
    
Click“![](./media/b8c516557596c51f73780a628fc6a933.png)Run current script”, the code starts executing, we will see that the LCD 128X32 DOT displays the voltage value of the thermistor and the temperature value in the current environment. Press“Ctrl+C”or click“![](./media/92a50d0579b5d50ea659a6b8930da44a.png)Stop/Restart backend”to exit the program.

![](./media/76838f88b0ab17d60b9b0dc878604d47.png)


### Project 32：RFID

1.**Introduction**
    
Nowadays, many residential districts use this function to open the door by swiping the card, which is very convenient. In this lesson, we will learn how to use RFID(radio frequency identification) wireless communication technology and read and write the key chain card (white card) and control the steering gear rotation by RFID-MFRC522 module.
    
2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/8eeca2083cc744159c642a792b53eba2.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/dac05f32017287326cbdb88227a11366.png)</td>
<td>![Img](./media/img-20231116164454.png)
</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>RFID-MFRC522 Module*1</td>
<td>Key Chain*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/img-20231116164551.png)
</td>
<td>![Img](./media/cd0bc424e9916881a1a903793821a042.png)</td>
<td>![Img](./media/img-20231116164519.png)
</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>F-F Dupont Wires</td>
<td>Servo*1</td>
<td>White Card*1</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.**Component Knowledge**
    
**RFID**：RFID (Radio Frequency Identification) is a wireless communication technology. A complete RFID system generally consists of a transponder and a reader. Usually we use tags as transponders, and each tag has a unique code attached to the object to identify the target object. The reader is a device that reads (or writes) tag information.
    
Products derived from RFID technology can be divided into three categories: passive RFID products, active RFID products and
semi-active RFID products. However, the passive RFID products are the earliest, most mature and most widely used products on the market, which can be seen everywhere in our daily life, such as bus card, meal card, bank card, hotel access card, etc., which are close contact identification. 
    
The main operating frequencies of the passive RFID products are 125KHZ(low frequency), 13.56mhz (high frequency), 433MHZ(UHF), and 915MHZ(UHF). The active and the semi-active RFID products operate at higher frequencies.
    
The RFID module we use is a passive RFID product with a working frequency of 13.56MHz.  
    
    
    
**RFID-RC522 Module：** The MFRC522 is a highly integrated reader/writer IC for 13.56MHz contactless communication. Its
internal transmitter is capable of driving a read/write antenna , which is designed to communicate with ISO/IEC 14443A /MIFARE cards and transponders without the need for additional active circuits. The receiving module provides an efficient implementation of demodulation and decoding of signals from ISO/IEC 14443 A /MIFARE compatible cards and transponders. The digital module manages complete ISO/IEC 14443A framing and error detection (parity and CRC) features.  
    
The RFID module uses the MFRC522 as the control chip and adopts I2C(Inter-Integrated Circuit) interface.  
    
![](./media/5a19d0dd224c2cdc78871f11e8951045.png)
    
Specifications:
    
Operating voltage: DC 3.3V-5V
    
Operating current: 13—100mA/DC 5V
    
Idling current: 10-13mA/DC 5V
    
Sleep current: \<80uA

Peak current: \<100mA
    
Operating frequency: 13.56MHz
    
Maximum power: 0.5W
    
Supported card types: mifare1 S50, mifare1 S70, mifare UltraLight, mifare Pro and mifare Desfire
    
Environmental operating temperature: -20 to 80 degrees Celsius
    
Environment storage temperature: -40 to 85 degrees Celsius
    
Relative Humidity: 5% to 95%
    
Data transfer rate: The maximum is 10Mbit/s.
    
4.**Read the Card Number Value**
    
We will read the UNIQUE ID number (UID) of the RFID card and identify its type. And display relevant information through the "Shell" window of Thonny IDE. The wiring diagram is as follows:
    
![](./media/654c447a08c85a3b54c80aea24577ad7.png)

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 32：RFID”.
Select“mfrc522\_config.py”,“mfrc522\_i2c.py”and“soft\_iic.py”，right-click and select “**Upload to /**”,waiting for the“mfrc522\_config.py”“mfrc522\_i2c.py”and“soft\_iic.py”to be uploaded to the Raspberry Pi Pico. And double left-click the“Project\_32.1\_RFID\_Read\_UID.py”.

![](./media/d7dca8ec63428a058574be248412f095.png)

![](./media/11cee31f3227c6c3bb67499c97127615.png)

![](./media/8913dd2bd13d948946c62b0721532b27.png)

![](./media/a88cc22de3853bc5c61e81c19b10c3ff.png)

```Python
import machine
import time
from mfrc522_i2c import mfrc522

#i2c config
addr = 0x28
scl = 21
sda = 20
    
rc522 = mfrc522(scl, sda, addr)
rc522.PCD_Init()
rc522.ShowReaderDetails()            # Show details of PCD - MFRC522 Card Reader details

while True:
    if rc522.PICC_IsNewCardPresent():
        #print("Is new card present!")
        if rc522.PICC_ReadCardSerial() == True:
            print("Card UID:")
            print(rc522.uid.uidByte[0 : rc522.uid.size])
    #time.sleep(1)
```

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/1496a550ee770cdb87db5cff7f4d3a15.png)Stop/Restart backend”.

![](./media/fa7b3a5a0597ab20339bd50824d4eb82.png)

Click“![](./media/e7b6acce1053bcc54eedf48f57df7c18.png)Run current script”, the code starts executing, we will see that

place the door card and key chain close to the module sensor area respectively, the "Shell" window of Thonny IDE will display the card number and key chain value respectively, as shown below. Press“Ctrl+C”or click“![](./media/92a50d0579b5d50ea659a6b8930da44a.png)Stop/Restart backend”to exit the program.

![](./media/1ddf042634e88934c5b4a3fb00988ac4.png)

![](./media/091b3f4fdd9b823b64487aec5d5834f8.png)

Note: the door card value and key chain value may be different for different RRFID -RC522 door cards and key chains.  

**Circuit Diagram and Wiring diagram of RFID-RC522 Controlling Servo Rotation**

Now we use a RFID-RC522 module, door card/key chain and servo to simulate an intelligent access control system. When the door card is close to the RFID-RC522 module induction area, the servo rotates. Wiring according to the figure below:

![](./media/671a93cf112889c8c5245ac6ebeb2c4d.png)

6.**Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 32：RFID”. Select“mfrc522\_config.py”“mfrc522\_i2c.py”and“soft\_iic.py”，right-click and select“**Upload to /**”,waiting for the“mfrc522\_config.py”“mfrc522\_i2c.py”and“soft\_iic.py”to be uploaded to the Raspberry Pi Pico. And double left-click the“Project\_32.2\_RFID\_Control\_Servo.py”.

![](./media/d7dca8ec63428a058574be248412f095.png)

![](./media/11cee31f3227c6c3bb67499c97127615.png)

![](./media/8913dd2bd13d948946c62b0721532b27.png)

![](./media/c24d28b4684756d8651b8e94f285d4f0.png)

```Python
from machine import Pin, PWM
import time
from mfrc522_i2c import mfrc522

#Define GPIO2’s output frequency as 50Hz and assign them to PWM.
pwm = PWM(Pin(2))
pwm.freq(50)

'''
#Duty cycle corresponding to steering gear Angle
0°----2.5%----1638
45°----5%----3276
90°----7.5%----4915
135°----10%----6553
180°----12.5%----8192
'''
#steering gear Angle are fit to its duty cycle. 
angle_0 = 1638
angle_45 = 3276
angle_90 = 4915
angle_135 = 6553
angle_180 = 8192

#i2c config
addr = 0x28
scl = 21
sda = 20
    
rc522 = mfrc522(scl, sda, addr)
rc522.PCD_Init()
rc522.ShowReaderDetails()            # Show details of PCD - MFRC522 Card Reader details

uid1 = [147, 173, 247, 32]
uid2 = [57, 182, 70, 194]

pwm.duty_u16(angle_180)
time.sleep(1)

while True:
    if rc522.PICC_IsNewCardPresent():
        #print("Is new card present!")
        if rc522.PICC_ReadCardSerial() == True:
            print("Card UID:", end=' ')
            print(rc522.uid.uidByte[0 : rc522.uid.size])
            if rc522.uid.uidByte[0 : rc522.uid.size] == uid1 or rc522.uid.uidByte[0 : rc522.uid.size] == uid2:
                pwm.duty_u16(angle_0)
            else :
                pwm.duty_u16(angle_180)
            time.sleep(500)
```

Note: For different RFID-RC522 modules, white cards and key chains, its RFID-RC522 modules may read different UID1 and UID2 values. You should replace the uID1 and UID2 values of the white cards and key chains read by your RRFID -RC522 module with the corresponding values in the program code, otherwise, click "Run current script" to run the code may cause your swipe cards and key chains can not control the servo.

For example, you replace the ![](./media/54b4d282380bd68468de99bbda6bd3ad.png) UID1 and UID2 values in the program code with the white card and key chain values read by your rFID-RC522 module.

7.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/987fc5989d931a49f61cc18b40d21b8c.png)Stop/Restart backend”.
    
![](./media/b86db6e849d05f2bb75264f491ac251b.png)
    
Click “![](./media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that when using the white card or a key card swiping, the "Shell" window of Thonny IDE will display the card number value respectively, and at the same time, the servo will rotate to the corresponding angle to simulate opening the door.
    
Press“Ctrl+C”or click“![](./media/92a50d0579b5d50ea659a6b8930da44a.png)Stop/Restart backend”to exit the program.

![](./media/4f64091f1a37dd59d7df959ed5727015.png)


### Project 33：Keypad Door

1.**Introduction**
    
In common digital button sensors, one button uses an IO port. However, sometimes it will occupy several IO ports when we need a lot of buttons . In order to save the use of IO ports, we are supposed to make a plurality of buttons into a matrix type, through the control of lines to achieve less IO port control the multiple buttons. In this project, we will learn a Raspberry Pi Pico and a 4\*4 membrane matrix keyboard control a servo and a buzzer.   
    
2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/ea74681ffd2116a2434692d34c25e829.jpeg)</td>
<td>![Img](./media/bbed91c0b45fcafc7e7163bfeabf68f9.png)</td>
<td>![Img](./media/cd0bc424e9916881a1a903793821a042.png)</td>
<td>![Img](./media/4b4f653a76a82a3b413855493cc58fba.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>Servo*1</td>
<td>Active Buzzer*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/fcd187eb009098d691927511606c991b.jpeg)</td>
<td>![Img](./media/e9a8d050105397bb183512fb4ffdd2f6.png)</td>
<td>![Img](./media/e380dd26e4825be9a768973802a55fe6.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>4*4 Membrane Matrix Keyboard*1</td>
<td>Jumper Wires</td>
<td>Breadboard*1</td>
<td>USB Cable*1</td>
</tr>
</tbody>
</table>

3.**Component Knowledge**
    
**4\*4 Matrix keyboard:** The keyboard is a device that integrates many keys. As shown in the figure below, a 4x4 keyboard integrates 16 keys.
    
![](./media/fcd187eb009098d691927511606c991b.jpeg)
    
As with the LED matrix integration, in the 4x4 keyboard, each row of keys is connected to a pin, each column of keys is the same. This connection reduces the use of processor ports. The internal circuit is shown below.
    
![](./media/5ebdacba906622079e0ef41dc1ea3fdf.png)

You can use row scan or column scan methods to detect the state of the keys on each column or each line. Take the column scan method as an example. Send a low level to column 4 (Pin4), detect the state of rows 1, 2, 3 and 4, and determine whether the A, B, C and D keys are pressed. Then send the low level to columns 3, 2, 1 in turn, and detect whether other keys are pressed. Then you can get the state of all keys.

4.**Read the Value**
    
We start with a simple code to read the values of the 4\*4 matrix keyboard and print them in the serial monitor. Its wiring diagram is shown below.

![](./media/a673f15964984f61170e2d7690e959c1.png)

![](./media/681be86e91946320131d4b11b12b77c2.png)

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 33：Keypad Door”. Select“keypad\.py”， right-click and select“**Upload to/**”，waiting for“keypad\.py”to be uploaded to the Raspberry Pi Pico. And double left-click the “Project\_33.1\_4x4\_Matrix\_Keypad\_Display.py”.

![](./media/aed2193522c15181e0d9d6f17289d50c.png)

![](./media/42a7c5b6378f578ad6b8d34c2c002153.png)

```Python
from keypad import KeyPad
import time

keyPad = KeyPad(26, 22, 21, 20, 19, 18, 17, 16)

def key():
    keyvalue = keyPad.scan()
    if keyvalue != None:
        print(keyvalue, end="\t")
        time.sleep_ms(300)
        return keyvalue
            
while True:
    key()
```

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/8841f93dbb1cf6462d84cdfeb170ba29.png)

Click“![](./media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that press the keyboard and the "Shell" window of Thonny IDE will print the corresponding key value, as shown below.
Click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/046f19e4e5f9262e114350efc5074d4b.png)

![](./media/2f82f861d68daaaad8085b6a1bcc2e8d.png)

5.**Circuit Diagram and Wiring Diagram**

In the last experiment, we have known the key values of the 4\*4 matrix keyboard. Next, we use it as the keyboard to control the servo and the buzzer.  

![](./media/f08b9ee128bc06300b3f8a05c73c2375.png)

![](./media/ccb5914d82d2b220e8a6afb944d13c54.png)

6.**Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 33： Keypad Door”. Select“keypad\.py”and“myservo\.py”， right-click and select“**Upload to /**”，waiting for the “keypad\.py”and“myservo\.py”to be uploaded to the Raspberry Pi Pico. And double left-click the“Project\_33.2\_Keypad\_Door.py”.

![](./media/aed2193522c15181e0d9d6f17289d50c.png)

![](./media/bd1d1f233c7953103b99ad60a1daefde.png)

![](./media/7da4463f4300f90b40a82218d3525c68.png)

```Python
from myservo import Servo
from keypad import KeyPad
from machine import Pin
import time

keyPad = KeyPad(26, 22, 21, 20, 19, 18, 17, 16)
servo = Servo(2)
servo.ServoAngle(0)
activeBuzzer = Pin(0, Pin.OUT)

passWord = "1234"
keyIn = ""
def key():
    keyvalue = keyPad.scan()
    if keyvalue != None:
        print('Your input:', keyvalue)
        time.sleep_ms(200)
        return keyvalue

while True:
    keydata = key()
    if keydata != None:
        activeBuzzer.value(1)
        time.sleep_ms(100)
        activeBuzzer.value(0)
        keyIn += keydata 
        
    if len(keyIn) == 4:
        if keyIn == passWord:
            print("passWord right!")
            servo.ServoAngle(90)
            time.sleep_ms(1000)
            servo.ServoAngle(0)
        else:
            print("passWord error!")
            activeBuzzer.value(1)
            time.sleep_ms(1000)
            activeBuzzer.value(0)
        keyIn = ""
```

7.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/cbcc9a007c9148a7101f141b72a04aae.png)

Click “![](./media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that press the keyboard to enter a four-character password. If the password is correct (correct password: 1234), the servo will turn at an angle and return to its original position. If the input is incorrect, an input error alert will be issued. Click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/04ba047131a4b5e66bc234515c15beee.png)

![](./media/d45bd766b2b2630219f8bef283a07417.png)


### Project 34：IR Control Sound and LED


1.**Introduction**

Infrared remote control is a low-cost, easy-to-use wireless communication technology. IR light is very similar to visible light, except that it has a slightly longer wavelength. This means that infrared rays cannot be detected by the human eye, which is perfect for wireless communication. For example, when you press a button on the TV remote control, an infrared LED will switch on and off repeatedly at a frequency of 38,000 times per second, sending information (such as volume or channel control) to the infrared sensor on the TV.

We will first explain how common IR communication protocols work. Then we will start this project with a remote control and an IR receiving component.

2.**Components Required**

<table>
<tbody>
<tr class="odd">
<td>![Img](./media/17098ffd05750eb6b34eb75b82fbb37a.jpeg)</td>
<td>![Img](./media/355118d2d21e57840d34a30ec500a900.png)</td>
<td>![Img](./media/88e6b057fb4b0c576c9b2111d15b26e5.png)</td>
<td>![Img](./media/f1a86fc81ab4b043263ce7e01e14d470.png)</td>
<td>![Img](./media/098a2730d0b0a2a4b2079e0fc87fd38b.png)</td>
<td>![Img](./media/7dcbd02995be3c142b2f97df7f7c03ce.png)</td>
</tr>
<tr class="even">
<td>Raspberry Pi Pico*1</td>
<td>Raspberry Pi Pico Expansion Board*1</td>
<td>IR Receiver *1</td>
<td>RGB LED*1</td>
<td>220ΩResistor*3</td>
<td>USB Cable*1</td>
</tr>
<tr class="odd">
<td>![Img](./media/8a6fb37dedef748e6c2609bff5c64906.png)</td>
<td>![Img](./media/e380dd26e4825be9a768973802a55fe6.png)</td>
<td>![Img](./media/d1ea1bb2b2749820cab389d5b85b838b.png)</td>
<td>![Img](./media/img-20231116164756.png)</td>
<td>![Img](./media/e9a8d050105397bb183512fb4ffdd2f6.png)</td>
<td></td>
</tr>
<tr class="even">
<td>IR Remote Controller*1</td>
<td>Breadboard*1</td>
<td>Passive Buzzer*1</td>
<td>10KΩResistor*1</td>
<td>Jumper Wires</td>
<td></td>
</tr>
</tbody>
</table>

3.**Component Knowledge**

**IR Remote Controller**: It is a device that has a certain number of buttons. Pressing different buttons causes the infrared transmitter tubes at the front of the remote control to send infrared signals in different codes. Infrared remote control technology is widely used, such as TV, air conditioner and so on. Therefore, in today's technologically advanced society, the infrared remote control technology makes it very convenient for us to change TV programs and adjust the temperature of the air conditioner.  

The remote control we used is as follows:

The infrared remote controller adopts NEC code and the signal cycle is 110ms.

![](./media/3c9d76cb0d24d9861811ce2cb0bb6ae4.png)

**IR Receiver:** It is a component that can receive infrared light, which can be used to detect the infrared signal sent by the infrared remote control. The infrared signal received by the infrared receiver demodulation can be converted back to binary, then the information will be passed to a microcontroller.

**Process Diagram：**

![](./media/3da1969e509f53706643c77d0534eb73.png)

**NEC Infrared communication protocol：**

**NEC Protocol**

To my knowledge the protocol I describe here was developed by NEC (Now Renesas). I've seen very similar protocol descriptions on the internet, and there the protocol is called Japanese Format.

I do admit that I don't know exactly who developed it. What I do know is that it was used in my late VCR produced by Sanyo and was marketed under the name of Fisher. NEC manufactured the remote control IC.

This description was taken from my VCR's service manual. Those were the days, when service manuals were filled with useful information\!

**Features**

8 bit address and 8 bit command length.

Extended mode available, doubling the address size.

Address and command are transmitted twice for reliability.

Pulse distance modulation.

Carrier frequency of 38kHz.

Bit time of 1.125ms or 2.25ms.

**Modulation**

![](./media/da33571c6f0afb94b1ec1d91caba3edb.png)

The NEC protocol uses pulse distance encoding of the bits. Each pulse is a 560µs long 38kHz carrier burst (about 21 cycles). A logical "1" takes 2.25ms to transmit, while a logical "0" is only half of that, being 1.125ms. The recommended carrier duty-cycle is 1/4 or 1/3

**Protocol**

![](./media/f970404e7bbfb5711fea5c776f689f3a.png)

The picture above shows a typical pulse train of the NEC protocol. With this protocol the LSB is transmitted first. In this case Address $59 and Command $16 is transmitted. A message is started by a 9ms AGC burst, which was used to set the gain of the earlier IR receivers. This AGC burst is then followed by a 4.5ms space, which is then followed by the Address and Command. 

Address and Command are transmitted twice. The second time all bits are inverted and can be used for verification of the received message. The total transmission time is constant because every bit is repeated with its inverted length. If you're not interested in this reliability you can ignore the inverted values, or you can expand the Address and Command to 16 bits each\!

Keep in mind that one extra 560µs burst has to follow at the end of the message in order to be able to determine the value of the last bit.

![](./media/63364daf21e5522c64eb8dfa82f2cef2.png)

A command is transmitted only once, even when the key on the remote control remains pressed. Every 110ms a repeat code is transmitted for as long as the key remains down. This repeat code is simply a 9ms AGC pulse followed by a 2.25ms space and a 560µs burst.

![](./media/afea92a3b5cc1aa2457d2b118b157c84.png)

**Extended NEC protocol**

The NEC protocol is so widely used that soon all possible addresses were used up. By sacrificing the address redundancy the address range was extended from 256 possible values to approximately 65000 different values. This way the address range was extended from 8 bits to 16 bits without changing any other property of the protocol.

By extending the address range this way the total message time is no longer constant. It now depends on the total number of 1's and 0's in the message. If you want to keep the total message time constant you'll have to make sure the number 1's in the address field is 8 (it automatically means that the number of 0's is also 8). This will reduce the maximum number of different addresses to just about 13000.

The command redundancy is still preserved. Therefore each address can still handle 256 different commands.

![](./media/2f78d1ce7f001926f6b90ad966796e91.png)

Keep in mind that 256 address values of the extended protocol are invalid because they are in fact normal NEC protocol addresses. Whenever the low byte is the exact inverse of the high byte it is not a valid extended address.

4.**Decode Infrared Signal:**
    
We connect the infrared receiving element to the Raspberry Pi Pico according to the wiring diagram below.  

![](./media/240a9b2efcdd0c0e7099ec5b69beaca6.png)

![](./media/a6a7f74730669dfa0272e9b5e88ac41e.png)

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 34：IR Control Sound and LED”. Select“irrecvdata\.py”， right-click and select“**Upload to /**”,waiting for the“irrecvdata\.py”to be uploaded to the Raspberry Pi Pico. And double left-click the “Project\_34.1\_Decoded\_IR\_Signal.py”.

![](./media/0e559f2f7ce06f100f33f2aa562669b3.png)

![](./media/91b7122d9d7183692a5cd243a9f493e1.png)

```Python
# Import the infrared decoder.
from irrecvdata import irGetCMD

# Associate the infrared decoder with GP16.
recvPin = irGetCMD(16)

#When infrared key value is obtained, print it out in"Shell". 
try:
    while True:
        irValue = recvPin.ir_read() #Call ir_read() to read the value of the pressed key and assign it to IRValue.
        if irValue:
            print(irValue)
except:
    pass
```

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/f74f668d149dbdab5ac8f19df19c1852.png)

Click“![](./media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that aim the infrared remote control transmitter at the infrared receiving head, press the button on the infrared controller, and the "Shell" window of Thonny IDE will print the current received key code values. Press“Ctrl+C”or click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/a75baa34fe256fdea2714b1b0c66cd66.png)

![](./media/623f8fa842b90a093d286954835483c6.png)

Write down the code associated with each button, because you will need that information later.

![](./media/ebcf0cb2055f7784505f76ceeaef9f47.jpeg)

**5. Circuit Diagram and Wiring Diagram**

![](./media/6e2da9ed5d5bdc5b251348903a37e5c0.png)

![](./media/d170f9c106c16175d34f20fdaa0f8970.png)

**6. Test Code**

Check the code in the folder "**...\6.Codes\Python_Codes(Raspberry-Pi)**".

You can move the code anywhere. For example, We copy the **Python_Codes(Raspberry-Pi).zip** to the <span style="color: rgb(255, 76, 65);">pi</span> folder of the Raspberry Pi system.

<span style="color: rgb(255, 76, 65);">Path: home/pi/Python_Codes(Raspberry-Pi)</span>

<br>
<br>

![](./media/ae27830403a2f741aa9b725e5324c215.png)

Open“Thonny”, click“This computer”→“home”→“pi”→“Python_Codes(Raspberry-Pi)”→“Project 34：IR Control Sound and LED”. Select“irrecvdata\.py”，right-click and select“**Upload to /**”,waiting for the“irrecvdata\.py”to be uploaded to the Raspberry Pi Pico. And double left-click the “Project\_34.2\_IR\_Control\_Sound\_And\_LED.py”.

![](./media/ae27830403a2f741aa9b725e5324c215.png)

![](./media/5c888c9be814f29b3e92ad5cfa3146a2.png)

![](./media/d6e208f4422581641228a7a53e14f9ad.png)

```Python
from machine import Pin,PWM
import utime
from irrecvdata import irGetCMD

#Set RGB light interface and frequency
rgb_r = PWM(Pin(19))
rgb_g = PWM(Pin(18))
rgb_b = PWM(Pin(17))
rgb_r.freq(1000)
rgb_g.freq(1000)
rgb_b.freq(1000)

# Initialize the buzzer pin to PWM function
buzzer=PWM(Pin(15, Pin.OUT))
buzzer.freq(262)
buzzer.duty_u16(0)

# Play the frequency of midrange tones 1-7
freq = [262, 294, 330, 350, 393, 441, 495]

#Configure infrared receiving pin and library
recvPin = irGetCMD(16)

# Set the buzzer to emit different tones.
# index=[0-7], where 0 is closed, and 1-7 respectively represent middle C, middle D, middle E, middle F, middle G, middle A, middle B.
# time represents the function delay time (a positive integer), in milliseconds.
# auto_off indicates whether the buzzer will be turned off automatically after the delay time.
def tone(index, time=0, auto_off=False):
    if index == 0:
        buzzer.duty_u16(0)
        utime.sleep_ms(time)
    elif index >= 1 and index <= 7:
        tone_freq = freq[int(index - 1)]
        buzzer.freq(tone_freq)
        buzzer.duty_u16(32768)
        utime.sleep_ms(time)
        if auto_off == True:
            buzzer.duty_u16(0)
        # print("----freq:", index, tone_freq)
    else:
        print("Tones must be 0-7")
 
delay = 0
 
tone(1, 100, True)

while True:
    irValue = recvPin.ir_read() # Read remote control data
# Determine whether there is a button that meets the needs 
    if irValue:
        print(irValue)
        if irValue == '0xff6897':   #1
           rgb_r.duty_u16(65535)
           rgb_g.duty_u16(0)
           rgb_b.duty_u16(0)
           tone(1, delay)
        elif irValue == '0xff9867': #2
            rgb_r.duty_u16(0)
            rgb_g.duty_u16(65535)
            rgb_b.duty_u16(0)
            tone(2, delay)
        elif irValue == '0xffb04f': #3
            rgb_r.duty_u16(0)
            rgb_g.duty_u16(0)
            rgb_b.duty_u16(65535)
            tone(3, delay)
        elif irValue == '0xff30cf': #4
            rgb_r.duty_u16(65535)
            rgb_g.duty_u16(65535)
            rgb_b.duty_u16(0)
            tone(4, delay)
        elif irValue == '0xff18e7': #5
            rgb_r.duty_u16(65535)
            rgb_g.duty_u16(0)
            rgb_b.duty_u16(65535)
            tone(5, delay)
        elif irValue == '0xff7a85': #6
            rgb_r.duty_u16(0)
            rgb_g.duty_u16(65535)
            rgb_b.duty_u16(65535)
            tone(6, delay)
        elif irValue == '0xff10ef': #7
            rgb_r.duty_u16(65535)
            rgb_g.duty_u16(65535)
            rgb_b.duty_u16(65535)
            tone(7, delay) 
        else:
            rgb_r.duty_u16(0)
            rgb_g.duty_u16(0)
            rgb_b.duty_u16(0)
            tone(0)
```
7.**Test Result**
    
Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”.

![](./media/289a530101aab3165cd1d1cf64823f83.png)

Click“![](./media/bb4d9305714a178069d277b20e0934b7.png)Run current script”, the code starts executing, we will see that press buttons 1 to 7 on the infrared remote controller, we can hear buzzers such as do、re、mi、fa、sol、la、si ,etc. At the same time, the RGB will be red , green , blue , yellow ,magenta, blue and green, white respectively. However, if we press other buttons (except 1-7), the buzzer stops playing and the RGB goes off. Click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend”to exit the program.

![](./media/d2a08d65ae5498348fcc389ef6870783.png)

**Note**：When the code is running, the following prompt appears, you just need to click“![](./media/ec00367ea605788eab454cd176b94c7b.png)Stop/Restart backend“, then click![](./media/bb4d9305714a178069d277b20e0934b7.png)“Run current script”to make the code run again.

![](./media/3f425db5cda9eb56bc1f29c27fa6696d.png)

(Note: Before use, we need to remove the plastic sheet from the bottom of the infrared remote controller.)

![](./media/3c9d76cb0d24d9861811ce2cb0bb6ae4.png)
