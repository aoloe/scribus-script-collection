# -*- coding: utf-8 -*-

# cc-by-sa 4.0 julius
# https://wiki.scribus-user.de/ressourcen:scripte#scribus_15-dokumente_in_14x_oeffnen

import scribus
import os
import re
 
slafile = scribus.fileDialog("Please, choose a Scribus document.", "Scribus Documents (*.sla)")
filecontent = open(slafile, "r").read()
filecontent = filecontent.replace('<SCRIBUSUTF8NEW Version="1.5.', '<SCRIBUSUTF8NEW Version="1.4.')
filecontent = filecontent.replace('<DefaultStyle/>', '')
filecontent = filecontent.replace('</StoryText>', '')
filecontent = filecontent.replace('<StoryText>', '')
filecontent = filecontent.replace('</Cell>', ' ')
filecontent = filecontent.replace('</TableData>', '')
filecontent = filecontent.replace('PTYPE="12"', 'PTYPE="7"')
filecontent = filecontent.replace('PTYPE="16"', 'PTYPE="4"')
# quick and dirty workaround for setting PRINTABLE attribute to 1 if not already set:
filecontent = filecontent.replace('CLIPEDIT="1" PWIDTH=', 'CLIPEDIT="1" PRINTABLE="1" PWIDTH=')
filecontent = filecontent.replace('CLIPEDIT="0" PWIDTH=', 'CLIPEDIT="0" PRINTABLE="1" PWIDTH=')
filecontent = re.sub(r"(<DefaultStyle[^>].*?>)", "", filecontent)
filecontent = re.sub(r"(<TableData[^>].*?>)", "", filecontent)
filecontent = re.sub(r"(<Cell [^>].*?>)", "", filecontent)
 
newfile = slafile.replace(".sla", "_1-4.sla")
if os.path.isfile(newfile):
    scribus.messageBox("Error: The file already exists", "The file '"+newfile+"' already exists.\The script has stopped; Please rename the existing file.")
else:
    ofile = open(newfile, "w").write(filecontent)
    scribus.openDoc(newfile)
 
    anzahl = scribus.pageCount()
 
    for seite in range(1,anzahl+1):
        scribus.gotoPage(seite)
        objects = scribus.getAllObjects()
        for x in objects:
            width,height = scribus.getSize(x)
            scribus.sizeObject(100,100,x)
            scribus.sizeObject(width,height,x)
            scribus.setLineShade(100, x)
