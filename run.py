# Imporiting random module
import random


# Create class for Battleship game
class Play_Battleship:
    def __init__(self, username):
        self.username = username
        (
            self.user_ocean,
            self.comp_ocean,
            self.user_battleship,
            self.comp_battleship,
        ) = self.create_ships()
        self.locate_ship(self.user_battleship)
        self.locate_ship(self.comp_battleship)

    # Function to create game oceans
    def create_ships(self):
        user_ocean, comp_ocean, user_battleship, comp_battleship = [], [], [], []
        for x in range(5):
            user_ocean.append(["*"] * 5)
            comp_ocean.append(["*"] * 5)
            user_battleship.append(["*"] * 5)
            comp_battleship.append(["*"] * 5)
        return user_ocean, comp_ocean, user_battleship, comp_battleship


# Create function to print oceans
def show_ocean():
    """
    This function will print User and Computer oceans
    """
    print("User ocean is shown below;")
    for row in self.user_ocean:
        print(" ".join(row))
    print("Computer ocean is shown below;")
    for row in self.comp_ocean:
        print(" ".join(row))


# Create function for randomly placing ships on oceans
def locate_ship(self, ocean):
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


# Getting user guess
def set_user_guess(self):
    user_guess_row = int(input("Select row between 1 and 5: ")) - 1
    user_guess_col = int(input("Select column between 1 and 5: ")) - 1
    return user_guess_row, user_guess_col


# Handling user's move
def user_move(self, user_guess_row, user_guess_col):
    if user_guess_row not in range(5) or user_guess_col not in range(5):
        print("Sorry, that is out of Ocean")
        return False
    elif (
        self.comp_ocean[user_guess_row][user_guess_col] == "H"
        or self.comp_ocean[user_guess_row][user_guess_col] == "M"
    ):
        print("You have already guessed that one")
        return False
    elif self.comp_battleship[user_guess_row][user_guess_col] == "S":
        print(f"Congrats, {self.username}! hit computer's Battleship.")
        self.comp_ocean[user_guess_row][user_guess_col] = "H"
        self.comp_battleship[user_guess_row][user_guess_col] = "H"
    else:
        print(f"{username} missed computer's Battleship")
        self.comp_ocean[user_guess_row][user_guess_col] = "M"
        return True



# Create game loop
for move in range(10):
    print("move", move + 1)
    show_ocean()

    # Computer move
    comp_guess_row = random.randint(0, 4)
    comp_guess_col = random.randint(0, 4)
    if (
        user_ocean[comp_guess_row][comp_guess_col] == "H"
        or user_ocean[comp_guess_row][comp_guess_col] == "M"
    ):
        print("Computer has already guessed that one")
        continue
    elif user_battleship[comp_guess_row][comp_guess_col] == "S":
        print("Computer hit player's Battleship")
        user_ocean[comp_guess_row][comp_guess_col] = "H"
        user_battleship[comp_guess_row][comp_guess_col] = "H"
    else:
        print("Computer missed player's Battleship")
        user_ocean[comp_guess_row][comp_guess_col] = "M"
    if "S" not in (element for sublist in user_battleship for element in sublist):
        print("Computer has won")
        break
    elif "S" not in (element for sublist in comp_battleship for element in sublist):
        comp_ocean[user_guess_row][user_guess_col] == "H"
        show_ocean()
        print(f"Congratulations, {username}! has won")
        break

    if move == 9:
        print("Moves has ended, it is draw.")

