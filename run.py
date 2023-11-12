# Imporiting random module
import random


# Create 5x5 user and computer boards
player_board = []
computer_board = []
# Loop to create two game boards
for i in range(5):
    player_board.append(["*"] * 5)
    computer_board.append(["*"] * 5)