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

    filename = scribus.fileDialog('Select a document', 'Scribus document (*.sla)')
    if not filename:
        sys.exit()

    # find the masterpages in use in the source document
    scribus.openDoc(filename)
    pages = tuple(range(1, scribus.pageCount() + 1))
    masterpages = [scribus.getMasterPage(p) for p in pages]
    scribus.closeDoc()

    # the current page before importing
    page = scribus.currentPage()

    # import pages by creating them after the current one
    scribus.importPage(filename, pages, 1, 1)

    for i, masterpage in enumerate(masterpages):
        scribus.applyMasterPage(masterpage, page + 1 + i)

if __name__ == '__main__':
    main()
