'''
Description:
    Enemy class and sprite object

OOP Principles Used:
   Inheritance 

Reasoning:
    In this file, the enemy class inherits from the pygame sprite class
'''


import pygame
from spritesheet import Spritesheet
from pygame.locals import *
from pygame.math import Vector2 as v2
from conf import Conf


class Enemy(pygame.sprite.Sprite):
    def __init__(self, pos, groups) -> None:
        self._layer = 8
        super().__init__(groups)

        self._name = 'assassin'
        self._animation = Spritesheet('sprites\\char\\assassin.xml', scale=80)
        self._animation.play('assassin_walk')
        self.image = self._animation.image()
        self.rect = self.image.get_rect() 
        self.rect.bottomleft = pos

        self._pos = pos
        self._vel = v2(0, 0)
        self._acc = v2(0, 0)
        self._speed = 2.5


    def animate(self):
        self._animation.play('assassin_walk')
        self.image = pygame.transform.flip(self._animation.image(), True, False)

    
    def render(self, display, offset):
        self.animate()
        display.blit(self.image, (self.rect.x - offset.x, self.rect.y - offset.y))