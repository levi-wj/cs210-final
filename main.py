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
    foreground = pygame.sprite.LayeredUpdates()

    cam = Camera(v2(Conf.WIDTH, Conf.HEIGHT))
    Background([
        'sprites\\tiles\\BG1.png',
        'sprites\\tiles\\BG2.png',
        'sprites\\tiles\\BG3.png'],
        v2(Conf.WIDTH, Conf.HEIGHT),
        cam, background)
    Level('levels\\1.csv', 'sprites\\tiles\\tileset.xml', interactables)
    player = Player(v2(10, 100), foreground)

    foreground.add(interactables)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        foreground.update(keys, interactables)
        background.update(keys)
        cam.move_towards(player._pos)

        display.fill((0, 0, 0))
        for sprite in background:
            display.blit(sprite.image, sprite.rect)
        for sprite in foreground:
            offset = cam.get_drawing_offset()
            display.blit(sprite.image, (sprite.rect.x - offset.x, sprite.rect.y - offset.y))

        pygame.display.update()
        clock.tick(Conf.FPS)
        # print(clock.get_fps())

if __name__ == "__main__":
    main()