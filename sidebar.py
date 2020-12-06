import pygame
from constants import WIDTH, HEIGHT, WIN_WIDTH, WIN_HEIGHT, BLACK, WHITE


# this class represents the sidebar of rules and buttons next to the puzzle
class Sidebar():
    def __init__(self):
        self.width = WIN_WIDTH - WIDTH
        self.height = WIN_HEIGHT

    
    def draw_sidebar(self, window):
        self.draw_background(window)


    def draw_background(self, window):
        background = pygame.Rect(WIDTH + 15, 0, self.width, self.height)
        pygame.draw.rect(window, WHITE, background)