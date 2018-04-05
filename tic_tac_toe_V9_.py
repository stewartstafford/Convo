#
# This is a script to construct and play Tic Tac Toe
#
# To do:					Fixed:
# 1.Button that resets
# 							2.Reset after game end or ties
# 							3.Fix multiple win bug
# 4.Random generator
#

# Define library
import random
import time  # use time delays to view screens
import os  # clear screen
import sys


# yeah I won
def yeah_I_won():
    print('Yea, I Won!, I Won!')
    print('Yea, I Won!, I Won!')
    time.sleep(5)
    # sys.exit("I win, I Win, exiting")
    #print ('Leaving yeah I won - rest_game', reset_game)
    return ()

# Is the grid full
def is_the_grid_full():
    reset_game = 0
    # print('Entering is the grid full')
    # Testing the full condition
    # board[1] = 'x'
    # board[2] = 'o'
    # board[3] = 'x'
    # board[4] = 'o'
    # board[5] = 'x'
    # board[6] = 'o'
    # board[7] = 'x'
    # board[8] = 'o'
    # board[9] = 'x'
    cnt = 0
    list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for valu in list:  # check all squares for x or o
        if (board[valu] == 'o'):
            cnt = cnt + 1  # count number of o squares in game
        if (board[valu] == 'x'):
            cnt = cnt + 1  # count number of x squares in game
        # print ('cnt', cnt)
        if cnt == 9:  # If  9  squares with x's and/or o's
            print('The game is a tie, Exiting game !')
            time.sleep(5)
            # sys.exit('The game is a tie, Exiting')
            reset_game = 1
            return (reset_game)
        else:
            # print('Squares not full, Exiting to check next square')
            exit
    return (reset_game)

# Check to see if o won
def did_I_winO():

    # print ('Here in did_I_winO')
    # time.sleep(3)
    reset_game = 0
    if (board[1] == 'o') and (board[4] == 'o') and (board[7] == 'o'):
        yeah_I_won()
        reset_game = 1

    if (board[2] == 'o') and (board[5] == 'o') and (board[8] == 'o'):
        yeah_I_won()

    if (board[3] == 'o') and (board[6] == 'o') and (board[9] == 'o'):
        yeah_I_won()
        reset_game = 1

    if (board[1] == 'o') and (board[2] == 'o') and (board[3] == 'o'):
        yeah_I_won()
        reset_game = 1

    if (board[4] == 'o') and (board[5] == 'o') and (board[6] == 'o'):
        yeah_I_won()
        reset_game = 1

    if (board[7] == 'o') and (board[8] == 'o') and (board[9] == 'o'):
        yeah_I_won()
        reset_game = 1

    if (board[1] == 'o') and (board[5] == 'o') and (board[9] == 'o'):
        yeah_I_won()
        reset_game = 1


    if (board[3] == 'o') and (board[5] == 'o') and (board[7] == 'o'):
        yeah_I_won()
        reset_game = 1

    # print ('Here in yeah did_i_winO Exiting did_I_winO')
    # time.sleep(3)
    #print ('Here in yeah did i winO - reset_game', reset_game)
    return (reset_game)

# Check to see if x won
def did_I_winX():
    # Test the X win scenario
    # print ('Here in did_i_winX')
    reset_game = 0
    if (board[1] == 'x') and (board[4] == 'x') and (board[7] == 'x'):
        yeah_I_won()
        reset_game = 1

    if (board[2] == 'x') and (board[5] == 'x') and (board[8] == 'x'):
        yeah_I_won()
        reset_game = 1

    if (board[3] == 'x') and (board[6] == 'x') and (board[9] == 'x'):
        yeah_I_won()
        reset_game = 1

    if (board[1] == 'x') and (board[2] == 'x') and (board[3] == 'x'):
        yeah_I_won()
        reset_game = 1

    if (board[4] == 'x') and (board[5] == 'x') and (board[6] == 'x'):
        yeah_I_won()
        reset_game = 1

    if (board[7] == 'x') and (board[8] == 'x') and (board[9] == 'x'):
        yeah_I_won()
        reset_game = 1

    if (board[1] == 'x') and (board[5] == 'x') and (board[9] == 'x'):
        yeah_I_won()
        reset_game = 1

    if (board[3] == 'x') and (board[5] == 'x') and (board[7] == 'x'):
        yeah_I_won()
        reset_game = 1

    print ('Here exiting did_i_winX - reset_game', reset_game)

    return(reset_game)

