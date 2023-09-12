# Programmer: Laura Castro
# Date: August 14, 2023
# Purpose: Write a tic tac toe program that plays the computer. 

# import random module to generate computer moves
import random 

# Store the squares in the board and update moves here
board = [[1, 2, 3], [4,"X",6], [7,8,9]]

# This function accepts one parameter containing the board's current status and prints it out to the console.
def display_board(board):
    for row in range(0,3):
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(" ")
        for column in range(0,3): #This loop prints the value of each square on the board
            print("|  ", board[row][column], " ", end=" ")
        print("|")
        print(" ")
        print("|       |       |       |")
    print("+-------+-------+-------+")
    
# The function accepts the board's current status, asks the user about their move, checks the input, and updates the board according to the user's decision.
def enter_move(board):
    # Get the user's input and validate that it is an integer between 0 and 10 and it cannot point to a field in the free squares list
    while True:
        try:
            user_move = int(input("Enter your move (1-9): "))
            row = (user_move - 1) // 3
            col = (user_move - 1) % 3
            if user_move < 1 or user_move > 9 or user_move == 5:
                # Print this to the screen because the entry is invalid
                print("Invalid move. Try again.")
            else:
                board[row][col]= 'O'
                break
        # This exception is raised if the input cannot be converted to an int
        except ValueError:
            print("Invalid move. Please enter a number.")
 
# This function browses the board and builds a list of all the free squares; the list consists of tuples, while each tuple is a pair of row and column numbers.
def make_list_of_free_fields(board):
    # Have a list that stores free squares using a tuple as the element
    free_squares = []
    # iterate through the board to index free fields
    for row in range(3): 
        for col in range (3) :
            if board[row][col] != 'O' and board[row][col] != 'X': # add square to the list if it is an integer
                free_squares.append(board[row][col])
    return free_squares

# This function analyzes the board's status in order to check if the player using 'O's or 'X's has won the game
def victory_for(board, sign):
    # Check if there is three in a row of the given sign
    if (board[0][0] == sign and board[0][1] == sign and board[0][2] == sign) or \
       (board[1][0] == sign and board[1][1] == sign and board[1][2] == sign) or \
       (board[2][0] == sign and board[2][1] == sign and board[2][2] == sign) or \
       (board[0][0] == sign and board[1][0] == sign and board[2][0] == sign) or \
       (board[0][1] == sign and board[1][1] == sign and board[2][1] == sign) or \
       (board[0][2] == sign and board[1][2] == sign and board[2][2] == sign) or \
       (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or \
       (board[1][2] == sign and board[1][1] == sign and board[2][0] == sign):
           return True

# This function draws the computer's move and updates the board.
def draw_move(board):
    move = random.choice(make_list_of_free_fields(board)) # Choose a random number in the list of free spaces
    # These two calculations index the computer's entry
    row = (move - 1) // 3
    col = (move - 1) % 3
    # Assign X to the indexed number
    board [row][col]='X'
    
# Main game loop
display_board(board)

while True:
    enter_move(board)
    display_board(board)
    if victory_for(board, 'O'):
        print("You win!")
        break
    if len(make_list_of_free_fields(board)) == 0:
        print("It\'s a tie!")
        break
    draw_move(board)
    display_board(board)
    if victory_for(board, 'X'):
        print("Computer wins!")
        break
