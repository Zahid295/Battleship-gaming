# Battleship Game

This is an implementation of the classic Battleship game in Python. The game is played on a 5x5 grid, and each player has 3 ships. Players take turns guessing the coordinates of the other player's ships. The first player to sink all of the other player's ships wins the game.

## Rules and Instructions on How to Play game

- Run the script in your Python environment.
- You will be prompted to enter your username. Please note that the username should only contain English   alphabets.
- The game will start, and you will be asked to guess the row and column of a ship on the opponent's board. Enter a number between 1 and 5 for both the row and the column.
- If you want to quit the game at any point, type 'q' when asked for your guess.
- The game will inform you whether your guess was a hit or a miss. Then, the computer will take its turn.
- The game continues until all ships of a player are sunk. The player who sinks all ships of the opponent first wins the game.
- After the game ends, you will be asked if you want to play again. Press 's' to start game again or 'q' to quit.

## Features

#### Interactive game
- The game prompts the user for input and responds with whether the guess was a hit or a miss.
- The user and the computer take turns to play, making the game interactive and engaging.
![](../Battleship-gaming/documentation/interactive_game_1.png)
![](../Battleship-gaming/documentation/interactive_game_2.png)
![](../Battleship-gaming/documentation/interactive_game_3.png)
#### Intuitive Interface
- The game uses a simple text-based interface that's easy to understand and use.
- The board is displayed after each turn, allowing players to see the current state of the game.
#### Automatic ship placement
- Game boards for user and computer are automatically generated and shown after entering username.
- After that, ships are also automatically placed on game boards that are hidden from user. 
- This feature saves time and allows the game to start quickly.
![](../Battleship-gaming/documentation/automatic_ship_placement_1.png)
![](../Battleship-gaming/documentation/automatic_ship_placement_2.png)
#### Play again option
- After each game, the user is given the option to play again or quit.
- This feature allows for continuous play without needing to restart the program.
![](../Battleship-gaming/documentation/play_again.png)
#### Input validation
- The game checks if the user's input is valid and prompts the user to enter a valid input if it's not.
- Also, if the user or computer guess the same row and column, the message says already guessed that one.
- Further, if user enters any alphabets instead of integer for guess, message says incorrect input,
 please enter required number.
- This feature ensures that the game runs smoothly without errors due to invalid input.
![](../Battleship-gaming/documentation/input_validation_1.png)
![](../Battleship-gaming/documentation/input_validation_2.png)


## Flow Chart
![](../Battleship-gaming/documentation/flow_chart.png)

## Testing

To test this project manually, I have
- Checked the lint validation embedded in code institute python essentials template
- Every issue has been fixed such as 'line too long', 'needs 2 spaces found one' and 'whitespaces'. Game is unaffected by these issue but the code quality is perserved.
- Inputs were checked by using differenet invalid inputs. For example, empty inputs, numbers out of range and invalid strings.
- All the code is tested in local and code institute Heroku terminal.

### Validation
To validate the code, I used code institute's [PEP8 python linter](https://pep8ci.herokuapp.com/).
![](../Battleship-gaming/documentation/code_validation.png)
## Technologies used
- Python language was used in the creation of this game.
- The Object oriented programming paradigm was the one I used to complete this Game project. It is made up of classes and methods. These methods are used to carry out the tasks of the desired result.
- [Github](https://github.com/) was used for hosting this project's source code.
- [Codeanywhere](https://codeanywhere.com/) was used as IDE for the development of this project.
- [Heroku](https://www.heroku.com/) was used to deploy this Application.
- Python Random module is used to generate random numbers in this project.

## Bugs
- pylint warnings regarding trailing white space and space found between any two line have been resolved by correctly formatting the code.
- During testing the game, a bug was found that at the end of the game loop, when somebody wins or turns ended, there was not any way to smoothly exit the game. So I applied while loop in function 'start again or quit' so that user can choose either to quit the game or play again at the end of game without throughing any error.
- After that, another bug was found that if someone enters something other than 's' which represents start game again and 'q' which represents quit game, an error was seen so the while statement was used in stat_again_or_quit function to handle this issue.

## Deployement
Heroku was used to host the project. The following are the steps to implement the project:

- Sign in to Heroku website first.
- Click "New" to create a new application.
- I gave my project the name "battleship-gamming," selected "Europe" as my area, and then hit "Create app."
- Next, choosing the 'Settings' tab.
- I then click "Reveal Config Vars" after scrolling down to "Config Vars."
- I typed 'PORT' in the key box and '8000' in the value field.
- I then continued to scroll down to "Buildpacks" and selected "Add buildpacks."
- I then selected "Python" and save changes.
- I chose "nodejs" this time when I selected "Add buildpack," and I then hit "Save changes."
- I then confirmed that the buildpacks were arranged with "python" at the top and "nodejs" afterwards.
- Next, choose the 'Deploy' tab.
- The next step is to choose a "Deployment method." I chose "GitHub," acknowledged that I wanted to connect to GitHub, and enetered my github account.
- I then looked at "Connect to GitHub" repository name and saw the name I gave the repository: "Battleship-gaming", the press "Search" button and then "Connect".
- I then scrolling down to "Manual Deploy" and pressed "Deploy Branch".
- Finally, I got the message "The app was successfully deployed" and  clicked the "View" button.
