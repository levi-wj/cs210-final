import pygame
from pygame.locals import *
from pygame.math import Vector2 as v2

class Tile(pygame.sprite.Sprite):
    def __init__(self, sprite, pos, size, layer, groups) -> None:
        self._layer = layer
        super().__init__(groups)

        self.image = sprite
        self.size = size
        self.rect = self.image.get_rect()
        self.rect.bottomleft = pos