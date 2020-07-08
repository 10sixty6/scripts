# Python 3
# https://github.com/tbxtbxtbx/
# National Lottery thunderball generator [https://www.national-lottery.co.uk/games/thunderball]
import random

# function to draw 5 numbers from 1-39
def draw():
	i = 0
	selected = []
	firstlist = list(range(1,40))
	while i < 5:
		rando = random.choice(firstlist)
		selected.append(rando)
		firstlist.remove(rando)
		i += 1
	return(sorted(selected))

# function to draw 1 number from 1-15
def thundraw():
	thunselected = []
	thunlist = list(range(1,16))
	thunrando = random.choice(thunlist)
	return(thunrando)

def winner():
	print('\nYour numbers came up! And it only took ' + str(numdraws) + ' draws!\n')
	print('\nYou chose: ' + str(yournumbers) + ' ' + str(yourthund) + ' + the computer chose: ' + str(compnumbers) + ' ' + str(compthund))

# user defined numbers/thunderball number
yournumbers = [1, 2, 3, 4, 5]
yourthund = 6
matching = False
numdraws = 0

# loop to check for winning matches
while matching == False: 
	compnumbers = draw()
	compthund = thundraw()
	numdraws += 1
	matching = ((compnumbers == yournumbers) & (compthund == yourthund))
else:
	winner()






	

	
