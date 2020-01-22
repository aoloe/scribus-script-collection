# -*- coding: utf-8 -*-
# (c) mit, ale rimoldi, 2020

import sys

try:
    import scribus
except ImportError as err:
    print("This script can can only be run from within Scribus.")
    sys.exit(1)

def main():
    if not scribus.haveDoc():
        return

    for color_name in scribus.getColorNames():
        if not color_name.startswith(('FromSVG', 'FromPDF')):
            continue
        c, m, y, k = scribus.getColor(color_name)
        cmyk_name = color_name[0:8]
        cmyk_name += f"{c*100//255:02x}{m*100//255:02x}{y*100//255:02x}{k*100//255:02x}"
        scribus.defineColor(cmyk_name, c, m, y, k)
        scribus.deleteColor(color_name, cmyk_name)

if __name__ == '__main__':
    main()
