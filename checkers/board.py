import pygame
from .constrant import BLACK, RED, ROWS, SQUARE_SIZE


class Board:
    def __init__(self):
        self.board = []
        self.selected_piece = None
        self.red_piece = self.white_piece = 12
        self.red_king = self.white_king = 0

    def draw_board(self, screen):
        screen.fill(BLACK)
        for row in range(ROWS):
            for col in range(row % 2, ROWS, 2):
                pygame.draw.rect(screen, RED, (row * SQUARE_SIZE, col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))

