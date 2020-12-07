from constants import *


# this class represents the pearls placed on the puzzle board
class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.x = 0
        self.y = 0
        self.calc_position()
        self.times_visited = 0


    def __repr__(self):
        return "Piece at " + str(self.row) + ":" + str(self.col)


    # finds middle of the square to get coordinates on window
    def calc_position(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2


    # draw the pieces onto the puzzle board
    def draw(self, window):
        radius = SQUARE_SIZE * 0.75 // 2
        pygame.draw.circle(window, BLACK, (self.x, self.y), radius + 2)  # outline
        pygame.draw.circle(window, self.color, (self.x, self.y), radius)
