import csv
from tile import Tile
from spritesheet import Spritesheet
from pygame.math import Vector2 as v2

'''
    Class: map
    Description: this class loads map data from an image and generates the corresponding entities 
'''
class Level:
    def __init__(self, mappath, tilespath, groups) -> None:
        self._tilesize = 32
        self._lvldata = self.read_lvldata(mappath)
        self._tiles = Spritesheet(tilespath, scale=self._tilesize)
        self._groups = groups
        self._entities = self.create_entities()
    
    def read_lvldata(self, mappath):
        with open(mappath, 'r') as csvfile:
            reader = csv.reader(csvfile)
            return list(reader)

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
                            self._groups
                        )
                    )
        return entities
