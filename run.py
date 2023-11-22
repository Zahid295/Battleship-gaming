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
        (
            user_ocean,
            comp_ocean,
            user_battleship,
            comp_battleship,
        ) = [], [], [], []
        for _ in range(5):
            user_ocean.append(["*"] * 5)
            comp_ocean.append(["*"] * 5)
            user_battleship.append(["*"] * 5)
            comp_battleship.append(["*"] * 5)
        return user_ocean, comp_ocean, user_battleship, comp_battleship

    # Create function to print oceans
    def show_ocean(self):
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

    # Function for getting user guess
    def set_user_guess(self):
        user_guess_row = int(input("Select row between 1 and 5: ")) - 1
        user_guess_col = int(input("Select column between 1 and 5: ")) - 1
        return user_guess_row, user_guess_col

    # Function for user's move
    def user_move(self, user_guess_row, user_guess_col):
        """
        This function handles user's moves
        """
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
            print(f"{self.username}! missed computer's Battleship")
            self.comp_ocean[user_guess_row][user_guess_col] = "M"
            return True

    # Function for compter's move
    def comp_move(self):
        """
        This function handles computer's moves
        """
        comp_guess_row = random.randint(0, 4)
        comp_guess_col = random.randint(0, 4)
        if (
            self.user_ocean[comp_guess_row][comp_guess_col] == "H"
            or self.user_ocean[comp_guess_row][comp_guess_col] == "M"
        ):
            print("Computer has already guessed that one")
            return False
        elif self.user_battleship[comp_guess_row][comp_guess_col] == "S":
            print("Computer hit player's Battleship")
            self.user_ocean[comp_guess_row][comp_guess_col] = "H"
            self.user_battleship[comp_guess_row][comp_guess_col] = "H"
        else:
            print("Computer missed player's Battleship")
            self.user_ocean[comp_guess_row][comp_guess_col] = "M"
        return True

    # Verify if the game has finished
    def verify_game_over(self):
        """
        This functions verifies if "S" is not in user battleship board,
        it says Computer won or if "S" not in computer battleship board,
        it says user has won
        """
        if "S" not in (
            element for sublist in self.user_battleship for element in sublist
        ):
            print("Computer has won")
            return True
        elif "S" not in (
            element for sublist in self.comp_battleship for element in sublist
        ):
            print(f"Congratulations, {username}! has won")
            return True
        return False

    # Start Battleship Game
    def start(self):
        for move in range(10):
            print("Move", move + 1)
            self.show_ocean()
            user_guess_row, user_guess_col = self.set_user_guess()
            if not self.user_move(user_guess_row, user_guess_col):
                continue
            if not self.comp_move():
                continue
            if self.verify_game_over():
                break
        if move == 9:
            print("Moves has ended, it is draw.")


# To start game
username = input("Please enter your username: ")
gaming = Play_Battleship(username)
gaming.start()