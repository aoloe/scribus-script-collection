# encoding: utf-8
try:
    import scribus
except ImportError:
    print('This script must be run from inside Scribus')
import sys

if scribus.selectionCount() != 1 or scribus.getObjectType() != 'TextFrame':
    scribus.messageBox('Script failed', 'You need to select one text frame selected.')
    sys.exit(2)
    

PLACEHOLDER_START = '{'
PLACEHOLDER_END = '}'

VALUES = {'name': 'Goofy', 'color': 'blue', 'food': 'pizza'}

len_start = len(PLACEHOLDER_START)
len_end = len(PLACEHOLDER_END)

scribus.selectText(0, 0)
text = scribus.getText()

i = text.find(PLACEHOLDER_START)
while i != -1:
    j = text.find(PLACEHOLDER_END, i)
    if j == -1:
        break

    key = text[i + 1:j]
    # print('>>>' + key)

    if key in VALUES:
        value = VALUES[key]
    else:
        value = PLACEHOLDER_START + key + PLACEHOLDER_END

    scribus.insertText(value, i + 1)

    # delete key}
    scribus.selectText(i + len(value) + 1, j - i)
    scribus.deleteText()
    # delete {
    scribus.selectText(i, 1)
    scribus.deleteText()


    text = text[0:i] + value + text[j + len_end:]
    i = text.find(PLACEHOLDER_START, i + len(value))
