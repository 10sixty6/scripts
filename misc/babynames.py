# Python 3
# Chooses a male and female name from a predetermined list of names
# https://github.com/tbxtbxtbx/

# Example names files can be downloaded from 'https://www.cs.cmu.edu/afs/cs/project/ai-repository/ai/areas/nlp/corpora/names/'
import random, os, pyfiglet
os.system('clear')
banner = pyfiglet.figlet_format("Name    Generator")
print(banner)
filegirls = '/path/to/file/girls.txt'
fileboys =  '/path/to/file/boys.txt'
fg = open(filegirls, 'r')
fb = open(fileboys, 'r')
girllines = fg.readlines()
boylines = fb.readlines()
randgirl = random.choice(girllines).title()
randboy = random.choice(boylines).title()
print('\nThe girls name should be: ' + '\033[1;35;40m' + str(randgirl) + '\x1b[0m' + '\nThe boys name should be: ' + '\033[1;34;40m' +  str(randboy)  + '\x1b[0m')
