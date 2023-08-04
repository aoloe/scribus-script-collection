# go through all text items in the document, search for a text snippet and apply a character style
#
# © mit, ale rimoldi, 2023

import re

search_text = '…'
character_style = 'fancy style'

try:
    import scribus
except ImportError:
    print('This script must be run from inside Scribus')
    sys.exit()

def main():
    if not scribus.haveDoc():
        return

    if character_style not in scribus.getCharStyles():
        scribus.createCharStyle(character_style)

    current_item = scribus.getSelectedObject()

    # scribus.setRedraw(False)
    for page in range(1, scribus.pageCount() + 1):
        scribus.gotoPage(page)

        page_text_frames = [item[0] for item in scribus.getPageItems()
            if item[1] == 4 and scribus.getPrevLinkedFrame(item[0]) is None]

        for item in page_text_frames:
            scribus.deselectAll()
            scribus.selectObject(item)
            story_text = scribus.getAllText()
            for m in re.finditer(search_text, story_text):
                scribus.selectText(m.start(), m.end() - m.start())
                scribus.setCharacterStyle(character_style)

    scribus.deselectAll()
    if current_item != '':
        scribus.selectObject(current_item)
    # scribus.setRedraw(True)

if __name__ == "__main__":
    main()
