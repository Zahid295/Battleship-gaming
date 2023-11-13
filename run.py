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
    return random.randint(0, len(board[0]) - 1)


# Placing ships at random loactions at user and computer boards
player_ship_row = rand_row_point(player_board)
player_ship_col = rand_col_point(player_board)

computer_ship_row = rand_row_point(computer_board)
computer_ship_col = rand_col_point(computer_board)

# Wellcome message
print("Wellcome to Battleship game")

# Asking for username
username = input("Please type in your username here: ")

# Create game loop
for move in range(10):
    print("move", move + 1)
    show_boards()
    user_guess_row = int(input("Select row between o and 4: "))
    user_guess_col = int(input("Select column between 0 and 4: "))

    # User move
    if user_guess_row not in range(5) or user_guess_col not in range(5):
        print("Sorry, that is out of Ocean")
        continue
    elif (
        computer_board[user_guess_row][user_guess_col] == "H"
        or computer_board[user_guess_row][user_guess_col] == "M"
    ):
        print("You have already guessed that one")
        continue
    elif user_guess_row == computer_ship_row and user_guess_col == computer_ship_col:
        print(f"Congrats, you hit computer's ship.")
        computer_board[user_guess_row][user_guess_col] = "H"
    else:
        print(f"Sorry, {username}. You missed computer's ship")
        computer_board[user_guess_row][user_guess_col] = "M"
    
    # Computer move
    computer_guess_row = random.randint(0, 4)
    computer_guess_col = random.randint(0, 4)
    if player_board[computer_guess_row][computer_guess_col] == "H" or player_board[computer_guess_row][computer_guess_col] == "M":
        print("Computer has already guessed that one")
        continue
    elif computer_guess_row == player_ship_row and computer_guess_col == player_ship_col:
        print("Computer hit player Battleship")
        player_board[computer_guess_row][computer_guess_col] = "H"
        break