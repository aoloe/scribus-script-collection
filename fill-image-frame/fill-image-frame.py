# -*- coding: utf-8 -*-
# © 2018, MIT license, Ale Rimoldi <a.l.e@graphicslab.org>

import scribus
import sys

if not scribus.haveDoc():
    scribus.messageBox('Usage Error', 'You need a Document open', icon=0, button1=1)
    sys.exit(2)

# TODO: ask for the range of pages (current page if empty)


unit = scribus.getUnit()
scribus.setUnit(unit)
scribus.setUnit(scribus.UNIT_MILLIMETERS)


item = scribus.getSelectedObject()

path = scribus.getImageFile(item)
if path == '':
    scribus.messageBox('Usage Error', 'You need to first load an image', icon=0, button1=1)
    sys.exit(2)

scribus.setScaleImageToFrame(True, False, item)
scribus.setScaleImageToFrame(False, False, item)
scale = scribus.getImageScale(item)
max_scale = max(scale)
scribus.setImageScale(max_scale, max_scale, item)

scribus.setUnit(unit)
