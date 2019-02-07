# Python3
# Quick script to read content of a file, defang URLs, write to a new file & open in Sublime.
# Change the defangedfile variable to a path of your choice.
# This will change all . to [.] and http to hxxp.
# https://github.com/tbxtbxtbx/

# imports
import sys, os

# usage check
if len(sys.argv) < 2:
    print('\x1b[0;30;41m' + 'Usage: defang.py *filename*' + '\x1b[0m')
    sys.exit()

# main
os.system('clear')
defangedfile = '/Users/tbx/Downloads/defanged.txt'
print('Cleaning up old defang file from: ' + defangedfile)
os.remove(defangedfile)
filename = sys.argv[1]
checkit = open(filename,'r')
display = checkit.read()
hyperchange = display.replace('http', 'hxxp')
dotchange = hyperchange.replace('.', '[.]')
open_new_file = open(defangedfile,'w')
open_new_file.write(dotchange)
checkit.close()
open_new_file.close()
print()
print('Defanged analysis written to: ' + defangedfile)
print()
print('Opening: ' + defangedfile + ' in Sublime')
os.system('/usr/local/bin/subl ' + defangedfile)
print()
print('Done!')
