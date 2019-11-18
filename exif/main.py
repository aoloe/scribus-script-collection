# encoding: utf-8
try:
    import scribus
except ImportError:
    print('This script must be run from inside Scribus')

# from exif import Image
# 
# with open('hiker-playmobil.jpg', 'rb') as image_file:
#     my_image = Image(image_file)
# 
# print(my_image.has_exif)

from iptcinfo3 import IPTCInfo

if not scribus.haveDoc():
    print("You need an open docuemnt")

item_name = scribus.getSelectedObject()
item_type = scribus.getObjectType


if item_type != 'Image':
    print("You need to select an image frame")

path = scribus.getImageFile()

if path == '':
    print("You need to an image in the frame")

x, y = scribus.getPosition()

width, height =  scribus.getSize()

info = IPTCInfo(path)
print(info)

text_content = info['object name'].decode("utf-8") + '\n' + info['copyright notice'].decode("utf-8")

unit = scribus.getUnit()
scribus.setUnit(unit)
scribus.setUnit(scribus.UNIT_MILLIMETERS)

text_frame = scribus.createText(x, y + height, width, 20)


scribus.setText(text_content, text_frame)

scribus.setUnit(unit)
