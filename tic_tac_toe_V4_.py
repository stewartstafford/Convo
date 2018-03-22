#
# This is a script to construct and play Tic Tac Toe
#
# define library
import random
import time	# use time delays to view screens
import os	# clear screen
import sys

# yeah I won 
def yeah_I_won():
	print ('Yeah, I WonI, I Won!')
	time.sleep(5)
	sys.exit("I win, I Win, exiting")

# Is the grid full
def is_the_grid_full():
# Testing the full condition
	#board[1] = 'o'
	#board[2] = 'o'
	#board[3] ='o'
	#board[4] = 'o'
	#board[5] = 'o'
	#board[6] = 'o'
	#board[7] = 'o'
	#board[8] = 'o'
	#board[9] = 'o'
	
	cnt = 0
	list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	for valu in list: # check all squares for x and y
		if (board[valu] == 'o'):
			cnt = cnt + 1
		if (board[valu] == 'x'):
			cnt = cnt + 1
			#print ('cnt', cnt)
		if cnt == 9 :
			print('The game is a tie, Exiting')
			time.sleep(5)
			sys.exit('The game is a tie, Exiting')
		else:
			exit
	return()

#Check to see if we did win
def did_I_winO():
	#print ('Here in did_I_winO')
	#time.sleep(3)
	if (board[1] == 'o') and (board[4] == 'o') and (board[7] == 'o'):
		yeah_I_won()
		
	if (board[2] == 'o') and (board[5] == 'o') and (board[8] == 'o'):
		yeah_I_won()	
	
	if (board[3] == 'o') and (board[6] == 'o') and (board[9] == 'o'):
		yeah_I_won()

	if (board[1] == 'o') and (board[2] == 'o') and (board[3] == 'o'):
		yeah_I_won()

	if (board[4] == 'o') and (board[5] == 'o') and (board[6] == 'o'):
		yeah_I_won()

	if (board[7] == 'o') and (board[8] == 'o') and (board[9] == 'o'):
		yeah_I_won()

	if (board[1] == 'o') and (board[5] == 'o') and (board[9] == 'o'):
		yeah_I_won()
		
	if (board[3] == 'o') and (board[5] == 'o') and (board[7] == 'o'):
		yeah_I_won()
		
	#print ('Exiting did_I_winO')
	#time.sleep(3)
	
	return()

#Check to see if we did win
def did_I_winX():
	#print ('Here in did_i_winX')
	if (board[1] == 'x') and (board[4] == 'x') and (board[7] == 'x'):
		yeah_I_won()
		
	if (board[2] == 'x') and (board[5] == 'x') and (board[8] == 'x'):
		yeah_I_won()	
	
	if (board[3] == 'x') and (board[6] == 'x') and (board[9] == 'x'):
		yeah_I_won()

	if (board[1] == 'x') and (board[2] == 'x') and (board[3] == 'x'):
		yeah_I_won()

	if (board[4] == 'x') and (board[5] == 'x') and (board[6] == 'x'):
		yeah_I_won()

	if (board[7] == 'x') and (board[8] == 'x') and (board[9] == 'x'):
		yeah_I_won()

	if (board[1] == 'x') and (board[5] == 'x') and (board[9] == 'x'):
		yeah_I_won()
		
	if (board[3] == 'x') and (board[5] == 'x') and (board[7] == 'x'):
		yeah_I_won()
		
	#print ('Exiting did_i_winX')
	return()

# Check to see if x is about to win if so block
def block_winX():
	#print ('Here in block_winX')
	#time.sleep(3)
	change_made = 0
#seq_spin1
	if (board[1] == 'x') and (board[4] == 'x') and (board[7] != 'x') and (board[7] != 'o'):
		board[7] = 'o'
		change_made = 1 
		
	if (board[3] == 'x') and (board[6] == 'x') and (board[9] != 'x') and (board[9] != 'o'):
		board[9] = 'o'
		change_made = 1
		
	if (board[2] == 'x') and (board[5] == 'x') and (board[8] != 'x') and (board[8] != 'o'):
		board[8] = 'o'
		change_made = 1
		
