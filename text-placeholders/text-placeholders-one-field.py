# encoding: utf-8
try:
    import scribus
except ImportError:
    print('This script must be run from inside Scribus')

text = scribus.getText()
print(text)
i = text.find('{')
j = text.find('}', i)
print(i)
print(j)
print(text[i+1:j])
scribus.selectText(i, j - i)
text = scribus.getText()
print('>>>>' + text)
value = 'replacement'
scribus.insertText(value, i + 1)

# delete placelholder}
scribus.selectText(i + len(value) + 1, j - i)
scribus.deleteText()
# {
scribus.selectText(i, 1)
scribus.deleteText()
