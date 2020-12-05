import pygame
from constants import SQUARE_SIZE, BLUE, GREEN, WIDTH, HEIGHT

class User():
    def __init__(self):
        self.path = []

    def get_coords_from_mouse(self, mouse_pos):
        x, y = mouse_pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE

        self.path.append((row, col))    
        return (row, col)

    def draw_path(self, window, coords):
        if len(self.path) == 1:  # the starting point
            self.draw_point(window, coords, GREEN, SQUARE_SIZE * 0.4 // 2)
        else:  # draw new point and line to previous point
            if self.valid_move(self.path[-2], self.path[-1]) is True:
                self.draw_point(window, coords, BLUE, SQUARE_SIZE * 0.2 // 2)
                self.draw_line(window, (self.path[-2]), coords)
            else:  # move is invalid
                del self.path[-1]

    def draw_point(self, window, coords, color, radius):
        row, col = coords[0] + 1, coords[1] + 1
        x = (col*SQUARE_SIZE) - (SQUARE_SIZE // 2)
        y = (row*SQUARE_SIZE) - (SQUARE_SIZE // 2)
        pygame.draw.circle(window, color, (x, y), radius)

    def draw_line(self, window, prev_point, curr_point):
        thick = 5
        prev_x = ((prev_point[1]+1)*SQUARE_SIZE) - (SQUARE_SIZE // 2)
        prev_y = ((prev_point[0]+1)*SQUARE_SIZE) - (SQUARE_SIZE // 2)
        curr_x = ((curr_point[1]+1)*SQUARE_SIZE) - (SQUARE_SIZE // 2)
        curr_y = ((curr_point[0]+1)*SQUARE_SIZE) - (SQUARE_SIZE // 2)
        print((prev_x, prev_y), (curr_x, curr_y))
        pygame.draw.line(window, BLUE, (prev_x, prev_y), (curr_x, curr_y), thick)

    def valid_move(self, prev_point, curr_point):
        # cannot move to an already visited point, except for starting point
        if curr_point in self.path[1:-2]:
            return False

        # cannot move to previous point
        if len(self.path) >= 3:
            if curr_point == self.path[-3]:
                return False

        # can only move to an adjacent square (ie up, down, left, or right)
        bool1 = (abs(curr_point[0] - prev_point[0]) == 1) and (curr_point[1] - prev_point[1] == 0)
        bool2 = (abs(curr_point[1] - prev_point[1]) == 1) and (curr_point[0] - prev_point[0] == 0)
        if bool1 or bool2:
            return True

        return False