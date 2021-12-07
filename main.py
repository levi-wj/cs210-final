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


def main():
    pygame.init()
    clock = pygame.time.Clock()

    display = pygame.display.set_mode((Conf.WIDTH, Conf.HEIGHT))
    pygame.display.set_caption(Conf.APPTITLE)

    background = pygame.sprite.LayeredUpdates()
    interactables = pygame.sprite.LayeredUpdates()
    player = pygame.sprite.LayeredUpdates()
    all_sprites = pygame.sprite.LayeredUpdates()

    cam = Camera(v2(Conf.WIDTH, Conf.HEIGHT))
    Background([
        'sprites\\tiles\\BG1.png',
        'sprites\\tiles\\BG2.png',
        'sprites\\tiles\\BG3.png'],
        v2(Conf.WIDTH, Conf.HEIGHT),
        cam, (background, all_sprites))
    Level('levels\\1.csv', 'sprites\\tiles\\tileset.xml', (interactables, all_sprites))
    player = Player(v2(10, 100), (player, all_sprites))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        all_sprites.update(keys, interactables)
        cam.move_towards(player._pos)

        display.fill((0, 0, 0))
        all_sprites.draw(display)

        pygame.display.update()
        clock.tick(Conf.FPS)
        # print(clock.get_fps())

if __name__ == "__main__":
    main()