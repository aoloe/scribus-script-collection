""" Ad hoc script for moving the Ada & Zangenmann to RTL

Cache the size and position of the full page items, reduce their size,
and put them in the middle of their page.

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
    items = []
    for page in range(1, scribus.pageCount() + 1):
        scribus.gotoPage(page)
        page_size = scribus.getPageNSize(page)
        for item, _, _ in scribus.getPageItems():
            item_position = scribus.getPosition(item)
            item_size = scribus.getSize(item)
            if item_size[0] >= page_size[0] and item_size[1] >= page_size[1]:
                items.append((page, item, item_position, item_size))
                scribus.sizeObject(page_size[0] / 2, item_size[1] / 2, item)
                scribus.moveObject(page_size[0] / 4, page_size[1] / 4, item)
    with open(SCRIPT_PATH.joinpath('data.json'), 'w') as f:
        json.dump(items, f)
    scribus.docChanged(True)

if __name__ == "__main__":
    main()

