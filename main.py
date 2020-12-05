import pygame
from constants import WIDTH, HEIGHT, WIN_WIDTH, WIN_HEIGHT, WHITE
from board import Board
from user import User

FPS = 30

# WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
WINDOW = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Pearl Puzzle")


def main():
    running = True
    clock = pygame.time.Clock()

    board = Board()
    user = User()

    board.draw(WINDOW)
    pygame.display.update()

    while running:
        clock.tick(FPS)  # set game speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                # if user clicks on a square in the puzzle grid
                if mouse_pos[0] <= WIDTH and mouse_pos[1] <= HEIGHT:
                    coords = user.get_coords_from_mouse(mouse_pos)
                    user.draw_path(WINDOW, coords)
                    pygame.display.update()

    print(user.path)
    pygame.quit()


if __name__ == "__main__":
    main()