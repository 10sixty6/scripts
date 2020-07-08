# Python3
# String reverser
# https://github.com/tbxtbxtbx/

# imports
import  os

# main
os.system('clear')
string_input = input('Enter the string you wish to have reversed!\n')
reverse_input = string_input[::-1]
if string_input == reverse_input:
	print('You entered a palindrome!')
print('\nYou entered: \'' + string_input + '\' \n\n The reversed string is: \n\n\'' + reverse_input + '\'\n')
