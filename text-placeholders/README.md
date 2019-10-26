# Replace placeholders in a text frame and keep the formatting

A script that looks for placeholders in the text and replaces them with corresponding values.

This script, might be helpful to create a mail merge script for Scribus.

In the example script, it looks for fields starting and ending with curly braces and replace the key by the corresponding value in the `VALUES` dictionary.

The formatting of the key is used for the formatting of the value inserted.

The `text-placeholders-one-field.py` script contain the first steps for the complete script and shows how to replace one occurrence of text between curly braces through a new text.

In order to retain the formatting, this script first insert the text before the first letter of the key and then deletes the key and the curly braces. This is a "trick" that needs also to be used when normally working with Scribus (deleting a selection and starting typing will not use the formatting of the deleted selection).
