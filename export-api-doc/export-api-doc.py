# inspired by https://wiki.scribus.net/canvas/Category:Scripts#Auto-Output_all_Scripter_Commands

import sys

import scribus
d = dir(scribus)

sys.stdout = open("api.txt", "w")

constants = []
functions = []

for command in d:
    exec('res = scribus.'+command)
    doc = None
    try:
        doc = res.__doc__
    except:
        pass
    if doc:
        if doc[0:5] == 'float':
            constants.append((command, 'float', str(res)))
        elif doc[0:3] == 'int':
            constants.append((command, 'integer', str(res)))
        elif doc[0:5] == 'tuple':
            constants.append((command, 'tuple', repr(res)))
        elif doc[0:3] == 'str':
            constants.append((command, 'string', repr(res)))
        else:
            functions.append((command, doc))

print('Constants')
print('')

for command in constants:
    print(command[0])
    print(command[1] + ': ' + command[2])
    print('')

print('Functions')
print()

for command in functions:
    print(command[0])
    print(command[1])
    print('')
