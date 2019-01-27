# Python3
# Quick script to read content of a file, defang URLs then write to a new file.
# Change the defangedfile variable to a path of your choice.
# This will change all . to [.] and http to hxxp.

import sys

if len(sys.argv) < 2:
    print('Usage: defang.py *filename*')
    sys.exit()

filename = sys.argv[1]
checkit = open(filename,'r')
display = checkit.read()
hyperchange = display.replace('http', 'hxxp')
dotchange = hyperchange.replace('.', '[.]')
defangedfile = '/Users/tbx/Downloads/defanged.txt'
open_new_file = open(defangedfile,'w')
open_new_file.write(dotchange)
checkit.close()
open_new_file.close()

print('Defanged analysis written to: ' + defangedfile)