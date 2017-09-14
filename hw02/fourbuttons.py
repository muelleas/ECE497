#!/usr/bin/env python3
# File: fourbuttons.py
# Author: Andrew Mueller
#
# This file takes input form 4 buttons on GP0 and toggles 4 leds on GP1

# Import PyBBIO library:
import Adafruit_BBIO.GPIO as GPIO
import time

button = ["GP0_3", "GP0_4", "GP0_5", "GP0_6"]  # the buttons used
led = ["GP1_3", "GP1_4", "RED", "GREEN"] # LEDs used

# Set the GPIO pins:
GPIO.setup(led[0],    GPIO.OUT)
GPIO.setup(led[1],    GPIO.OUT)
GPIO.setup(led[2],    GPIO.OUT)
GPIO.setup(led[3],    GPIO.OUT)

GPIO.setup(button[0], GPIO.IN)
GPIO.setup(button[1], GPIO.IN)
GPIO.setup(button[2], GPIO.IN)
GPIO.setup(button[3], GPIO.IN)

# Turn on the LEDs
GPIO.output(led[0], 1)
GPIO.output(led[1], 1)
GPIO.output(led[2], 1)
GPIO.output(led[3], 1)

# Map buttons to LEDs
map = {button[0]: led[0], button[1]: led[1], button[2]: led[2], button[3]: led[3]}

def updateLED(channel):      #interrupt
    state = GPIO.input(channel)     #get the state
    GPIO.output(map[channel], state) #toggle the LED

print("Running...")

GPIO.add_event_detect(button[0], GPIO.BOTH, callback=updateLED) #adding the interrupt
GPIO.add_event_detect(button[1], GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(button[2], GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(button[3], GPIO.BOTH, callback=updateLED)

try:
    while True:
        time.sleep(100)   # Let other processes run

except KeyboardInterrupt:
    print("Cleaning Up")
    GPIO.cleanup()
