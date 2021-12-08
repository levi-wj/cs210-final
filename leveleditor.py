import pygame
from pygame.math import Vector2 as v2
from level import Level

class LevelEditor():
    def __init__(self, levelname, rendergroup) -> None:
        self._level = Level('levels\\' + levelname, 'sprites\\tiles\\tileset.png', rendergroup)
        self._curtile = 1

    def place_tile(self, tile, pos):
        pass

    def save_lvl_file(filename):
        pass