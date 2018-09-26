# -*- coding: utf-8 -*-
# © 2009, 2018, MIT license, Ale Rimoldi <a.l.e@graphicslab.org>
"""
this script adjust the top and bottom distance of a text frame
to exactly put its content in the middle of the frame
"""

import sys
try:
   import scribus
except ImportError:
   print("This script only works from within Scribus")
   sys.exit(1)

# check that the selection is one text frame and get that frame
frame_n = scribus.selectionCount()
if frame_n == 0 :
    scribus.messageBox('Error:', 'No frame selected');
    sys.exit(1)
elif frame_n > 1 :
    scribus.messageBox('Error:', 'You may select only one frame');
    sys.exit(1)

frame = scribus.getSelectedObject(0)
try:
    char_n = scribus.getTextLength(frame)
except scribus.WrongFrameTypeError:
    scribus.messageBox('Error:', 'You may only adjust text frames');
    sys.exit(1)

if char_n == 0 :
    scribus.messageBox('Error:', 'You can\'t adjust an empty frame');
    sys.exit(1)

if (scribus.textOverflows(frame) == 1) :
    scribus.messageBox('Error:', 'You can\' center a text which is overflowing');
    sys.exit(1)

# get some page and frame measure

(x, y) = scribus.getPosition(frame)

(w, h) = scribus.getSize(frame)

original_height = h

(dl, dr, dt, db) = scribus.getTextDistances();

scribus.setTextDistances(dl, dr, 0, 0);

# if the frame doesn't overflow, shorten it to make it overflow
while ((scribus.textOverflows(frame) == 0) and (h > 0)) :
    h -= 10
    scribus.sizeObject(w, h, frame)

# resize the frame in 10pt steps
while (scribus.textOverflows(frame) > 0) :
    h += 10
    scribus.sizeObject(w, h, frame)

# undo the latest 10pt step and fine adjust in 1pt steps
h -= 10
scribus.sizeObject(w, h, frame)

while (scribus.textOverflows(frame) > 0) :
    h += 1
    scribus.sizeObject(w, h, frame)


scribus.sizeObject(w, original_height, frame)

dt = (original_height - h) / 2

scribus.setTextDistances(dl, dr, dt, dt);
