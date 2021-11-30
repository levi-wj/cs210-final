import pygame
from spritesheet import Spritesheet
from pygame.locals import *
from pygame.math import Vector2 as v2

class Tile(pygame.sprite.Sprite):
    def __init__(self, sprite, pos, size, layer) -> None:
        self._layer = layer
        super().__init__()

        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.bottomleft = pos