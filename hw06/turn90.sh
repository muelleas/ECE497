#!/bin/sh
#turn the display to 90 degrees
# Connect the display before running this.

sudo bash << EOF
    # remove the framebuffer modules
    rmmod --force fb_ili9341
    rmmod --force fbtft
    rmmod --force fbtft_device
    
    sleep 1
    
    # Insert the framebuffer modules
    modprobe fbtft_device name=adafruit28 busnum=1 rotate=90 gpios=reset:113,dc:116 cs=0

EOF
