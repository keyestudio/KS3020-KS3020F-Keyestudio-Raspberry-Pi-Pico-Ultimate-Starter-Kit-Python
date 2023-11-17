# Python_Tutorial(Windows)

## Preparation for Python（Important）

Before we start building a project, we need to do some preparations first, 

which is so important that we can't skip it. 

### 1. Install Thonny

Thonny is a free and open source software platform with small size, simple interface, simple operation and rich functions. It is a Python IDE suitable for beginners. In this tutorial, we use this IDE to develop a Raspberry Pi Pico. Thonny supports multiple operating systems including Windows, Mac OS, Linux.

#### 1.1. Download Thonny

1) Enter the website: [https://thonny.org](https://thonny.org) to download the latest version of Thonny.
    
2) Thonny open-source code library: [https://github.com/thonny/thonny](https://github.com/thonny/thonny)  
     
Please follow the instructions on the official website or click the link below to download and install.  (Please select the appropriate option based on your operating system.)  

<table>
<tbody>
<tr class="odd">
<td>System</td>
<td>Download link</td>
</tr>
<tr class="even">
<td>MAC OS：</td>
<td><a href="https://github.com/thonny/thonny/releases/download/v3.2.7/thonny-3.2.7.pkg">https://github.com/thonny/thonny/releases/download/v3.2.7/thonny-3.2.7.pkg</a></td>
</tr>
<tr class="odd">
<td>Windows：</td>
<td><a href=" https:/github.com/thonny/thonny/releases/download/v3.2.7/thonny-3.2.7.exe">https://github.com/thonny/thonny/releases/download/v3.2.7/thonny-3.2.7.exe</a></td>
</tr>
<tr class="even">
<td>Linux：</td>
<td><p><a href="javascript:;"><strong>latest</strong></a> <a href="javascript:;"><strong>version</strong></a></p>
<p><strong>Binary bundle for PC (Thonny+Python):</strong></p>
<p>bash &lt;(wget -O - https://thonny.org/installer-for-linux)</p>
<p><strong>With pip:</strong></p>
<p>pip3 install thonny</p>
<p><strong>Distro packages (may not be the latest version):</strong></p>
<p><strong>Debian, Rasbian, Ubuntu, Mint and others:</strong></p>
<p>sudo apt install thonny</p>
<p><strong>Fedora:</strong></p>
<p>sudo dnf install thonny</p></td>
</tr>
</tbody>
</table>

![](./media/bd5823ede2c01d1fa4696438c62aec51.png)

#### 1.2. Install Thonny on Windows

1). The downloaded Thonny icon is as follows.

![](./media/d3caa98d406fa06a124d5c98195b90db.png)

2). Double-click “Thonny-3.3.13.exe”. The following dialog box is displayed. I choose“![](./media/11fb59a50abe0bf54df7e4cb891ad2c0.png)”to operate. You can also select“![](./media/37be3f3bcc9aa0eb48c8b844eb46a71c.png)” to operate.
    
![](./media/4c044b255da8b14fe674eb9cce01627d.png)
    
3). If you are not familiar with computer software installation, click “Next” until the installation is complete.  
    
![](./media/995b36640124b6a9b23f10473ff8a38a.png)
    
![](./media/8bcc17840b9fc15d76f79fee8a0168ee.png)
    
4). If you want to change the route of installing Thonny，just click“**Browse...**”to select a new route and click “OK”. 
    
If you don’t want to change the route of installing Thonny, just click “Next”and then click“Next”again.
    
![](./media/df6f63b42ebb1676b22c26b25dc9c7aa.png)
    
![](./media/f5cd6d619b4645601c5b098ffdbec12a.png)
    
5). Select "Create Desktop Icon". Thonny software will generate a shortcut on your desktop for you to open Thonny software later.
    
![](./media/a30c89dde3de81ad00aced30510071be.png)
    
6). Click "Install"
    
![](./media/6ace65142291e5e8af5f81e4a6b2f180.png)

7). Wait for a while but don’t click **Cancel**
    
![](./media/a504b3a3ab16b4d91040cd5878acea0c.png)

8). Once we see the following screen, Thonny software has been successfully installed. Click “Finish”.  
    
![](./media/a1fb6027e54a975de1c0aa1e1a0d6a29.png)
    
9). If we select “Create Desktop Icon” during the installation, the following icon will be displayed on the desktop.  
    
![](./media/80f35044d91d66f734e36059db35f273.png)

#### 1.3. Basic configuration of Thonny software

1). Double-click the desktop icon of Thonny software, we can see the following interface, and we can also choose the language and initial settings.  Once set, click "Let's Go\!"  
    
![](./media/ee240978a4f844184f1ea9f5a21d0395.png)
    
![](./media/619a856895d95e00beed748b1438072d.png)
    
![](./media/bcf6c31e4f69c904a7a0c0e9df7e8d7d.png)
    
2). Select“View”→“File”和“Shell”
    
![](./media/5ff5c305585dbe7e832cc41183db5818.png)
    
![](./media/d41b79772c9846fd8bf295c8451f8321.png)
    
![](./media/3d04fe6893ca104e4e593a0786cb3799.png)

<!-- end list -->

### 2. Update Micropython firmware

To run MicroPython programs on Raspberry Pi Pico, we first need to burn a firmware into Raspberry Pi Pico.  

**Why do we need to update the firmware?**

The Raspberry Pi Pico can be programmed in both C and MicroPython, and which is shipped without MicroPython firmware, which we need to download before we can program with MicroPython. 

<span style="color: rgb(255, 76, 65);">Note:</span> MicroPython Firmware only needs to be downloaded once and does not need to be downloaded again when programming with MicroPython.  If we have downloaded the.uf2 firmware written in C, it will be overwritten, so the next time we use MicroPython, we need to update our Raspberry Pi Pico firmware by following the steps.  

<br>
<br>

#### 2.1. Download the Micropython Firmware**

<span style="color: rgb(255, 76, 65);">Method 1:</span> Raspberry Pi Pico official website：[https://www.raspberrypi.com/documentation/microcontrollers/](https://www.raspberrypi.com/documentation/microcontrollers/)

<br>
<br>

1). Click the link above, we can see the following interface:
    
![](./media/3b3e6a639416b76c44f2a0854dc451cc.png)

2). Scroll the mouse and we can see the following again:
    
![](./media/5d04d67506852588d126ce760739a3c5.png)

3). Click MicroPython(Getting Started MicroPython) to go to the firmware download page.  
    
![](./media/137e21851df02502fb989d8541fa0da8.png)
    
<span style="color: rgb(255, 76, 65);">Method 2:</span> By clicking on the download link:
[https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2](https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2), we can download directly.  

<br>
<br>  

<span style="color: rgb(255, 76, 65);">Method 3:</span> If we can't download it due to network problems or other reasons, we can use the.uf2 file we prepared, which is located in the following file path.  
    
![](./media/ca4858fd34bc267a5b6089ad8ef1d277.png)

<!-- end list -->

#### 2.2. The procedures for burning MicroPython firmware

① Connect one end of the microUSB cable to the USB port of our computer.  

② Long press the white button on the "Raspberry Pi Pico" (BOOTSEL).  The Raspberry Pi Pico is then connected to the computer via the microUSB wire.  

![](./media/33c91d51b2aeb2c943691706354aaad1.png)

③ Release the button, when the connection is successful, open [Device Manager\] on our computer, the computer will automatically recognize the removable disk (RPI-RP2), as shown below:

![](./media/87e24af3ea812b5492a06b0141060b86.png)

④ Copy the file (RP2-Pico-20210902-v1.17.uf2) to a removable disk (RPI-rp2) and wait for it to complete, just like copying the file to a USBflash drive.  

![](./media/916dc807eb08231d8410603e944d405e.png)

⑤ Raspberry Pi Pico automatically restarts after the firmware is burned.  After that, we  can run Micropython.  

#**1.5. Thonny connects to Raspberry Pi Pico**

Open "Thonny", click “Run” and select “Select interpreter…”.

![](./media/09593c45eabe111d9f75848e39312b75.png)

Select“Micropython (generic)”or“Micropython (Raspberry Pi Pico)”How to select“Micropython(generic)”? As follows:

![](./media/0dda06df90ad37a0490c56559108ba51.png)

Select USB-Serial (COMx). The COMx number may be different on different PCS.  Just make sure we select "USB-Serial (COMx)".  

**How to determine which port does the Raspberry Pi Pico communicate with our computer?**

<span style="color: rgb(255, 76, 65);">Step 1:</span> When our Raspberry Pi Pico is not connected to the computer, open Thonny software, click "Run", select "Select Interpreter", the dialog will pop up, click "Port", we can view the currently connected port, as shown in the picture below:
  
<br>
<br>

![](./media/0112f6cc9da283b3e257d3b1e494f610.png)

<span style="color: rgb(255, 76, 65);">Step 2:</span> Close the dialog box.  Connect Raspberry Pi Pico to our computer, click "Run" again and select "Select Interpreter".  Click “Port” in the window that is displayed to view the current port.  Now add another port, so this port is used to communicate with the computer.

<br>
<br>

![](./media/58613bc6727537a24a253c1cc7d9b5cf.jpeg)

Select“Micropython(generic)”and port，and click“OK”.

![](./media/52262cb23cd963079c41b6b015a43261.jpeg)

When the following message is displayed on Thonny, then the Thonny successfully connects to the Raspberry Pi Pico.  

![](./media/e33d2e9552d2cecedc50bf96a5036845.png)

So far, all the preparations have been made.

### 3. Text Code

#### Test Shell commands:  

In“**Shell**”window , type“**print (Hello World\!)**”，press“**Enter**”.

![](./media/2b4feabe1126134057046b6a0dd5bbdb.png)

#### Run Code Online:

To run Raspberry Pi Pico online, we need to connect the Raspberry Pi Pico to our computer, which allows us to compile or debug programs using Thonny software.  

**Advantages:** you can compile or debug programs using Thonny software. Through the "Shell" window, we can view the error information and output results generated during the operation of the program, and query related function information online to help improve the program.  

**Disadvantages:** To run Raspberry Pi Pico online, you must connect Raspberry Pi Pico to a computer and run it with Thonny software.  

If the Raspberry Pi Pico is disconnected from the computer, when they reconnect, the program won't run again.  

<span style="color: rgb(255, 169, 0);">**basic operation :**</span>

Open Thonny and click![](./media/6388aa0daa514f9325fb07fd5ab6749b.png)“**Open...**”.

![](./media/b65264767d6ff04d5f3530b8eebe218c.png)

Click“**This computer**”in the new pop-up window

![](./media/5bdbc66ef89b41a53e46696c07b2c282.png)

In the new dialog box, go to the folder ...\\Python_Codes(Windows)\\Project 01：Hello World . Select“Project\_01\_HelloWorld.py”,click“Open”. 
The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere.  For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

![](./media/9b61f563870ec1235e6cc48ca748cec5.png)

Click![](./media/f79b2c42507d12b91ca23ea0bb87c5c2.png)“Run current script”to execute program“Hello World\!”, "Welcome Keyestudio" will print in the “Shell”window.

![](./media/39eb24657c5733544944dd643640a61d.png)

**Exit online:**

When running online, click ![Img](./media/img-20231116131805.png)“**Stop /Restart Backend**” on Thonny or press **“Ctrl+C”** to exit the program.  

![](./media/dc2a210535724a7d601b5ad8b02ca8ed.png)

#### Offline running code:

When running offline, the Raspberry Pi Pico doesn't need to connect to a computer and Thonny.  Once powered up, it can run the main.pyprogram stored in the Raspberry Pi Pico.  

**Pros**: We don't need to connect a computer to Thonny's software to run the program.  

**Cons**: The program stops automatically when an error occurs or the Raspberry Pi Pico runs out of power, and the code is hard to change.

<span style="color: rgb(255, 76, 65);">**Basic Operation:**</span>

Once powered up, the Raspberry Pi Pico will  check for the presence of main\.py on the device automatically.  If so, run the program in main\.py and go to the shell command system.  (If we want the code to run offline, we can save it as main\.py);  If the main\.py does not exist, go directly to the shell command system.  

Click “File”→“New”, create and write code.

![](./media/7a6988dfff80ecb0479e3e878ccde171.png)

Enter the code in the newly opened file. Here we use the Project\_02\_Onboard\_LED\_Flashing. Py code as an example.  

![](./media/59f397a5c32e3bbe1bb8ff5e2d0316ae.png)

Click“**Save**”on the menu bar, we can save the code in This computer or MicroPython device.

![](./media/abec708857f37ac0871ffa7ad5b4c913.png)

<!-- end list -->

Select“MicroPython device”，enter“main\.py”in the new pop-up window and click“OK”.

![](./media/eb375d7b67d432efb0253a825d5ee5a4.png)

![](./media/d7f40a82158a71b22909f519a9078e94.png)

We can see the code has been uploaded to the Raspberry Pi Pico.

![](./media/aace831a6a8e1199b2a9e0fc6ef40d56.png)

Disconnect the microUSB cable to the Raspberry Pi Pico and reconnect, and the LEDs on the Raspberry Pi Pico will  flash repeatedly. 

![Img](./media/img-20231116105310.png)


**Exit from Offline operation**

Connect Raspberry Pi Pico to the computer，click ![Img](./media/img-20231116131842.png)“Stop/Restart backend”on Thonny to end the offline operation.  

![](./media/5efb6f20a190d482be423126eced88d5.png)

If it does’t work, click ![Img](./media/img-20231116131856.png) “Stop/Restart backend”on Thonny several times or reconnect to the Raspberry Pi Pico.

![](./media/2d507294736e68b68cad4e8060ae1db6.jpeg)

We provide a \.py file to run offline.  The code added to main\.py is the bootstrap that executes the user code file. We just need to upload the offline project's code file (.py) to the "MicroPython Device".

① Make the program folder **...\6.Codes\Python_Codes(Windows)** move ahead to the **Disk(D)**，the path is **D:\\Python_Codes(Windows).** Open the Thonny software.  

![](./media/2da93159095ee2355449a27a22f988b4.png)

② Expand Project 00 : main in Disk(D) directory D:\\Python_Codes(Windows). Double-click **main\.py** to make the code in "**MicroPython Device**" run offline.  

 ![](./media/30ed08309a2c6d6b53ea9b1cd4beb299.png)

Here, we use project 00 and Project 02 cases as examples.  The results are displayed using an LED(GP25 pin) on a Raspberry Pi Pico.  If we have modified the Project\_02\_Onboard\_LED\_Flashing. Py file, then we need to modify it accordingly. Right-click the
Project\_02\_Onboard\_LED\_Flashing. Py file and select '**Upload to/**' to upload the code to Raspberry Pi Pico, as shown below.  

![](./media/2b0dfdd7becf42730b1baa0ca45e6ea3.png)

Upload the **main\.py** in the same way.

![](./media/4e8bc42dbffa1e0432a94e99977d426f.jpeg)

Disconnect and reconnect the microUSB cable to the Raspberry Pi Pico, and the LEDs will flash repeatedly .

![Img](./media/img-20231116105322.png)


Note:

The code here runs offline.  If we want to stop running offline and go to "Shell", simply click![Img](./media/img-20231116132025.png) "Stop/Restart Backend" on Thonny software.

![](./media/dc2a210535724a7d601b5ad8b02ca8ed.png)

### 4. Thonny common operations

#### (1) Upload the code to Raspberry Pi Pico

