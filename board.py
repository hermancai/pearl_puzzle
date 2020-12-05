import pygame
from constants import *
from piece import Piece

class Board:
    def __init__(self):
        self.board = [[0 for x in range(ROWS)] for i in range(COLS)]
        self.place_pieces()

    def draw_grid(self, window):
        # create grid with borders
        for x in range(ROWS):
            for y in range(COLS):
                rect = pygame.Rect(x*(SQUARE_SIZE+1), y*(SQUARE_SIZE+1), SQUARE_SIZE, SQUARE_SIZE)
                pygame.draw.rect(window, WHITE, rect)

    def place_pieces(self):
        # hardcode a puzzle instance
        self.board[0][1] = Piece(0, 1, BLACK)
        self.board[2][1] = Piece(2, 1, BLACK)
        self.board[2][3] = Piece(2, 3, BLACK)
        self.board[2][4] = Piece(2, 4, BLACK)
        self.board[2][6] = Piece(2, 6, BLACK)
        self.board[0][3] = Piece(0, 3, WHITE)
        self.board[4][3] = Piece(4, 3, WHITE)
        self.board[4][6] = Piece(4, 6, WHITE)
    
    def draw(self, window):
        self.draw_grid(window)
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw(window)
