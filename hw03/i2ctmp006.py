#!/usr/bin/env python3

import smbus
import time

bus = smbus.SMBus(1)
address = 64

try:
    print("running")
    while True:
        temp = bus.read_byte_data(address, 1)
        print(temp)
        time.sleep(1)
except KeyboardInterrupt:
    print("cleanup")