# Check to see if x is about to win if so block
def block_winX():
    # print ('Here in block_winX')
    # time.sleep(3)
    change_made = 0

    # seq_spin1
    if (board[1] == 'x') and (board[4] == 'x') and (board[7] != 'x') and (board[7] != 'o') and (change_made == 0):
        board[7] = 'o'
        change_made = 1  # Sinal a entry has been made and not to go to place_char

    if (board[2] == 'x') and (board[5] == 'x') and (board[8] != 'x') and (board[8] != 'o') and (change_made == 0):
        board[8] = 'o'
        change_made = 1

    if (board[3] == 'x') and (board[6] == 'x') and (board[9] != 'x') and (board[9] != 'o') and (change_made == 0):
        board[9] = 'o'
        change_made = 1

    # seq_spin2
    if (board[1] == 'x') and (board[2] == 'x') and (board[3] != 'x') and (board[3] != 'o') and (change_made == 0):
        board[3] = 'o'
        change_made = 1

    if (board[4] == 'x') and (board[5] == 'x') and (board[6] != 'x') and (board[6] != 'o') and (change_made == 0):
        board[6] = 'o'
        change_made = 1

    if (board[7] == 'x') and (board[8] == 'x') and (board[9] != 'x') and (board[9] != 'o') and (change_made == 0):
        board[9] = 'o'
        change_made = 1

    # seq_spin3
    if (board[2] == 'x') and (board[3] == 'x') and (board[1] != 'x') and (board[1] != 'o') and (change_made == 0):
        board[1] = 'o'
        change_made = 1

    if (board[5] == 'x') and (board[6] == 'x') and (board[4] != 'x') and (board[4] != 'o') and (change_made == 0):
        board[4] = 'o'
        change_made = 1

    if (board[8] == 'x') and (board[9] == 'x') and (board[7] != 'x') and (board[7] != 'o') and (change_made == 0):
        board[7] = 'o'
        change_made = 1

    # seq_spin4
    if (board[4] == 'x') and (board[7] == 'x') and (board[1] != 'x') and (board[1] != 'o') and (change_made == 0):
        board[1] = 'o'
        change_made = 1

    if (board[5] == 'x') and (board[8] == 'x') and (board[2] != 'x') and (board[2] != 'o') and (change_made == 0):
        board[2] = 'o'
        change_made = 1

    if (board[6] == 'x') and (board[9] == 'x') and (board[3] != 'x') and (board[3] != 'o') and (change_made == 0):
        board[3] = 'o'
        change_made = 1

    # edge_spin1
    if (board[1] == 'x') and (board[7] == 'x') and (board[4] != 'x') and (board[4] != 'o') and (change_made == 0):
        board[4] = 'o'
        change_made = 1

    if (board[2] == 'x') and (board[8] == 'x') and (board[5] != 'x') and (board[5] != 'o') and (change_made == 0):
        board[5] = 'o'
        change_made = 1

    if (board[3] == 'x') and (board[9] == 'x') and (board[6] != 'x') and (board[6] != 'o') and (change_made == 0):
        board[6] = 'o'
        change_made = 1

    # edge_spin2
    if (board[1] == 'x') and (board[3] == 'x') and (board[2] != 'x') and (board[2] != 'o') and (change_made == 0):
        board[2] = 'o'
        change_made = 1

    if (board[4] == 'x') and (board[6] == 'x') and (board[5] != 'x') and (board[5] != 'o') and (change_made == 0):
        board[5] = 'o'
        change_made = 1

    if (board[7] == 'x') and (board[9] == 'x') and (board[8] != 'x') and (board[8] != 'o') and (change_made == 0):
        board[8] = 'o'
        change_made = 1

    # center_spin1
    if (board[1] == 'x') and (board[9] == 'x') and (board[5] != 'x') and (board[5] != 'o') and (change_made == 0):
        board[5] = 'o'
        change_made = 1

    if (board[3] == 'x') and (board[7] == 'x') and (board[5] != 'x') and (board[5] != 'o') and (change_made == 0):
        board[5] = 'o'
        change_made = 1

    if (board[3] == 'x') and (board[5] == 'x') and (board[7] != 'x') and (board[7] != 'o') and (change_made == 0):
        board[7] = 'o'
        change_made = 1

    if (board[2] == 'x') and (board[5] == 'x') and (board[8] != 'x') and (board[8] != 'o') and (change_made == 0):
        board[8] = 'o'
        change_made = 1

    if (board[1] == 'x') and (board[5] == 'x') and (board[9] != 'x') and (board[9] != 'o') and (change_made == 0):
        board[9] = 'o'
        change_made = 1

    # if (board[4] == 'x') and (board[5] == 'x') and (board[6] != 'x') and (board[6] != 'o') and (change_made == 0):
    # board[6] = 'o'
    # change_made = 1

    if (board[7] == 'x') and (board[5] == 'x') and (board[3] != 'x') and (board[3] != 'o') and (change_made == 0):
        board[3] = 'o'
        change_made = 1

    if (board[8] == 'x') and (board[5] == 'x') and (board[2] != 'x') and (board[2] != 'o') and (change_made == 0):
        board[2] = 'o'
        change_made = 1

    if (board[9] == 'x') and (board[5] == 'x') and (board[1] != 'x') and (board[1] != 'o') and (change_made == 0):
        board[1] = 'o'
        change_made = 1

    if (board[6] == 'x') and (board[5] == 'x') and (board[4] != 'x') and (board[4] != 'o') and (change_made == 0):
        board[4] = 'o'
        change_made = 1

    # print ('Exiting block_winX')
    # time.sleep(3)
    # return(change_made)
    return (change_made)


