# encoding: utf-8
# (c) MIT, ale rimoldi <ale@graphicslab.org>

"""
Replace multiple items by a copy of a specific item.
For more details see the README.md
"""

try:
    import scribus
except ImportError:
    print('This script must be run from inside Scribus')

def main():
    pass

    n = scribus.selectionCount()
    if n == 0:
        scribus.messageBox('Error', 'No item selected')
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
