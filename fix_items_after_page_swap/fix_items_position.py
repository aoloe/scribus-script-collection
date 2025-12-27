""" Ad hoc script for moving the Ada & Zangenmann to RTL

Restore the full page items size and position from the cached values;
move all other items by the difference in the inner / outer margins.

(c) MIT 2025 ale rimoldi"""

try:
    import scribus
except ImportError as ex:
    print('\nThis script must be run from inside Scribus\n')
    raise ex
import json
from pathlib import Path

SCRIPT_PATH = Path(__file__).parent

def main():
    processed = []
    items = []
    with open(SCRIPT_PATH.joinpath('data.json'), 'r') as f:
        items = json.load(f)
    for page, item_name, item_position, item_size in items:
        if page < scribus.pageCount():
            page += 1
        scribus.gotoPage(page)
        page_size = scribus.getPageSize()
        if page % 2 == 0:
            scribus.moveObjectAbs(0, item_position[1], item_name)
        else:
            scribus.moveObjectAbs(item_position[0], item_position[1], item_name)
        processed.append(item_name)
        scribus.sizeObject(*item_size, item_name)
    # fix the position of the items by the difference between the inner and outer margin
    for page in range(1, scribus.pageCount() + 1):
        scribus.gotoPage(page)
        page_size = scribus.getPageSize()
        page_margins = scribus.getPageMargins()
        move_by = page_margins[1] - page_margins[2]
        if page % 2 != 0:
            move_by *= -1
        for item, _, _ in scribus.getPageItems():
            if item in processed:
                continue
            scribus.moveObject(move_by, 0, item)
    scribus.docChanged(True)
if __name__ == "__main__":
    main()

