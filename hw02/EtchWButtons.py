#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time

button = ["GP0_3", "GP0_4", "GP0_5", "GP0_6"]

GPIO.setup(button[0], GPIO.IN)
GPIO.setup(button[1], GPIO.IN)
GPIO.setup(button[2], GPIO.IN)
GPIO.setup(button[3], GPIO.IN)

def updateBoard(channel):
    print("channel")

GPIO.add_event_detect(button[0], GPIO.BOTH, callback=updateBoard)
GPIO.add_event_detect(button[1], GPIO.BOTH, callback=updateBoard)
GPIO.add_event_detect(button[2], GPIO.BOTH, callback=updateBoard)
GPIO.add_event_detect(button[3], GPIO.BOTH, callback=updateBoard)

try:
    while True:
        time.sleep(100)

except KeyboardInterrupt:
    print("cleaning up")
    GPIO.cleanup()

