'''
    Name: main.py
    Object oriented philosophy: 
    Purpose: Handle the main game loop
'''

import sys
import pygame
from pygame.math import Vector2 as v2
from camera import Camera
from conf import Conf
from player import Player
from level import Level
from background import Background
from menu import Menu


class Main():
    def __init__(self):
        pygame.init()
        self._clock = pygame.time.Clock()
        self._display = pygame.display.set_mode((Conf.WIDTH, Conf.HEIGHT))
        pygame.display.set_caption(Conf.APPTITLE)

        self._background = pygame.sprite.LayeredUpdates()
        self._interactables = pygame.sprite.LayeredUpdates()
        self._foreground = pygame.sprite.LayeredUpdates()

        self._cam = Camera(v2(Conf.WIDTH, Conf.HEIGHT))
        Background([
            'sprites\\tiles\\BG1.png',
            'sprites\\tiles\\BG2.png',
            'sprites\\tiles\\BG3.png'],
            v2(Conf.WIDTH, Conf.HEIGHT),
            self._cam, self._background)

        self.start_menu()


    def clear_graphics(self):
        self._interactables.empty()
        self._foreground.empty()
    

    def start_menu(self):
        for sprite in self._background:
            self._display.blit(sprite.image, sprite.rect)
        Menu(self._display, lambda: self.start_level('1'), self.start_leveleditor, pygame.quit, self._foreground)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                click = event.type == pygame.MOUSEBUTTONDOWN

            mouse = pygame.mouse.get_pos()

            for sprite in self._foreground:
                sprite.update(v2(mouse[0], mouse[1]), click)
                self._display.blit(sprite.surf, sprite.rect)
                self._display.blit(sprite.text, sprite.rect)

            pygame.display.update() 


    def start_level(self, levelname):
        self.clear_graphics()

        Level('levels\\' + str(levelname) + '.csv', 'sprites\\tiles\\tileset.xml', (self._interactables, self._foreground))
        player = Player(v2(0, 500), self._foreground)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            player.update(keys, self._interactables)
            self._background.update(keys)
            self._cam.move_towards(player._pos)

            self._display.fill((0, 0, 0))
            for sprite in self._background:
                self._display.blit(sprite.image, sprite.rect)
            for sprite in self._foreground:
                offset = self._cam.get_drawing_offset()
                self._display.blit(sprite.image, (sprite.rect.x - offset.x, sprite.rect.y - offset.y))

            pygame.display.update()
            self._clock.tick(Conf.FPS)
            # print(clock.get_fps())

    def start_leveleditor(self):
        pass

if __name__ == "__main__":
    Main()