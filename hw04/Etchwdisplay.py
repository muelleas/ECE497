#!/usr/bin/env python3
# File: EthchWButtons.py
# Author: Andrew Mueller
#
# This file takes input form 4 buttons on GP0 and the PAU button. With these inputs a game of Etch-a-sketch is played on a 8 by 8led matrix
#The buttons on GP0 act as directionals and PAU is the reset.

import Adafruit_BBIO.GPIO as GPIO
import time
import rcpy
import rcpy.encoder as encoder
import smbus
bus = smbus.SMBus(1)   # set up the bus
rcpy.set_state(rcpy.RUNNING)
print('runnimg')

matrix = 0x70	# address of the display
resetButton = "PAUSE"  #the clear button

#setup GPIO
GPIO.setup(resetButton, GPIO.IN)

#set up the display
bus.write_byte_data(matrix, 0x21, 0)
bus.write_byte_data(matrix, 0x81, 0)
bus.write_byte_data(matrix, 0xe7, 0)

#encoders values
xloc = 0
yloc = 0

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

def update():
    global xPos
    global yPos
    global xloc
    global yloc
    e2 = encoder.get(2)
    e3 = encoder.get(3)
    array[2*xPos] = array[2*xPos] | array[2*xPos+1] 
    array[2*xPos + 1] = 0x00
    diffx = (e2-xloc)//4
    diffy = (e3-yloc)//4
    if diffx > 0:   #moves the currsor
        if xPos < size-1:
            xPos += 1
    if diffx < 0:
        if xPos > 0:
            xPos += -1
    if diffy > 0:
        if yPos < size-1:
            yPos += 1
    if diffy < 0:
        if yPos > 0:
            yPos += -1
    xloc = e2
    yloc = e3
    array[2*xPos] = array[2*xPos] | array[2*xPos+1] 
    array[2*xPos + 1] =   pow(2, yPos)  #place cursor
    printArray()
    
GPIO.add_event_detect(resetButton, GPIO.FALLING, callback=reset)

try:
    reset()
    while True:
        #if rcpy.get_state() == rcpy.RUNNING:
        update()
        time.sleep(.1)

except KeyboardInterrupt:
    print("cleaning up")
    GPIO.cleanup()

