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

    
    # write the title of the puzzle in the sidebar
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
        
    
    # write the goals of the puzzle in the sidebar
    def write_goals(self, window):
        goals_list = []
        goals_list.append('Goal:')
        goals_list.append('Create a closed path that does not cross itself.')
        goals_list.append('Pass through each pearl once.')
        goals_list.append('Turn at each black pearl and go straight before or after.')
        goals_list.append('Go straight through each white pearl and turn before or after.')

        self.write_text(window, goals_list)


    # write instructions to play the puzzle in the sidebar
    def write_instructions(self, window):
        instructions = []
        instructions.append('Instructions:')
        instructions.append('Click on a grid square to set your starting point.')
        instructions.append('Keep clicking to squares to make your path.')
        instructions.append('You can only move to adjacent squares (up, down, left, right).')
        instructions.append('You can check if your solution is valid at any time.')
        instructions.append('Click the Reset button to refresh the board.')

        self.write_text(window, instructions)

    
    # create text objects to render on the window given a list of strings
    def write_text(self, window, text_list):
        font_size = 18
        font = pygame.font.SysFont('arial', font_size)

        left = self.spacing + WIDTH  # set left margin
        self.space_from_top += self.spacing  # update spacing

        for string in text_list:  # create text objects
            top = self.space_from_top
            window.blit(font.render(string, True, BLACK, WHITE), (left, top))
            self.space_from_top += font_size + 2
