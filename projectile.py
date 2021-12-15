'''
Description:
    The projectile class displays an image and moves it in a direction

OOP Principles Used:
     Abstraction, Inheritance 

Reasoning:
    This class uses abstraction because the concept of a projectile is very abstracted from the image and velocity attributes
    This class uses inheritance because the player inherits from the pygame sprite class
'''

import pygame
from pygame.locals import *
from pygame.math import Vector2 as v2
from conf import Conf


class Projectile(pygame.sprite.Sprite):
    def __init__(self, pos, sprite, velocity, tilesgroup, groups):
        self._layer = 15
        super().__init__(groups)
        self._name = 'projectile'
        self.image = sprite
        self.rect = self.image.get_rect()
        self.rect.bottomleft = pos
        self._collayer = tilesgroup

        self._pos = pos
        self._vel = velocity

    
    def check_col(self):
        for tile in self._collayer:
            if pygame.sprite.collide_rect(self, tile):
                if tile._name == 'assassin':
                    tile.kill()


    def update(self):
        self._pos += self._vel
        self.rect.bottomleft = self._pos


    def render(self, display, offset):
        display.blit(self.image, (self.rect.x - offset.x, self.rect.y - offset.y))