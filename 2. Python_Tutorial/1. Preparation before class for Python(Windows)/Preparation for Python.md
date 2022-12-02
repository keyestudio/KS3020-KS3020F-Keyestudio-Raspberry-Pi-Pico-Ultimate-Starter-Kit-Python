# **Preparation for Python（Important）**

Before we start building a project, we need to do some preparations first, 

which is so important that we can't skip it. 

1.  **Install Thonny**

Thonny is a free and open source software platform with small size,
simple interface, simple operation and rich functions. It is a Python
IDE suitable for beginners. In this tutorial, we use this IDE to develop
a Raspberry Pi Pico. Thonny supports multiple operating systems
including Windows, Mac OS, Linux.

1.  **Download Thonny**

<!-- end list -->

1)  Enter the website: https://thonny.org to download the latest version
    of Thonny.

2)   Thonny open-source code library: https://github.com/thonny/thonny  
    
    Please follow the instructions on the official website or click the
    link below to download and install.  (Please select the appropriate
    option based on your operating system.)  

<table>
<tbody>
<tr class="odd">
<td><a href="javascript:;">System</a></td>
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

![](/media/bd5823ede2c01d1fa4696438c62aec51.png)

2.  **Install Thonny on Windows  **

<!-- end list -->

1.  The downloaded Thonny icon is as follows.

![](/media/d3caa98d406fa06a124d5c98195b90db.png)

2.  Double-click “Thonny-3.3.13.exe”. The following dialog box is
    displayed. I choose“![](/media/11fb59a50abe0bf54df7e4cb891ad2c0.png)”to operate. You can also
    select“![](/media/37be3f3bcc9aa0eb48c8b844eb46a71c.png)” to operate.
    
    ![](/media/4c044b255da8b14fe674eb9cce01627d.png)

3.  If you are not familiar with computer software installation, click
    “Next” until the installation is complete.  
    
    ![](/media/995b36640124b6a9b23f10473ff8a38a.png)
    
    ![](/media/8bcc17840b9fc15d76f79fee8a0168ee.png)

4.  If you want to change the route of installing Thonny，just
    click“**Browse...**”to select a new route and click “OK”. 
    
    If you don’t want to change the route of installing Thonny, just
    click “Next”and then click“Next”again.
    
    ![](/media/df6f63b42ebb1676b22c26b25dc9c7aa.png)
    
    ![](/media/f5cd6d619b4645601c5b098ffdbec12a.png)

5.  Select "Create Desktop Icon". Thonny software will generate a
    shortcut on your desktop for you to open Thonny software later.
    
    ![](/media/a30c89dde3de81ad00aced30510071be.png)

6.  Click "Install"
    
    ![](/media/6ace65142291e5e8af5f81e4a6b2f180.png)

7.  Wait for a while but don’t click **Cancel**
    
    ![](/media/a504b3a3ab16b4d91040cd5878acea0c.png)

8.  Once we see the following screen, Thonny software has been
    successfully installed. Click “Finish”.  
    
    ![](/media/a1fb6027e54a975de1c0aa1e1a0d6a29.png)

9.  If we select “Create Desktop Icon” during the installation, the
    following icon will be displayed on the desktop.  
    
    ![](/media/80f35044d91d66f734e36059db35f273.png)

<!-- end list -->

3.  **Basic configuration of Thonny software**

<!-- end list -->

1.  Double-click the desktop icon of Thonny software, we can see the
    following interface, and we can also choose the language and initial
    settings.  Once set, click "Let's Go\!"  
    
    ![](/media/ee240978a4f844184f1ea9f5a21d0395.png)
    
    ![](/media/619a856895d95e00beed748b1438072d.png)
    
    ![](/media/bcf6c31e4f69c904a7a0c0e9df7e8d7d.png)

2.  Select“View”→“File”和“Shell”
    
    ![](/media/5ff5c305585dbe7e832cc41183db5818.png)
    
    ![](/media/d41b79772c9846fd8bf295c8451f8321.png)
    
    ![](/media/3d04fe6893ca104e4e593a0786cb3799.png)

<!-- end list -->

