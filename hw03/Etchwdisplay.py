#!/usr/bin/env python3
# File: EthchWButtons.py
# Author: Andrew Mueller
#
# This file takes input form 4 buttons on GP0 and the PAU button. With these inputs a game of Etch-a-sketch is played in the terminal.
#The buttons on GP0 act as directionals and PAU is the reset.

import Adafruit_BBIO.GPIO as GPIO
import time
import smbus
bus = smbus.SMBus(1)
matrix = 0x70

button = ["GP0_3", "GP0_4", "GP0_5", "GP0_6"]   # the buttons used
map = {button[0]:'u', button[1]:'r', button[2]: 'd', button[3]:'l'} #map the buttons to their dirrection
resetButton = "PAUSE"  #the clear button

#setup GPIO
GPIO.setup(button[0], GPIO.IN)
GPIO.setup(button[1], GPIO.IN)
GPIO.setup(button[2], GPIO.IN)
GPIO.setup(button[3], GPIO.IN)
GPIO.setup(resetButton, GPIO.IN)

bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)

#Game board setup
size = 8
xPos = 4
yPos = 4
array = [0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 
         0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00];

def reset(channel = 'NULL'):  #clears the board
    for i in range(0, 2*size):  #set all tiles to empty
        array[i] = 0x00
    array[2*xPos + 1] =   pow(2, yPos)  #place cursor
    printArray();

def printArray():		#prints the board
    bus.write_i2c_block_data(matrix, 0, array)

def update(channel):
    global xPos
    global yPos
    if GPIO.input(channel):
        if (channel == button[0]) | (channel == button[2]):
            time.sleep(.05)
            return
    else:
        if (channel == button[1]) | (channel == button[3]):
            time.sleep(.05)
            return
    array[2*xPos] = array[2*xPos] | array[2*xPos+1] 
    array[2*xPos + 1] = 0x00
    if map[channel] == 'd':   #moves the currsor
        if xPos < size-1:
            xPos += 1
    if map[channel] == 'u':
        if xPos > 0:
            xPos += -1
    if map[channel] == 'r':
        if yPos < size-1:
            yPos += 1
    if map[channel] == 'l':
        if yPos > 0:
            yPos += -1
    array[2*xPos] = array[2*xPos] | array[2*xPos+1] 
    array[2*xPos + 1] =   pow(2, yPos)  #place cursor
    printArray()
    time.sleep(.05)

GPIO.add_event_detect(button[0], GPIO.BOTH, callback=update)	#adding the interrupts
GPIO.add_event_detect(button[1], GPIO.BOTH, callback=update)
GPIO.add_event_detect(button[2], GPIO.BOTH, callback=update)
GPIO.add_event_detect(button[3], GPIO.BOTH, callback=update)
GPIO.add_event_detect(resetButton, GPIO.FALLING, callback=reset)

try:
    reset()
    while True:
        time.sleep(100)

except KeyboardInterrupt:
    print("cleaning up")
    GPIO.cleanup()