In the Project 01：Hello World file, right-click and select Project\_01\_HelloWorld.py，select “**Upload to /**” and upload the code to the root directory of the Raspberry Pi Pico.

![](./media/18f24b958cc2efe1e332c429383b8df1.png)

#### (2) Download the code to the computer

In the“**MicroPython device**”, right-click and select Project\_01\_HelloWorld.py，select“**Download to ...**”to download the code to our computer.

![](./media/867e40f907c512aa4a17c0f4fb6d75e6.png)

#### (3) Delete the files in the Raspberry Pi Pico root directory

In the“**MicroPython device**”，right-click and select Project\_01\_HelloWorld.py，select“**Delete**”，delete the Project\_01\_HelloWorld.py from the Raspberry Pi Pico root directory.

![](./media/d97823ab15b1afd831a438e2863ab270.png)

#### (4) Delete files from the computer's directory

In the Project\_01 : Hello World file, right-click and select Project\_01\_HelloWorld.py，select“**Move to Recycle Bin**”，then it can be deleted from the Project\_01\_HelloWorld file.

![](./media/9d73a385a0855eb68c453088bd0748f4.png)

#### (5) Create and Save Code

① Click“**File**”→“**New**”to create and compile code.

![](./media/373922a344188cda87b797b0ad639522.png)

② Enter code in the newly opened file, here we use Project\_02\_Onboard\_LED\_Flashing.py code as an example.

![](./media/4aab2202442af7b04e880414af8f44fe.png)

③ Click“**Save**”，and we can save the code to our computer or the Raspberry Pi Pico.

![](./media/19773e65bc454d549ae95422b645692a.png)

④ Select“**MicroPython device**”，enter“**main\.py**”in the new pop-up window and click“**OK**”.

![](./media/92c1b5f2bb76f21462da37cdb9a3f18f.png)

![](./media/d7f40a82158a71b22909f519a9078e94.png)

⑤ We can see the code has been uploaded to the Raspberry Pi Pico.

![](./media/4be452d7471f5110efdc50737007d714.png)

⑥ Click“**Run current script**”, the LED on the Raspberry Pi Pico will flash periodically.

![](./media/3c0b64be3cc1a0750f187e063dcabd29.png)

![Img](./media/img-20231116105340.png)

## Projects

### Project 01: Hello World

**Introduction**

For Raspberry Pi Pico beginners, we will start with some simple things. In this project, you only need a Raspberry Pi Pico and a USB cable to complete the "Hello World\!" project, which is a test of communication between Raspberry Pi Pico and the PC as well as a primary project.

**Components**

| ![img](./media/wps100.png) | ![img](./media/wps101.jpg) |
| ------------------------ | ------------------------ |
| Raspberry Pi Pico*1      | USB Cable*1              |

**Wiring Up**

In this project, we use a USB cable to connect the Raspberry Pi Pico to the computer.

![](./media/8ea81d60b8e2132c358041235490b7d5.jpeg)

**Online running code:**

To run the Raspberry Pi Pico online, you need to connect the Raspberry Pi Pico to your computer, which allows you to compile or debug programs using Thonny software.  

Advantages:

1). You can use the Thonny software to compile or debug programs. 
2). Through the "Shell" window, you can view error messages and output results generated during the running of the program as well as query related function information online to help improve the program.  

Disadvantages:

1). To run the Raspberry Pi Pico online, you must connect the Raspberry Pi Pico to a computer and run it with the Thonny software.  
2). If the Raspberry Pi Pico is disconnected from the computer, when they reconnect, the program won't run again.  

<span style="color: rgb(255, 76, 65);">Basic Operation:</span>

Open Thonny and click“Open...”.

![](./media/b65264767d6ff04d5f3530b8eebe218c.png)

Click“This computer”in the new pop-up window.

![](./media/5bdbc66ef89b41a53e46696c07b2c282.png)

In the new dialog box，select“Project\_01\_HelloWorld.py”,click“Open”.

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere.  For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

![](./media/9b61f563870ec1235e6cc48ca748cec5.png)

Click“Run current script”to execute the program“Hello World\!”, "Welcome Keyestudio" , which will be printed in the“Shell”window.

![](./media/39eb24657c5733544944dd643640a61d.png)

**Exit running online**

When running online, click ![Img](./media/img-20231116132129.png)“Stop /Restart Backend” or press “Ctrl+C” to exit the program.  

![](./media/dc2a210535724a7d601b5ad8b02ca8ed.png)

**Test Code**

```python
print("Hello World!")
print("Welcome Keyestudio")
```

### Project 02: Onboard LED flashing

**Introduction**

Raspberry Pi Pico has an onboard LED, which is a GP25 pin attached to the Raspberry Pi Pico. In this project, we will learn the effect of making the onboard LED blink. 

**Components**

| ![img](media/wps102.png) | ![img](media/wps103.jpg) |
| ------------------------ | ------------------------ |
| Raspberry Pi Pico*1      | USB Cable*1              |

**Wiring Up**

In this project, we use a USB cable to connect the Raspberry Pi Pico to the computer. Please refer to the documentation for the connection methods: Preparation for Python（Important）

![](./media/8ea81d60b8e2132c358041235490b7d5.jpeg)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere.  For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

**Code running online:**

Open“Thonny”，click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 02：Onboard LED flashing”.

![](./media/17519952e7c0019f1f0591903caa26d8.png)

Enter the file“Project 02：Onboard LED flashing”，double left-click the file“Project\_02\_Onboard\_LED\_flashing.py”, open it, as follows :

![](./media/87a877076f95cbe7d684ecc05de3e0cf.png)

```python
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


Ensure that the Raspberry Pi Pico is connected to the computer, click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”，then see what the **"Shell**" window displays.

![](./media/a53cb17aaa0b29d1c5f359f222868c69.png)

Click“![](./media/da852227207616ccd9aff28f19e02690.png)Run current script”， the code starts to execute, we will see that the LED on the Raspberry Pi Pico begins flashing. Press“Ctrl+C”or click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](./media/79796116d54281366ee2e4871dd4ca33.png)

![](./media/529c3be102eb7414ac1e5e66fb203b6e.png)

Note：This is the code that runs online.  If you disconnect the USB cable and restart the Raspberry Pi Pico, the LEDS on the Raspberry Pi Pico will stop flashing. The following information will be displayed in the "Shell" window of Thonny software:  

![](./media/dde0b82feb441565c2bfa9517dedfed0.png)

Code running offline（upload the code to the Raspberry Pi Pico）：

Ensure that the Raspberry Pi Pico is connected to the computer, click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](./media/705d3bdd9cad821399137c7c0df72e86.png)

As shown in the following figure, right-click the file “Project\_02\_Onboard\_LED\_flashing.py” and select“**Upload to /**” to upload the code to the Raspberry Pi Pico.  

![](./media/4e83ee98b0da014fae6896f4fb14c889.png)

Upload main.py in the same way

![](./media/1591c6146bbcd2df9c9ba1aec14a86ca.png)

Disconnect the USB cable from the Raspberry Pi Pico and reconnect, and the LED will flash repeatedly. 

![Img](./media/img-20231116105340.png)

Note: The code here runs offline.  If you want to stop it and display the information in the "Shell" window, simply click ![Img](./media/img-20231116132233.png)"Stop/Restart Backend" in Thonny software.  

![](./media/f7ca5b1be220957141fb119e6cc4ab37.png)

### Project 03：External LED flashing

**Introduction**

In this project, we are going to show you the external LED flashing effect.  We will use the Raspberry Pi Pico's digital pins to turn on the LED and make it flash.

**Components**

| ![img](media/wps104.png)            | ![img](media/wps105.jpg) | ![img](media/wps106.jpg) | ![img](media/wps107.jpg) |
| ----------------------------------- | ------------------------ | ------------------------ | ------------------------ |
| Raspberry Pi Pico*1                 | red LED*1                | 220Ω Resistor*1          | Jumper Wire*2            |
| ![img](media/wps110.jpg)            | ![img](media/wps109.jpg) | ![img](media/wps108.jpg) |                          |
| Raspberry Pi Pico Expansion Board*1 | Breadboard*1             | USB Cable*1              |                          |

**Knowledge**

**（1）LED:**

![img](media/wps105.jpg)

The LED is a kind of semiconductor called “light-emitting diode”, which is an electronic device made from semiconducting materials (silicon, selenium, germanium, etc.).  It has a anode and a cathode.  The short lead is cathode, which connects to GND, the long lead is anode , which connects to3.3V or 5V.

![](./media/f70404aa49540fd7aecae944c7c01f83.jpeg)

**(2) 5-band Resistor**

A resistor is an electronic component in a circuit that restricts or regulates the flow current flow. On the left is the appearance of the resistor and on the right is the symbol for the resistance in the circuit . Its unit is(Ω). 1 mΩ= 1000 kΩ，1kΩ= 1000Ω.

![image-20231013135230353](media/image-20231013135230353.png)

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

In the same voltage, there will be less current and more resistance. The connection between current, voltage, and resistance can be expressed by the formula: I=U/R. In the figure below, if the voltage is 3V, the current through R1 is: I = U / R = 3 V / 10 KΩ= 0.0003A=0.3mA.

![](./media/b3eec552e4dfad361833730698621776.png)

Do not directly connect resistors with very low resistance to the two poles of the power supply, as this will cause excessive current to damage the electronic components. Resistors do not have positive and negative poles.

**(3) Breadboard**

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

**How to use the keyestudio raspberry pico expansion board.**

Stack the Raspberry Pi Pico on the expansionboardto use, as shown below:


![](./media/fae969ca3b1a4592a83a4e05f5795a5b.png)

**Power Supply**

In this project, we use a USB to connect the Raspberry Pi Pico to the computer. Please refer to the documentation for connection methods:
Preparation for Python

![](./media/8ea81d60b8e2132c358041235490b7d5.jpeg)

**Circuit Diagram and Wiring Diagram**

First, cut all power to the Raspberry Pi Pico.  Then build the circuit according to the circuit diagram and wiring diagram.  After the circuits are set up and verified, using a USB cable to connect the Raspberry Pi Pico to a computer .  Note: Avoid any possible short circuits (especially connecting 3.3V and GND)\!

Warning: A short circuit may cause a large current in the circuit, causing components to overheat and permanent damage to the hardware.

![](./media/cb069d7553d861e3293d8bdbe85bbd05.png)

**Circuit Diagram**

![](./media/898285da10fa9b39e52a02bc68758d27.png)

**Wiring Diagram**

Note:

How to connect a LED

![](./media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω five-band resistor

![](./media/55c0199544e9819328f6d5778f10d7d0.png)

**Test Code**

According to the circuit diagram, when the GP16 output of the Pico is high, the LED will light up;  When the output power is low, the LED will light off.  Therefore, we can make the LED flash repeatedly by controlling the GP16 to repeatedly output high and low levels.  

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere.  For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Code running online:

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project
03：External LED flashing”.

![](./media/4607246406f23fa569aa3cea202f3863.png)

Enter the file“Project 03：External LED flashing”, double left-click“Project\_03\_External\_LED\_flashing.py”, open it, as shown below:

![](./media/387934a09c74f4d5c0e8ed19c4cde926.png)

```python
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

Ensure that the Raspberry Pi Pico is connected to the computer, click“Stop/Restart backend”and see what will display in
the“Shell”window.

![](./media/139fa290786502af65584b20ba61fb82.png)

Click“![](./media/da852227207616ccd9aff28f19e02690.png)Run current script”, the code starts to execute, and the LED will begin flashing. Press“Ctrl+C”or click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](./media/f0a8b15499b9ef17c9d09002aafa4d58.png)

![Img](./media/img-20231116151459.png)

<span style="color: rgb(255, 76, 65);">Note:</span> This is the code that runs online, if we disconnect the USB cable, then restart the“Raspberry Pi Pico”, the LED will stop flashing. The following information will be displayed in the "Shell" window of Thonny software:  

![](./media/20f0f44738c9119895ccbf2dadb21a65.png)

Code running offline（Upload the code to the Raspberry Pi Pico）：

Ensure that the Raspberry Pi Pico is connected to the computer, click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”

![](./media/6a9f8cdac46a55b5e0f3d8ba4ee6f0f9.png)

As shown below, right-click the file“Project\_03\_External\_LED\_flashing.py”，select**Upload to/**”to upload the code to the Raspberry Pi Pico.

![](./media/60ed038ee245d8c58cd921d388988b81.png)

Upload main\.py in the same way

![](./media/6ab80f86d06be94d54bd5c737370151d.png)

Disconnect the USB from the Raspberry Pi Pico and reconnect, the LED in the circuit will flash repeatedly.

![Img](./media/img-20231116151435.png)


Note: The code here runs offline.  If you want to stop and display the information in the Shell window, simply click“Stop/Restart backend” in Thonny software.  

![](./media/f7ca5b1be220957141fb119e6cc4ab37.png)


### Project 04: Breathing Led

**Introduction**

In previous studies, we know that LEDS have on/off state, so how to enter the intermediate state?  How to output an intermediate state to make the LED "half bright"?  That's what we're going to learn.  Breathing lights, or LEDS turn on and off again, which are like "breathing".  So, how to control the brightness of LEDS?  We will use the Raspberry Pi Pico PWM to achieve this goal.  

**Components**

| ![img](media/wps111.png) | ![img](media/wps112.jpg)            |
| ------------------------ | ----------------------------------- |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 |
| ![img](media/wps113.jpg) | ![img](media/wps114.jpg)            |
| Red LED*1                | 220ΩResistance*1                    |
| ![img](media/wps115.jpg) | ![img](media/wps116.jpg)            |
| Breadboard*1             | Jumper Wire*2                       |
| ![img](media/wps117.jpg) |                                     |
| USB Cable*1              |                                     |

**Knowledge**

![](./media/6549bdbfd4e7b6b2b341012105d655e8.png)

**Analog & Digital**

Analog signals are continuous signals in both time and value.  In contrast, a digital or discrete time signal is a time series consisting of a series of numbers.  Most signals in life are analog signals.  A familiar example of an analog signal is how temperatures change continuously throughout the day, rather than suddenly changing from 0 to 10 in a flash.  However, the value of a digital signal can change instantaneously. This change is represented numerically as 1 and 0(the basis of binary code).  It's easier to see the difference, as shown below:

![](./media/4bdf6127e563b453a1fd8953b4ebb277.png)

In practical applications, we often use a binary as a digital signal, which are a series of 0 and 1. Since binary signals have only two values (0 or 1), they have great stability and reliability.  Finally, analog and digital signals can be converted to each other. 

**PWM：**

Pulse Width Modulation (PWM) is an effective method to control analog circuit by digital signal.  Ordinary processors cannot directly output analog signals.  The PWM makes this conversion (convert digital signal to analog signal) very convenient, which uses digital pins to send square waves at a certain frequency, which is high and low output to alternate for a period of time.  The total time of each set of high and low levels is generally fixed, which is called the period (Note: the reciprocal of the period is the frequency). The time of the high level output is usually called pulse width, and the duty cycle is the percentage of the pulse width (PW) to the total period (T) of the waveform. The longer the duration of the high level output as well as the duty cycle is, the higher the corresponding voltage in the analog signal will be. The figure below shows the variation of analog signal voltage from 0V to 3.3V(high level is 3.3V) corresponding to pulse width of 0% to 100%.  

![](./media/a439e1bd8a4578b43b7188c821d58594.jpeg)

We all know that the longer the PWM duty cycle is, the higher the output power will be. Therefore, we can use PWM to control the brightness of LEDS or the speed of dc motors and so on.  As can be seen from the above, the PWM is not a real analog signal, and the effective value of the voltage is equal to the corresponding analog signal.  Therefore, we can control the output power of LEDS and other output modules to achieve different effects.

**Raspberry Pi Pico and PWM**

The Raspberry Pi Pico has 16 PWM channels, each of which can control frequency and duty cycle independently. The clock frequency ranges from 7Hz to 125MHz.  Each pin on the Raspberry Pi Pico can be configured for PWM output.  

**Circuit Diagram and** **Wiring Diagram**

![](./media/cb069d7553d861e3293d8bdbe85bbd05.png)

![](./media/898285da10fa9b39e52a02bc68758d27.png)

**Note:**

How to connect the LED

![](./media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω 5-band resistor

![](./media/55c0199544e9819328f6d5778f10d7d0.png)

**Test Code**

The design of this project makes the GP16 output PWM, and the pulse width gradually increases from 0% to 100%, and then gradually decreases from 100% to 0%.  

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere.  For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 04：Breathing Led”. And double left-click “Project\_04\_Breathing\_Led.py”.

![](./media/d0616993fc8b1deb9db4414e3146e602.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer, and click “![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](./media/4daa8b74aec8af6056ec2a61ebabf397.png)

Click“![](./media/da852227207616ccd9aff28f19e02690.png)Run current script”， the code starts to execute, we will see that The LEDS in the circuit fade from dark to light, and then from light to dark again, which is like breathing . Press“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Ctrl+C”or“Stop/Restart backend”to exit the program.

![](./media/957f4e2178c1126f724bc8e012568e31.png)

![image-20231013135940226](media/image-20231013135940226.png)


### Project 05：Traffic Lights

**Introduction**

Traffic lights are closely related to people's daily lives, which generally show red, yellow, and green. Everyone should obey the traffic rules, which can avoid many traffic accidents. In this project, we will use Raspberry Pi Pico and some LEDs (red, green and yellow) to simulate the traffic lights.

**Components Required**

| ![img](media/wps118.png) | ![img](media/wps119.jpg)            | ![img](media/wps120.jpg)                |
| ------------------------ | ----------------------------------- | --------------------------------------- |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | Red LED*1                               |
| ![img](media/wps121.jpg) | ![img](media/wps122.jpg)            | ![img](media/wps123-16971769965132.jpg) |
| Green LED*1              | USB Cable*1                         | 220ΩResistor*3                          |
| ![img](media/wps126.jpg) | ![img](media/wps124.jpg)            | ![img](media/wps125.jpg)                |
| Yellow LED*1             | Breadboard*1                        | Jumper Wires                            |

**Circuit Diagram and Wiring Diagram**



![](./media/98f9db025163638c33095cbd16abe7e7.png)

Note:

How to connect an LED

![](./media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω 5-band resistor

![](./media/55c0199544e9819328f6d5778f10d7d0.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→”Project 05：Traffic Lights”and double left-click the“Project\_05\_Traffic\_Lights.py”.

![](./media/23e79112920bc111a9bc621dc75162a0.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer, click “![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](./media/914349b7c46f99b24beaada57db00815.png)

Click“![](./media/da852227207616ccd9aff28f19e02690.png)Run current script”, the code starts executing, what we will see are below:

1). First, the green light will be on for 5 seconds and then off; 

2). Next, the yellow light blinks three times and then goes off. 

3). Then, the red light goes on for five seconds and then goes off. 
    

Repeat steps 1 to 3 above and press“Ctrl+C”or click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend” to exit the program.

![](./media/ff8674d60cc99a8c3bbef24bf65ae20c.png)

### Project 06: RGB LED

**Introduction**

![](./media/94bdff69e438989d8e0934e57f2e5c00.png)

RGB LEDS are made up of three colors (red, green, and blue) , which can emit different colors by mixing these three basic colors. In this project, we will introduce the RGB LED and show you how to use the Raspberry Pi Pico to control the RGB LED. Even though RGB LED is very basic, it is also a great way to learn the fundamentals of electronics and coding.

**Components Required**

| ![img](media/wps127.png) | ![img](media/wps128.jpg)            | ![img](media/wps129.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | RGB LED*1                |
| ![img](media/wps130.jpg) | ![img](media/wps131.jpg)            | ![img](media/wps132.jpg) |
| 220ΩResistor*3           | Breadboard*1                        | Jumper Wires             |
| ![img](media/wps133.jpg) |                                     |                          |
| USB Cable*1              |                                     |                          |

**Component Knowledge**

The monitors mostly adopt the RGB color standard, and all the colors on the computer screen are composed of the three colors of red, green and blue mixed in different proportions.

![](./media/8bf1339719a922f2fbc1e01a4347b4ab.png)

This RGB LED has 4 pins and a common cathode. To change its brightness, we can use the PWM of the Raspberry Pi Pico pins, which can give different duty cycle signals to the RGB LED to produce different colors.

If we use three 10-bit PWM to control the RGBLED, theoretically we can create ![Img](./media/img-20231117083036.png) = 1,073,741,824(1 billion) colors through different combinations.

**Circuit Diagram and Wiring Diagram**

![](./media/f6950bc8498e6139cbb67db84cdd5a9a.png)

![](./media/fdab8c2fd2dfdd1670c09962e7b458ce.png)

Note:

RGB LED longest pin (common cathode) connected to GND.

![](./media/1584356c63bf99934ae0810ee02dced3.png)

How to identify the 220Ω 5-band resistor

![](./media/55c0199544e9819328f6d5778f10d7d0.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 06：RGB LED”. And double left-click the“Project\_06\_RGB\_LED.py”.

![](./media/4d197d2ef390d93cbdcd6606fa754188.png)

```pyton
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](./media/a2b85aea8a2bd67ad184662be36a1c9e.png)

Click ![](./media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts executing, we will see that RGB LED starts showing random colors. Press“Ctrl+C”or click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](./media/296bcab9a2eaccf483b8cb9e8b8a0e43.png)


### Project 07: Flowing Water Light

**Introduction**

In our daily life, we can see many billboards made up of different colors of LED. They constantly change the light to attract the attention of customers. In this project, we will use Raspberry Pi Pico to control 10 LEDs to achieve the effect of flowing water.

**Components Required**

| ![img](media/wps134.png) | ![img](media/wps135.jpg)            | ![img](media/wps136.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | Red LED*10               |
| ![img](media/wps137.jpg) | ![img](media/wps138.jpg)            | ![img](media/wps139.jpg) |
| 220ΩResistor*10          | Breadboard*1                        | Jumper Wires             |
| ![img](media/wps140.jpg) |                                     |                          |
| USB Cable*1              |                                     |                          |

**Circuit Diagram and Wiring Diagram**

![](./media/fc6e73a6664012c9a33262b50d6e256f.png)

Note:

How to connect the LED

![](./media/42ff6f405dfa128593827de5aa03e94b.png)

How to identify the 220Ω 5-band resistor

![](./media/55c0199544e9819328f6d5778f10d7d0.png)

**Test Code**

This project is to design and manufacture a flowing water light.  Here are the steps: first , turn on LED \#1, then turn it off.  Second, turn on LED \#2, then turn off... . Do the same for the 10 LEDs until the last one is turned off.  Repeating the process to achieve the "movement" of the water.

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 07：Flowing Water Light”. And double left-click the“Project\_07\_Flowing\_Water\_Light.py”.

![](./media/a923fafe77f629ea8288ec40b52a6059.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](./media/b908750521d4d2b64c55751825916a7e.png)

Click ![](./media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts executing, we will see that the 10 LEDs will light up from left to right and then return from right to left. Press“Ctrl+C”or click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](./media/c9814fae261b7f8c9d2b33938d8e6144.png)

![image-20231013142059620](media/image-20231013142059620.png)


### Project 08: 1-Digit Digital Tube

**Introduction**

The seven-segment digital tube is an electronic display device that displays decimal numbers. It is widely used in digital clocks,
electronic meters, basic calculators and other electronic devices that display digital information. The tubes are an alternative to more complex dot-matrix displays that are easy to use in both limited light conditions and strong sunlight. In this project, we will use the Raspberry Pi Pico to control 1-digit digital tube to display numbers.

**Components Required**

| ![img](media/wps141.png) | ![img](media/wps142.jpg)            | ![img](media/wps143.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | 1-digit Digital Tube*1   |
| ![img](media/wps144.jpg) | ![img](media/wps145.jpg)            | ![img](media/wps146.jpg) |
| 220ΩResistor*8           | Breadboard*1                        | Breadboard Wires         |
| ![img](media/wps147.jpg) |                                     |                          |
| USB Cable*1              |                                     |                          |

**Component Knowledge**

**Display principle:** The digital tube display is a semiconductor light-emitting device. Its basic unit is a light-emitting diode (LED).
The digital tube display can be divided into 7-segment digital tube and 8-segment digital tube according to the number of segments. The8-segment digital tube has one more LED unit than the 7-segment digital tube (used for decimal point display). Each segment of the 7-segment LED display is a separate LED. According to the connection mode of the LED unit, the digital tube can be divided into a common anode digital tube and a common cathode digital tube.

In the common cathode 7-segment digital tube, all the cathodes (or negative electrodes) of the segmented LEDs are connected together, so you should connect the common cathode to GND. To light up a segmented LED, you can set its associated pin to“HIGH”.

In the common anode 7-segment digital tube, the LED anodes (positive electrodes) of all segments are connected together, so you should connect the common anode to “+5V”. To light up a segmented LED, you can set its associated pin to “LOW”.

![](./media/28fd057848fbe0e8c8e3362768e7aa44.png)

Each part of the digital tube is composed of an LED. So when you use it, you also need to use a current limiting resistor. Otherwise, the LED will be damaged. In this experiment, we use an ordinary common cathode one-bit digital tube. As we mentioned above, you should connect the common cathode to GND. To light up a segmented LED, you can set its
associated pin to “HIGH”.

**Circuit Diagram and Wiring Diagram**

![](./media/84e67e0ce2d7627a96b83156324d92d5.png)

**Note:** The direction of the 7-segment digital tube inserted into the breadboard is the same as the wiring diagram, and there is one more point in the lower right corner.

![](./media/66da2f88234019c4a712494174ea4426.png)

![](./media/d99daa4165cf32b2283aae82466981bd.png)

**Test Code**

The digital display is divided into 7 segments, and the decimal point display is divided into 1 segment. When certain numbers are displayed, the corresponding segment will be illuminated. For example, when the number 1 is displayed, segments b and c will be opened.

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 08：1-Digit Digital Tube”. And double left-click the“Project\_08\_One\_Digit\_Digital\_Tube.py”.

![](./media/c9b3cf2f06c5261b112afde681d7c3a2.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/f6eed549d1acfd058333e95306edeb1d.png)

Click“![](./media/da852227207616ccd9aff28f19e02690.png)Run current script”, the code starts executing, we will see that the 1-digit digital tube will display numbers from 9 to 0. Press“Ctrl+C”or click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](./media/4d06038bf94823da20012d28475cc6b9.png)


### Project 09：4-Digit Digital Tube

**Introduction**

The 4-digit 7-segment digital tube is a very practical display device, and it is used for devices such as electronic clocks and score counters. Due to the low price and it is easy to use, more and more projects will use 4-digit 7-segment digital tubes. In this project, we will use the Raspberry Pi Pico to control a 4-bit 7-segment digital tube to create a manual counter.

**Components Required**

| ![img](media/wps148.png)      | ![img](media/wps149.jpg)            |                          |
| ----------------------------- | ----------------------------------- | ------------------------ |
| Raspberry Pi Pico*1           | Raspberry Pi Pico Expansion Board*1 |                          |
| ![img](media/wps150.jpg)      | ![img](media/wps151.jpg)            | ![img](media/wps152.jpg) |
| 4-Digit Digital Tube Module*1 | M-F Dupont Wires                    | USB Cable*1              |

**Component Knowledge**

**TM1650 4-digit digital tube:** It is a 12-pin 4-digit tube display module with clock dots. The driver chip is TM1650 which only needs 2 signal lines to enable the microcontroller to control the 4-digit 8-segment digital tube. The control interface level can be 5V or 3.3V.

**Specifications of 4-bit digital tube module:**

Working voltage: DC 3.3V-5V

Maximum current: 100MA

Maximum power: 0.5W

**Schematic diagram of 4-digit digital tube module:**

![](./media/5f400887c90fc00098a3e77beca656ef.png)

**Circuit Diagram and Wiring Diagram**

![](./media/39b708e69b2fb10057b71fe2321584b2.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 09：4-Digit Digital Tube”. Select“TM1650\.py”，right-click and select“**Upload to /**”， and wait for“TM1650\.py to be uploaded to the Raspberry Pi Pico. And double left-click the“Project\_09\_Four\_Digit\_Digital\_Tube.py”.

![](./media/b4026879bc9491754fa118c103e86c5f.png)

![](./media/0c3fcafccf88e7e48fbaf712a94b367a.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](./media/682029610c29b14122b37787bbd2ae53.png)

Click“![](./media/da852227207616ccd9aff28f19e02690.png)Run current script”, the code starts executing, we will see that the 4-digit digital tube circularly displays numbers from 0000 to 9999. Press“Ctrl+C”or click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](./media/3ef28f4dda60e7c14e1ffd8aa5d823aa.png)

### Project 10：8×8 Dot-matrix Display

**Introduction**

The dot-matrix display is an electronic digital display device that can show information on machines, clocks and many other devices. In this project, we will use the Raspberry Pi Pico to control the 8x8 LED dot matrix to make a“❤”pattern.

**Components Required**

| ![img](media/wps153.png)  | ![img](media/wps154.jpg)            |                          |
| ------------------------- | ----------------------------------- | ------------------------ |
| Raspberry Pi Pico*1       | Raspberry Pi Pico Expansion Board*1 |                          |
| ![img](media/wps155.jpg)  | ![img](media/wps156.jpg)            | ![img](media/wps157.jpg) |
| 8*8 Dot-matrix Display *1 | M-F Dupont Wires                    | USB Cable*1              |

**Component Knowledge**

**8\*8 Dot-matrix display module:**

The 8\*8 dot matrix is composed of 64 LEDs, and each LED is placed at the intersection of a row and a column. When using a single-chip microcomputer to drive an 8\*8 dot matrix, we need to use a total of 16 digital ports, which greatly wastes the data of the single-chip microcomputer. For this reason, we specially designed this module, using the HT16K33 chip to drive an 8\*8 dot matrix, and only need to use the I2C communication port of the single-chip microcomputer to control the dot matrix, which greatly saves the microcontroller resources.

**Specifications:**

Working voltage: DC 5V

Current: 200MA

Maximum power: 1W

**Schematic diagram:**

Some modules have three DIP switches that you can flip at will. These switches are used to set the I2C communication address. The setting method is as follows. The module has fixed the communication address. A0, A1 and A2 are connected to GND, and the address is 0x70.  

![Img](./media/img-20231116110058.png)

**Circuit Diagram and Wiring Diagram**

![](./media/f4fc6111c35b571928d0f0a4a4bf45b3.png)

![](./media/ad529b82657cd9c7ddcd4b8828a0b1e8.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny, click “This computer” → “D:” → “Python_Codes(Windows)” → “Project 10：8×8 Dot-matrix Display”. Select “ht16k33\_matrix.py” and “matrix\_fonts.py”, right-click and select “**Upload to /**” and wait for “ht16k33\_matrix.py” and “matrix\_fonts.py” to be uploaded to the Raspberry Pi Pico. And double left-click the “Project\_10\_8×8\_Dot\_Matrix\_Display.py”.

![](./media/487405e5443d1dcba1706351ffea6d11.png)

![](./media/7a3a8ed25fcc739a74453588dfe3abd5.png)

![](./media/0e9ede0023678e49711608cf3845505a.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/d195d37e4eb32c656c741c8c6c391572.png)

Click“Run current script”, the code starts executing, we will see that the 8 x 8 dot matrix displays the character "A" 1S, "B" 1S, and "C" 1S. Then scroll to display the string "Hello World” repeatedly. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/476f84b2194fc6ef6e9d2df0cbd787d4.png)
### Project 11：74HC595N Control 8 LEDs

**Introduction**

In previous projects, we have learned how to light an LED.  However, how to light up a lot of LEDs with only 26 I/O ports on the Raspberry Pi Pico? Sometimes we may run out of pins , at that time, we need to extend it with the shift register. You can use a 74HC595N chip to control up to eight outputs at a time, using only a few pins on your microcontroller. In addition, You can also connect multiple registers together to further expand the output. In this project, we will use a Raspberry Pi Pico, a 74HC595 chip and LEDs to make a flowing water light to understand the function of the chip.  

**Components Required**

| ![img](media/wps158.png) | ![img](media/wps159.jpg)            | ![img](media/wps160.jpg) | ![img](media/wps161.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | 74HC595N Chip*1          | Red LED*8                |
| ![img](media/wps162.jpg) | ![img](media/wps163.jpg)            | ![img](media/wps164.jpg) | ![img](media/wps165.jpg) |
| 220ΩResistor*8           | Breadboard*1                        | Jumper Wires             | USB Cable*1              |

**Component Knowledge**

![](./media/6921c6d60135e072ed4bd24564ec4a6d.png)

**74HC595N Chip:** To put it simply, 74HC595N chip is a combination of 8-digit shifting register, memorizer and equipped with tri-state output. The shift register and the memorizer are synchronized to different clocks, and the data is input on the rising edge of the shift register clock SCK and goes into the memory register on the rising edge of the memory register clock RCK. If the two clocks are connected together, the shift register is always one pulse earlier than the storage register.

The shift register has a serial shift input (SI) and a serial output (SQH) for cascading. The 8-bit shift register can be reset
asynchronously (low-level reset), and the storage register has an 8-bit three-state parallel bus output, when the output enable (OE) is enabled (active low), the storage register is output to the 74HC595N pin (bus).

![](./media/858b189f06ad68afe051b15043b2affd.png)

**Pins**：

| PIN                   | FUNCTION                                                     |
| --------------------- | ------------------------------------------------------------ |
| Pin13 OE              | It is an output enable pin to ensure that the data of the latch is input to the Q0 to Q7 pins or not. When it is low, no high level is output. In this experiment, we directly connect to GND and keep the data output low. |
| Pin14 SI              | This is the pin for 74HC595 to receive data, i.e. serial data input, only one bit can be input at a time, then 8 times in a row, it can form a byte. |
| Pin10 SCLR            | A pin to initialize the storage register pins. It initializes the internal storage registers at a low level. In this experiment, we connect VCC to maintain a high level. |
| Pin11  SCK            | The clock pin of the shift register. At the rising edge, the data in the shift register is shifted backward as a whole, and new data input is received. |
| Pin12 RCK             | The clock input pin of the storage register . At the rising edge, the data is transferred from the shift register to the storage register. At this time, the data is output in parallel from the Q0 to Q7 ports. |
| Pin9 SQH              | It is a serial output pin dedicated for chip cascading to the SI terminal of the next 74HC595. |
| Q0--Q7(Pin 15,Pin1-7) | Eight-bit parallel output, can directly control the 8 segments of the digital tube. |

**Circuit Diagram and Wiring Diagram**

![](./media/1738cecf584c83b55370153ebc1688b7.png)

Note: Pay attention to the direction in which the 74HC595N chip is inserted.

![](./media/a6d03617539b70d6d69fa7e9acb25be9.png)

![](./media/91833532723f4ee623902c0252092741.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 11：74HC595N Control 8 LEDs”. Select“my74HC595\.py”， right-click and select“**Upload to /**”，wait for“my74HC595\.py”to be uploaded to the Raspberry Pi Pico. And double left-click the “Project\_11\_74HC595N\_Controls\_8\_LEDs.py”.

![](./media/e062ee8e0d8ac1aaba4df1ff403d3cf3.png)

![](./media/2325da1459f6092c063eac913e620264.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/faebdbd5720409f07bf6c03ee6ba9d65.png)

Click “![](./media/da852227207616ccd9aff28f19e02690.png)Run current script”, the code starts executing, we will see that the 8 LEDs start flashing in flowing water mode. Press “Ctrl+C” or click “![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend” to exit the program.

![](./media/eda98e28568ebec03cc1ec41ec6492b1.png)

### Project 12：Active Buzzer

**Introduction**

Active buzzer is a sound making element, which is widely used on computers, printers, alarms, electronic toys, telephones, timers, etc. It has an inner vibration source. In this project, we will use a Raspberry Pi Pico to control the active buzzer to buzz.

**Components Required**

| ![img](media/wps169.png) | ![img](media/wps170.jpg)            | ![img](media/wps171.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | Active Buzzer*1          |
| ![img](media/wps166.jpg) | ![img](media/wps167.jpg)            | ![img](media/wps168.jpg) |
| Breadboard*1             | Jumper Wires                        | USB Cable*1              |

**Component Knowledge**

The active buzzer inside has a simple oscillator circuit , which can convert constant direct current into a certain frequency pulse signal. Once active buzzer receives a high level, it will sound. The passive buzzer is an integrated electronic buzzer with no internal vibration source. It must be driven by 2K to 5K square wave instead of a DC signal. The appearance of the two buzzers is very similar, but passive buzzers come with a green circuit board, and active buzzers come with a black tape. Passive buzzers don't have positive pole, but active buzzers have. As shown below:

![](./media/0f9825969867ac2d65bb1a19ed0ad2ab.png)

**Circuit Diagram and Wiring Diagram**

![](./media/48e73ef2d6090fe7cda58c385bad2ab2.png)

![](./media/56df73f7ac711e510b30164c5759615f.png)

Note:

1)\. The buzzer power supply in this circuit is 5V.  On a 3.3V power supply, the buzzer will work, but it will reduce the loudness.  

2)\. The VUSB should connect to the positive terminal of the USB cable, if it connects to GND, it could burn out the computer or Raspberry Pi Pico.  Similarly, the Raspberry Pi Pico's 36-40 pins need to be connected carefully to avoid short circuits. 

3)\. The positive terminal ("+"/long pin) of the active buzzer is connected to pin 16, and the negative terminal (short pin) is connected to GND.

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 12：Active Buzzer”. And double left-click the Project\_12\_Active\_Buzzer.py”.

![](./media/a2b4775a67925f2380686d61ec5e9b71.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer, and click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](./media/29ff4d3cfefcc7cef8786a31d004da30.png)

Click “![](./media/da852227207616ccd9aff28f19e02690.png)Run current script”, the code starts executing, we will see that the the active buzzer starts to buzz. Press “Ctrl+C” or click “![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend” to exit the program.

![](./media/655dae76dfb3987d7ed9bc5838711b2e.png)
### Project 13：Passive Buzzer

**Introduction**

In a previous project, we have learned an active buzzer, which can only produce one sound and may let you feel monotonous. In this project, we will learn a passive buzzer and use the Raspberry Pi Pico to control the passive buzzer to sound an alarm. Unlike the active buzzer, the passive buzzer can emit sounds of different frequencies.

**Components Required**

| ![img](media/wps175.png) | ![img](media/wps176.jpg)           | ![img](media/wps177.jpg) |
| ------------------------ | ---------------------------------- | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi PicoExpansion Board*1 | Passive Buzzer*1         |
| ![img](media/wps172.jpg) | ![img](media/wps173.jpg)           | ![img](media/wps174.jpg) |
| Breadboard*1             | Jumper Wires                       | USB Cable*1              |

**Component Knowledge**

![](./media/8d0020e53824072cbe9d4f7d2f8acb4f.png)

A passive buzzer is an integrated electronic buzzer with no internal vibration source. It must be driven by 2K to 5K square wave, not a DC signal. The two buzzers are very similar in appearance, but one buzzer with a green circuit board is a passive buzzer, while the other with black tape is an active buzzer. Passive buzzers cannot distinguish between positive polarity while active buzzers can.

![](./media/fc42c5ed014609ff0b290ee5361bb2fd.png)

**Circuit Diagram and Wiring Diagram**

![](./media/e0da1ccdbff24d256db130816c55da74.png)

![](./media/e601e48f8deddb3e9e7734d0022106b3.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 13：Passive Buzzer”. And double left-click the“Project\_13\_Passive\_Buzzer.py”.

![](./media/4e4cf166f1de082468ebf77ef6ba3d4d.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/699667c6aea0990e6a2fa408ef7ca3a1.png)

Click “![](./media/da852227207616ccd9aff28f19e02690.png)Run current script”, the code starts executing, we will see that the the passive buzzer sounds the alarm. Press “Ctrl+C” or click “![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend” to exit the program.

![](./media/02d6cb5bd3d2cef4e669886b957544ed.png)


### Project 14 : Mini Table Lamp

**Introduction**

Did you know that a Raspberry Pi Pico can light up an LED when you press a button? In this project, we will use the Raspberry Pi Pico, a key switch and an LED to make a Mini Table lamp.

**Components Required**

| ![img](media/wps178.png) | ![img](media/wps179.jpg)            | ![img](media/wps180.jpg) | ![img](media/wps181.jpg) | ![img](media/wps182.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ | ------------------------ | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | Button*1                 | Red LED*1                | 10KΩResistor*1           |
| ![img](media/wps183.jpg) | ![img](media/wps184.jpg)            | ![img](media/wps185.jpg) | ![img](media/wps186.jpg) | ![img](media/wps187.jpg) |
| Breadboard*1             | 220ΩResistor*1                      | USB Cable*1              | JumperWires              | Button Cap*1             |

**Component Knowledge**

![](./media/5b8fea4657b47510d199f740fdcaaa9d.png)

**Button:** The button can control the circuit on and off. The circuit is disconnected when the button is not pressed. But it breaks when you release it. Why does it only work when you press it? It starts from the internal structure of the button, which is shown in the figure:![](./media/d2a204e61c768f18924150db58aee093.png). 

Before the button is pressed, 1 and 2 are on, 3 and 4 are also on, but 1, 3 or 1, 4 or 2, 3 or 2, 4 are off (not working). Only when the button is pressed, 1, 3 or 1, 4 or 2, 3 or 2, 4 are on. The key switch is one of the most commonly used components in circuit design.

**Schematic diagram of the button:**

![](./media/5e42fde9876f9be810d85a7fb8b331f7.png)![](./media/8677548f9e756281629430d66ba3a460.png)

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

**Circuit Diagram and Wiring Diagram**

![](./media/0753a2a452e0292b31f79f9b6dabb0cc.png)

![](./media/a03a6553dc194ab61fb7b4d914740f90.png)

**Note:**

How to connect the LED

![](./media/f70404aa49540fd7aecae944c7c01f83.jpeg)

How to identify the 220Ω 5-band resistor and 10KΩ 5-band resistor

![](./media/55c0199544e9819328f6d5778f10d7d0.png)

![](./media/246cf3885dc837c458a28123885c9f7b.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 14：Mini Table Lamp”. And double left-click the“Project\_14\_Mini\_Table\_Lamp.py”.

![](./media/0efc0a37e75cff4ac3d0007dbf3f2829.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](./media/32daa1b963c18ba89686184df6e0ffe9.png)

Click ![](./media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts executing, we will see that press the button, the LED lights up;  when the button is released, the LED remains lit.  Press the button again, the LED goes off;  When the button is released, the LED remains off. Doesn't it look like a little lamp? Press“Ctrl+C”or click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](./media/f208593b20f934d9b8c71e6e7905cccd.png)
### Project 15：Tilt And LED

**Introduction**

The ancients without electronic clocks, so the hourglass are invented to measure time.  The hourglass has a large capacity on both sides, and which is filled with fine sand on one side. What’s more, there is a small channel in the middle, which can make the hourglass stand upright , the side with fine sand is on the top. 

However, due to the action of gravity, the fine sand will flow down through the channel to the other side of the hourglass. When the sand reaches the bottom, turn it upside down and record the number of times it has gone through the hourglass, therefore, the next day we can know the approximate time of the day by it. In this project, we will use a Raspberry Pi Pico to control the tilt switch and LED lights to simulate an hourglass and make an electronic hourglass. 

**Components Required**

| ![img](media/wps188.png) | ![img](media/wps189.jpg)            | ![img](media/wps190.jpg) | ![img](media/wps191.jpg) | ![img](media/wps192.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ | ------------------------ | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | Tilt Switch*1            | Red LED*4                | 10KΩResistor*1           |
| ![img](media/wps193.jpg) | ![img](media/wps194.jpg)            | ![img](media/wps195.jpg) | ![img](media/wps196.jpg) |                          |
| Breadboard*1             | 220ΩResistor*4                      | USB Cable*1              | Jumper Wires             |                          |

**Component Knowledge**

![](./media/8c40739f8e05f753f145420b421a0f47.png)

Tilt switch is also called digital switch. Inside is a metal ball that can roll. The principle of rolling the metal ball to contact with the
conductive plate at the bottom, which is used to control the on and off of the circuit. When it is a rolling ball tilt sensing switch with single directional trigger, the tilt sensor is tilted toward the trigger end (two gold-plated pin ends), the tilt switch is in a closed circuit and the voltage at the analog port is about 5V (binary number is 1023).

In this way, the LED will light up. When the tilt switch is in a horizontal position or tilted to the other end, it is open and the
voltage of the analog port is about 0V (binary number is 0), the LED will turn off. In the program, we judge the state of the switch based on whether the voltage value of the analog port is greater than 2.5V (binary number is 512).

As shown in the figure, use the internal structure of the tilt switch to illustrate how it works.

![](./media/bf8b10ad248ac939ac4ef96d02ed87c7.png)

**Circuit Diagram and Wiring Diagram**

![](./media/8735f9531646b77c35932404a681b76d.png)

![](./media/9127e65ff0d7b3d5e579263fd06ec674.png)

Note:

How to connect the LED

![](./media/f70404aa49540fd7aecae944c7c01f83.jpeg)

How to identify the 220Ω 5-band resistor and 10KΩ 5-band resistor

![](./media/55c0199544e9819328f6d5778f10d7d0.png)

![](./media/246cf3885dc837c458a28123885c9f7b.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 15：Tilt And LED”. And double left-click the“Project\_15\_Tilt\_And\_LED.py”.

![](./media/f6e58ba03bbfa0cf1707b1e48ae4968d.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](./media/d1171ab1ce593168fbe85f0b36ab5a0f.png)

Click ![](./media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts executing, we will see that when you tilt the breadboard to an angle, the LEDs will light up one by one. When you turn the breadboard to the original angle, the LEDs will turn off one by one. Like the hourglass, the sand will leak out over time. Press“Ctrl+C”or click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](./media/71e2f26ed3dc928a66d9950e8862cfed.png)
### Project 16：Burglar Alarm

**Introduction**

PIR motion sensor measures the thermal infrared (IR) light emitted by moving objects. The sensor can detect the movement of people, animals, and cars to trigger safety alarms and lighting. They are used to detect movement and ideal for security such as burglar alarms and security lighting systems. In this project, we will use a Raspberry Pi Pico to control PIR motion sensor, buzzers and LEDs to simulate burglar alarms.

**Components Required**

| ![img](media/wps197.png) | ![img](media/wps198.jpg)            | ![img](media/wps199.jpg) | ![img](media/wps200.jpg) | ![img](media/wps201.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ | ------------------------ | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | PIR Motion Sensor*1      | Active Buzzer*1          | Red LED*1                |
| ![img](media/wps202.jpg) | ![img](media/wps203.jpg)            | ![img](media/wps204.jpg) | ![img](media/wps205.jpg) | ![img](media/wps206.jpg) |
| Breadboard*1             | F-F Dupont Wires                    | 220ΩResistor*1           | USB Cable*1              | Jumper Wires             |

**Component Knowledge**

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

**Circuit Diagram and Wiring Diagram**

![](./media/8af6a40d69c138216548320abc46ed35.png)

![](./media/d028bb819eed7cf3a08af69a47ecfce6.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 16：Burglar Alarm”. And double left-click the“Project\_16\_Burglar\_Alarm.py”.

![](./media/7f73cbbb7625a6a44b48265d65a3c61d.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](./media/e14873ab851f66c6e90699457100c992.png)

Click ![](./media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts executing, we will see that If the PIR motion sensor detects someone nearby, the buzzer will give an alarm and the LEDs will flash continuously. At the same time, the "Shell" window of the Thonny IDE will print the string "ALARM\! Motion detected\!" Press“Ctrl+C”or click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](./media/7883b057dfdf98de0af0bdc02012d93f.png)
### Project 17: I2C 128×32 LCD

**Introduction**

We can use modules such as monitors to do various experiments in life. You can also DIY a variety of small objects. For example, you can make a temperature meter with a temperature sensor and display, or make a distance meter with an ultrasonic module and display.

In this project, we will use the LCD\_128X32\_DOT module as a display and connect it to a Raspberry Pi Pico, which will be used to control the LCD\_128X32\_DOT display to show various English characters, common symbols and numbers.

**Components Required**

| ![img](media/wps207.png) | ![img](media/wps208.jpg) | ![img](media/wps209.jpg) | ![img](media/wps210.jpg) |
| ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| Raspberry Pi Pico*1      | LCD_128X32_DOT*1         | 10CM M-F Dupont Wires    | USB Cable*1              |

**Component Knowledge**

![](./media/2c2645e94a00867ac23e8a022f0a631a.png)

**LCD\_128X32\_DOT:** It is an LCD module with 128\*32 pixels and its driver chip is ST7567A. The module uses the IIC communication mode, while the code contains a library of all alphabets and common symbols that can be called directly. When using, we can also set it in the code so that the English letters and symbols show different text sizes. To make it easy to set up the pattern display, we also provide a mold capture software that converts a specific pattern into control code and then copies it directly into the test code for use.

**Schematic diagram:**

![](./media/5451aed32bc5b7b30fbd5613ad09a65b.png)

**Features:**

Pixel: 128\*32 character

Operating voltage(chip)：4.5V to 5.5V

Operating current：100mA (5.0V)

Optimal operating voltage(module):5.0V

**Circuit Diagram and Wiring Diagram**

Note: The LCD\_128X32\_DOT must be connected with 10CM M-F Dupont wires, which can make the LCD\_128X32\_DOT display normally. Otherwise, using 20CM M-F Dupont wires may cause the LCD\_128X32\_DOT display abnormally.  

![](./media/82aae0a70e5628c53d7f81f7730cf79a.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 17： I2C 128×32 LCD”. Select“lcd128\_32.py”and“lcd128\_32\_fonts.py”，right-click and select“**Upload to /**”，wait for the“lcd128\_32.py”and the“lcd128\_32\_fonts.py”to be uploaded to the Raspberry Pi Pico. And double left-click the“Project\_17\_I2C\_128\_32\_LCD.py”.

![](./media/5179fb729732c80c15e04f98dcdb3e79.png)

![](./media/8f22ebcc66f08942fe2b2219f98eef55.png)

![](./media/9cfe11b33969c11c04f707a031065b15.png)

```python
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

if use_i2c:
    scan_for_devices()
    lcd = lcd128_32(data_pin, clock_pin, bus, i2c_addr)

lcd.Clear()

lcd.Cursor(0, 4)
lcd.Display("KEYESTUDIO")
lcd.Cursor(1, 0)
lcd.Display("ABCDEFGHIJKLMNOPQR")
lcd.Cursor(2, 0)
lcd.Display("123456789+-*/<>=$@")
lcd.Cursor(3, 0)
lcd.Display("%^&(){}:;'|?,.~\\[]")
"""
while True:
    scan_for_devices()
    time.sleep(0.5)
"""
```

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](./media/64d9744cb23391f83a080f35475f2d73.png)

Click“![](./media/da852227207616ccd9aff28f19e02690.png)Run current script”, the code starts executing, we will see that the LCD module display will show "KEYESTUDIO" at the first line. "ABCDEFGHIJKLMNOPQR" will be displayed at the second line. "123456789 + - \* / \<\> = $ @ " will be shown at the third line and "% ^ & () {} :; '|?,. \~ \\\\ \[\] " will be displayed at the fourth line. Press“Ctrl+C”or click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](./media/e481e701c6323f7b36dcafb33ea55c6f.png)
### Project 18：Small Fan

**Introduction**

In the hot summer, we need an electric fan to cool us down, so in this project, we will use a Raspberry Pi Pico to control 130 motor module and small blade to make a small fan.

**Components Required**

| ![img](media/wps211.png) | ![img](media/wps212.jpg)            |                          |
| ------------------------ | ----------------------------------- | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 |                          |
| ![img](media/wps213.jpg) | ![img](media/wps214.jpg)            | ![img](media/wps215.jpg) |
| 130 Motor Module*1       | M-F Dupont Wires                    | USB Cable*1              |

**Component Knowledge**

![](./media/a572bcde7a5e3bf01d273b3d9a024701.png)

130 motor module: The motor control module uses the HR1124S motor control chip, which is a single-channel H-bridge driver chip for DC motor. The H-bridge driving part of the HR1124S features low on-resistance PMOS and NMOS power tube. The low on-resistance ensures low power loss of the chip, making the chip work safely for a longer time. In addition, HR1124S has low standby current and low quiescent current, which makes HR1124S easy to be used in toy scheme.

**Features:**

Working voltage: 5V

Working current: 200MA

Working power: 2W

Working temperature: -10℃\~ +50℃

**Schematic diagram:**

![](media/image-20231013144859189.png)

**Circuit Diagram and Wiring Diagram**

![](./media/98c9335e5ef2e5304e2cddde04e6e168.png)

![](./media/aad9f071a4d7a6a9a62c2899c78822b8.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 18：Small Fan”. And double left-click the“Project\_18\_ Small\_Fan.py”.

![](./media/0a7b9fe7963cba3df7b1a96be10702eb.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/7e210ba077606904946c6fff935d2ba3.png)

Click “Run current script”, the code starts executing, we will see that the small fan turns counterclockwise for 5 seconds and stops for 2 seconds, and then turns clockwise for 5 seconds and stops for 2 seconds. Repeat this rule for 5 times and then the small fan stops. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/71e2f26ed3dc928a66d9950e8862cfed.png)


### Project 19：Servo Sweep

**Introduction**

Servo is a kind of motor that can rotate very precisely. It has been widely used in toy cars, RC helicopters, airplanes, robots, etc. In this project, we will use a Raspberry Pi Pico to control the rotation of the servo.

**Components Required**

| ![img](media/wps216.png) | ![img](media/wps217.jpg)            |                          |
| ------------------------ | ----------------------------------- | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 |                          |
| ![img](media/wps218.jpg) | ![img](media/wps219.jpg)            | ![img](media/wps220.jpg) |
| Servo*1                  | JumperWires                         | USB Cable*1              |

**Component Knowledge**

**Servo:**

![](./media/99830768916233a9c5900ac399006c17.png)

The servo is a kind of position servo driver, which is mainly composed of housing, circuit board, coreless motor, gear and position detector. The working principle is that the receiver or microcontroller sends a signal to the servo, which has an internal reference circuit that generates a reference signal with a period of 20ms and a width of 1.5ms, and compares the DC bias voltage with the voltage of the potentiometer to output voltage difference. 

The IC on the circuit board determines the direction of rotation, and then drives the coreless motor to start rotation and transmits the power to the swing arm through the reduction gear, while the position detector sends back a signal to determine
whether it has reached the positioning. It is suitable for those control systems that require constant change of angle and can be maintained.

When the motor rotates at a certain speed, the potentiometer is driven by the cascade reduction gear to rotate so that the voltage difference is 0 and the motor stops rotating. The angle range of general servo rotation is 0 to 180 degrees.

The pulse period for controlling the servo is 20ms, the pulse width is 0.5ms to 2.5ms, and the corresponding position is -90° to +90°. The following is an example of a 180 degree servo.

![](./media/708316fde05c62113a3024e0efb0c237.jpeg)

Servo motors have many specifications, but they all have three connecting wires, which are brown, red, and orange (different brands may have different colors). The brown is GND, the red is the positive power supply, and the orange is the signal line.

![](./media/3f5bc31305e64108bed3b3619d602891.jpeg)

**Wiring Diagram**

When supplying the servo, please note that the power supply voltage should be 3.3V-5V. Make sure there are no errors when connecting the servo to the power supply.

 

![](./media/64a80947d0cd45b50d4bd1d125509bbe.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 19：Servo Sweep”. Select“myservo.py”，right-click and select“Upload to/”, waiting for the“myservo.py”to be uploaded to the Raspberry Pi Pico. And double left-click the“Project\_19\_Servo\_Sweep.py”.

![](./media/31cd81f84d6666bf9806abddbe0d1632.png)

![](./media/7167ad374cdf0aa592739e0aa9f0dcec.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/e04de0afec735a4f27700be0d990121d.png)

Click “Run current script”, the code starts executing, we will see that the servo will rotate from 0° to 180°, then reverse direction to rotate from 180° to 0°, and repeat these actions in an infinite loop. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/33bbece8b90ae027e1a8af54fcbac01e.png)

![](./media/c5250405a4290ecb2d758ff1097310c7.png)
### Project 20：Stepping Motor

**Introduction**

Stepping motors are accurately positioned and are the most important components in industrial robots, 3D printers, large lathes, and other mechanical devices. In this project, we will use a Raspberry Pi Pico to control the ULN2003 stepper motor drive board to make the motors rotate.

**Components Required**

| ![img](media/wps221.png) | ![img](media/wps222.jpg)            | ![img](media/wps223.png)            |
| ------------------------ | ----------------------------------- | ----------------------------------- |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | ULN2003 Stepper Motor Drive Board*1 |
| ![img](media/wps224.jpg) | ![img](media/wps225.jpg)            | ![img](media/wps226.jpg)            |
| Stepper Motor *1         | M-F Dupont Wires                    | USB Cable*1                         |

**Component Knowledge**

![](./media/8ebb14a35091dc8d02d95cb6748dd1e9.png)

**Stepper motor:** It is a motor controlled by a series of electromagnetic coils. It can rotate by the exact number of degrees (or
steps) needed, allowing you to move it to a precise position and keep it there. It does this by supplying power to the coil inside the motor in a very short time, but you must always supply power to the motor to keep it in the position you want. There are two basic types of stepping motors, namely unipolar stepping motor and bipolar stepping motor. In this project, we use a 28-BYJ48 unipolar stepper motor.

![](./media/bea0e202b7bfe23d1fdcdbbe996aa6da.jpeg)

**Working Principle:**

The stepper motor is mainly composed of a stator and a rotor. The stator is fixed. As shown in the figure below, the part of the coil group A, B, C, and D will generate a magnetic field when the coil group is energized. The rotor is the rotating part. As follows, the middle part of the stator, two poles are permanent magnets.

![](./media/32748e0804b1fff434181cb228b23242.png)

Single -phase four beat: At the beginning, the coils of group A are turned on, and the poles of the rotor point at A coil. Next, the group A coil are disconnected, and the group B coils are turned on. The rotor will turn clockwise to the group B. Then, group B is disconnected, group C is turned on, and the rotor is turned to group C. After that, group C is disconnected, and group D is turned on, and the rotor is turned to group D. Finally, group D is disconnected, group A is turned on, and the rotor is turned to group A coils. Therefore, rotor turns 180° and continuously rotates B-C-D-A, which means it runs a circle (eight phase). As shown below, he rotation principle of stepper motor is A - B C - D - A.

You make order inverse(D - C - B - A - D .....) if you want to make stepper motor rotate anticlockwise.

![](./media/b8ae50bbdee2dd5bc683e8c450baee6a.png)

Half-phase and eight beat: 8 beat adopts single and dual beat way，A - AB B - BC - C - CD - D - DA - A ...... ，rotor will rotate half phase in this order. For example, when A coil is electrified，rotor faces to A coil , then A and B coil are connected, on this condition, the strongest magnetic field produced lies in the central part of AB coil, which means rotating half-phase clockwise.

**Stepper Motor Parameters:**

The rotor rotates one circle when the stepper motor we provide rotates 32 phases and with the output shaft driven by 1:64 reduction geared set. Therefore the rotation (a circle) of output shaft requires 32 \* 64 =2048 phases.

The step angle of 4-beat mode of 5V and 4-phase stepper motor is 11.25. And the step angle of 8-beat mode is 5.625, the reduction ratio is 1:64.

**ULN2003Stepper Motor Drive Board:** It is a stepper motor driver, which converts the weak signal into a stronger control signal to drive the stepper motor. 

The following schematic diagram shows how to use the ULN2003 stepper motor driver board interface to connect a unipolar stepper motor to the pins of the Raspberry Pi Pico, and shows how to use four TIP120 interfaces.

![](./media/6fa632d2b70e97dd55565d23ec15d245.png)

**Schematic Diagram and Wiring Diagram:**

![](./media/ba02656bb1cb44ce8edb187a10dc7bef.png)

![](./media/6f72f7b5f6a520099d7714236372a9fe.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 20：Stepping Motor”. And double left-click the“Project\_20\_Stepping\_Motor.py”.

![](./media/34958f86adf283299bb17c3ae3ac5533.png)

```python
from machine import Pin
import time
 