4.  **Update Micropython firmware**
    
    To run MicroPython programs on Raspberry Pi Pico, we first need to
    burn a firmware into Raspberry Pi Pico.  
    
    **Why do we need to update the firmware?**
    
    The Raspberry Pi Pico can be programmed in both C and MicroPython,
    and which is shipped without MicroPython firmware, which we need to
    download before we can program with MicroPython. 
    
    Note: MicroPython Firmware only needs to be downloaded once and does
    not need to be downloaded again when programming with
    MicroPython.  If we have downloaded the.uf2 firmware written in C,
    it will be overwritten, so the next time we use MicroPython, we need
    to update our Raspberry Pi Pico firmware by following the steps.  

<!-- end list -->

1.  **Download the Micropython Firmware  **
    
    Method1: Raspberry Pi Pico official
    website：[<span class="underline">https://www.raspberrypi.com/documentation/microcontrollers/</span>](https://www.raspberrypi.com/documentation/microcontrollers/)

<!-- end list -->

1.  Click the link above, we can see the following interface:
    
    ![](/media/3b3e6a639416b76c44f2a0854dc451cc.png)

2.  Scroll the mouse and we can see the following again:
    
    ![](/media/5d04d67506852588d126ce760739a3c5.png)

3.  Click MicroPython(Getting Started MicroPython) to go to the firmware
    download page.  
    
    ![](/media/137e21851df02502fb989d8541fa0da8.png)
    
    Method 2: By clicking on the download link:
    https://micropython.org/download/rp2-pico/rp2-pico-latest.uf2, we
    can download directly.  
    
    Method 3: If we can't download it due to network problems or other
    reasons, we can use the.uf2 file we prepared, which is located in
    the following file path.  
    
    ![](/media/ca4858fd34bc267a5b6089ad8ef1d277.png)

<!-- end list -->

5.  **The procedures for burning MicroPython firmware  **
    
    ① Connect one end of the microUSB cable to the USB port of our
    computer.  
    
    ② Long press the white button on the "Raspberry Pi Pico"
    (BOOTSEL).  The Raspberry Pi Pico is then connected to the
    computer via the microUSB wire.  
    
    ![](/media/33c91d51b2aeb2c943691706354aaad1.png)
    
    ③ Release the button, when the connection is successful, open
    \[Device Manager\] on our computer, the computer will automatically
    recognize the removable disk (RPI-RP2), as shown below:
    
    ![](/media/87e24af3ea812b5492a06b0141060b86.png)
    
    ④ Copy the file (RP2-Pico-20210902-v1.17.uf2) to a removable disk
    (RPI-rp2) and wait for it to complete, just like copying the file to
    a USBflash drive.  
    
    ![](/media/916dc807eb08231d8410603e944d405e.png)
    
    ⑤ Raspberry Pi Pico automatically restarts after the firmware is
    burned.  After that, we  can run Micropython.  

6.  **Thonny connects to Raspberry Pi Pico**

1.Open Thonny, click“Run”and select“Select interpreter…”

![](/media/09593c45eabe111d9f75848e39312b75.png)

2.Select“Micropython (generic)”or“Micropython (Raspberry Pi Pico)”How to
select“Micropython(generic)”? As follows:

![](/media/0dda06df90ad37a0490c56559108ba51.png)

1.  Select USB-Serial (COMx). The COMx number may be different on
    different PCS.  Just make sure we select "USB-Serial (COMx)".  
    
    **How to determine which port does the Raspberry Pi Pico communicate
    with our computer?  **
    
    Step 1: When our Raspberry Pi Pico is not connected to the computer,
    open Thonny software, click "Run", select "Select Interpreter", the
    dialog will pop up, click "Port", we can view the currently
    connected port, as shown in the picture below:  
    
    ![](/media/0112f6cc9da283b3e257d3b1e494f610.png)
    
    Step 2: Close the dialog box.  Connect Raspberry Pi Pico to our
    computer, click "Run" again and select "Select Interpreter".  Click
    “Port” in the window that is displayed to view the current
    port.  Now add another port, so this port is used to communicate
    with the computer.
    
    ![](/media/58613bc6727537a24a253c1cc7d9b5cf.jpeg)

2.  Select“Micropython(generic)”and port，and click“OK”.

![](/media/52262cb23cd963079c41b6b015a43261.jpeg)

3.  When the following message is displayed on Thonny, then the Thonny
    successfully connects to the Raspberry Pi Pico.  

![](/media/e33d2e9552d2cecedc50bf96a5036845.png)

So far, all the preparations have been made.

7.  **Text Code**

<!-- end list -->

1.  Test Shell commands  

In“**Shell**”window , type“**print (Hello World\!)**”，press“**Enter**”.

![](/media/2b4feabe1126134057046b6a0dd5bbdb.png)

2.  Run Code Online:
    
    To run Raspberry Pi Pico online, we need to connect the Raspberry Pi
    Pico to our computer, which allows us to compile or debug programs
    using Thonny software.  
    
    Advantages: you can compile or debug programs using Thonny software.
     
    
    Through the "Shell" window, we can view the error information and
    output results generated during the operation of the program, and
    query related function information online to help improve the
    program.  
    
    Disadvantages: To run Raspberry Pi Pico online, you must connect
    Raspberry Pi Pico to a computer and run it with Thonny software.  
    
    If the Raspberry Pi Pico is disconnected from the computer, when
    they reconnect, the program won't run again.  
    
    [basic](javascript:;) [operation](javascript:;):
    
    Open Thonny and click![](/media/6388aa0daa514f9325fb07fd5ab6749b.png)“**Open...**”.

![](/media/b65264767d6ff04d5f3530b8eebe218c.png)

Click“**This computer**”in the new pop-up window

![](/media/5bdbc66ef89b41a53e46696c07b2c282.png)

In the new dialog box, go to the folder 2. Python Projects\\Project
01：Hello World . Select“Project\_01\_HelloWorld.py”,click“Open”. The
code used in this tutorial is saved in the file KS3020 Keyestudio
Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows System\\1.
Python\_Tutorial\\2. Python Projects. We can move the code
anywhere.  For example, we save the 2. Python Projects in the Disk(D),
the route is D:\\2. Python Projects.

![](/media/9b61f563870ec1235e6cc48ca748cec5.png)

1.  Click![](/media/f79b2c42507d12b91ca23ea0bb87c5c2.png)“Run current script”to execute
    program“Hello World\!”, "Welcome Keyestudio" will print in the
    “Shell”window.
    
    ![](/media/39eb24657c5733544944dd643640a61d.png)
    
    **Exit online**
    
    When running online, click **“**Stop /Restart Backend**”** on Thonny
    or press **“Ctrl+C”** to exit the program.  
    
    ![](/media/dc2a210535724a7d601b5ad8b02ca8ed.png)

<!-- end list -->

3.  Offline running code:
    
    When running offline, the Raspberry Pi Pico doesn't need to connect
    to a computer and Thonny.  Once powered up, it can run the
    main.pyprogram stored in the Raspberry Pi Pico.  
    
    **Pros**: We don't need to connect a computer to Thonny's software
    to run the program.  
    
    **Cons**: The program stops automatically when an error occurs or
    the Raspberry Pi Pico runs out of power, and the code is hard to
    change.
    
    [Basic](javascript:;) [Operation](javascript:;):
    
    Once powered up, the Raspberry Pi Pico will  check for the presence
    of main.py on the device automatically.  If so, run the program in
    main.py and go to the shell command system.  (If we want the code to
    run offline, we can save it as main.py);  If the main.py does not
    exist, go directly to the shell command system.  

<!-- end list -->

1.  Click “File”→“New”, create and write code.

![](/media/7a6988dfff80ecb0479e3e878ccde171.png)

(2)Enter the code in the newly opened file. Here we use the
Project\_02\_Onboard\_LED\_Flashing. Py code as an example.  

![](/media/59f397a5c32e3bbe1bb8ff5e2d0316ae.png)

3)  Click“**Save**”on the menu bar, we can save the code in This
    computer or MicroPython device.
    
    ![](/media/abec708857f37ac0871ffa7ad5b4c913.png)

