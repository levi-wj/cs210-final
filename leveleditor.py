import pygame
import csv
from pygame.math import Vector2 as v2
from pygame.locals import *
from level import Level, Tile
from menu import Button
from conf import Conf

class LevelEditor():
    def __init__(self, levelname, callback, rendergroup) -> None:
        self._level = Level(levelname, 'sprites\\tiles\\tileset.xml', rendergroup)
        self._curtile = 1
        self._previewTile = Tile(self._level._tiles.get_sprite(1), v2(0, 0), v2(32, 32), 5, rendergroup)
        self._spritecount = self._level._tiles.spritecount
        self._placing = False
        self._switching = False
        self._rendergroup = rendergroup
        self._filename = levelname

        Button(v2(Conf.WIDTH - 70, 25), v2(140, 50), 'EXIT', (140, 140, 210), (160, 160, 230), lambda: self.save_lvl_file(callback), rendergroup)

    def place_tile(self):
        t = self._previewTile
        Tile(t.image, t.rect.bottomleft, t.size, t.layer, self._rendergroup)
        self._level._lvldata[int((t.rect.centery / t.size.y) - 1)][int((t.rect.centerx / t.size.x) - 1)] = self._curtile

    def save_lvl_file(self, callback):
        with open(self._filename, 'w+') as lvlfile:
            csvWriter = csv.writer(lvlfile, delimiter=',')
            csvWriter.writerows(self._level._lvldata)
        callback()

    def update(self, keys, mousepos, click):
        if not self._switching:
            if keys[K_LEFT]:
                self._curtile -= 1
                if self._curtile < 0:
                    self._curtile = self._spritecount - 1
                self._previewTile.image = self._level._tiles.get_sprite(self._curtile)
            if keys[K_RIGHT]:
                self._curtile += 1
                if self._curtile > self._spritecount - 1:
                    self._curtile = 0
                self._previewTile.image = self._level._tiles.get_sprite(self._curtile)
        self._switching = (keys[K_LEFT] or keys[K_RIGHT])

        self._previewTile.setgridpos(mousepos[0], mousepos[1])

        if not self._placing and click:
            self.place_tile()
        self._placing = click