import pygame
from checkers.constrant import WIDTH, HEIGHT

FPS = 60

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('checkers')


def main():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(FPS)
        pass

main()