<!-- end list -->

4.  Select“MicroPython device”，enter“main.py”in the new pop-up window
    and click“OK”.

![](/media/eb375d7b67d432efb0253a825d5ee5a4.png)

![](/media/d7f40a82158a71b22909f519a9078e94.png)

5.  We can see the code has been uploaded to the Raspberry Pi Pico.

![](/media/aace831a6a8e1199b2a9e0fc6ef40d56.png)

6.  Disconnect the microUSB cable to the Raspberry Pi Pico and
    reconnect, and the LEDs on the Raspberry Pi Pico will  flash
    repeatedly. 
    
    ![](/media/529c3be102eb7414ac1e5e66fb203b6e.png)

**Exit from Offline operation**

Connect Raspberry Pi Pico to the computer，click“Stop/Restart backend”on
Thonny to end the offline operation.  

![](/media/5efb6f20a190d482be423126eced88d5.png)

If it does’t work, click“Stop/Restart backend”on Thonny several times or
reconnect to the Raspberry Pi Pico.

![](/media/2d507294736e68b68cad4e8060ae1db6.jpeg)

We provide a main.py file to run offline.  The code added to main.py is
the bootstrap that executes the user code file. We just need to upload
the offline project's code file (.py) to the "MicroPython Device".

① Make the program folder **KS3020 Keyestudio Raspberry Pi Pico Learning
Kit Ultimate Edition\\2. Windows System\\1. Python\_Tutorial\\2. Python
Projects** move ahead to the **Disk(D)**，the path is **D:\\2. Python
Projects.** Open the Thonny software.  

