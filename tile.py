import pygame
from spritesheet import Spritesheet
from pygame.locals import *
from pygame.math import Vector2 as v2

class Tile(pygame.sprite.Sprite):
    def __init__(self, sprite, pos, size) -> None:
        super().__init__()
        self.surf = pygame.Surface((size.x, size.y))
        self.rect = self.surf.get_rect(center=(pos.x, pos.y))