### Pin initialization
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
 
### Pin output low level
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](./media/b7c4b4c9d56f42d1319ce3f08dd5f3b2.png)

Click“![](./media/da852227207616ccd9aff28f19e02690.png)Run current script”, the code starts executing, we will see that the four LEDS ( D1,D2,D3 ,D4) on the ULN2003 drive module will light up. The stepper motor rotates clockwise first, then counterclockwise, and keeps this state circulating. Press“Ctrl+C”or click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](./media/cfd6cf396fa21c64aced220a9a402490.png)

![](./media/8dc4a0547390e0108c3960c31d330ee7.png)
### Project 21：Relay

**Introduction**

In daily life, we generally use AC to drive electrical equipment, and sometimes we use switches to control electrical appliances. If the switch is directly connected to the AC circuit, once electricity leakage occurs, people are in danger. From a safety point of view, we specially designed this relay module with NO (normally open) and NC (normally closed) terminals. In this lesson we will learn a special and easy-to-use switch, which is the relay module.

**Components Required**

| ![img](media/wps227.png) | ![img](media/wps228.jpg)            | ![img](media/wps229.jpg) | ![img](media/wps230.jpg) | ![img](media/wps231.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ | ------------------------ | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | Relay Module*1           | M-F Dupont Wires         | USB Cable*1              |

**Component Knowledge**

**Relay:** It is an "automatic switch" that uses a small current to control the operation of a large current.

Input voltage：3.3V-5V

Rated load：5A 250VAC (NO/NC) 5A 24VDC (NO/NC)

The rated load means that devices with dc voltage of 24V or AC voltage of 250V can be controlled using 3.3V-5V microcontrollers.  

**Schematic diagram of the Relay:**

![image-20231013145356951](media/image-20231013145356951.png)

**Wiring Diagram**

![](./media/0e76ea13b2034301be2ecdfde7f21f1e.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 21：Relay”. And double left-click the“Project\_21\_Relay.py”.

![](./media/6b610e7e5081befcea5305663f426d38.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](./media/e9e38c240d8278f282fd2912cc73d331.png)

Click![](./media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts executing, we will see that the relay will cycle on and off, on for 1 second, off for 1 second.  At the same time, you can hear the sound of the relay on and off, and you can also see the change of the indicator light on the relay. Press“Ctrl+C”or click![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”to exit the program.

![](./media/be6f35e062c5656930fffa6dce839777.png)
### Project 22 : Dimming Light

**Introduction**

A potentiometer is a three-terminal resistor with a sliding or rotating contact that forms an adjustable voltage divider. It works by varying the position of a sliding contact across a uniform resistance. In a potentiometer, the entire input voltage is applied across the whole length of the resistor, and the output voltage is the voltage drop between the fixed and sliding contact.

In this project, we are going to learn how to use Raspberry Pi Pico to read the values of the potentiometer, and make a dimming lamp with LEDs.

**Components Required**

| ![img](media/wps232.png) | ![img](media/wps233.jpg)            | ![img](media/wps234.jpg) | ![img](media/wps235.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | Potentiometer*1          | Red LED*1                |
| ![img](media/wps236.jpg) | ![img](media/wps237.jpg)            | ![img](media/wps238.jpg) | ![img](media/wps239.jpg) |
| Breadboard*1             | 220ΩResistor*1                      | Jumper Wires             | USB Cable*1              |

**Component Knowledge**

![](./media/03ab81e8b4f09287d2781ef0fd297f85.png)

**Adjustable potentiometer:** It is a kind of resistor and an analog electronic component, which has two states of 0 and 1(high level and low level). The analog quantity is different, its data state presents a linear state such as 1 \~ 1024.

**Read the Potentiometer Value**

We connect the adjustable potentiometer to the analog IO of the Raspberry Pi Pico to read its value and voltage value . Please refer to the following wiring diagram for wiring.

![](./media/b8ee6320bce8729a4309857f257d30ec.png)

![](./media/cb970a340d830569e9ac4462a1318e44.png)

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 22：Dimming Light”. And double left-click the“Project\_22.1\_Read\_Potentiometer\_Analog\_Value.py”.

![](./media/d9cf3ce6c364675b7e787b625232e23a.png)

```python
from machine import ADC, Pin
import time
# Initialize the potentiometer to pin 26 (ADC function)
adc = ADC(26)

### Print the current adc value of the potentiometer cyclically 
### Print the current voltage value of the potentiometer cyclically
try:
    while True:
        adcValue = adc.read_u16() # read the ADC value of potentiometer
        voltage = adcValue / 65535.0 * 3.3
        print("ADC Value:", adcValue, "Voltage:", voltage, "V")
        time.sleep(0.1)
except:
    pass
```


Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/463e789ae8824b5c724e8ff9a084a674.png)

Click “Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the ADC value and voltage value of the potentiomete, turn the potentiometer handle, the ADC value and voltage value will change. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/00c8eafb82c2ade2b6efe03ff4c5d8ac.png)

![](./media/969b9de3cf505f05d6a9361286cef9c9.png)

**Circuit Diagram and Wiring Diagram**

In the last step, we read the value of the potentiometer, and now we need to convert the value of the potentiometer into the brightness of the LED to make a lamp that can adjust the brightness. The wiring diagram is as follows:

![](./media/66f721b77035d40556c873e0c4577b4a.png)

![](./media/93b03f3cdc8af506d9035b748839ac33.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 22：Dimming Light”. And double left-click the“Project\_22.2\_Dimming\_Light.py”.

![](./media/a9b04adef7ed5ed1429a923974241984.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/1d2b9866779f2f666fcf4a65e22a2173.png)

Click “Run current script”, the code starts executing, we will see that turn the potentiometer handle and the brightness of the LED will change accordingly. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/a00b986be5645a89d8fbcfb235b79cb9.png)

![](./media/eca30dead3f4923afa0dcb0306db2319.jpeg)
### Project 23：Flame Alarm

**Introduction**

Fire is a terrible thing and fire alarm systems are very useful in houses, commercial buildings and factories. In this project, we will use a Raspberry Pi Pico to control a flame sensor , a buzzer and LEDs to make fire alarm devices, which is a meaningful maker activity.

**Components Required**

| ![img](media/wps240.png) | ![img](media/wps241.jpg)            | ![img](media/wps242.jpg) | ![img](media/wps243.jpg) | ![img](media/wps244.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ | ------------------------ | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | Flame Sensor*1           | Red LED*1                | Active Buzzer*1          |
| ![img](media/wps245.jpg) | ![img](media/wps246.jpg)            | ![img](media/wps247.jpg) | ![img](media/wps248.jpg) | ![img](media/wps249.jpg) |
| Breadboard               | 220ΩResistor*1                      | 10KΩResistor*1           | Jumper Wires             | USBCable*1               |

**Component Knowledge**

![](./media/a50ec3e38adf10643eafac8cb62bec8a.png)

**Flame Sensor**：The flame emits a certain degree of IR light, which is invisible to the human eye, but our flame sensor can detect it and alert the microcontroller. If the Raspberry Pi Pico has detected a fire, it has a specially designed infrared receiver to detect the flame, and then convert the flame brightness into a fluctuating level signal. The short pin of the receiving triode is negative pole and the other long pin is positive pole. We should connect the short pin (negative pole) to 5V and the long pin (positive pole) to the analog pin, a resistor and GND. As shown in the figure below.

![](./media/87bd204db523c602c80745266c1ee452.png)

Note: Since vulnerable to radio frequency radiation and temperature changes, the flame sensor should be kept away from heat sources like radiators, heaters and air conditioners, as well as direct irradiation of sunlight, headlights and incandescent light.

**Read the Simulation Value**

We start with a simple code to read the value of the flame sensor and print it on the serial monitor. For wiring, please refer to the
following wiring diagram.

![](./media/85531078db041bba05599b3a1118a7bc.png)

![](./media/1e3c424f7cc7ac797ab0b8ae4a00f4f1.png)

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 23：Flame Alarm”. And double left-click the“Project\_23.1\_Read\_Analog\_Value\_Of\_Flame\_Sensor.py”.

![](./media/1022a0e91bbb58b2ef61716f04ac94c5.png)

```python
from machine import ADC, Pin
import time
# Initialize the flame sensor to pin 26 (ADC function)
adc = ADC(26)

# Read the current analog value of the flame sensor and return [0, 1023]
def get_value():
    return int(adc.read_u16() * 1024 / 65536)
 
### Print the current value of the flame sensor cyclically, value=[0, 1023]
while True:
    value = get_value()
    print(value)
    time.sleep(0.1)
```


Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

Click “Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the simulation value read by the flame sensor. When the flame is close to the sensor, the simulation value increases. On the contrary, the simulated value decreases. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/c3b2a4122662e655eb45e32937732991.png)

![](./media/7c04b9dd8c4a10e7b9788ecd95eeeeaa.png)

**Circuit Diagram and Wiring Diagram** 

Next, we will use a flame sensor, a buzzer, and LEDs to make an interesting project, that is flame alarm. When flame is detected, the LED flashes and the buzzer alarms.

![](./media/c2b7feb8039e618ba070a9714ef06554.png)

![](./media/0cd1ee17a6f8de81464817090c5832eb.png)

**Test Code**

（Note：![](./media/40a3ea572836945268b22dfc0cce29c3.png) The threshold of 500 in the code can be reset itself as required)

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 23：Flame Alarm”. And double left-click the“Project\_23.2\_Flame\_Alarm.py”.

![](./media/e2d832ba9e809f04f0990d9df446acf6.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/5197b36be26f10de1b40e5c814974ab3.png)

Click “Run current script”, the code starts executing, we will see that when the flame sensor detects the flame, the LED flashes and the buzzer alarms. Otherwise, the LED does not light, the buzzer does not sound. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/536af226e9ed390ca3cc102b0f02f9cb.png)
### Project 24：Night Lamp

**Introduction**

Sensors or components are ubiquitous in our daily life. For example, some public street lights turn on automatically at night and turn off automatically during the day. 

Why? In fact, this make use of a photosensitive element that senses the intensity of external ambient light. When the outdoor brightness decreases at night, the street lights will automatically turn on. In the daytime, the street lights will automatically turn off. The principle of this is very simple. In this lesson we will use Raspberry Pi Pico to control LEDs to implement the function of this street light.

**Components Required**

| ![img](media/wps250.png) | ![img](media/wps251.jpg)            | ![img](media/wps252.jpg) | ![img](media/wps253.jpg) | ![img](media/wps254.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ | ------------------------ | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | Photoresistor*1          | Red LED*1                | 10KΩResistor*1           |
| ![img](media/wps255.jpg) | ![img](media/wps256.jpg)            | ![img](media/wps257.jpg) | ![img](media/wps258.jpg) |                          |
| Breadboard*1             | 220ΩResistor*1                      | Jumper Wires             | USB Cable*1              |                          |

**Component Knowledge**

![](./media/9e553e75b6f976f33438171eb2f2e775.png)

It is a photosensitive resistor, its principle is that the photoresistor surface receives brightness (light) to reduce the resistance. The resistance value will change with the detected intensity of the ambient light . With this property, we can use photoresistors to detect light intensity.  Photoresistors and other electronic symbols are as follows:


![](./media/7d575da675a2f6cb511d28b801e2abaa.png)

The following circuit is used to detect changes in resistance values of photoresistors:

![](./media/5a7f7e641eb78007760a94151c1d80a5.png)

In the circuit above, when the resistance of the photoresistor changes due to the change of light intensity, the voltage between the  photoresistor and resistance R2 will also change.  Thus, the intensity of light can be obtained by measuring this voltage.

**Read the Analog Value**

We first use a simple code to read the value of the photoresistor, print it in the serial monitor. For wiring, please refer to the following wiring diagram.

![](./media/e3fde13b200927346e04b032373ce638.png)

![](./media/b97ff27ae10e3499c36312c8ee4881f8.png)

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 24：Night Lamp”. And double left-click the“Project\_24.1\_Read\_Photosensitive\_Analog\_Value.py”.

![](./media/bbda9735710eb80196f54a5096f16799.png)

```python
from machine import ADC, Pin
import time
# Initialize the photoresistance to pin 26 (ADC function)
adc = ADC(26)

# Read the current analog value of the photoresistance and return [0, 1023]
def get_value():
    return int(adc.read_u16() * 1024 / 65536)
 
### Print the current value of the photoresistance cyclically, value=[0, 1023]
while True:
    value = get_value()
    print(value)
    time.sleep(0.1)
```


Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/8a0c37dff4793d4132a9c88e932f499b.png)

Click “Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the analog value read by the photoresistor. When the light intensity around the photoresistor is gradually reduced, the analog value will gradually increase. On the contrary, the analog value decreases gradually. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/889383400283bc151486ce0bf5820a92.png)