# Place a character in grid
def place_char():
    # print('Here in place_char function')
    # time.sleep(3)
    # list of squares to choose from
    my_ai = [1, 3, 5, 7, 9, 2, 6, 8, 4]
    for valu in my_ai:
        # print('Make sure square is empty then apply value to square')
        if (board[valu] != 'x') and (board[valu] != 'o'):
            # print('Apply value to square', board[valu])
            board[valu] = 'o'  # !!!!!!!!!!!
            os.system('cls')
            grid()
            print('Computer (O) is now playing')
            print('Please Wait!: ')
            return ()
        else:
            # print('Exiting place_char else option')
            exit
    return ()


# Execute the Computer player
def c_player():
    # Execute Computer player
    # print('Here in c_player')
    # print('chang_made', change made)
    reset_game = 0
    change_made = 0
    os.system('cls')
    grid()
    print('Computer (O) is now playing')
    print('Working!')

    #print('Here in C_palyer before block winX - change_made', change_made)
    # time.sleep(3)
    change_made = block_winX()
    #print('Here in C_palyer return from block winX - change_made', change_made)
    # time.sleep(3)
    os.system('cls')
    grid()
    print('Computer (O) is now playing')
    print('Working!')
    # print ('change_made =', change_made)
    # time.sleep(3)
    # Test the O win condition
    #board[3] = 'o'
    #board[6] = 'o'
    #board[9] = 'o'
    #change_made = 1  ########## remove after test
    reset_game = did_I_winO()
    print ('Here in c_player - reset_game', reset_game)

    # jump over place_char if = 1
    #print('change_made before place_char', change_made)
    #print('Here in c_player return from did_I_winO()- reset_game', reset_game )
    # time.sleep(3)
    if (change_made == 0): # if no blocking placement was made, go to place_char program
        place_char()
    # print('placed character')
    # time.sleep(3)
    # print('change_made after place char', change_made)
    # time.sleep(3)
    os.system('cls')
    grid()
    print('Computer (O) is now playing')
    print('Working!')
    # print ('change_made before step 4 did i wino', change_made)
    # time.sleep(3)
    if (change_made == 0): # if no blocking placement was made, check place_char action
        reset_game = did_I_winO()
        reset_game = is_the_grid_full()
    #print ('Here in c_player - reset_game', reset_game)
    return (reset_game)

