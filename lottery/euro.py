# Python 3
# https://github.com/tbxtbxtbx/
# National Lottery EuroMillions generator [https://www.national-lottery.co.uk/games/euromillions]
import random

# function to draw 5 numbers from 1-50
def draw():
	i = 0
	selected = []
	firstlist = list(range(1,51))
	while i < 5:
		rando = random.choice(firstlist)
		selected.append(rando)
		firstlist.remove(rando)
		i += 1
	return(sorted(selected))

# function to draw 1 number from 1-12
def luckystar():
	i = 0
	luckyselected = []
	luckylist = list(range(1,13))
	while i < 2:
		luckyrando = random.choice(luckylist)
		luckyselected.append(luckyrando)
		luckylist.remove(luckyrando)
		i += 1
	return(sorted(luckyselected))

def winner():
	print('\nYour numbers came up! And it only took ' + str(numdraws) + ' draws!\n')
	print('\nYou chose: ' + str(yournumbers) + ' ' + str(yourlucky) + ' + the computer chose: ' + str(compnumbers) + ' ' + str(complucky))

# user defined numbers/lucky numbers
yournumbers = [1, 2, 3, 4, 5]
yourlucky = [6, 7]
matching = False
numdraws = 0

# loop to check for winning matches
while matching == False: 
	compnumbers = draw()
	complucky = luckystar()
	numdraws += 1
	matching = ((compnumbers == yournumbers) & (complucky == yourlucky))
else:
	winner()
