# encoding: utf-8
# (c) MIT, ale rimoldi <ale@graphicslab.org>

"""
Import all pages from a Scribus document and apply the master pages
For more details see the README.md
"""

import sys

try:
    import scribus
except ImportError:
    print('This script must be run from inside Scribus')

def main():
    if not scribus.haveDoc():
        sys.exit()

    filename = scribus.fileDialog('Select a docuent', 'Scribus document (*.sla)')
    if not filename:
        sys.exit()
    
    scribus.openDoc(filename)
    pages = tuple(range(1, scribus.pageCount() + 1))
    masterpages = []
    for page in pages:
        masterpages.append(scribus.getMasterPage(page))
    scribus.closeDoc()
    # import pages and create the pages after the current one
    page = scribus.currentPage()
    scribus.importPage(filename, pages, 1, 1)
    page += 1
    for masterpage in masterpages:
        scribus.applyMasterPage(masterpage, page)
        page += 1

if __name__ == '__main__':
    main()
