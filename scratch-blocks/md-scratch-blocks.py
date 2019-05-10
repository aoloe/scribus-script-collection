#!/usr/bin/env python
# -*- coding: utf-8 -*-
# © 2019 MIT license, Ale Rimoldi <a.l.e@graphicslab.org>

import os
import sys
import argparse
import re
from subprocess import check_output

parser = argparse.ArgumentParser(description='Convert a svn referenced in a markdown line into png.')
parser.add_argument('-p', dest='path', action='store',
    default=None,
    help='Base path, where the .md file is located')
parser.add_argument('-d', dest='download_path', action='store',
    default=None,
    help='Download path, where the scratchblocks.svg file is located')
parser.add_argument(dest='lines', nargs='?', type=argparse.FileType('r'), default=sys.stdin)

args = parser.parse_args()

base_path = '' if args.path is None else args.path
download_path = '/tmp/' if args.download_path is None else args.download_path

scratchblocks_svg = os.path.join(download_path, 'scratchblocks.svg')


if not os.path.isfile(scratchblocks_svg):
    sys.exit(1)

for l in args.lines:
    m = re.search('\((.+)\)', l)
    if m:
        # print(m.group(1))
        filename_svg = os.path.join(base_path, m.group(1))
        filename_png = os.path.splitext(filename_svg)[0] + '.png'

        # print(filename_png)
        # print(filename_svg)
        os.rename(scratchblocks_svg, filename_svg)

        # https://gitlab.com/inkscape/inbox/issues/405
        # FitCanvasToDrawing cannot be run without a GUI
        out = check_output(['inkscape', '--verb=FitCanvasToDrawing', '--verb=FileSave', '--verb=FileQuit', filename_svg])
        out = check_output(['inkscape', '-z', '--export-dpi=300', filename_svg, '-e', filename_png])
        # print(out)

        break
