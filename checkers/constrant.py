import pygame

WIDTH, HEIGHT = 700, 700
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

RED = (68, 63, 66)
BLUE = (0, 0, 255)
WHITE = (226, 209, 183)
BLACK = (139, 91, 59)
BLACK2 = (161, 116, 85)
GRAY = (128, 128, 128)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown3.png'), (WIDTH // 20, HEIGHT // 20))
