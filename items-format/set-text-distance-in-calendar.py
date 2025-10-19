"""
Apply the distances defined in TEXT_DISTANCE_LTRB (left, top, right, bottom...)
to each text frame in the document that only contains digits (in your case the frames with the dates)

There is no way to undo the changes, so if you're not happy with the result,
you can run again the same script with different values or close the document without saving it.
"""

old_unit = scribus.getUnit()
scribus.setUnit(scribus.UNIT_MM)

TEXT_DISTANCE_LTRB = [0, 2, 1, 0] # mm

for page in range(1, scribus.pageCount() + 1):
  scribus.gotoPage(page)
  for item in scribus.getPageItems():
    if item[1] == 4 and scribus.getAllText(item[0]).isdigit():
      scribus.setTextDistances(*TEXT_DISTANCE_LTRB, item[0])

scribus.setUnit(old_unit)
