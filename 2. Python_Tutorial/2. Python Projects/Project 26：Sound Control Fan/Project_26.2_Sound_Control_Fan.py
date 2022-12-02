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