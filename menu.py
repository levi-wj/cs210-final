import pygame
from pygame.math import Vector2 as v2
from conf import Conf

class Menu():
    def __init__(self, display, startgame, quitgame, groups) -> None:
        self._font_size = 70
        self._font = pygame.font.Font('sprites\\block.ttf', self._font_size)
        display.blit(self._font.render('ARCHER', False, (255, 255, 255)), (Conf.WIDTH / 2 - (3 * (self._font_size - 5)), 50)) 
        Button(v2(Conf.WIDTH / 2, Conf.HEIGHT / 2), v2(200, 80), 'Start', (150, 255, 255), (180, 255, 255), startgame, groups)
        Button(v2(Conf.WIDTH / 2, (Conf.HEIGHT / 2) + 120), v2(200, 80), 'Quit', (255, 100, 100), (255, 130, 130), quitgame, groups)


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, size, text, color, highlight_color, onclick, groups):
        super().__init__(groups)
        self._pos = pos
        self._size = size
        self._text = text
        self._color = color
        self._highlight_color = highlight_color
        self._onclick = onclick
        self.surf = pygame.Surface(size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect(center=pos)

    def check_bounds(self, point):
        return self._pos.x - self._size.x / 2 <= point.x <= self._pos.x + self._size.x / 2 \
        and self._pos.y - self._size.y / 2 <= point.y <= self._pos.y + self._size.y / 2

    def update(self, mousepos, click):
        if self.check_bounds(mousepos):
            self.surf.fill(self._highlight_color)
            if click:
                self._onclick()
        else:
            self.surf.fill(self._color)