'''
Description:
    this class loads map data from an image and generates the corresponding entities 

OOP Principles Used:
  Inheritance, Abstraction, encapsulation, polymorphism

Reasoning:
  This class uses inheritance because...
  This file uses polymorphism etc....
'''


import csv
from conf import Conf
from spritesheet import Spritesheet
import pygame
from pygame.locals import *
from pygame.math import Vector2 as v2


class Level:
    def __init__(self, mappath, tilespath, groups) -> None:
        self._tilesize = 32
        self._lvldata = self.read_lvldata(mappath)
        self._tiles = Spritesheet(tilespath, scale=self._tilesize)
        self._groups = groups
        self._entities = self.create_entities()
    
    def read_lvldata(self, mappath):
        if mappath:
            with open(mappath, 'r') as csvfile:
                reader = csv.reader(csvfile)
                return list(reader)
        else:
            return [[0 for _ in range(Conf.LVLWIDTH)] for _ in range(Conf.LVLHEIGHT)]

    def create_entities(self):
        entities = []
        for i, row in enumerate(self._lvldata):
            for j, item in enumerate(row):
                if item != '0':
                    entities.append(
                        Tile(
                            self._tiles.get_sprite(item),
                            v2(j * self._tilesize, i * self._tilesize),
                            self._tilesize,
                            1,
                            self._groups)
                    )
        return entities

class Tile(pygame.sprite.Sprite):
    def __init__(self, sprite, pos, size, layer, groups) -> None:
        self._layer = layer
        super().__init__(groups)

        self.image = sprite
        self.size = size
        self.rect = self.image.get_rect()
        self.rect.bottomleft = pos

    def setgridpos(self, x, y, camoffset):
        mid = v2((x + camoffset.x) - (self.size.x / 2), (y + camoffset.y) + (self.size.y / 2))
        self.rect.bottomleft = v2(
            self.size.x * round(mid.x / self.size.x),
            self.size.y * round(mid.y / self.size.y))

    def render(self, display, offset):
        display.blit(self.image, (self.rect.x - offset.x, self.rect.y - offset.y))