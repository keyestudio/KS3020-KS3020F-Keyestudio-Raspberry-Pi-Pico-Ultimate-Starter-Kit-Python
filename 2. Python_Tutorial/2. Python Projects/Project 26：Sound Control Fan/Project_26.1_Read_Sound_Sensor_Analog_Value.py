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