# Execute the x player
def x_player():
    # Place the entry into grid for X
    x_playEntry = 1
    reset_game = 0
    while x_playEntry == 1:  # Use while loop to repeat retries of occupied spaces
        os.system('cls')
        grid()
        print('Player (X) is now playing')
        val = input('\tSelect a square for entry: ')
        val = int(val)
        # Make sure square is empty then apply value to square
        if (board[val] != 'x') and (board[val] != 'o'):
            # apply value to square
            board[val] = 'x'  # !!!!!!!!!!
            # Test the Win condition
            #board[1] = 'x'
            #board[5] = 'x'
            #board[9] = 'x'
            os.system('cls')
            grid()
            print('Player(X)is now playing')
            print('Working, Please Wait ! ')
            # print ('going to did I winX')
            reset_game = did_I_winX() # Look for reset_game = 1 from Yeah,_I_won
            #print ('Here in x_play : Returned from did I winX - reset_game', reset_game)
            # print ('going to is the grill full')
            if reset_game  == 0:
                reset_game = is_the_grid_full()  # Look for reset_game = 1 from Yea,_I_won
            #print ('Here in x_play : Returned from is_the_grid_full, - reset_game', reset_game)
            # print ('Here back in x_player, - reset_game', reset_game)
            # time.sleep(4)
            #print('Here in x_play : Leaving x_player - reset_game',  reset_game)
            x_playEntry = 0  # Entry was made, Break out of x_player program
        else:
            # You tried to place in an occupied space, try again
            os.system('cls')
            grid()
            print('player (X) is now playing')
            print('You are trying to overwrite an existing entry')
            print('Select another entry.......')
            x_playEntry = 1
            time.sleep(5)  # holding to see printouts
            # print('Leaving x_player')
    return (reset_game)

board = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
reset_game = 0

# Create the grid
def grid():
    print()
    print(board[1], '|', board[2], '|', board[3])
    print('----------')
    print(board[4], '|', board[5], '|', board[6])
    print('----------')
    print(board[7], '|', board[8], '|', board[9])
    print()

# Start the game over
def start_new_game():
    os.system('cls')
    print('\nGame Rules: \n1.You will always play againt the AI as X or O\n2.You can choose to go 1st or 2nd: ')
    input('\nPress Enter to continue....')

    os.system('cls')
    print ('Here in start_new_game, Select players')
    playerA = 'y'
    playerB = input('\nDo you want to go First?__y/n  ')

    restart_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for restart_value in restart_list:
        board[restart_value] = restart_value
    grid()
    return (playerB)

#########################################
# Main
# Script Introduction
print('\nHello Convo Communications, Here is my Tic Tac Toe scripting \nassignment written in Object Oriented form...')
input('\nPress Enter to continue....')
os.system('cls')

print('\nGame Rules: \n1.You will always play againt the AI as X or O\n2.You can choose to go 1st or 2nd: ')
input('\nPress Enter to continue....')
os.system('cls')

# Select players
playerA = 'y'
playerB = input('\nDo you want to go First?__y/n  ')

#print ('Call the players of the game')

while True:
    if (playerA == 'y') and (playerB == 'y'):
        reset_game = 0
        while (True):
            print('You are the X player')
            reset_game = x_player()
            print('Here in Main : Returned from x_player: reset_game', reset_game)
            if reset_game == 1:
                playerB = start_new_game()
                break
                # time.sleep(3)
            print('You are the Computer O player')
            # time.sleep(3)
            reset_game = 0
            reset_game = c_player()
            #print('Here in Main : Returned from c_player: reset_game', reset_game)
            time.sleep(3)
            if reset_game == 1:
                start_new_game()
                break

    if (playerA == 'y') and (playerB == 'n'):
        reset_game = 0
        while (True):
            print('The Computer is the X player')
            reset_game = c_player()
            # print('returned from x_player')
            # time.sleep(1)
            if (reset_game == 1):
                start_new_game()
                exit
            print('You are the O player')
            x_player()
            # print('returned to main')
            # time.sleep(1)
            if (reset_game == 1):
                start_new_game()
                exit

# Pause execution so the Users can see the results
input('Press Enter to Exit the script ...')