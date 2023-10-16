# Project 01: Hello World

### **Introduction**

For Raspberry Pi Pico beginners, we will start with some simple things. In this project, you only need a Raspberry Pi Pico and a USB cable to complete the "Hello World\!" project, which is a test of communication between Raspberry Pi Pico and the PC as well as a primary project.

### **Components**

| ![img](media/wps100.png) | ![img](media/wps101.jpg) |
| ------------------------ | ------------------------ |
| Raspberry Pi Pico*1      | USB Cable*1              |

### **Wiring Up**

In this project, we use a USB cable to connect the Raspberry Pi Pico to the computer.

![](/media/8ea81d60b8e2132c358041235490b7d5.jpeg)

### **Online running code:**

To run the Raspberry Pi Pico online, you need to connect the Raspberry Pi Pico to your computer, which allows you to compile or debug programs using Thonny software.  

Advantages:

1. You can use the Thonny software to compile or debug programs. 
2. Through the "Shell" window, you can view error messages and output results generated during the running of the program as well as query related function information online to help improve the program.  

Disadvantages:

1. To run the Raspberry Pi Pico online, you must connect the Raspberry Pi Pico to a computer and run it with the Thonny software.  
2. If the Raspberry Pi Pico is disconnected from the computer, when they reconnect, the program won't run again.  

Basic Operation:

Open Thonny and click“Open...”.

![](/media/b65264767d6ff04d5f3530b8eebe218c.png)

Click“This computer”in the new pop-up window.

![](/media/5bdbc66ef89b41a53e46696c07b2c282.png)

In the new dialog box，select“Project\_01\_HelloWorld.py”,click“Open”.

The code used in this tutorial is saved in the file KS3020 Keyestudio Raspberry Pi Pico Learning Kit Ultimate Edition\\2. Windows
System\\1.Python\_Tutorial\\2. Python Projects. You can move the code to anywhere,for example,we can save the 2. Python Projects file in the Disk(D), the route is D:\\2. Python Projects.

![](/media/9b61f563870ec1235e6cc48ca748cec5.png)

Click“Run current script”to execute the program“Hello World\!”, "Welcome Keyestudio" , which will be printed in the“Shell”window.

![](/media/39eb24657c5733544944dd643640a61d.png)

### **Exit running online**

When running online, click“Stop /Restart Backend” or press “Ctrl+C” to exit the program.  

![](/media/dc2a210535724a7d601b5ad8b02ca8ed.png)

### **Test Code**

```python
print("Hello World!")
print("Welcome Keyestudio")
```

