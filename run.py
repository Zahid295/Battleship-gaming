# Imporiting random module
import random


# Create 5x5 user and computer boards
user_ocean = []
comp_ocean = []
# Loop to create two game boards
for i in range(5):
    user_ocean.append(["*"] * 5)
    comp_ocean.append(["*"] * 5)


# Create function to print the boards
def show_ocean():
    """
    This function will print User and Computer Boards
    """
    print("User board is shown below;")
    for row in user_ocean:
        print(" ".join(row))
    print("Computer board is shown below;")
    for row in comp_ocean:
        print(" ".join(row))


# Create function for randomly placing ships on boards
def locate_ship(ocean):
    direction = random.choice(["horizonatl", "vertical"])
    if direction == "horizontal":
        row_point = random.randint(0, len(ocean) - 1)
        col_point = random.randint(0, len(ocean[0] - 3))
        for x in range(3):
            ocean[row_point][col_point + x] = "S"
    else:
        row_point = random.randint(0, len(ocean) - 3)
        col_point = random.randint(0, len(ocean[0]) - 1)
        for x in range(3):
            ocean[row_point + x][col_point] = "S"


# Placing ships at random loactions at user and computer boards
locate_ship(user_ocean)
locate_ship(comp_ocean)

# Wellcome message
print("Wellcome to Battleship game")

# Asking for username
username = input("Please type in your username here: ")

# Create game loop
for move in range(10):
    print("move", move + 1)
    show_ocean()
    user_guess_row = int(input("Select row between 1 and 5: ")) - 1
    user_guess_col = int(input("Select column between 1 and 5: ")) - 1

    # User move
    if user_guess_row not in range(5) or user_guess_col not in range(5):
        print("Sorry, that is out of Ocean")
        continue
    elif (
        comp_ocean[user_guess_row][user_guess_col] == "H"
        or comp_ocean[user_guess_row][user_guess_col] == "M"
    ):
        print("You have already guessed that one")
        continue
    elif comp_ocean[user_guess_row][user_guess_col] == "S":
        print(f"Congrats, you hit computer's Battleship.")
        comp_ocean[user_guess_row][user_guess_col] = "H"
    else:
        print(f"{username} missed computer's Battleship")
        comp_ocean[user_guess_row][user_guess_col] = "M"

    # Computer move
    comp_guess_row = random.randint(0, 4)
    comp_guess_col = random.randint(0, 4)
    if (
        user_ocean[comp_guess_row][comp_guess_col] == "H"
        or user_ocean[comp_guess_row][comp_guess_col] == "M"
    ):
        print("Computer has already guessed that one")
        continue
    elif user_ocean[comp_guess_row][comp_guess_col] == "S":
        print("Computer hit player's Battleship")
        user_ocean[comp_guess_row][comp_guess_col] = "H"
        break
    else:
        print("Computer missed player's Battleship")
        user_ocean[comp_guess_row][comp_guess_col] = "M"

    if move == 9:
        print("Game is over")