![](./media/bbabb2d5c4a997c5024e6023cb272261.png)

**Circuit Diagram and Wiring Diagram**

We made a little dimmer in the front, now let's make a light controlled lamp. The principle is the same, the Raspberry Pi Pico will be used to obtain the analog value of the sensor and then adjust the brightness of the LED.  

![](./media/b8e8d95bdc869bf76465fa73645db831.png)

![](./media/71f2886dc6fa97d02e2ecd0d429af71b.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 24：Night Lamp”. And double left-click the“Project\_24.2\_Night\_Lamp.py”.

![](./media/c08014a9603cbf3b2411440b5e7d761e.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/dcf4815ce265653df6759637b24087c0.png)

Click “Run current script”, the code starts executing, we will see that when the intensity of light around the photoresistor is reduced, the LED will be bright, on the contraty, the LED will be dim. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/03dd68eab6f2579e15852f13c10ddc98.png)
### Project 25：Human Induction Lamp

**Introduction**

With the development of science and technology, the use of human induction lamp that usually used in the dark corridor area is very common in our real life, such as the corridor of the community, the bedroom of the room, the garage of the dungeon, the bathroom and so on. The human induction lamp are generally composed of a PIR Motion Sensor, a lamp, a photoresistor sensor and so on. In this project, we will learn how to use a PIR Motion Sensor, LEDs, and a photoresistor to make a human induction lamp .

