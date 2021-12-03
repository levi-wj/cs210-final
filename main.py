import sys
import pygame
from pygame.math import Vector2 as v2
from conf import Conf
from player import Player
from level import Level

def main():
    pygame.init()
    clock = pygame.time.Clock()

    display = pygame.display.set_mode((Conf.WIDTH, Conf.HEIGHT))
    pygame.display.set_caption(Conf.APPTITLE)

    all_sprites = pygame.sprite.LayeredUpdates()
    level_sprites = pygame.sprite.LayeredUpdates()

    Level('levels\\1.csv', 'sprites\\tiles\\tileset.xml', (level_sprites, all_sprites))

    all_sprites.add(Player(v2(Conf.WIDTH/2, Conf.HEIGHT/2)))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        all_sprites.update(keys, level_sprites)

        display.fill((0, 0, 0))
        all_sprites.draw(display)

        pygame.display.update()
        clock.tick(Conf.FPS)

if __name__ == "__main__":
    main()