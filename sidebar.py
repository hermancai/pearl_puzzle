import pygame
from constants import WIDTH, HEIGHT, WIN_WIDTH, WIN_HEIGHT, BLACK, WHITE, RED


# this class represents the sidebar of rules and buttons next to the puzzle
class Sidebar():
    def __init__(self):
        pygame.font.init()
        self.width = WIN_WIDTH - WIDTH
        self.height = WIN_HEIGHT
        self.spacing = WIN_HEIGHT * 0.05
        self.space_from_top = 0
        self.button_padding = 10
        
    
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
        goals_list.append('Turn at each black pearl and go straight before AND after.')
        goals_list.append('Go straight through each white pearl and turn before OR after.')

        self.write_text(window, goals_list)


    # write instructions to play the puzzle in the sidebar
    def write_instructions(self, window):
        instructions = []
        instructions.append('Instructions:')
        instructions.append('Click on a grid square to set your starting point.')
        instructions.append('Keep clicking on squares to make your path.')
        instructions.append('You can only move to adjacent squares (up, down, left, right).')
        instructions.append('Click on "VERIFY SOLUTION" to verify at any time.')
        instructions.append('Click on "RESET" button to refresh the board.')

        self.write_text(window, instructions)

    
    # create text objects to render on the window given a list of strings
    def write_text(self, window, text_list):
        font_size = 18
        font = pygame.font.SysFont('arial', font_size)

        left = self.spacing + WIDTH  # set left margin
        self.space_from_top += self.spacing  # update spacing

        for string in text_list:  # create text objects
            window.blit(font.render(string, True, BLACK, WHITE), (left, self.space_from_top))
            self.space_from_top += font_size + 3


    # draw a button onto the sidebar given the button text and color
    def draw_button(self, window, button_text, color):
        self.space_from_top += self.spacing

        # create text object
        font = pygame.font.SysFont('arial', 20)
        button = font.render(button_text, True, color, WHITE)

        # get dimensions of text and button rectangle. draw rectangle
        text_width, text_height = pygame.font.Font.size(font, button_text)
        rect_width, rect_height = self.draw_button_rect(window, text_width, text_height)

        # draw text
        left = WIDTH + self.spacing + self.button_padding
        top = self.space_from_top + self.button_padding
        window.blit(button, (left, top))

        # return ranges of where button exists on window
        rect_left = WIDTH + self.spacing
        rect_top = self.space_from_top
        self.space_from_top += rect_height
        return (rect_left, rect_left + rect_width), (rect_top, rect_top + rect_height)


    # draw a rectangle to outline a button
    def draw_button_rect(self, window, text_width, text_height):
        rect_width = text_width + self.button_padding * 2
        rect_height = text_height + self.button_padding * 2

        # create and draw rectangle object
        rect = pygame.Rect(self.spacing + WIDTH, self.space_from_top, rect_width, rect_height)
        pygame.draw.rect(window, BLACK, rect, 3, 3)
        return rect_width, rect_height

    
    # display on the sidebar whether the solution is correct
    def display_solution_text(self, text, color, window, rect_width, rect_height):
        # create and render text object
        font = pygame.font.SysFont('arial', 20)
        display = font.render(text, True, color, WHITE)
        window.blit(display, (rect_width[1] + self.spacing, rect_height[0] + self.button_padding))


    # hide the solution text after clicking 'reset' button
    def hide_solution_text(self, window, rect_width, rect_height):
        # draw a white rectangle over the solution text
        left, top = rect_width[1] + self.spacing, rect_height[0]
        width, height = rect_width[1] - rect_width[0], rect_height[1] - rect_height[0]
        rect = pygame.Rect(left, top, width, height)
        pygame.draw.rect(window, WHITE, rect)