**Components Required**

| ![img](media/wps259.png) | ![img](media/wps260.jpg)            | ![img](media/wps261.jpg) | ![img](media/wps262.jpg) | ![img](media/wps263.jpg) |                          |
| ------------------------ | ----------------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | Photoresistor*1          | Red LED*1                | 10KΩResistor*1           |                          |
| ![img](media/wps264.jpg) | ![img](media/wps265.jpg)            | ![img](media/wps266.jpg) | ![img](media/wps267.jpg) | ![img](media/wps268.jpg) | ![img](media/wps269.jpg) |
| Breadboard*1             | PIR Motion Sensor*1                 | 220ΩResistor*1           | F-F Dupont Wires         | Jumper Wires             | USB Cable*1              |

**Circuit Diagram and Wiring Diagram**

![](./media/79c069794eed2b3eb611f4aee7952862.png)

![](./media/643c9552a922ed3ddde80be42481481d.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 25：Human Induction Lamp”. And double left-click the“Project\_25\_Human\_ Induction\_Lamp.py”.

![](./media/810cf76703d01a67fb24892be056ea26.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/5328e0e2f11967549f347f7719420f02.png)

Click “Run current script”, the code starts executing, we will see that when your hand covers the light-sensitive part of the photoresistor to simulate darkness, the Raspberry Pi Pico's built-in LED will light up. Then shake it in front of the PIR motion sensor with your other hand, the external LED will light up, too, and after a delay of a few seconds, the external LED will automatically turn off.  

At the same time, the "Shell" window of Thonny IDE will print the delay time when the external LED lights up . If the sensitive part of the photoresistor is not covered, you can see that the the Raspberry Pi Pico's built-in LED lights go out , at this time, shake in front of the PIR motion sensor with your hand, the external LED is off. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/1694a3ff1f0fd065862961ebde40c063.png)

![](./media/af94ad9d2f008956592ee64e207aa8b5.png)
### Project 26：Sound Control Fan

**Introduction**

The sound sensor has a built-in capacitive electret microphone and power amplifier. It can be used to detect the sound intensity of the environment. In this project, we use a Raspberry Pi Pico to control a sound sensor and a motor module to make a voice-activated fan.

**Components Required**

| ![img](media/wps270.png) | ![img](media/wps271.jpg)            | ![img](media/wps272.jpg) | ![img](media/wps273.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | Sound Sensor*1           | USB Cable*1              |
| ![img](media/wps274.jpg) | ![img](media/wps275.jpg)            | ![img](media/wps276.jpg) |                          |
| 130 Motor Module*1       | F-F Dupont Wires                    | M-F Dupont Wires         |                          |

**Component Knowledge**

**Sound sensor** is usually used to detect the loudness of the sound in the surroundings. Arduino can collect its output signal through the analog input interface. The S pin is an analog output, which is the real-time output of the microphone voltage signal. The sensor comes with a potentiometer so you can adjust the signal strength. It also has two fixing holes so that the sensor can be installed on any other equipment. You can use it to make some interactive works, such as voice-operated switches.

**Read the Analog Value of the Sound Sensor**

We first use a simple code to read the analog value of the sound sensor and print it to the serial monitor, please refer to the following wiring diagram for the wiring.

![](./media/7bcfe48423953695c677c0c504d8f745.png)

![](./media/547329f9d46a7267798728d385b60912.png)

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 26：Sound Control Fan”. And double left-click the“Project\_26.1\_Read\_Sound\_Sensor\_Analog\_Value.py”.

![](./media/dcb5c22ff7ba7c8f1ca0621b6d2edd8b.png)

```python
from machine import ADC, Pin
import time
# Initialize the sound sensor to pin 28 (ADC function)
adc = ADC(28)

# Read the current analog value of the sound sensor and return [0, 1023]
def get_value():
    return int(adc.read_u16() * 1024 / 65536)
 
### Print the current value of the sound sensor cyclically, value=[0, 1023]
while True:
    value = get_value()
    print(value)
    time.sleep(0.1)
```


Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/cbb7fb1e59c8224034609e4672482714.png)

Click “Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the analog values read by the sound sensor. When you clap your hands to the sensor, the analog value of the sound sensor will change significantly. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/033a647d45e8b533d703af6c57bd503a.png)

