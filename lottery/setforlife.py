# Python 3
# https://github.com/tbxtbxtbx/
# National Lottery Set for Life generator [https://www.national-lottery.co.uk/games/set-for-life]

import random

# function to draw 5 numbers from 1-47
def draw():
	i = 0
	selected = []
	firstlist = list(range(1,48))
	while i < 5:
		rando = random.choice(firstlist)
		selected.append(rando)
		firstlist.remove(rando)
		i += 1
	return(sorted(selected))

# function to draw 1 number from 1-10
def lifeballdraw():
	lifeselected = []
	lifelist = list(range(1,11))
	liferando = random.choice(lifelist)
	return(liferando)

def winner():
	print('\nYour numbers came up! And it only took ' + str(numdraws) + ' draws!\n')
	print('\nYou chose: ' + str(yournumbers) + ' ' + str(yourlifed) + ' + the computer chose: ' + str(compnumbers) + ' ' + str(complifed))

# user defined numbers/life ball number
yournumbers = [3, 13, 14, 17, 28]
yourlifed = 5
matching = False
numdraws = 0

# loop to check for winning matches
while matching == False: 
	compnumbers = draw()
	complifed = lifeballdraw()
	numdraws += 1
	matching = ((compnumbers == yournumbers) & (complifed == yourlifed))
else:
	winner()
