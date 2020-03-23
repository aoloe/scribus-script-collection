#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Extracts all images that are embedded in a .sla file into individual image files.
© 2019 MIT license, Ale Rimoldi <a.l.e@graphicslab.org>
"""
import os
import sys
import argparse
import re
import zlib
from pathlib import Path
import base64

parser = argparse.ArgumentParser(description='Extracts all images that are embedded in a .sla file into individual image files.')
parser.add_argument('in_file',
                   help='.sla file to be processed.')
parser.add_argument('-o', dest='out_file', action='store',
                   help='Destination .sla file.')
parser.add_argument('-i', dest='out_images', action='store',
                   help='Destination directory for the images.')

args = parser.parse_args()

SLA_INPUT_FILE = args.in_file
PARENT_PATH = Path(SLA_INPUT_FILE).parent
SLA_OUTPUT_FILE = args.out_file if args.out_file is not None else Path(PARENT_PATH) / (Path(SLA_INPUT_FILE).stem + '-out.sla')
IMAGES_RELATIVE_PATH = 'images'
IMAGES_ABSOLUTE_PATH = args.out_images if args.out_images is not None else Path(PARENT_PATH) / IMAGES_RELATIVE_PATH

if not os.path.exists(IMAGES_ABSOLUTE_PATH):
    print('cannot store images', IMAGES_ABSOLUTE_PATH, 'does not exist')
    sys.exit()
    # os.makedirs(images_paths)

p_image_ext = re.compile(r'inlineImageExt="(.+?)"')
p_item_id = re.compile(r'ItemID="(.+?)"')
p_page = re.compile(r'OwnPage="(.+?)"')

with open(SLA_INPUT_FILE) as sla_input:
    with open(SLA_OUTPUT_FILE, 'w') as sla_output:
        for line in sla_input:
            pos_start = line.find('ImageData')
            if pos_start > 0:
                image_type = p_image_ext.search(line)[1]
                # print(match_image_ext[1])
                item_id = p_item_id.search(line)[1]
                page_number = max(int(p_page.search(line)[1]), 0)

                image_file = f'{page_number:03d}-{item_id}.{image_type}'
                print(image_file)
                 
                pos_start += 11
                pos_end = line.find('"', pos_start)
                with open(Path(IMAGES_ABSOLUTE_PATH) / image_file, 'wb') as image_output:
                    # images are qcompress(ed) and stored as base64.
                    # to decompress a qcompress bytes sequence one need to remove the first 4 bytes (size information)
                    # see https://doc.qt.io/qt-5/qbytearray.html#qUncompress
                    # see Scribus150Format::pasteItem
                    decoded = base64.standard_b64decode(line[pos_start:pos_end])
                    image_output.write(zlib.decompress(decoded[4:]))
                line = line[0:pos_start - 11] + line[pos_end + 1:]
                # print(line)
                # replace: PFILE="relative url"
                # remove: isInlineImage="1" inlineImageExt="*", ImageData="*"
                line = line.replace('isInlineImage="1"', '')
                line = line.replace(f'inlineImageExt="{image_type}"', '')
                line = line.replace('PFILE=""', f'PFILE="{Path(IMAGES_RELATIVE_PATH) / image_file}"')
                # re.sub(r'inlineImageExt=".\{-}"', '', line)
                # print(line)
                # sys.exit()
            sla_output.write(line)



# A linked image:
#         <PAGEOBJECT XPOS="280.5" YPOS="260.945881889764" OwnPage="0" ItemID="28811912" PTYPE="2" WIDTH="159" HEIGHT="120.804118110236" FRTYPE="0" CLIPEDIT="0" PWIDTH="1" PLINEART="1" LOCALSCX="0.125837623031496" LOCALSCY="0.125837623031496" LOCALX="0" LOCALY="0" LOCALROT="0" PICART="1" SCALETYPE="0" RATIO="1" Pagenumber="0" PFILE="bleiben.jpg" PRFILE="Embedded c2" EPROF="Embedded c2" IRENDER="0" path="M0 0 L159 0 L159 120.804 L0 120.804 L0 0 Z" copath="M0 0 L159 0 L159 120.804 L0 120.804 L0 0 Z" gXpos="280.5" gYpos="260.945881889764" gWidth="0" gHeight="0" LAYER="0" NEXTITEM="-1" BACKITEM="-1"/>
#
# An embedded image (with ImageData emptied)
#         <PAGEOBJECT XPOS="406.0008" YPOS="59202.2288" OwnPage="141" ItemID="1365294098" PTYPE="2" WIDTH="234" HEIGHT="231.72" FRTYPE="0" CLIPEDIT="0" PWIDTH="1" PLINEART="1" LOCALSCX="0.12" LOCALSCY="0.12" LOCALX="0" LOCALY="0" LOCALROT="0" PICART="1" SCALETYPE="0" RATIO="1" Pagenumber="0" PFILE="" isInlineImage="1" inlineImageExt="tiff" ImageData="" PRFILE="sRGB IEC61966-2.1" IRENDER="0" EMBEDDED="0" path="M0 0 L234 0 L234 231.72 L0 231.72 L0 0 Z" copath="M0 0 L234 0 L234 231.72 L0 231.72 L0 0 Z" gXpos="406.0008" gYpos="59202.2288" gWidth="0" gHeight="0" LAYER="0" NEXTITEM="-1" BACKITEM="-1"/>
