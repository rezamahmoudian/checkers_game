import pygame

WIDTH, HEIGHT = 700, 700
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown3.png'), (WIDTH // 20, HEIGHT // 20))
