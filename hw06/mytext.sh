# Here's how to use imagemagick to display text
# Make a blank image
SIZE=320x240
TMP_FILE=/tmp/frame.png

# From: http://www.imagemagick.org/Usage/text/
convert boris.png -resize $SIZE -fill black -font Times-Roman -pointsize 35\
       	-draw "text 0,50 'By Andrew'" -draw "text 0,225 'Boris.png'"\
       	-append $TMP_FILE

sudo fbi -noverbose -T 1 $TMP_FILE


