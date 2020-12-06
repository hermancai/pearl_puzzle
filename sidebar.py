import pygame
from constants import WIDTH, HEIGHT, WIN_WIDTH, WIN_HEIGHT, BLACK, WHITE


# this class represents the sidebar of rules and buttons next to the puzzle
class Sidebar():
    def __init__(self):
        pygame.font.init()
        self.width = WIN_WIDTH - WIDTH
        self.height = WIN_HEIGHT
        self.spacing = WIN_HEIGHT * 0.05
        self.space_from_top = 0
        
    
    # build the sidebar from top to bottom
    def draw_sidebar(self, window):
        self.draw_background(window)
        self.write_title(window)
        self.write_goals(window)
        self.write_instructions(window)


    # create a white background
    def draw_background(self, window):
        background = pygame.Rect(WIDTH + 15, 0, self.width, self.height)
        pygame.draw.rect(window, WHITE, background)

    
    def write_title(self, window):
        # create text object
        string = 'Pearl Puzzle'
        font = pygame.font.SysFont('arial', 24)
        title = font.render(string, True, BLACK, WHITE)

        x, y = pygame.font.Font.size(font, string)  # dimensions of text object
        left = ((self.width - x) // 2) + WIDTH  # position of top left corner

        # update space to place text
        top = self.space_from_top + self.spacing 
        self.space_from_top += top + y

        window.blit(title, (left, top))
        
    
    def write_goals(self, window):
        # create text objects
        font_size = 18
        font = pygame.font.SysFont('arial', font_size)
        goals_list = []
        goals_list.append('Goal:')
        goals_list.append('Create a closed path that does not cross itself.')
        goals_list.append('Pass through each pearl once.')
        goals_list.append('Turn at each black pearl and go straight before or after.')
        goals_list.append('Go straight through each white pearl and turn before or after.')

        left = self.spacing + WIDTH
        self.space_from_top += self.spacing

        # create and render text object for each string
        for string in goals_list:
            top = self.space_from_top
            window.blit(font.render(string, True, BLACK, WHITE), (left, top))
            self.space_from_top += font_size + 2
            

    def write_instructions(self, window):
        # create text objects
        font_size = 18
        font = pygame.font.SysFont('arial', font_size)
        instructions = []
        instructions.append('Instructions:')
        instructions.append('Click on a grid square to set your starting point.')
        instructions.append('Keep clicking to squares to make your path.')
        instructions.append('You can only move to adjacent squares (up, down, left, right).')
        instructions.append('You can check if your solution is valid at any time.')
        instructions.append('Click the Reset button to refresh the board.')

        left = self.spacing + WIDTH
        self.space_from_top += self.spacing

        # create and render text object for each string
        for string in instructions:
            top = self.space_from_top
            window.blit(font.render(string, True, BLACK, WHITE), (left, top))
            self.space_from_top += font_size + 2