#!/usr/bin/env python3
# File: i2ctmp101.py
# Author: Andrew Mueller
# This program watched 2 tmp101s to see when they reach a given tempeture and then display the current tempeture in F

import Adafruit_BBIO.GPIO as GPIO
import smbus
import time
bus = smbus.SMBus(1)  # set up bus

address0 = 0x48       #addresses of tmp101's
address1 = 0x49
alert0 = "GP0_3"      #pins the alerts are tied to
alert1 = "GP0_4"
map = {alert0: address0, alert1: address1}   #map the alerts to the proper sensor

# init setup
GPIO.setup(alert0, GPIO.IN)
GPIO.setup(alert1, GPIO.IN)

bus.write_byte_data(address0, 3, 24)   #set the upper and lower bounds for the alert pins
bus.write_byte_data(address0, 2, 24)

bus.write_byte_data(address1, 3, 24)
bus.write_byte_data(address1, 2, 24)


def tempPrint(channel):   #print the converted temp
    device = map[channel]
    temp = bus.read_byte_data(device, 0)
    print (temp*9/5+32)

# attach interrupts
GPIO.add_event_detect(alert0, GPIO.FALLING, callback=tempPrint)
GPIO.add_event_detect(alert1, GPIO.FALLING, callback=tempPrint)

try:
    print("running")
    while True:
        time.sleep(100)
except KeyboardInterrupt:
    print("cleanup")
    GPIO.cleanup()
