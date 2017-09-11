#!/usr/bin/env python3

import Adafruit_BBIO.GPIO as GPIO
import time

button = ["GP0_3", "GP0_4", "GP0_5", "GP0_6"]
map = {button[0]:'r', button[1]:'d', button[2]:'l', button[3]:'u'}
resetButton = "PAUSE"

GPIO.setup(button[0], GPIO.IN)
GPIO.setup(button[1], GPIO.IN)
GPIO.setup(button[2], GPIO.IN)
GPIO.setup(button[3], GPIO.IN)
GPIO.setup(resetButton, GPIO.IN)

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

def reset(channel = 'NULL'):
    for i in range(0, size+1):
        for j in range(0, size+1):
            array[i][j] = ' '
    for i in range(0, size):
        array[0][i+1] = i
        array[i+1][0] = i
    array[xPos][yPos] = 'o'
    printArray();

def printArray():
    for i in range(0, size+1):
        print(*array[i])

def updateBoard(channel):
    print("channel"+ channel)
    global xPos
    global yPos
    if map[channel] == 'd':
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
    array[xPos][yPos] = 'o'
    printArray()

GPIO.add_event_detect(button[0], GPIO.FALLING, callback=updateBoard)
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

