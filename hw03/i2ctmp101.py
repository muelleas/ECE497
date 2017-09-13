#!/usr/bin/env python3
# Read a TMP101 sensor

import Adafruit_BBIO.GPIO as GPIO
import smbus
import time
bus = smbus.SMBus(1)
address0 = 0x48
address1 = 0x49
alert0 = "GP0_3"
alert1 = "GP0_4"
map = {alert0: address0, alert1: address1}

GPIO.setup(alert0, GPIO.IN)
GPIO.setup(alert1, GPIO.IN)

bus.write_byte_data(address0, 3, 24)
bus.write_byte_data(address0, 2, 24)

bus.write_byte_data(address1, 3, 24)
bus.write_byte_data(address1, 2, 24)


def tempPrint(channel):
    device = map[channel]
    temp = bus.read_byte_data(device, 0)
    print("hot")
    print (temp*9/5+32)

GPIO.add_event_detect(alert0, GPIO.FALLING, callback=tempPrint)
GPIO.add_event_detect(alert1, GPIO.FALLING, callback=tempPrint)

try:
    print("running")
    while True:
        #temp = bus.read_byte_data(address0,0)
        #print(temp)
        time.sleep(100)
except KeyboardInterrupt:
    print("cleanup")
    GPIO.cleanup()
