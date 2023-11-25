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
        # variables to keep track of hits done by user and Computer
        self.user_to_hit = 3
        self.comp_to_hit = 3
        # Functions to place random ships on user and computer ocean
        self.locate_ship(self.user_battleship)
        self.locate_ship(self.comp_battleship)
        print(f"{self.comp_to_hit} ships for user to hit")
        print(f"{self.user_to_hit} ships for computer to hit")

    # Function to create game oceans
    def create_ships(self):
        (user_ocean, comp_ocean, user_battleship, comp_battleship,) = (
            [],
            [],
            [],
            [],
        )
        for _ in range(5):
            user_ocean.append(["*"] * 5)
            comp_ocean.append(["*"] * 5)
            user_battleship.append(["*"] * 5)
            comp_battleship.append(["*"] * 5)
        return user_ocean, comp_ocean, user_battleship, comp_battleship

    # Create function to print oceans
    def show_ocean(self):
        print(f"{username} ocean is shown below;")
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
            print(f"Congrats, {self.username} hit computer's Battleship.")
            self.comp_ocean[user_guess_row][user_guess_col] = "H"
            self.comp_battleship[user_guess_row][user_guess_col] = "H"
            self.comp_to_hit -= 1
            return True
        else:
            print(f"{self.username}! missed computer's Battleship")
            self.comp_ocean[user_guess_row][user_guess_col] = "M"
            return False

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
            print("Computer hit user's Battleship")
            self.user_ocean[comp_guess_row][comp_guess_col] = "H"
            self.user_battleship[comp_guess_row][comp_guess_col] = "H"
            self.user_to_hit -= 1
            return True
        else:
            print("Computer missed user's Battleship")
            self.user_ocean[comp_guess_row][comp_guess_col] = "M"
        return False

    # Verify if the game has finished
    def verify_game_over(self):
        """
        This function checks wether the remaining hits for user and computer
        are zero, if hits are zero for any one, that one wins.
        """
        if self.user_to_hit == 0:
            print("Computer has won")
            return True
        elif self.comp_to_hit == 0:
            print(f"Congratulations, {username} has won")
            return True
        return False

    # Play again or Quit function
    def start_again_or_quit(self):
        while True:
            start_again = input("Enter 's' to start again or 'q' to quit: ")
            if start_again.lower() == "q":
                return False
            elif start_again.lower() == "p":
                (
                    self.user_ocean,
                    self.comp_ocean,
                    self.user_battleship,
                    self.comp_battleship,
                ) = self.create_ships()
                self.user_to_hit = 3
                self.comp_to_hit = 3
                self.locate_ship(self.user_battleship)
                self.locate_ship(self.comp_battleship)
                print(f"{self.comp_to_hit} ships for user to hit")
                print(f"{self.user_to_hit} ships for computer to hit")
                return True
            else:
                print(
                    "Incorrect, Please enter 's' to start agaon or 'q' to quit"
                     )

    # Start Battleship Game
    def start(self):
        for move in range(10):
            print("Move", move + 1)
            self.show_ocean()
            user_guess_row, user_guess_col = self.set_user_guess()
            self.user_move(user_guess_row, user_guess_col)
            self.comp_move()
            print(f"{self.comp_to_hit} ships for {username} to hit")
            print(f"{self.user_to_hit} ships for computer to hit")
            if self.verify_game_over():
                break
        if move == 9:
            print("Moves has ended, it is draw.")


# To start game
print("Lets play Battleship Game\n")
print("M denotes the missed target.")
print("H denotes the hit target.\n")
username = input("Please enter your username: ")
gaming = Play_Battleship(username)
gaming.start()
