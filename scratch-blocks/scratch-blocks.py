#!/usr/bin/env python
# -*- coding: utf-8 -*-
# © 2019 MIT license, Ale Rimoldi <a.l.e@graphicslab.org>

import sys
import os
from subprocess import call
import scribus

print('---')

download_path = '/tmp/'

# TODO: make sure that there is a document
# TODO: make sure that the document has been saved (has a name)

frame_n = scribus.selectionCount()

if frame_n == 0 :
    scribus.messageBox('Error:', 'No frame selected');
    sys.exit(1)
elif frame_n > 1 :
    scribus.messageBox('Error:', 'Please select one single frame');
    sys.exit(1)

item = scribus.getSelectedObject(0)

path_images = None
filename_png = None
path_png = None
path_svg = None

if (scribus.getObjectType(item) == 'TextFrame'):
    path = scribus.getAllText()
    if path != '':
        base_path = os.path.dirname(scribus.getDocName())
        filename_png = os.path.join(base_path, path)
elif (scribus.getObjectType(item) == 'ImageFrame'):
    filename_png = scribus.getImageFile()

if path_png == '':
    filename_png = None

if filename_png == None:
    scribus.messageBox('Error:', 'You need to select a text frame containing the path to the image or an image frame with an old version of the image');
    sys.exit(1)

print(filename_png)

filename_svg = os.path.splitext(filename_png)[0] + '.svg'

print(filename_svg)

scratchblocks_svg = os.path.join(download_path, 'scratchblocks.svg')
print(scratchblocks_svg + ' >> ' + filename_svg)
if os.path.isfile(scratchblocks_svg):
    os.rename(scratchblocks_svg, filename_svg)
else:
    scribus.messageBox('Error:', 'Cannot find ' + filename_svg);


call(['inkscape', '-z', '--verb=FitCanvasToDrawing', '--verb=FileSave', '--verb=FileQuit', filename_svg])
call(['inkscape', '-z', '--export-dpi=300', filename_svg, '-e', filename_png])

if (scribus.getObjectType(item) == 'TextFrame'):
    (x, y) = scribus.getPosition()
    (w, h) = scribus.getSize()
    scribus.deleteObject()
    name = scribus.createImage(x, y, w, h)
    scribus.selectObject(name)
    scribus.loadImage(filename_png)
