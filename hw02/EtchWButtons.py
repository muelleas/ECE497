#!/usr/bin/env python3
# File: EthchWButtons.py
# Author: Andrew Mueller
#
# This file takes input form 4 buttons on GP0 and the PAU button. With these inputs a game of Etch-a-sketch is played in the terminal.
#The buttons on GP0 act as directionals and PAU is the reset.

import Adafruit_BBIO.GPIO as GPIO
import time

button = ["GP0_3", "GP0_4", "GP0_5", "GP0_6"]   # the buttons used
map = {button[0]:'r', button[1]:'d', button[2]:'l', button[3]:'u'} #map the buttons to their dirrection
resetButton = "PAUSE"  #the clear button

#setup GPIO
GPIO.setup(button[0], GPIO.IN)
GPIO.setup(button[1], GPIO.IN)
GPIO.setup(button[2], GPIO.IN)
GPIO.setup(button[3], GPIO.IN)
GPIO.setup(resetButton, GPIO.IN)

#Game board setup
size = 8
xPos = 1
yPos = 1
array = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']];

def reset(channel = 'NULL'):  #clears the board
    for i in range(0, size+1):  #set all tiles to empty
        for j in range(0, size+1):
            array[i][j] = ' '
    for i in range(0, size):     #place the side numbers
        array[0][i+1] = i
        array[i+1][0] = i
    array[xPos][yPos] = 'o'     #place curser
    printArray();

def printArray():		#prints the board
    for i in range(0, size+1):
        print(*array[i])

def updateBoard(channel):
    global xPos
    global yPos
    if map[channel] == 'd':   #moves the currsor
        if xPos < size:
            xPos += 1
    if map[channel] == 'u':
        if xPos > 1:
            xPos += -1
    if map[channel] == 'r':
        if yPos < size:
            yPos += 1
    if map[channel] == 'l':
        if yPos > 1:
            yPos += -1
    array[xPos][yPos] = 'o'   #place cursor
    printArray()
    time.sleep(.05)	#debounce button

GPIO.add_event_detect(button[0], GPIO.FALLING, callback=updateBoard)	#adding the interrupts
GPIO.add_event_detect(button[1], GPIO.FALLING, callback=updateBoard)
GPIO.add_event_detect(button[2], GPIO.FALLING, callback=updateBoard)
GPIO.add_event_detect(button[3], GPIO.FALLING, callback=updateBoard)
GPIO.add_event_detect(resetButton, GPIO.FALLING, callback=reset)

try:
    reset()
    while True:
        time.sleep(100)

except KeyboardInterrupt:
    print("cleaning up")
    GPIO.cleanup()

