import pygame
from assets.constants import *
from assets.piece import Piece
from random import randint, getrandbits



# this class represents the puzzle board 
class Board:
    def __init__(self):
        self.board = [[0 for x in range(ROWS)] for i in range(COLS)]  # 2D array
        self.pearl_locations = []
        if RANDOM_GENERATOR:
            self.random_place_pieces()
        else:
            self.hardcode_place_pieces()


    # return the content on the board given list indices
    def get_content_at(self, x, y):
        return self.board[x][y]


    # create a grid with borders
    def draw_grid(self, window):
        for x in range(ROWS):
            for y in range(COLS):
                rect = pygame.Rect(x*(SQUARE_SIZE+1), y*(SQUARE_SIZE+1), SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(window, WHITE, rect)


    # hardcode a puzzle instance
    def hardcode_place_pieces(self):
        self.add_piece(0, 1, BLACK)
        self.add_piece(2, 1, BLACK)
        self.add_piece(2, 3, BLACK)
        self.add_piece(2, 4, BLACK)
        self.add_piece(2, 6, BLACK)
        self.add_piece(0, 3, WHITE)
        self.add_piece(4, 3, WHITE)
        self.add_piece(4, 6, WHITE)
    

    # generate pearls randomly on board
    def random_place_pieces(self):
        for i in range(PEARL_COUNT):
            # randomly select pearl color
            if bool(getrandbits(1)):
                color = BLACK
            else:
                color = WHITE
            
            # create coordinates for an unoccupied space on the board
            new_location = False
            while new_location is False:
                x = randint(0, ROWS - 1)
                y = randint(0, COLS - 1)
                if (x, y) not in self.pearl_locations:
                    new_location = True

            self.add_piece(x, y, color)


    # create and add pieces to the board
    def add_piece(self, x, y, color):
        piece = Piece(x, y, color)
        self.board[x][y] = piece
        self.pearl_locations.append((x, y))


    # draw the board and pearl pieces
    def draw_board(self, window):
        self.draw_grid(window)

        for row in range(ROWS):  # loop through board and draw pieces
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(window)
