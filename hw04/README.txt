HW04

GPIO via mmap
This part of the homework can be found in the file gpioThru.c and mmaptoggle.c. These files can be found precompiled in the file gpiothru and mmaptoggle.
This homework was intended to teach about memory mapping so I started with gpioThru. For this I had to edit the file to read a switch and light an led to match. This is done with USR3 as the LED and a button on GP0_25. The next part was to expand on that concept. In mmaptoggle.c I took two buttons on GPIO3 and two LEDs on GPIO1 and would light the matching LED when a button was pressed.

Rotary Encoders
This part of the homework can be found in the file Etchwdisplay.py
This program continues to build of of the previous homeworks. This time the buttons are replaced with two rotary encoders more simmilar to an actual etch-a-sketch. Then spinning the encoders the screen will move the draw pixel to match.

# Comments from Prof. Yoder
# Found your memory map file, but it was missing the .png so it was hard to read.
# Looks good.
# Grade:  9/10