# Imporiting random module
import random


# Create 5x5 user and computer boards
player_board = []
computer_board = []
# Loop to create two game boards
for i in range(5):
    player_board.append(["*"] * 5)
    computer_board.append(["*"] * 5)

# Create function to print the boards
def show_boards():
    """
    This function will print User and Computer Boards
    """
    print("User board is shown below;")
    for row in player_board:
        print(" ".join(row))
    print("Computer board is shown below;")
    for row in computer_board:
        print(" ".join(row))


# Create function for randomly placing ships on boards
def rand_row_point(board):
    return random.randint(0, len(board) - 1)

def rand_col_point(board):
    return random.randint(0, len(board[0]) -1)

# Placing ships at random loactions at user and computer boards
player_ship_row = rand_row_point(player_board)
player_ship_col = rand_col_point(player_board)
