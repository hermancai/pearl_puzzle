import pygame
from constants import WIDTH, HEIGHT, WIN_WIDTH, WIN_HEIGHT, WHITE, BLACK, RED
from verification import *
from board import Board
from user import User
from sidebar import Sidebar

FPS = 30
WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Pearl Puzzle")


def main():
    running = True
    clock = pygame.time.Clock()

    board = Board()
    user = User()
    sidebar = Sidebar()

    # draw puzzle grid, sidebar, and buttons
    board.draw_board(WINDOW)
    sidebar.draw_sidebar(WINDOW)
    verify_btn_width, verify_btn_height = sidebar.draw_button(WINDOW, 'VERIFY SOLUTION', BLACK)
    reset_btn_width, reset_btn_height = sidebar.draw_button(WINDOW, 'RESET', RED)

    pygame.display.update()

    while running:
        clock.tick(FPS)  # set game speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            # when user clicks the mouse
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # user clicks on a square in the puzzle grid
                if mouse_pos[0] <= WIDTH and mouse_pos[1] <= HEIGHT:
                    coords = user.get_coords_from_mouse(mouse_pos)
                    user.draw_path(WINDOW, coords)
                    pygame.display.update()

                # user clicks on 'verify solution' button
                if (verify_btn_width[0] <= mouse_pos[0] <= verify_btn_width[1] and 
                        verify_btn_height[0] <= mouse_pos[1] <= verify_btn_height[1]):
                    print(verify_solution(user.path, board))

                # user clicks on the 'reset' button
                if (reset_btn_width[0] <= mouse_pos[0] <= reset_btn_width[1] and 
                        reset_btn_height[0] <= mouse_pos[1] <= reset_btn_height[1]):
                    # reset board and user solution
                    board.draw_board(WINDOW)
                    user.clear_user_path()
                    pygame.display.update()
                    
    pygame.quit()


if __name__ == "__main__":
    main()
