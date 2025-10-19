old_unit = scribus.getUnit()
scribus.setUnit(scribus.UNIT_MM)

TEXT_DISTANCE_LTRB = [0, 2, 1, 0] # mm

for page in range(1, scribus.pageCount() + 1):
  scribus.gotoPage(page)
  for item in scribus.getPageItems():
    if item[1] == 4 and scribus.getAllText(item[0]).isdigit():
      scribus.setTextDistances(*TEXT_DISTANCE_LTRB, item[0])

scribus.setUnit(old_unit)
