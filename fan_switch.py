import RPi.GPIO as gpio
import time
import os

gpio.setmode(gpio.BCM)
gpio.setup(4, gpio.OUT)

while True:
    temp = os.popen('vcgencmd measure_temp').readline()
    threshold = int(35)
    temp = int(temp[5:7])
    
    if temp >= threshold:
        print('Fan On | {} >= {}' .format(temp, threshold))
        gpio.output(4,True)
        time.sleep(3)

    else:
        print('Fan OFF | {} <= {}' .format(temp, threshold))
        gpio.output(4, False)
        time.sleep(3)