![](./media/ebe92f3cc97f7d21b92d498c9f04f625.png)

**Wiring Diagram**

Next, we use a sound sensor, a 130 motor module and a fan leaf to make a voice-activated fan. The wiring diagram is as follows.

![](./media/631b461716fe53a2c1138f561acae5f7.png)

![](./media/340c224f0f71765f71d17afc623d595d.png)

**Test Code**

（Note：![](./media/c20911df19d11290cf099072fe250029.png)The threshold 600 in the code can be reset itself as needed)

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 26：Sound Control Fan”. And double left-click the“Project\_26.2\_Sound\_Control\_Fan.py”.

![](./media/2fd3e5837ddbbe6883f558f9f3922a49.png)

```python
from machine import ADC, Pin
import time
 
# Onboard LED light initialization
led = Pin(25, Pin.OUT)
 
# Initialize the Sound sensor to pin 28 (ADC function)
adc = ADC(28)
 
### Pin initialization
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
        led.value(0)   # Set led turn off
```

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/4ef29066484fdc0818796ad3cffcfc61.png)

Click“Run current script”, the code starts executing, we will see that clap your hands to the sound sensor, and when the sound intensity exceeds a threshold, the small fan spins while the Raspberry Pi Pico's built-in LED lights up.  Instead, the small fan doesn't rotate, and the Raspberry Pi Pico's built-in LEDS don't light up. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/ab4cfcab677950942adac1410e7e7e6e.png)
### Project 27：Temperature Measurement

**Introduction**

LM35 is a commonly used and easy-to-use temperature sensor. It does not require other hardware, only needs an analog port. The difficulty lies in compiling the code and converting the analog values to Celsius temperature. In this project, we use a temperature sensor and 3 LEDs to make a temperature tester. When the temperature sensor touches objects with different temperature, the LEDs will show different colors.

#**Components Required**

| ![img](media/wps277.png) | ![img](media/wps278.jpg)            | ![img](media/wps279.jpg) | ![img](media/wps280.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | LM35Temperature Sensor*1 | USB Cable*1              |
| ![img](media/wps281.jpg) | ![img](media/wps282.jpg)            | ![img](media/wps283.jpg) | ![img](media/wps284.jpg) |
| 220Ω Resistor*3          | Red LED*1                           | Yellow LED*1             | Green LED*1              |
| ![img](media/wps285.jpg) | ![img](media/wps286.jpg)            | ![img](media/wps287.jpg) |                          |
| F-F Dupont Wires         | Breadboard*1                        | Jumper Wires             |                          |

**Component Knowledge**

![](./media/0fded1cfe95575d0fa4aa03839d8e30d.png)

**Working principle of LM35 temperature sensor:** LM35 is a widely used temperature sensor with many different package types. At room temperature, it can achieve the accuracy of 1/4°C without additional calibration processing. LM35 temperature sensor can produce different voltage by different temperature. When the temperature is 0 ℃, it outputs 0V. If increasing 1 ℃, the output voltage will increase 10mv. The output temperature is 0℃ to 100℃, the conversion formula is as follows.

![](./media/0dfa07fa69f2a98658a3822c2da93bf7.jpeg)

**Read the Temperature Value**

We first use a simple code to read the value of the temperature sensor, print it in the serial monitor. The wiring diagram is shown below.

![](./media/952016b1b69fcad9f4eea889de63106a.png)

![](./media/2c05b1929588977832c955526f519e89.png)

LM35 output is given to analog pin GP26 of theRaspberry Pi Pico. This analog voltage is converted to its digital form and processed to get the temperature reading.

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 27：Temperature Measurement”. And double left-click the“Project\_27.1\_Read\_LM35\_Temperature\_Value.py”.

![](./media/e2cf3b46ed80db641574699f08923ee8.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/03e9ea412789d6560b11e25e2fbe48dc.png)

Click “Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the temperature values read by the LM35 temperature sensor. Hold the LM35 element by hand, the temperature value read by the LM35 temperature sensor will change. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/de9286949268fb2f1202ba91ff143b13.png)

![](./media/9c2c52dbee8a37315075178f167ba342.png)

**Circuit Diagram and Wiring Diagram**

Now we use a LM35 temperature sensor and three LED lights to do a temperature test. When the LM35 temperature sensor senses different temperatures, different LED lights will light up. Follow the diagram below for wiring.

![](./media/65b5f44e3a73ff102a40f6c90bdf6d4c.png)

