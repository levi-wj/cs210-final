import csv
from pygame.math import Vector2 as v2
from pygame.locals import *
from level import Level, Tile
from menu import Button
from conf import Conf

class LevelEditor():
    def __init__(self, callback, cam, rendergroup) -> None:
        self._level = Level(None, 'sprites\\tiles\\tileset.xml', rendergroup)
        self._curtile = 1
        self._previewTile = Tile(self._level._tiles.get_sprite(1), v2(0, 0), v2(32, 32), 5, rendergroup)
        self._spritecount = self._level._tiles.spritecount
        self._placing = False
        self._switching = False
        self._rendergroup = rendergroup
        self._cam = cam
        self._exitbtn = Button(v2(80, 35), v2(140, 50), 'EXIT', (140, 140, 210), (160, 160, 230), lambda: self.save_lvl_file(callback), rendergroup)

    def place_tile(self):
        t = self._previewTile
        Tile(t.image, t.rect.bottomleft, t.size, t.layer, self._rendergroup)
        self._level._lvldata[int((t.rect.centery / t.size.y) - 1)][int((t.rect.centerx / t.size.x) - 1)] = self._curtile

    def save_lvl_file(self, callback):
        with open('levels\\1.csv', 'w', newline='') as lvlfile:
            csvWriter = csv.writer(lvlfile, delimiter=',')
            csvWriter.writerows(self._level._lvldata)
        callback()

    def update(self, keys, mousepos, click):
        if not self._switching:
            if keys[K_LEFT]:
                self._curtile -= 1
                if self._curtile < 0:
                    self._curtile = self._spritecount - 1
            if keys[K_RIGHT]:
                self._curtile += 1
                if self._curtile > self._spritecount - 1:
                    self._curtile = 0
        self._switching = (keys[K_LEFT] or keys[K_RIGHT])

        self._previewTile.setgridpos(mousepos.x, mousepos.y, self._cam.get_drawing_offset())
        self._exitbtn.update(mousepos, click)

        # Check that the tile is in the bounds of the level
        if -1 < (self._previewTile.rect.bottomleft[0] / self._previewTile.size.x) < Conf.LVLWIDTH and -1 < (self._previewTile.rect.bottomleft[1] / self._previewTile.size.y) < Conf.LVLHEIGHT:
            self._previewTile.image = self._level._tiles.get_sprite(self._curtile)
            # Check for mouseclick and make sure we're not clicking the exit button
            if not self._placing and click and not self._exitbtn.check_bounds(mousepos):
                self.place_tile()
        else:
            self._previewTile.image = self._level._tiles.get_sprite(0) 
        self._placing = click