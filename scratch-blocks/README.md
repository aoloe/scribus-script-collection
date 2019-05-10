# Get Svg Scratch blocks into Scribus as images

Scratch Blocks are created through <https://scratchblocks.github.io> or <https://s3blocks.github.io/generator/?id=282753934>.

Since the PNG export does not have a resolution high enough for printing, we export to SVG and convert the SVG to PNG before loading it into Scribus.

This script assumes that you are downloading the `scratchblocks.svg` file to a _standard_ place and are not renaming it.

The script will copy the `scratchblocks.svg` file to your project's directory, rename it to the name you will have specified, fit he canvas to the drawing, convert it to a PNG and load the resulting file into Scribus.

The `md-scratch-blocks.py` script copies the file to an SVG target defined in a markdown image tag and makes a PNG copy of it.
