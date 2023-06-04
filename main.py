import pygame
from checkers.constrant import WIDTH, HEIGHT
from checkers.board import Board

FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('checkers')


def main():
    run = True
    clock = pygame.time.Clock()
    board = Board()

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                pass
        board.draw_board(screen)
        pygame.display.update()

    pygame.quit()

main()
