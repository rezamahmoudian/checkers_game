import pygame
from .constrant import RED, WHITE
from .board import Board


class Game:
    def __init__(self, screen):
        self._init()
        self.screen = screen

    def update(self):
        self.board.draw(self.screen)
        pygame.display.update()

    def _init(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_moves = {}

    def reset(self):
        self._init()