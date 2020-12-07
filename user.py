import pygame
from constants import SQUARE_SIZE, BLUE, GREEN, WIDTH, HEIGHT


# this class keeps track of the user's moves on the board
class User():
    def __init__(self):
        self.path = []


    # clear the solution path after user clicks on 'reset' button
    def clear_user_path(self):
        self.path = []


    # convert mouse position into grid coords
    def get_coords_from_mouse(self, mouse_pos):
        x, y = mouse_pos
        row = y // SQUARE_SIZE
        col = x // SQUARE_SIZE

        self.path.append((row, col))    
        return (row, col)


    # convert grid coords to resolution coords
    def convert_coords(self, coords):
        x = ((coords[1]+1)*SQUARE_SIZE) - (SQUARE_SIZE // 2)
        y = ((coords[0]+1)*SQUARE_SIZE) - (SQUARE_SIZE // 2)
        return x, y


    # draw the path that the user creates on the grid
    def draw_path(self, window, coords):
        if len(self.path) == 1:  # the starting point
            self.draw_point(window, coords, GREEN, SQUARE_SIZE * 0.4 // 2)
            self.draw_point(window, coords, BLUE, SQUARE_SIZE * 0.2 // 2)

        else:  # draw new point and line to previous point
            if self.valid_move(self.path[-2], self.path[-1]):
                self.draw_point(window, coords, BLUE, SQUARE_SIZE * 0.2 // 2)
                self.draw_line(window, self.path[-2], coords)

            else:  # move is invalid
                del self.path[-1]


    # draw the user's current location on the grid
    def draw_point(self, window, coords, color, radius):
        x, y = self.convert_coords(coords)
        pygame.draw.circle(window, color, (x, y), radius)


    # draw a line connecting the user's current and previous location
    def draw_line(self, window, prev_point, curr_point):
        prev_x, prev_y = self.convert_coords(prev_point)
        curr_x, curr_y = self.convert_coords(curr_point)

        pygame.draw.line(window, BLUE, (prev_x, prev_y), (curr_x, curr_y), 5)


    # check if the user's new move is valid
    def valid_move(self, prev_point, curr_point):
        # cannot move to an already visited point, except for starting point
        if curr_point in self.path[1:-2]:
            return False

        # cannot move to previous point or move after going back to the starting point
        if len(self.path) >= 3:
            if curr_point == self.path[-3] or self.path[0] == self.path[-2]:
                return False

        # can only move to an adjacent square (up, down, left, right)
        bool1 = (abs(curr_point[0] - prev_point[0]) == 1) and (curr_point[1] - prev_point[1] == 0)
        bool2 = (abs(curr_point[1] - prev_point[1]) == 1) and (curr_point[0] - prev_point[0] == 0)
        
        return bool1 or bool2
        