#seq_spin2
	if (board[1] == 'x') and (board[2] == 'x') and (board[3] != 'x') and (board[3] != 'o'):
		board[3] = 'o'
		change_made = 1
		
	if (board[4] == 'x') and (board[5] == 'x') and (board[6] != 'x') and (board[6] != 'o'):
		board[6] = 'o'
		change_made = 1
		
	if (board[7] == 'x') and (board[8] == 'x') and (board[9] != 'x') and (board[9] != 'o'):
		board[9] = 'o'
		change_made = 1
		
#seq_spin3
	if (board[2] == 'x') and (board[3] == 'x') and (board[1] != 'x') and (board[1] != 'o'):
		board[1] = 'o'
		change_made = 1
		
	if (board[5] == 'x') and (board[6] == 'x') and (board[4] != 'x') and (board[4] != 'o'):
		board[4] = 'o'
		change_made = 1
		
	if (board[8] == 'x') and (board[9] == 'x') and (board[7] != 'x') and (board[7] != 'o'):
		board[7] = 'o'
		change_made = 1
		
#seq_spin4
	if (board[4] == 'x') and (board[7] == 'x') and (board[1] != 'x') and (board[1] != 'o'):
		board[1] = 'o'
		change_made = 1
		
	if (board[5] == 'x') and (board[8] == 'x') and (board[2] != 'x') and (board[2] != 'o'):
		board[2] = 'o'
		change_made = 1
		
	if (board[6] == 'x') and (board[9] == 'x') and (board[3] != 'x') and (board[3] != 'o'):
		board[3] = 'o'
		change_made = 1
		
#edge_spin1
	if (board[1] == 'x') and (board[7] == 'x') and (board[4] != 'x') and (board[4] != 'o'):
		board[4] = 'o'
		change_made = 1
		
	if (board[2] == 'x') and (board[8] == 'x') and (board[5] != 'x') and (board[5] != 'o'):
		board[5] = 'o'
		change_made = 1
		
	if (board[3] == 'x') and (board[9] == 'x') and (board[6] != 'x') and (board[6] != 'o'):
		board[6] = 'o'
		change_made = 1
		
#edge_spin2
	if (board[1] == 'x') and (board[3] == 'x') and (board[2] != 'x') and (board[2] != 'o'):
		board[2] = 'o'
		change_made = 1
		
	if (board[4] == 'x') and (board[6] == 'x') and (board[5] != 'x') and (board[5] != 'o'):
		board[5] = 'o'
		change_made = 1
		
	if (board[7] == 'x') and (board[9] == 'x') and (board[8] != 'x') and (board[8] != 'o'):
		board[8] = 'o'
		change_made = 1
		
#center_spin1
	if (board[1] == 'x') and (board[9] == 'x') and (board[5] != 'x') and (board[5] != 'o'):
		board[5] = 'o'
		change_made = 1
		
	if (board[3] == 'x') and (board[7] == 'x') and (board[5] != 'x') and (board[5] != 'o'):
		board[5] = 'o'
		change_made = 1
		
	if (board[3] == 'x') and (board[5] == 'x') and (board[7] != 'x') and (board[7] != 'o'):
		board[7] = 'o'
		change_made = 1
		
	if (board[2] == 'x') and (board[5] == 'x') and (board[8] != 'x') and (board[8] != 'o'):
		board[8] = 'o'	
		change_made = 1
		
	if (board[1] == 'x') and (board[5] == 'x') and (board[9] != 'x') and (board[9] != 'o'):
		board[9] = 'o'	
		change_made = 1
		
	if (board[4] == 'x') and (board[5] == 'x') and (board[6] != 'x') and (board[6] != 'o'):
		board[6] = 'o'
		change_made = 1
		
	if (board[7] == 'x') and (board[5] == 'x') and (board[2] != 'x') and (board[2] != 'o'):
		board[2] = 'o'
		change_made = 1
		
	if (board[8] == 'x') and (board[5] == 'x') and (board[7] != 'x') and (board[7] != 'o'):
		board[7] = 'o'
		change_made = 1
		
	if (board[9] == 'x') and (board[5] == 'x') and (board[1] != 'x') and (board[1] != 'o'):
		board[1] = 'o'
		change_made = 1
		
	if (board[6] == 'x') and (board[5] == 'x') and (board[4] != 'x') and (board[4] != 'o'):
		board[4] = 'o'
		change_made = 1
	
	#print ('Exiting block_winX')
	#time.sleep(3)
	return( change_made )

