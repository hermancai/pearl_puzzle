# import pygame

# randomly generate a pearl puzzle 
# Change RANDOM_GENERATOR to False for a hardcoded instance
RANDOM_GENERATOR = True
# RANDOM_GENERATOR = False
PEARL_COUNT = 4

# dimensions
WIDTH, HEIGHT = 560, 560
SMALL_FONT, LARGE_FONT = 18, 24

# WIDTH, HEIGHT = 400, 400  # for fitting into repl.it
# SMALL_FONT, LARGE_FONT = 13, 18  # for fitting into repl.it

WIN_WIDTH, WIN_HEIGHT = WIDTH * 2, HEIGHT
ROWS, COLS = 7, 7
SQUARE_SIZE = WIDTH//COLS

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 64, 64)
GREEN = (52, 235, 52)
BLUE = (0, 98, 255)
