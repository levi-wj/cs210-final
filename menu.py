import pygame
from pygame.math import Vector2 as v2
from conf import Conf

class Menu():
    def __init__(self, display, startgame, leveleditor, quitgame, groups) -> None:
        self._title_size = 70
        self._font = pygame.font.Font('sprites\\block.ttf', self._title_size)
        display.blit(self._font.render('ARCHER', False, (255, 255, 255)), (Conf.WIDTH / 2 - (3 * (self._title_size - 5)), 50)) 
        Button(v2(Conf.WIDTH / 2, (Conf.HEIGHT / 2) - 40), v2(200, 80), 'START', (150, 220, 150), (160, 230, 160), startgame, groups)
        Button(v2(Conf.WIDTH / 2, (Conf.HEIGHT / 2) + 50), v2(200, 80), 'EDITOR', (80, 80, 220), (100, 100, 240), leveleditor, groups)
        Button(v2(Conf.WIDTH / 2, (Conf.HEIGHT / 2) + 140), v2(200, 80), 'QUIT', (220, 50, 50), (240, 70, 70), quitgame, groups)


class Button(pygame.sprite.Sprite):
    def __init__(self, pos, size, text, color, highlight_color, onclick, groups):
        self._layer = 100
        super().__init__(groups)
        self._pos = pos
        self._size = size
        self._color = color
        self._highlight_color = highlight_color
        self._onclick = onclick
        self._font_size = 30
        self._font = pygame.font.Font('sprites\\block.ttf', self._font_size)
        self._text = self._font.render(text, False, (255, 255, 255))
        self.surf = pygame.Surface(size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect(center=pos)

        textw, texth = self._font.size(text)
        self._text_pos = v2(self._pos.x - (textw / 2), self._pos.y - (texth / 2))

    def check_bounds(self, point):
        return self._pos.x - self._size.x / 2 <= point.x <= self._pos.x + self._size.x / 2 \
        and self._pos.y - self._size.y / 2 <= point.y <= self._pos.y + self._size.y / 2

    def render(self, display, *args):
        display.blit(self.surf, self.rect)
        display.blit(self._text, self._text_pos)

    def update(self, mousepos, click):
        if self.check_bounds(mousepos):
            self.surf.fill(self._highlight_color)
            if click:
                self._onclick()
        else:
            self.surf.fill(self._color)

'''class InputBox:
    def __init__(self, pos, size, onsubmit):
        self.surf = pygame.Surface(size)
        self.surf.fill(color)
        self.rect = self.surf.get_rect(center=pos)
        self._text = font.render(text, False, (255, 255, 255))

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    print(self.text)
                    self.text = ''
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Re-render the text.
                self.txt_surface = FONT.render(self.text, True, self.color'''