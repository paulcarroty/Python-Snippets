# Getting Our Feet Wet
board=[]

# Make a List
board=[]
for num in range(0,5):
    board.append(["O"] * 5)
print board

# Check it Twice
board=[]
for num in range(0,5):
    board.append(["O"] * 5)
print board

# Custom Print
board=[]
for num in range(0,5):
    board.append(["O"] * 5)


def print_board(board):
    for i in board:
        print i
        
print_board(board)

# Printing Pretty
board=[]
for num in range(0,5):
    board.append(["O"] * 5)
#print board

def print_board(board):
    for i in board:
        i = " ".join(i)
        print i
        
print_board(board)

# Hide
from random import randint 

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

# Add your code below!
def random_row(board):
    return randint(0, len(board) -1)
    
    
def random_col(board):
    return randint(0, len(board) -1)
    
print random_col(board)




# ...and Seek!
from random import randint

board = []

for x in range(0,5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

# Add your code below!
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))




# It's Not Cheating—It's Debugging!
from random import randint

board = []

for x in range(0,5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = ra2
ndom_col(board)

# Add your code below!
guess_row = int(raw_input("Guess Row: "))
guess_col = int(raw_input("Guess Col: "))
print ship_col
print ship_row




# You win!
from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:"))

print ship_row
print ship_col

if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
    
    
    
    
# Danger, Will Robinson!!
from random import randint

board = []

for x in range(0, 5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)
guess_row = int(raw_input("Guess Row:"))
guess_col = int(raw_input("Guess Col:"))

print ship_row
print ship_col

# Write your code below!
if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
else:
    print "You missed my battleship!"
    board[guess_row][guess_col] = "X"
    print print_board(board)
    
    
    
# Bad Aim
if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
else:
    print "You missed my battleship!"
    board[guess_row][guess_col] = "X"
    print print_board(board)
    if guess_row not in range(5) or \
        guess_col not in range(5):
        print "Oops, that's not even in the ocean."
    else:
        print "Miss the ship!!"
    
    
    
# Not Again!
if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"
else:
    print "You missed my battleship!"
    board[guess_row][guess_col] = "X"
    print print_board(board)
    if guess_row not in range(5) or \
        guess_col not in range(5):
        print "Oops, that's not even in the ocean."
    elif  board[guess_row][guess_col] == "X":
        print "You guessed that one already."
    else:
        print "Miss the ship!!"
    
    
# Play It, Sam
from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)
for turn in range(4):
    ship_row = random_row(board)
    ship_col = random_col(board)
    print ship_row
    print ship_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            print "Turn", turn+1
            print_board(board)
            
            
            
# Game Over
  guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            print "Turn", turn+1
            if turn == 3:
                print "Game Over"
            print_board(board)
            
            
# Done!
from random import randint

board = []

for x in range(5):
    board.append(["O"] * 5)

def print_board(board):
    for row in board:
        print " ".join(row)

print "Let's play Battleship!"
print_board(board)

def random_row(board):
    return randint(0, len(board) - 1)

def random_col(board):
    return randint(0, len(board[0]) - 1)
for turn in range(4):
    ship_row = random_row(board)
    ship_col = random_col(board)
    print ship_row
    print ship_col

# Everything from here on should go in your for loop!
# Be sure to indent four spaces!
    guess_row = int(raw_input("Guess Row:"))
    guess_col = int(raw_input("Guess Col:"))
    if guess_row == ship_row and guess_col == ship_col:
        print "Congratulations! You sunk my battleship!"
        break
    else:
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
            print "Oops, that's not even in the ocean."
        elif(board[guess_row][guess_col] == "X"):
            print "You guessed that one already."
        else:
            print "You missed my battleship!"
            board[guess_row][guess_col] = "X"
            print "Turn", turn+1
            if turn == 3:
                print "Game Over"
            print_board(board)   















