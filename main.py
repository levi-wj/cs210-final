'''
Description:
    This main file handles the game loops and state

OOP Principles Used:
  Encapsulation

Reasoning:
    This file uses encapsulation because all the details of the game are handled in other classes
'''


from os import curdir
import sys
import pygame
from pygame.math import Vector2 as v2
from camera import Camera
from conf import Conf
from player import Player
from level import Level 
from background import Background
from menu import Menu
from leveleditor import LevelEditor


class Main():
    def __init__(self):
        pygame.init()
        self._clock = pygame.time.Clock()
        self._display = pygame.display.set_mode((Conf.WIDTH, Conf.HEIGHT))
        self._curlevel = 1
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
        self.clear_graphics()
        click = False
        for sprite in self._background:
            self._display.blit(sprite.image, sprite.rect)
        Menu(self._display, lambda: self.start_level(self._curlevel), self.start_leveleditor, pygame.quit, self._foreground)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                click = event.type == pygame.MOUSEBUTTONDOWN

            mouse = pygame.mouse.get_pos()

            for sprite in self._foreground:
                sprite.update(v2(mouse[0], mouse[1]), click)
                sprite.render(self._display, None)

            pygame.display.update() 


    def start_leveleditor(self):
        self.clear_graphics()
        click = False 

        Player(v2(0, 360), None, self._foreground)
        leveledit = LevelEditor(self.start_menu, self._cam, self._foreground)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONUP:
                    click = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    click = True

            mousepos = pygame.mouse.get_pos()

            keys = pygame.key.get_pressed()
            leveledit.update(keys, v2(mousepos[0], mousepos[1]), click)
            self._cam.move(keys)

            offset = self._cam.get_drawing_offset()
            
            for sprite in self._background:
                sprite.render(self._display, offset)
            for sprite in self._foreground:
                sprite.render(self._display, offset)

            pygame.display.update()
            self._clock.tick(Conf.FPS)


    def start_level(self, levelname):
        self.clear_graphics()

        Level('levels\\' + str(levelname) + '.csv', 'sprites\\tiles\\tileset.xml', (self._interactables, self._foreground))
        player = Player(v2(0, 360), self.next_level, self._foreground)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            keys = pygame.key.get_pressed()
            player.update(keys, self._interactables)
            self._background.update()
            self._cam.move_towards(player._pos)

            for sprite in self._background:
                self._display.blit(sprite.image, sprite.rect)
            for sprite in self._foreground:
                offset = self._cam.get_drawing_offset()
                sprite.render(self._display, offset)

            pygame.display.update()
            self._clock.tick(Conf.FPS)
            # print(clock.get_fps())

    
    def next_level(self):
        self._curlevel += 1
        if self._curlevel < 4:
            self.start_level(self._curlevel)
        else:
            self.start_menu


if __name__ == "__main__":
    Main()