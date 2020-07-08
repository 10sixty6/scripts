# Python3
# Defangs input file and produces output file.
# Change the defangedfile variable to a path of your choice.
# https://github.com/tbxtbxtbx/

# imports
import sys, os, time
from defang import defang

# usage check
if len(sys.argv) < 2:
    print('\x1b[0;30;41m' + 'Usage: *script*.py *filename*' + '\x1b[0m')
    sys.exit()

#global variables
defangedfile = '/Users/tbx/Downloads/defanged.txt'

def firstbit():
	os.system('clear')
	if os.path.isfile(defangedfile) == True:
		print('Cleaning up old defang file from: ' + defangedfile)
		time.sleep(1)
		os.remove(defangedfile)
	else:
		print()


def main():
	filename = sys.argv[1]
	checkit = open(filename,'r')
	display = checkit.read()
	alldone = defang(display)
	open_new_file = open(defangedfile,'w')
	open_new_file.write(alldone)
	checkit.close()
	open_new_file.close()
	print()
	print('Defanged analysis written to: ' + defangedfile)
	time.sleep(1)
	print()
	print('Opening: ' + defangedfile + ' in Sublime')
	os.system('/usr/local/bin/subl ' + defangedfile)
	print()
	time.sleep(1)
	print('Done!')
	print()

if __name__ == '__main__':
    firstbit()
    main()
