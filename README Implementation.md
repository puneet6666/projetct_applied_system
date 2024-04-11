Welcome to our Connect Four Game implementation. This document provides details on how to interact with the system and play the game.

# Getting Started

To start the game, you need to have Python installed on your system.
Implementation Details
Steps for interactions:
1) Start the Game: 
Run the script, and the game board will be shown.
The board consists of 6 rows and 7 columns, initially filled with blue tokens indicating empty slots.
2) Player Moves: 
Players will be prompted to input the number of the column where they wish to place their token.
If the picked column is full, the game will request a different column number.
3) Game Progress:
The game alternates turns between two players, starting with the red player.
The board updates and displays after each move, with the respective token color shown in the chosen column.
4) Checking for win:
The game automatically checks for a win condition after each move.
A win is declared if a player aligns four tokens either vertically, horizontally, or diagonally.
5) Draw Condition:
If the board is filled without any player winning, the game will declare a draw and ends the game.
6) Exiting the game:
To exit the game at any point, type ‘e’ when prompted for a column number.


Additional Features Included:
1) Alternate Turns: The game changes the active token after each valid move.
2) Victory Check: Automatically detects and gives the winner.
3) Draw Detection: Identifies a draw situation if the board is complete and ends the game.
4) User-Friendly Interface: Clear Instructions about the game and updates are provided through the console.



Additional Information to be noted:
1) Ensure you are running the latest version of python for optimal performance.
2) The game is designed for two players taking turns on the same machine.
