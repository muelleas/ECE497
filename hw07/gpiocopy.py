#!/usr/bin/env python3
# File: fourbuttons.py
# Author: Andrew Mueller
#
# This file takes input form 4 buttons on GP0 and toggles 4 leds on GP1

# Import PyBBIO library:
import Adafruit_BBIO.GPIO as GPIO
import time

# Set the GPIO pins:
GPIO.setup("GP1_3",    GPIO.IN)
GPIO.setup("GP1_4",    GPIO.OUT)

def updateLED(channel):      #interrupt
    state = GPIO.input(channel)     #get the state
    GPIO.output("GP1_4", state)     #toggle the LED

print("Running...")

GPIO.add_event_detect("GP1_3", GPIO.BOTH, callback=updateLED) #adding the interrupt

try:
    while True:
        time.sleep(100)   # Let other processes run

except KeyboardInterrupt:
    print("Cleaning Up")
    GPIO.cleanup()
