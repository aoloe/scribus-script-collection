import scribus

for page in range(1, scribus.pageCount() + 1):
    scribus.gotoPage(page)
    for item in scribus.getPageItems():
        if item[1] == 2:
            print(scribus.getImageFile(item[0]))
