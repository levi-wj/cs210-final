import pygame

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

    def update(self, *args):
        self.rect.bottomleft = (self._cam.pos.x * self._bglayer * self._movespeed * -1, self._bottom)