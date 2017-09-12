#!/usr/bin/env python3
# Read a TMP101 sensor

import Adafruit_BBIO.GPIO as GPIO
import smbus
import time
bus = smbus.SMBus(1)
address = 0x48
alert = "GP0_3"

GPIO.setup(alert, GPIO.IN)

bus.write_byte_data(address, 3, 23)
bus.write_byte_data(address, 2, 22)

def tempPrint(channel):
    temp = bus.read_byte_data(address, 0)
    print("hot")
    print (temp)

GPIO.add_event_detect(alert, GPIO.BOTH, callback=tempPrint)

try:
    print("running")
    while True:
        #temp = bus.read_byte_data(address, 0)
        #print(temp)
        time.sleep(.25)
except KeyboardInterrupt:
    print("cleanup")
    GPIO.cleanup()
