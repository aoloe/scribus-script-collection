# -*- coding: utf-8 -*-
# © 2018, MIT license, Ale Rimoldi <a.l.e@graphicslab.org>

import scribus
import sys

if not scribus.haveDoc():
    scribus.messageBox('Usage Error', 'You need a Document open', icon=0, button1=1)
    sys.exit(2)

if scribus.selectionCount() == 0:
    scribus.messageBox('Usage Error', 'You need to select a frame', icon=0, button1=1)
    sys.exit(2)

unit = scribus.getUnit()
scribus.setUnit(unit)
scribus.setUnit(scribus.UNIT_MILLIMETERS)

item = scribus.getSelectedObject()
size = scribus.getSize(item)
position = scribus.getPosition(item)

thickness = 3

items_border = []

items_border.append(scribus.createRect(position[0], position[1], size[0], thickness))
items_border.append(scribus.createRect(position[0], position[1], thickness, size[1]))
items_border.append(scribus.createRect(position[0], position[1] + size[1] - thickness, size[0], thickness))
items_border.append(scribus.createRect(position[0] + size[0] - thickness, position[1],  thickness, size[1]))

for i in items_border:
    scribus.setFillColor('Black', i)

scribus.groupObjects(items_border)

scribus.setUnit(unit)
