import pygame
from .constrant import RED, WHITE
from .board import Board
from main import screen


class Game:
    def __init__(self):
        self.selected = None
        self.board = Board()
        self.turn = RED
        self.valid_move = {}
        self.screen = screen

    