# Place a character in grid
def place_char():
	#print('Here in place_char function')
	#time.sleep(3)
# list of squares to choose from
	my_list = [1, 3, 5, 7, 9, 2, 6, 8, 4]
	for valu in my_list:
# Make sure square is empty then apply value to square
		if (board[valu] != 'x') and (board[valu] != 'o'):
# Apply value to square
			#time.sleep(3)
			board[valu] = 'o'
			#time.sleep(3)
			os.system('cls')
			grid()
			print ('Computer (O) is now playing')
			print ('Please Wait!: ')
# Test the win codition
			#board[2] = 'o' 
			#board[5]  = 'o' 
			#board[8] = 'o'
			#is_the_grid_full()
			#print('waiting 5 sec')
			#time.sleep(5)
			return()
		else:
			#print('Here at if else')
			exit

# Execute the Computer player
def c_player():
# Execute Computer player
	change_made = block_winX()
	#print('Here in c_player')
	#print('chang_made', change made)
	os.system('cls')
	grid()
	print ('Computer (O) is now playing')
	print ('Working!')
	time.sleep(3)
	block_winX()
	did_I_winO()
	#print ('change_made =', change made)
	#time.sleep(3)
	#jump over if change made 1
	if (change_made == 0):
		place_char()
	os.system('cls')
	grid()
	print ('Computer (O) is now playing')
	print ('Working!')	
	did_I_winO()
	is_the_grid_full()
	time.sleep(1)
	#print ('returning to main')
	#time.sleep(1)

# Execute the x player
def x_player():
# Place the entry into grid for X
	os.system('cls')
	grid()
	print ('Player (X) is now playing')
	val = input('\tSelect a square for entry: ')
	val = int(val)
# Make sure square is empty then apply value to square
	if (board[val] != 'x') and (board[val] != 'o'):
	# apply value to square
		board[val] = 'x'
#Test the Win condition
		#board[1] = 'x'
		#board[5] = 'x'
		#board[9] = 'x'
		os.system('cls')
		grid()
		print ('Player (X) is now playing')
		print ('Working, Please Wait ! ')
		#print ('going to did I winX')
		did_I_winX()
		#print ('return from did I winX')
		#print ('going to is the grill full')
		is_the_grid_full()
		#print ('return from is the grid full')
		time.sleep(1)
	else:
		os.system('cls')
		grid()
		print ('player (X) is now playing')
		print ('You are trying to overwrite an existing entry, select another entry')
		time.sleep(3)


# Create the grid
def grid():
	print()
	print(board[1], '|',  board[2], '|', board[3])
	print('----------')
	print(board[4], '|',  board[5], '|', board[6])
	print('----------')
	print(board[7], '|',  board[8], '|', board[9])
	print()

	
#########################################

# Script Introduction
print('\nHello Convo Communications, Here is my Tic Tac Toe scripting \nassignment written in Object Oriented form...')
input ('\nPress Enter to continue....')
os.system('cls')
print('\nGame Rules: \n1.You will always play againt the AI as X or O\n2.You can choose to go 1st or 2nd: ')
input ('\nPress Enter to continue....')
os.system('cls')
# Select players
a = 'y'
os.system('cls')
b = input('\nDo you want to go First?__y/n  ')

board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
grid()

# Call the players of the game

if (a == "y") and (b == 'y'):
	while (True) :
		print('You are the X player')
		x_player()
		#print('returned from x_player')
		time.sleep(3)
		#print('Computer is O player')
		#time.sleep(3)
		c_player()
		#print('returned from c_player')
		#time.sleep(3)

if (a == "y") and (b =='n'):
	while (True):
		print('The Computer is the X player')
		c_player()
		#print('returned from x_player')
		#time.sleep(1)
		print('You are the O player')
		x_player()
		#print('returned to main')
		#time.sleep(1)

# Pause execution so the Users can see the results
input('Press Enter to Exit the script ...')
