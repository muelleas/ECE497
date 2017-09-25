#!/usr/bin/env python3

import smbus
import time

bus = smbus.SMBus(1)
address = 64

try:
    print("running")
    while True:
        temp = bus.read_word_data(address, 0)
        print(temp)
        time.sleep(1)
except KeyboardInterrupt:
    print("cleanup")
