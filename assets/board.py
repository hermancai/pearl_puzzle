import pygame
from assets.constants import *
from assets.piece import Piece



# this class represents the puzzle board 
class Board:
    def __init__(self):
        self.board = [[0 for x in range(ROWS)] for i in range(COLS)]  # 2D array
        self.pearl_locations = []
        self.place_pieces()


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
    def place_pieces(self):
        self.add_piece(0, 1, BLACK)
        self.add_piece(2, 1, BLACK)
        self.add_piece(2, 3, BLACK)
        self.add_piece(2, 4, BLACK)
        self.add_piece(2, 6, BLACK)
        self.add_piece(0, 3, WHITE)
        self.add_piece(4, 3, WHITE)
        self.add_piece(4, 6, WHITE)
    

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
