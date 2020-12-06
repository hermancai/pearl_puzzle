import pygame
from constants import WIDTH, HEIGHT, WIN_WIDTH, WIN_HEIGHT, BLACK, WHITE


# this class represents the sidebar of rules and buttons next to the puzzle
class Sidebar():
    def __init__(self):
        pygame.font.init()
        self.width = WIN_WIDTH - WIDTH
        self.height = WIN_HEIGHT
        self.spacing = WIN_HEIGHT * 0.1
        self.space_from_top = 0
        
    
    # build the sidebar from top to bottom
    def draw_sidebar(self, window):
        self.draw_background(window)
        self.write_title(window)
        self.write_rules(window)


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
        self.space_from_top += top

        window.blit(title, (left, top))
        