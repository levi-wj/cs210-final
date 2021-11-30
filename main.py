import sys
import pygame
from pygame.math import Vector2 as v2
from conf import Conf
from player import Player

def main():
    pygame.init()
    clock = pygame.time.Clock()

    display = pygame.display.set_mode((Conf.WIDTH, Conf.HEIGHT))
    pygame.display.set_caption(Conf.APPTITLE)

    player = Player(v2(Conf.WIDTH/2, Conf.HEIGHT/2))

    all_sprites = pygame.sprite.LayeredUpdates()
    all_sprites.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        all_sprites.update(keys)

        display.fill((0, 0, 0))
        all_sprites.draw(display)

        pygame.display.update()
        clock.tick(Conf.FPS)

if __name__ == "__main__":
    main()