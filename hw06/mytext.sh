# File: mytext.sh
# Author: Andrew Mueller
# This file take the image of boris and resizes it to the screen.
# It then writes some text on it and then displayes it on the screen

SIZE=320x240
TMP_FILE=/tmp/frame.png

#place boris on the frame with some text on it.
convert boris.png -resize $SIZE -fill black -font Times-Roman -pointsize 35\
       	-draw "text 0,50 'By Andrew'" -draw "text 0,225 'Boris.png'"\
       	$TMP_FILE

#show frame
sudo fbi -noverbose -T 1 $TMP_FILE


