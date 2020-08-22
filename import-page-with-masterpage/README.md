# Import pages with master pages

Import all pages from a Scribus document and apply the master pages.

- Open the document where you want to import the pages.
- Make sure that it's the only document open.
- Go to the page where you want to import the pages
- Run this script (`Scripter > Execute script`)
- Pick the file from where you want to import the pages.
- The script will
  - Detect all the master pages used in the source document
  - Import all the pages from the source document.
  - Place them after the current page in the target document.
  - Apply the master pages by using the name from the source document.
- Warning: All the master pages used in the imported pages must already exist in the target document.

