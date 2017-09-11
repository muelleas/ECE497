#!/usr/bin/env python3
# Reads the PAUSE button using interupts and sets the LED
# Pin table at https://github.com/beagleboard/beaglebone-blue/blob/master/BeagleBone_Blue_Pin_Table.csv

# Import PyBBIO library:
import Adafruit_BBIO.GPIO as GPIO
import time

button = ["GP0_3", "GP0_4", "GP0_5", "GP0_6"]
led = ["GP1_3", "GP1_4", "RED", "GREEN"]

# Set the GPIO pins:
GPIO.setup(led[0],    GPIO.OUT)
GPIO.setup(led[1],    GPIO.OUT)
GPIO.setup(led[2],    GPIO.OUT)
GPIO.setup(led[3],    GPIO.OUT)

GPIO.setup(button[0], GPIO.IN)
GPIO.setup(button[1], GPIO.IN)
GPIO.setup(button[2], GPIO.IN)
GPIO.setup(button[3], GPIO.IN)

# Turn on both LEDs
GPIO.output(led[0], 1)
GPIO.output(led[1], 1)
GPIO.output(led[2], 1)
GPIO.output(led[3], 1)

# Map buttons to LEDs
map = {button[0]: led[0], button[1]: led[1], button[2]: led[2], button[3]: led[3]}

def updateLED(channel):
    print("channel = " + channel)
    state = GPIO.input(channel)
    GPIO.output(map[channel], state)
    print(map[channel] + " Toggled")

print("Running...")

GPIO.add_event_detect(button[0], GPIO.BOTH, callback=updateLED) # RISING, FALLING or BOTH
GPIO.add_event_detect(button[1], GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(button[2], GPIO.BOTH, callback=updateLED)
GPIO.add_event_detect(button[3], GPIO.BOTH, callback=updateLED)

try:
    while True:
        time.sleep(100)   # Let other processes run

except KeyboardInterrupt:
    print("Cleaning Up")
    GPIO.cleanup()
