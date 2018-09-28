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

item = scribus.getSelectedObject()

if (scribus.getObjectType(item) != 'TextFrame'):
    scribus.messageBox('Usage Error', 'You need to select a text frame', icon=0, button1=1)
    sys.exit(2)

print(scribus.getTextLength(item))
if scribus.getTextLength(item) > 0:
    scribus.messageBox('Usage Error', 'The text frame should be empty', icon=0, button1=1)
    sys.exit(2)

answer = scribus.valueDialog('Numbered lines', 'Start number, step', '1,1') 
start, step = answer.split(',')
start = int(start)
step = int(step)

i = start
print(scribus.textOverflows(item))
while scribus.textOverflows(item) == 0 :
    if i == start or i % step == 0:
        scribus.insertText(str(i)+"\n", -1, item)
    else:
        scribus.insertText("\n", -1, item)
    i += 1

length = scribus.getTextLength(item)
while scribus.textOverflows(item) != 0 :
    scribus.selectText(length - 2, 1, item)
    scribus.deleteText(item)
    length -= 1
