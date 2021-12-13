import pygame
from pygame.math import Vector2 as v2

class Background():
    def __init__(self, bgimgs, screen, cam, groups):
        self._groups = groups
        self._cam = cam
        for i, img in enumerate(bgimgs):
            BGLayer(pygame.transform.scale(pygame.image.load(img).convert_alpha(), screen), screen.y, i + 1, self._cam, groups)

class BGLayer(pygame.sprite.Sprite):
    def __init__(self, sprite, screenbottom, bglayer, cam, groups):
        super().__init__(groups)

        self.image = sprite
        self.rect = self.image.get_rect()
        self._bglayer = bglayer
        self._cam = cam
        self._bottom = screenbottom 
        self._movespeed = .02

    def render(self, display, offset):
        display.blit(self.image, v2(offset.x * self._bglayer * self._movespeed * -1, 0))