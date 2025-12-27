# Ad hoc script for moving the Ada & Zangenmann to RTL

- Run `store_and_reduce_full_page_items.py`.
- Change to rtl, first left.
- "Apply master page", left to odd, and right to even
- Run `fix_items_position.py`.
- Manually fix the placement of the page numbers on the master pages.
- The image frame on page 57 is not expanding to the bleed and does not get fixed.
  You need to manually fix it.

The script might be of interest for fixing the placement when converting document from LTR to RTL or changing the first page from being right to left.