![](/media/2da93159095ee2355449a27a22f988b4.png)

② Expand Project 00 : main in Disk(D) directory D:\\2. Python Projects.
Double-click **main.py** to make the code in **"**MicroPython Device**"
ru**n offline.  

 ![](/media/30ed08309a2c6d6b53ea9b1cd4beb299.png)

Here, we use project 00 and Project 02 cases as examples.  The results
are displayed using an LED(GP25 pin) on a Raspberry Pi Pico.  If we have
modified the Project\_02\_Onboard\_LED\_Flashing. Py file, then we need
to modify it accordingly. Right-click the
Project\_02\_Onboard\_LED\_Flashing. Py file and select **'**Upload to/'
to upload the code to Raspberry Pi Pico, as shown below.  

![](/media/2b0dfdd7becf42730b1baa0ca45e6ea3.png)

Upload the main.py in the same way

![](/media/4e8bc42dbffa1e0432a94e99977d426f.jpeg)

Disconnect and reconnect the microUSB cable to the Raspberry Pi Pico,
and the LEDs will flash repeatedly .

![](/media/529c3be102eb7414ac1e5e66fb203b6e.png)

Note:

The code here runs offline.  If we want to stop running offline and go
to "Shell", simply click "Stop/Restart Backend" on Thonny software.

![](/media/dc2a210535724a7d601b5ad8b02ca8ed.png)

5.  ** Thonny common operations**

**Upload the code to Raspberry Pi Pico**

In the Project 01：Hello World file, right-click and select
Project\_01\_HelloWorld.py，select“**Upload to /**”and upload the code to
the root directory of the Raspberry Pi Pico.

![](/media/18f24b958cc2efe1e332c429383b8df1.png)

**Download the code to the computer**

In the“**MicroPython device**”, right-click and select
Project\_01\_HelloWorld.py，select“**Download to ...**”to download the
code to our computer.

![](/media/867e40f907c512aa4a17c0f4fb6d75e6.png)

**Delete the files in the Raspberry Pi Pico root directory**

In the“**MicroPython device**”，right-click and select
Project\_01\_HelloWorld.py，select“**Delete**”，delete the
Project\_01\_HelloWorld.py from the Raspberry Pi Pico root directory.

![](/media/d97823ab15b1afd831a438e2863ab270.png)

**Delete files from the computer's directory**

In the Project\_01 : Hello World file, right-click and select
Project\_01\_HelloWorld.py，select“**Move to Recycle Bin**”，then it can
be deleted from the Project\_01\_HelloWorld file.

![](/media/9d73a385a0855eb68c453088bd0748f4.png)

**Create and Save Code**

①Click“**File**”→“**New**”to create and compile code.

![](/media/373922a344188cda87b797b0ad639522.png)

②Enter code in the newly opened file, here we use
Project\_02\_Onboard\_LED\_Flashing.py code as an example.

![](/media/4aab2202442af7b04e880414af8f44fe.png)

③Click“**Save**”，and we can save the code to our computer or the
Raspberry Pi Pico.

![](/media/19773e65bc454d549ae95422b645692a.png)

④ Select“**MicroPython device**”，enter“**main.py**”in the new pop-up
window and click“**OK**”.

![](/media/92c1b5f2bb76f21462da37cdb9a3f18f.png)

![](/media/d7f40a82158a71b22909f519a9078e94.png)

⑤ We can see the code has been uploaded to the Raspberry Pi Pico.

![](/media/4be452d7471f5110efdc50737007d714.png)

⑥Click“**Run current script**”, the LED on the Raspberry Pi Pico will
flash periodically.

![](/media/3c0b64be3cc1a0750f187e063dcabd29.png)
