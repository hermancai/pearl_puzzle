# pearl_puzzle
Pearl Puzzle is a board game where finding a solution is proven to be NP-complete. 
This is an implementation of the puzzle using Python 3 and the pygame module.

How to run on Windows:
- Download all files
- Have Python 3 installed
- Navigate to the directory containing main.py
- >pip install pygame
- >python3 main.py

NOTES: 
- The puzzle board instance is hardcoded by default. 
- Get a random puzzle by changing the constant 'RANDOM_GENERATOR' to True in /assets/constants.py
- Some randomly generated puzzles may be impossible to solve. Close and rerun main.py for a new puzzle.
- The solution to the hardcoded puzzle is available in this directory.
- More constant values can be found and changed in /assets/constants.py

![example puzzle](https://github.com/hermancai/pearl_puzzle/blob/main/random_puzzle_solution.png?raw=true)
