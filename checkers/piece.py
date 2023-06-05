from .constrant import *
import pygame


class Piece:
    PADDING = 10
    BORDER = 2

    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False

        if self.color == RED:
            self.diricion = 1
        else:
            self.diricion = 0

        self.x = 0
        self.y = 0
        self.calculate_position()

    def calculate_position(self):
        self.x = self.col * SQUARE_SIZE + SQUARE_SIZE // 2
        self.y = self.row * SQUARE_SIZE + SQUARE_SIZE // 2

    def make_king(self):
        self.king = True

    def draw_pieces(self, screen):
        radius = SQUARE_SIZE // 2 - self.PADDING
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius + self.BORDER)
        pygame.draw.circle(screen, self.color, (self.x, self.y), radius)
