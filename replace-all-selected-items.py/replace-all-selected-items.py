# encoding: utf-8
# (c) MIT, ale rimoldi <ale@graphicslab.org>

import logging
from pathlib import Path

"""
Export all Scribus Scripter API commands into a set of Markdown files.
For more details see the README.md
"""

try:
    import scribus
except ImportError:
    print('This script must be run from inside Scribus')

def main():
    pass

    SCRIPT_PATH = Path(__file__).parent

    logging.basicConfig(
        filename=SCRIPT_PATH.joinpath('logs.txt'),
        level=logging.DEBUG, filemode='w')

    n = scribus.selectionCount()
    if n == 0:
        logging.warning('No item selected')
        return
    
    items = []
    for i in range(n):
        items.append(scribus.getSelectedObject(i))
    
    for item in items:
        pos = scribus.getPosition(item)
        dx, dy = pos
        scribus.pasteObject()
        new_item = scribus.getSelectedObject()
        pos = scribus.getPosition(new_item)
        dx, dy = dx - pos[0], dy - pos[1]
        scribus.moveObject(dx, dy, new_item)
        scribus.deleteObject(item)

    
if __name__ == '__main__':
    main()