![](./media/fa3eddc7bda77c7c8420d0f3a0b0d2eb.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 27：Temperature Measurement”. And double left-click the“Project\_27.2\_Temperature\_Measurement.py”.

<span style="color: rgb(255, 76, 65);">Note:</span> The temperature threshold in the code can be reset itself as required.  

![](./media/0496bf3b0c767e809c6ecd8b7bdc9ba3.png)

```python
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
    time.sleep(1)
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/25cd2e58ae326217ffbe622a282b0b8b.png)

Click “Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the temperature values read by the LM35 temperature sensor. When the LM35 temperature sensor senses different temperatures, different LEDS will light up. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/bbe1ee004d2a3daeb041da650c1768f6.png)
### Project 28：Rocker control light

**Introduction**

The joystick module is a component with two analog inputs and one digital input. It is widely used in game operation, robot control, drone control and other fields.

In this project, we will use a Raspberry Pi Pico and a joystick module to control RGB. You can have a deeper understanding of the principle and operation of the joystick module in practice.

**Components Required**

| ![img](media/wps288.png) | ![img](media/wps289.jpg)            | ![img](media/wps290.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | Joystick Module*1        |
| ![img](media/wps291.jpg) | ![img](media/wps292.jpg)            | ![img](media/wps293.jpg) |
| RGB LED*1                | 220ΩResistor*3                      | Jumper Wires             |
| ![img](media/wps294.jpg) | ![img](media/wps295.jpg)            | ![img](media/wps296.jpg) |
| USB Cable*1              | M-F Dupont Wires                    | Breadboard*1             |

**Component Knowledge**

![](./media/d087b123748cbfb8ed9f517150db71c5.png)

**Joystick module**: It mainly uses PS2 joystick components. In fact, the joystick module has 3 signal terminal pins, which simulate a
three-dimensional space. The pins of the joystick module are GND, VCC, and signal terminals (B, X, Y). The signal terminals X and Y simulate the X-axis and Y-axis of the space. When controlling, the X and Y signal terminals of the module are connected to the analog port of the microcontroller. The signal terminal B simulates the Z axis of the space, it is generally connected to the digital port and used as a button.

VCC is connected to the microcontroller power output VCC (3.3V or 5V), GND is connected to the microcontroller GND, the voltage in the original state is about 1.65V or 2.5V. In the X-axis direction, when moving in the direction of the arrow, the voltage value increases, and the maximum voltage can be reached. Moving in the opposite direction of the arrow, the voltage value gradually decreases to the minimum voltage. In the Y-axis direction, the voltage value decreases gradually as it moves in the direction of the arrow on the module, decreasing to the minimum voltage. As the arrow is moved in the opposite direction, the voltage
value increases and can reach the maximum voltage. In the Z-axis direction, the signal terminal B is connected to the digital port and outputs 0 in the original state and outputs 1 when pressed. In this way, we can read the two analog values and the high and low level conditions of the digital port to determine the operating status of the joystick on the module.

**Features:**

Input Voltage：DC 3.3V \~ 5V

Output Signal：X/Y dual axis analog value +Z axis digital signal

Range of Application：Suitable for control point coordinate movement in plane as well as control of two degrees of freedom steering gear, etc.  

Product Features：Exquisite appearance, joystick feel superior, simple operation, sensitive response, long service life.  

**Read the Value**

We have to use analog Raspberry Pi Pico pin IO to read the data from X or Y pins, and use digital IO port to read the values of the button. Please follow the wiring diagram below for wiring.

![](./media/36004a41553a2f413ba05775e9b696eb.png)

![](./media/b843cdff62b3ccf3f3f028a834b468aa.png)

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 28：Rocker control light”. And double left-click the“Project\_28.1\_Read\_Rocker\_Value.py”.

![](./media/6b333ee03c3f9fb71860c83c1bcae81b.png)

```python
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
 
### Print the current value of the X axis,Y axis,Z axis cyclically.
while True:
    value_x = read_x()
    value_y = read_y()
    state = btn_state()
    print("x:%d, y:%d, press:%s" % (value_x, value_y, state))
    time.sleep(0.1)
```


Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/3981469747a51ddd09a4c177e9b56adf.png)

Click “Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the analog and digital values of the current joystick. Moving the joystick or pressing it will change the analog and digital values in "Shell". Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/7e4012f9f4e55f14361b0db5b443f78d.png)

![](./media/c8097bd115d4c564192c19a08df2702a.jpeg)

![](./media/20904cf7c75d3dd861da3b3575670a0e.png)

**Circuit Diagram and Wiring Diagram**

We just read the value of the joystick module. Now we need to do something with the joystick module and RGB, connecting according to the following diagram.

![](./media/000ec2c5dae0b0d5368569abbd026f35.png)

![](./media/68601044f75ee6840f0b97cad9bea891.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 28：Rocker control light”. And double left-click the“Project\_28.2\_Rocker\_Control\_Light.py”.

![](./media/ffadbdf940cf18a81dd2c7b618dc0159.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/79afea801b881d4c848bb295da1ee833.png)

Click“Run current script”, the code starts executing, we will see that①If the joystick is moved to the far left in the X direction, the RGB light turns red. ② If the joystick is moved to the far right in the X direction, the RGB light turns green. ③If the joystick is moved to the top in the Y direction, the RGB light turns white. ④If the joystick is moved to the bottom in the Y direction, the RGB light turns blue. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/e93935d3790240b04176f479f1981313.png)

![](./media/9c2d0d8777200827b16c49b752d45c4c.jpeg)
### Project 29：Temperature and Humidity Meter 

**Introduction**

In winter, the humidity in the air is very low, that is, the air is very dry. Coupled with the cold, the human skin is prone to crack from excessive dryness. Therefore, you need to use a humidifier to increase the humidity of the air at home. But how do you know that the air is too dry? Then you need equipment to detect air humidity. In this lesson, we will learn how to use the temperature and humidity sensor. We use the sensor to create a thermohygrometer and also combined with an LCD\_128X32\_DOT to display the temperature and humidity values.

**Components Required**

| ![img](media/wps297.png) | ![img](media/wps298.jpg)          | ![img](media/wps299.jpg) |
| ------------------------ | --------------------------------- | ------------------------ |
| Raspberry Pi Pico*1      | Temperature and Humidity Sensor*1 | LCD 128X32 DOT*1         |
| ![img](media/wps300.jpg) | ![img](media/wps301.jpg)          | ![img](media/wps302.jpg) |
| 20CM M-F Dupont Wires    | 10CM M-F Dupont Wires             | USB Cable*1              |

**Component Knowledge**

![](./media/34bafe8113e2db36c8f0c8492b835474.png)

**Temperature and Humidity Sensor:** It is a temperature and humidity composite sensor with calibrated digital signal output. Its accuracy humidity is ±5%RH, temperature is ±2℃. Range humidity is 20 to 90%RH, and temperature is 0 to 50℃. The temperature and humidity sensor applies dedicated digital module acquisition technology and temperature and humidity sensing technology to ensure extremely high reliability and excellent long-term stability of the product. The temperature and humidity sensor includes a resistive-type humidity measurement and an NTC temperature measurement component, which is very suitable for
temperature and humidity measurement applications where accuracy and real-time performance are not required.

The operating voltage is in the range of 3.3V to 5.5V.

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

![image-20231013151445240](media/image-20231013151445240.png)

**Read the Value**

![](./media/c3b585b4747d3ba04be7af544bbbe27c.png)

![](./media/751a9a67b2657cac8dfaddf451e7b74a.png)

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 29：Temperature Humidity Meter”. Select“dht11.py”， right-click and select“Upload to /”，waiting for the “dht11.py”to be uploaded to the Raspberry Pi Pico. And double left-click the“Project\_29.1\_Detect\_Temperature\_Humidity.py”.

![](./media/4e72290107f42992138c883132081bac.png)

![](./media/109a99a8546fa851f4c62be307ec49df.png)

```python
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


Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/8e5cd9d0e407b4e254e8f098e73f0350.png)

Click “Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the temperature and humidity data in the current surroundings, as shown in the following figure. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/1a81b6a62a73b13dcebd29e9f7ac4356.png)

![](./media/af350892cefaa74dae1740153a0c1626.png)

**Circuit Diagram and Wiring Diagram**

Now we start printing the value of the XHT11 temperature and humidity sensor with LCD screen. We will see the corresponding values on the LCD screen. Let's get started with this project. Please follow the wiring diagram below.

Note: LCD\_128X32\_DOT must be connected with 10CM M-F Dupont wires, the LCD\_128X32\_DOT will display normally;  Otherwise, using a 20CM M-F Dupont wire may cause the LCD\_128X32\_DOT display abnormally.  

![](./media/d78889590f1945eec0125ee7dc250d73.png)

