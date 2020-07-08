# Python 3
# https://github.com/tbxtbxtbx/
# National Lottery Lotto generator [https://www.national-lottery.co.uk/games/lotto]
import random

# function to draw 6 numbers from 1-59
def draw():
	i = 0
	selected = []
	firstlist = list(range(1,60))
	while i < 6:
		rando = random.choice(firstlist)
		selected.append(rando)
		firstlist.remove(rando)
		i += 1
	return(sorted(selected))


def winner():
	print('\nYour numbers came up! And it only took ' + str(numdraws) + ' draws!\n')
	print('\nYou chose: ' + str(yournumbers)+ ' + the computer chose: ' + str(compnumbers))

# user defined numbers
yournumbers = [1, 2, 3, 4, 5, 6]
matching = False
numdraws = 0

# loop to check for winning matches
while matching == False: 
	compnumbers = draw()
	numdraws += 1
	matching = (compnumbers == yournumbers)
else:
	winner()
