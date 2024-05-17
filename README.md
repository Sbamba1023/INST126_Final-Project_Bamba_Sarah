# INST126_Final-Project_Bamba_Sarah
# Tuple Out Dice Game

Tuple Out Dice Game with Data Analysis

This is a Python implementation of the "Tuple Out" Dice Game, a simple dice game where players take turns rolling three dice. The objective is to score points by rolling different combinations of dice values, with the goal of being the first player to reach a target score.

Game Rules

1. Each player rolls three dice on their turn.
2. If all three dice show the same value (a tuple), the player's turn ends with a score of 0.
3. If two dice show the same value (fixed dice), those dice are set aside, and the player re-rolls the remaining dice until they have no more unfixed dice.
4. If all dice show different values, the player's turn score is the sum of the dice values.
5. Players continue taking turns until one player reaches or exceeds the target score (default is 50 points).
6. If the maximum number of turns is reached (default is 5 turns) and no player has reached the target score, the game ends in a draw.

Data Analysis

This implementation includes data analysis features to track and analyze game and player statistics. The following statistics are collected:

Game Statistics

- Total number of turns
- Number of tuples rolled
- Number of fixed dice rolled
- Highest score achieved by any player
- Lowest score achieved by any player

Player Statistics

- Number of wins
- Average score per game
- Highest score achieved
- Number of tuples rolled
- Number of fixed dice rolled

These statistics are printed at the end of each game, allowing you to analyze the performance of individual players and the overall game dynamics.

Usage
 Run the script:

python dice_game.py

4. Enter the number of players when prompted.
5. The game will start, and players will take turns rolling the dice.
6. After the game ends, the game statistics and player statistics will be printed.


License

This project is licensed under the MIT License. See the LICENSE.txt file for details.

Contributions

This project was developed by Sarah Bamba with help from Elaina Magnum.
## License

This project is licensed under the MIT License. See the [LICENSE.txt](LICENSE.txt) file for details.
