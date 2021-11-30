from tile import Tile
from spritesheet import Spritesheet

'''
    Class: map
    Description: this class loads map data from an image and generates the corresponding entities 
'''
class Map:
    def __init__(self) -> None:
        self._img = self.load_mapimg()
        self._tiles = self.setup_tilesprites()
        self.create_entities()

    def load_mapimg(self, path):
        pass

    def setup_tilesprites(self):
        pass

    def create_entities(self):
        pass