![](./media/78cb8eb87aa36af901a7a839fbf7eb10.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 29：Temperature Humidity Meter”. Select“dht11\.py”,“lcd128\_32.py”and “lcd128\_32\_fonts.py”，right-click and select“**Upload to /**”，waiting for the“dht11\.py”，“lcd128\_32.py”and“lcd128\_32\_fonts.py”to be uploaded to the Raspberry Pi Pico. And double left-click the“Project\_29.2\_Temperature\_Humidity\_Meter.py”.

![](./media/4e72290107f42992138c883132081bac.png)

![](./media/1b547dfc772378fe450c185a3f72059c.png)

![](./media/a40e1d929304074a1c63354338ab82e6.png)

![](./media/340ac580344b9c6a94c51ec5824340f7.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/3b865acac86da4d0e81dae45ee9117a9.png)

Click “Run current script”, the code starts executing, we will see that the LCD\_128X32\_DOT will display temperature and humidity in the current environment. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/eb2a301072b2e37a0feb30b23c0098d5.png)
### Project 30：Ultrasonic Ranger

**1. Introduction**

The HC-SR04 ultrasonic sensor is a very affordable distance sensor, mainly used for obstacle avoidance in various robotic projects. It is also used for water level sensing and even as a parking sensor. We treat the ultrasonic sensors as bat's eyes. In the dark, bats can still identify objects in front of them and directions through ultrasound. In this project, we will use a Raspberry Pi Pico to control the ultrasonic sensor and an LED analog ultrasonic ranger.  

**2. Components Required**

| ![img](media/wps303.png) | ![img](media/wps304.jpg)            | ![img](media/wps305.jpg) | ![img](media/wps306.jpg) |                          |
| ------------------------ | ----------------------------------- | ------------------------ | ------------------------ | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | Ultrasonic Sensor*1      | Red LED*4                |                          |
| ![img](media/wps307.jpg) | ![img](media/wps308.jpg)            | ![img](media/wps309.jpg) | ![img](media/wps310.jpg) | ![img](media/wps311.jpg) |
| M-F Dupont Wires         | 220ΩResistor*4                      | Jumper Wires             | Breadboard*1             | USB Cable*1              |

**3. Component Knowledge**

**HC-SR04 Ultrasonic Sensor:** Like bats, sonar is used to determine the distance to an object. It provides accurate non-contact range detection, high-precision and stable readings. Its operation is not affected by sunlight or black materials, just like a precision camera (acoustically softer materials like cloth are difficult to detect). It has an ultrasonic transmitter and receiver.

![](./media/e6f6037071e434febf7090b56ac35802.png)

In front of the ultrasonic sensor are two metal cylinders, these are the converters. The converters convert the mechanical energy into an electrical signal. In the ultrasonic sensor, there are transmitting converters and receiving converters. The transmitting converter converts the electric signal into an ultrasonic pulse, and the receiving converter converts the reflected ultrasonic pulse back to an electric signal. If you look at the back of the ultrasonic sensor, you will see an IC behind the transmitting converter, which controls the transmitting converter. There is also an IC behind the receiving converter, which is a quad operational amplifier that amplifies the signal generated by the receiving converter into a signal large enough to be transmitted to the
Raspberry Pi Pico.

**Sequence diagrams:**

The figure shows the sequence diagram of the HC-SR04. To start the measurement, the Trig of SR04 must receive at least 10us high pulse(5V), which will activate the sensor to emit 8 cycles of 40kHz ultrasonic pulses, and wait for the reflected ultrasonic pulses. When the sensor detects ultrasound from the receiver, it sets the Echo pin to high (5V) and delays it by one cycle (width), proportional to the distance. To get the distance, measure the width of the Echo pin.

![](./media/4114885ac4b6214953e3224d8c1d52c4.png)

Time = Echo pulse width, its unit is “us” (microseconds)

Distance in centimeters = time / 58

Distance in inches = time / 148

**4. Read the Distance Value**

We will start with a simple ultrasonic distance measurement and print the measured distance on the serial monitor.

![](./media/db430baa07e2e4d9ac9efca1950b953a.jpeg)

The HC-SR04 ultrasonic sensor has four pins, they are Vcc, Trig, Echo and GND. The Vcc pin provides the power source for generating ultrasonic pulses and is connected to Vcc (+5V). The GND pin is grounded. The Trig pin is where the Arduino sends a signal to start the ultrasonic pulse. The Echo pin is where the ultrasonic sensor sends information about the duration of the ultrasonic pulse to the Plus control board. Wiring as shown below.

![](./media/2e5a5d288a21bc75933876f223a278e4.png)

![](./media/92213eb45109991180d9eeadbba009b1.png)

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 30：Ultrasonic Ranger”. And double left-click the“Project 30.1\_Ultrasonic\_Ranging.py”.

![](./media/48037f18fd3e4308beebdfb30f0a698e.png)

```python
from machine import Pin
import time

#Define the control pins of the ultrasonic ranging module. 
Trig = Pin(27, Pin.OUT, 0)
Echo = Pin(26, Pin.IN, 0)

distance = 0 # Define the initial distance to be 0.
soundVelocity = 340 #Set the speed of sound.

# The getDistance() function is used to drive the ultrasonic module to measure distance, the Trig pin keeps at high level for 10us to start the ultrasonic module. Echo.value() is used to read the status of ultrasonic module’s Echo pin, and then use timestamp function of the time module to calculate the duration of Echo pin’s high level,calculate the measured distance based on time and return the value.
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

# Delay for 2 seconds and wait for the ultrasonic module to stabilize, Print data obtained from ultrasonic module every 500 milliseconds. 
time.sleep(2)
while True:
    time.sleep_ms(500)
    distance = getDistance()
    print("Distance: ", distance, "cm")
```


Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/feaec689d9eaa50061242ebf7b004c76.png)

Click “Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the distance value between the ultrasonic sensor and the object . Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/1a10f586a983ac9a4cbfcba22426260e.png)

![](./media/ce873cf513307a15f9aa58078c8dd7d6.png)

**5. Circuit Diagram and Wiring Diagram**

Next, we will make a simple ultrasonic ranger using a Raspberry Pi Pico to control an ultrasonic sensor and 4 LED lights. Connect the wires as shown below.

![](./media/fde13d356d164fa9bf4e2f01253a3523.png)

![](./media/1d9e98a0287beea858503dacd289a809.png)

**6. Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 30：Ultrasonic Ranger”. And double left-click the“Project\_30.2\_Ultrasonic\_Ranger.py”.

![](./media/27cbf4cd71b6d9b6f50a07e45bd17b4a.png)

```python
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

# The getDistance() function is used to drive the ultrasonic module to measure distance, the Trig pin keeps at high level for 10us to start the ultrasonic module. Echo.value() is used to read the status of ultrasonic module’s Echo pin, and then use timestamp function of the time module to calculate the duration of Echo pin’s high level,calculate the measured distance based on time and return the value.
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

# Delay for 2 seconds and wait for the ultrasonic module to stabilize, Print data obtained from ultrasonic module every 500 milliseconds. 
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

**7. Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click “Stop/Restart backend”.

![](./media/005bd195c009f3c37770253790792352.png)

Click “Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will print the distance
between the ultrasonic sensor and the object, and the corresponding LED will light up when we move our hand in front of the ultrasonic sensor. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/1b2217472e14ebacf06fbef7af122584.png)
### Project 31：Temperature Instrument

**Introduction**

Thermistor is a kind of resistor whose resistance depends on temperature changes, which is widely used in gardening, home alarm system and other devices. Therefore, we can use this feature to make a temperature instrument.

**Components Required**

| ![img](media/wps312.png) | ![img](media/wps313.jpg)            | ![img](media/wps314.jpg) |
| ------------------------ | ----------------------------------- | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | Thermistor*1             |
| ![img](media/wps315.jpg) | ![img](media/wps316.jpg)            | ![img](media/wps317.jpg) |
| 10CM M-F Dupont Wires    | Breadboard*1                        | LCD 128X32 DOT*1         |
| ![img](media/wps318.jpg) | ![img](media/wps319.jpg)            | ![img](media/wps320.jpg) |
| 10KΩResistor*1           | Jumper Wires                        | USB Cable*1              |

**Component Knowledge**

Thermistor: A thermistor is a temperature sensitive resistor. When it senses a change in temperature, the thermistor's resistance changes. We can use this feature to detect temperature intensity with thermistor. Thermistors and its electronic symbols are shown below:

![](./media/809b8634747fb295021f12e3b92b7894.png)

The relation between thermistor resistance and temperature is:

![img](media/wps321.png)

**in the formula: **

Rt is the resistance of the thermistor at T2 temperature.

R is the nominal resistance value of the thermistor at T1 room temperature.

EXP\[n\] is the nth power of e.

B is the temperature index

T1 and T2 refer to K degrees, that is, Kelvin temperature. Kelvin temperature =273.15 + Celsius temperature. For thermistor parameters, we use : B=3950, R=10KΩ，T1=25℃.The circuit connection method of thermistor is similar to that the photoresistor, as shown below :

![](./media/ac0d68aac58bffa5c99e1d0ed3a8bc37.jpeg)

We can use the value measured by the ADC converter to get the resistance value of the thermistor, and then use the formula to get the temperature value. Therefore, the temperature formula can be deduced as:

![img](media/wps322.png)

**Read the Values**

First we will learn the thermistor to read the current ADC value, voltage value and temperature value and print them out . Please connect the wires according to the following wiring diagram.

![](./media/c143dc239ceaa5e65a63f47d6512630c.png)

![](./media/c0ad763fa1dda5ce55d03fe9b3d61bcd.png)

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 31：Temperature Instrument”. And double left-click the“Project\_31.1\_Read\_the\_thermistor\_analog\_value.py”.

![](./media/ad5f606c570f0ae011d4a28e7a48d848.png)

```python
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


Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](./media/73a6c53febad0486b1286b38a0625f9d.png)

Click ![](./media/da852227207616ccd9aff28f19e02690.png)“Run current script”, the code starts executing, we will see that the "Shell" window of Thonny IDE will continuously display the thermistor's current ADC value, voltage value, and temperature value.  Try pinching the thermistor with your index finger and thumb (don't touch the wire) for a while, and you will see the temperature increase. Press“Ctrl+C”or click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”to exit the program.

![](./media/fbf956504f3e5246fe465e789c10690d.png)

![](./media/0a035900fbc73a112eced64a926872ad.png)

**Circuit Diagram and Wiring Diagram**

Note : LCD\_128X32\_DOT must be connected with a 10CM M-F Dupont wire, the LCD\_128X32\_DOT will display normally. Otherwise, using a 20CM M-F Dupont wire may cause the LCD\_128X32\_DOT display abnormally.  

![](./media/281774a4fbf4f7f2ca0fd1e60c89516c.png)

![](./media/91445212232765942d482b84da03f598.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open “Thonny”, click “This computer” → “D:” → “Python_Codes(Windows)” → “Project 31：Temperature Instrument”. Select “lcd128\_32.py” and “lcd128\_32\_fonts.py”,  right-click and select “**Upload to /**”, waiting for the “lcd128\_32.py” and “lcd128\_32\_fonts.py” to be uploaded to the Raspberry Pi Pico. And double left-click the “Project\_31.2\_Temperature\_Instrument.py”.

![](./media/96328c28b0e82498218b114936fe7e78.png)

![](./media/c3542c1f9ccb781e566a7e2e0329089f.png)

![](./media/2d174fc09d012690cb2de6e12e6f0ba1.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)Stop/Restart backend”.

![](./media/09d2a491dfb201b3b9c9cfd00ab8a8ac.png)

Click “Run current script”, the code starts executing, we will see that the LCD 128X32 DOT displays the voltage value of the thermistor and the temperature value in the current environment. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/3b29267af1b5bb81abd99c53aee49e8f.png)
### Project 32：RFID

**Introduction**

Nowadays, many residential districts use this function to open the door by swiping the card, which is very convenient. In this lesson, we will learn how to use RFID(radio frequency identification) wireless communication technology and read and write the key chain card (white card) and control the steering gear rotation by RFID-MFRC522 module.

**Components Required**

| ![img](media/wps323.png) | ![img](media/wps324.jpg)            | ![img](media/wps325.jpg) | ![img](media/wps326.png) |
| ------------------------ | ----------------------------------- | ------------------------ | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | RFID-MFRC522 Module*1    | Key Chain*1              |
| ![img](media/wps327.jpg) | ![img](media/wps328.jpg)            | ![img](media/wps329.png) | ![img](media/wps330.jpg) |
| F-F Dupont Wires         | Servo*1                             | White Card*1             | USB Cable*1              |

**Component Knowledge**

**RFID**：RFID (Radio Frequency Identification) is a wireless communication technology. A complete RFID system generally consists of a transponder and a reader. Usually we use tags as transponders, and each tag has a unique code attached to the object to identify the target object. The reader is a device that reads (or writes) tag information.

Products derived from RFID technology can be divided into three categories: passive RFID products, active RFID products and
semi-active RFID products. However, the passive RFID products are the earliest, most mature and most widely used products on the market, which can be seen everywhere in our daily life, such as bus card, meal card, bank card, hotel access card, etc., which are close contact identification. The main operating frequencies of the passive RFID products are 125KHZ(low frequency), 13.56mhz (high frequency), 433MHZ(UHF), and 915MHZ(UHF). The active and the semi-active RFID products operate at higher frequencies.

The RFID module we use is a passive RFID product with a working frequency of 13.56MHz.  

**RFID-RC522 Module：**The MFRC522 is a highly integrated reader/writer IC for 13.56MHz contactless communication. Its
internal transmitter is capable of driving a read/write antenna, which is designed to communicate with ISO/IEC 14443A /MIFARE cards and transponders without the need for additional active circuits. The receiving module provides an efficient implementation of demodulation and decoding of signals from ISO/IEC 14443 A /MIFARE compatible cards and transponders. The digital module manages complete ISO/IEC 14443A framing and error detection (parity and CRC)
features.  

The RFID module uses the MFRC522 as the control chip and adopts I2C(Inter-Integrated Circuit) interface.  

![](./media/5a19d0dd224c2cdc78871f11e8951045.png)

**Specifications**:

Operating voltage: DC 3.3V-5V

Operating current: 13—100mA/DC 5V

Idling current: 10-13mA/DC 5V

Sleep current: \<80uA

Peak current: \<100mA

Operating frequency: 13.56MHz

Maximum power: 0.5W

Supported card types: mifare1 S50、mifare1 S70、mifare UltraLight、mifare Pro、mifare Desfire

Environmental operating temperature: -20 to 80 degrees Celsius

Environment storage temperature: -40 to 85 degrees Celsius

Relative Humidity: 5% to 95%

Data transfer rate: The maximum is 10Mbit/s.

**Read the Card Number Value**

We will read the UNIQUE ID number (UID) of the RFID card and identify its type . And display relevant information through the
"Shell" window of Thonny IDE. The wiring diagram is as follows:

![](./media/654c447a08c85a3b54c80aea24577ad7.png)

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

You can move the code to anywhere, for example, we can save the code in the Disk(D), the route is D:\\2. Python Projects.

Open Thonny, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 32：RFID”.

Select“mfrc522\_config.py”“mfrc522\_i2c.py”and“soft\_iic.py”，right-click and select“**Upload to /**”,waiting for the“mfrc522\_config.py”“mfrc522\_i2c.py”and“soft\_iic.py”to be uploaded to the Raspberry Pi Pico. And double left-click the“Project\_32.1\_RFID\_Read\_UID.py”.

![](./media/16a289ade8d67f22ec39faef236ea8b3.png)

![](./media/3ec54155e10e80dc2a8132a3cc22cf7d.png)

![](./media/dafb6349a78a115b7f3b13d62e81f0fe.png)

![](./media/a7c2cf9283e2dd36e232e5603dc82b48.png)

```python
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


Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/1f6a9dec0c6e1ca3e8955e2b719ed377.png)

Click “Run current script”, the code starts executing, we will see that

place the door card and key chain close to the module sensor area respectively, the "Shell" window of Thonny IDE will display the card number and key chain value respectively, as shown below. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/f756e0c4dc6360842d7c97d7fdd80a70.png)

![](./media/091b3f4fdd9b823b64487aec5d5834f8.png)

Note: the door card value and key chain value may be different for different RRFID -RC522 door cards and key chains.  

**Circuit Diagram and Wiring Diagram**

Now we use a RFID-RC522 module, door card/key chain and servo to simulate an intelligent access control system. When the door card is close to the RFID-RC522 module induction area, the servo rotates. Wiring according to the figure below:

![](./media/671a93cf112889c8c5245ac6ebeb2c4d.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open Thonny, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 32：RFID”. 

Select“mfrc522\_config.py”“mfrc522\_i2c.py”and“soft\_iic.py”，right-click and select“**Upload to /**”,waiting for the“mfrc522\_config.py”“mfrc522\_i2c.py”and“soft\_iic.py”to be uploaded to the Raspberry Pi Pico. And double left-click the“Project\_32.2\_RFID\_Control\_Servo.py”.

![](./media/16a289ade8d67f22ec39faef236ea8b3.png)

![](./media/3ec54155e10e80dc2a8132a3cc22cf7d.png)

![](./media/dafb6349a78a115b7f3b13d62e81f0fe.png)

![](./media/e8c3b1f0e1f2d3c168eaed26ee239e95.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/52511e1772f5d695c42ddb1dd7d67eeb.png)

Click “Run current script”, the code starts executing, we will see that when using the white card or a key card swiping, the "Shell" window of Thonny IDE will display the card number value respectively, and at the same time, the servo will rotate to the corresponding angle to simulate opening the door. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/77cf190202d54f9ab93e2379c8d2a29f.png)
### Project 33：Keypad Door

**Introduction**

In common digital button sensors, one button uses an IO port. However, sometimes it will occupy several IO ports when we need a lot of buttons . In order to save the use of IO ports, we are supposed to make a plurality of buttons into a matrix type, through the control of lines to achieve less IO port control the multiple buttons. In this project, we will learn a Raspberry Pi Pico and a 4\*4 membrane matrix keyboard control a servo and a buzzer.   

**Components Required**

| ![img](media/wps331.png)        | ![img](media/wps332.jpg)            | ![img](media/wps333.jpg) | ![img](media/wps334.jpg) |
| ------------------------------- | ----------------------------------- | ------------------------ | ------------------------ |
| Raspberry Pi Pico*1             | Raspberry Pi Pico Expansion Board*1 | Servo*1                  | Active Buzzer*1          |
| ![img](media/wps335.png)        | ![img](media/wps336.jpg)            | ![img](media/wps337.jpg) | ![img](media/wps338.jpg) |
| 4*4 Membrane Matrix Keyboard *1 | Jumper Wires                        | Breadboard*1             | USB Cable*1              |

**Component Knowledge**

**4\*4 Matrix keyboard:**The keyboard is a device that integrates many keys. As shown in the figure below, a 4x4 keyboard integrates 16 keys.

![](./media/fcd187eb009098d691927511606c991b.jpeg)

As with the LED matrix integration, in the 4x4 keyboard, each row of keys is connected to a pin, each column of keys is the same. This connection reduces the use of processor ports. The internal circuit is shown below.

![](./media/5ebdacba906622079e0ef41dc1ea3fdf.png)

You can use row scan or column scan methods to detect the state of the keys on each column or each line. Take the column scan method as an example. Send a low level to column 4 (Pin4), detect the state of rows 1, 2, 3 and 4, and determine whether the A, B, C and D keys are pressed. Then send the low level to columns 3, 2, 1 in turn, and detect whether other keys are pressed. Then you can get the state of all keys.

**Read the Value**

We start with a simple code to read the values of the 4\*4 matrix keyboard and print them in the serial monitor. Its wiring diagram is shown below.

![](./media/a673f15964984f61170e2d7690e959c1.png)

![](./media/681be86e91946320131d4b11b12b77c2.png)

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 33：Keypad Door”. Select“keypad\.py”, right-click and select“**Upload to/**”，waiting for“keypad\.py”to be uploaded to the Raspberry Pi Pico. And double left-click the “Project\_33.1\_4x4\_Matrix\_Keypad\_Display.py”.

![](./media/e85a02f16a7ed46914ce4f92dac7afc6.png)

![](./media/e3e28e7310d676dad68f34aeb025f01a.png)

```python
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


Ensure that the Raspberry Pi Pico is connected to the computer, click“Stop/Restart backend”.

![](./media/49cc342796f0f16969047ae33d1b3ad7.png)

Click “Run current script”, the code starts executing, we will see that press the keyboard and the "Shell" window of Thonny IDE will print the corresponding key value, as shown below. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/687ad6b6d337449dec60e84aa469cbe5.png)

![](./media/2f82f861d68daaaad8085b6a1bcc2e8d.png)

**Circuit Diagram and Wiring Diagram**

In the last experiment, we have known the key values of the 4\*4 matrix keyboard. Next, we use it as the keyboard to control the servo and the buzzer.  

![](./media/f08b9ee128bc06300b3f8a05c73c2375.png)

![](./media/ccb5914d82d2b220e8a6afb944d13c54.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 33： Keypad Door”. 

Select“keypad\.py”and“myservo\.py”， right-click and select“**Upload to /**”，waiting for the “keypad\.py”and“myservo\.py”to be uploaded to the Raspberry Pi Pico. And double left-click the“Project\_33.2\_Keypad\_Door.py”.

![](./media/e85a02f16a7ed46914ce4f92dac7afc6.png)

![](./media/5debc33ea5ee12b02fddf85cad73725c.png)

![](./media/e275ebc9ce82a01ee9f0f06e4686bfed.png)

```python
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/cbcc9a007c9148a7101f141b72a04aae.png)

Click “Run current script”, the code starts executing, we will see that press the keyboard to enter a four-character password. If the password is correct (correct password: 1234), the servo will turn at an angle and return to its original position. If the input is incorrect, an input error alert will be issued. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/3af6d6b1400a9de15f8a874b574e5444.png)

![](./media/d45bd766b2b2630219f8bef283a07417.png)
### Project 34：IR Control Sound and LED

**Introduction**

Infrared remote control is a low-cost, easy-to-use wireless communication technology. IR light is very similar to visible light,
except that it has a slightly longer wavelength. This means that infrared rays cannot be detected by the human eye, which is perfect for wireless communication. For example, when you press a button on the TV remote control, an infrared LED will switch on and off repeatedly at a frequency of 38,000 times per second, sending information (such as volume or channel control) to the infrared sensor on the TV.

We will first explain how common IR communication protocols work. Then we will start this project with a remote control and an IR receiving component.

**Components Required**

| ![img](media/wps339.png) | ![img](media/wps340.jpg)            | ![img](media/wps341.jpg) | ![img](media/wps342.jpg) | ![img](media/wps343.jpg) |                          |
| ------------------------ | ----------------------------------- | ------------------------ | ------------------------ | ------------------------ | ------------------------ |
| Raspberry Pi Pico*1      | Raspberry Pi Pico Expansion Board*1 | IR Receiver *1           | RGB LED*1                | 220ΩResistor*3           |                          |
| ![img](media/wps344.jpg) | ![img](media/wps345.jpg)            | ![img](media/wps346.jpg) | ![img](media/wps347.jpg) | ![img](media/wps348.jpg) | ![img](media/wps349.jpg) |
| IR Remote Controller*1   | Breadboard*1                        | Passive Buzzer*1         | 10KΩResistor*1           | Jumper Wires             | USB Cable*1              |

**Component Knowledge**

**IR Remote Controller**: It is a device that has a certain number of buttons. Pressing different buttons causes the infrared transmitter tubes at the front of the remote control to send infrared signals in different codes. Infrared remote control technology is widely used, such as TV, air conditioner and so on. Therefore, in today's technologically advanced society, the infrared remote control technology makes it very convenient for us to change TV programs and adjust the temperature of
the air conditioner.  

The remote control we used is as follows:

The infrared remote controller adopts NEC code and the signal cycle is 110ms.

![](./media/3c9d76cb0d24d9861811ce2cb0bb6ae4.png)

**IR Receiver:** It is a component that can receive infrared light, which can be used to detect the infrared signal sent by the infrared
remote control. The infrared signal received by the infrared receiver demodulation can be converted back to binary, then the information will be passed to a microcontroller.

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

Address and Command are transmitted twice. The second time all bits are inverted and can be used for verification of
the received message. The total transmission time is constant because every bit is repeated with its inverted length. If you're not interested in this reliability you can ignore the inverted values, or you can expand the Address and Command to 16 bits each\!

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

**Decode Infrared Signal:**

We connect the infrared receiving element to the Raspberry Pi Pico according to the wiring diagram below.  

![](./media/240a9b2efcdd0c0e7099ec5b69beaca6.png)

![](./media/a6a7f74730669dfa0272e9b5e88ac41e.png)

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 34：IR Control Sound and LED”. Select“irrecvdata\.py”， right-click and select“**Upload to /**”,waiting for the“irrecvdata\.py”to be uploaded to the Raspberry Pi Pico. And double left-click the“Project\_34.1\_Decoded\_IR\_Signal.py”.

![](./media/0e559f2f7ce06f100f33f2aa562669b3.png)

![](./media/91b7122d9d7183692a5cd243a9f493e1.png)

```python
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


Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/f74f668d149dbdab5ac8f19df19c1852.png)

Click “Run current script”, the code starts executing, we will see that aim the infrared remote control transmitter at the infrared receiving head, press the button on the infrared controller, and the "Shell" window of Thonny IDE will print the current received key code values. Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/a75baa34fe256fdea2714b1b0c66cd66.png)

![](./media/623f8fa842b90a093d286954835483c6.png)

Write down the code associated with each button, because you will need that information later.

![](./media/ebcf0cb2055f7784505f76ceeaef9f47.jpeg)

**Circuit Diagram and Wiring Diagram**

![](./media/6e2da9ed5d5bdc5b251348903a37e5c0.png)

![](./media/d170f9c106c16175d34f20fdaa0f8970.png)

**Test Code**

The code used in this project is saved in the file **...\6.Codes\Python_Codes(Windows)**. We can move the code anywhere. For example, we save the <span style="color: rgb(255, 76, 65);">Python_Codes(Windows)</span> in the Disk(D), <span style="color: rgb(0, 209, 0);">the route is D:\\Python_Codes(Windows)</span>.

Open“Thonny”, click“This computer”→“D:”→“Python_Codes(Windows)”→“Project 34：IR Control Sound and LED”. Select“irrecvdata\.py”，right-click and select“**Upload to /**”,waiting for the“irrecvdata\.py”to be uploaded to the Raspberry Pi Pico. And double left-click the“Project\_34.2\_IR\_Control\_Sound\_And\_LED.py”.

![](./media/0e559f2f7ce06f100f33f2aa562669b3.png)

![](./media/cdbe2c4d1e154cfa7983588113189876.png)

```python
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

### Play the frequency of midrange tones 1-7
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
        ### Print("----freq:", index, tone_freq)
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

**Test Result**

Ensure that the Raspberry Pi Pico is connected to the computer，click“Stop/Restart backend”.

![](./media/91f4a1a976aa6dc5e3008f1c1e6ea864.png)

Click “Run current script”, the code starts executing, we will see that press buttons 1 to 7 on the infrared remote controller, we can hear buzzers such as do、re、mi、fa、sol、la、si ,etc. At the same time, the RGB will be red , green , blue , yellow , magenta, blue and green, white respectively. However, if we press other buttons(except 1-7), the buzzer stops playing and the RGB goes off.  Press“Ctrl+C”or click“Stop/Restart backend”to exit the program.

![](./media/6b00ce3539b5537d80fd0a614b70902c.png)

**Note**：When the code is running, the following prompt appears, you just need to click![](./media/27451c8a9c13e29d02bc0f5831cfaf1f.png)“Stop/Restart backend”，then click![](./media/da852227207616ccd9aff28f19e02690.png)“Run current script”to make the code run again.

![](./media/3f425db5cda9eb56bc1f29c27fa6696d.png)

(<span style="color: rgb(255, 76, 65);">Note: </span>Before use, we need to remove the plastic sheet from the bottom of the infrared remote controller.)

![image-20231013153101361](media/image-20231013153101361.png)
