import pygame
from pygame.transform import scale
from spritesheet import Spritesheet
from pygame.locals import *
from pygame.math import Vector2 as v2
from conf import Conf

class Player(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.surf = pygame.Surface((64, 64))
        self.rect = self.surf.get_rect(center = (pos.x, pos.y))
        self.setup_sprite()

        self.pos = pos
        self.vel = v2(0, 0)
        self.acc = v2(0, 0)
        self.speed = .5
        self.jump_speed = 2

    def setup_sprite(self):
        self.animation = Spritesheet('sprites\\archer_sheet.xml', scale=3)
    
    def handle_input(self, keys):
        self.acc = v2(0, 0)
        if keys[K_LEFT]:
            self.acc.x = -self.speed
        if keys[K_RIGHT]:
            self.acc.x = self.speed
        if keys[K_UP]:
            self.acc.y = -self.jump_speed

    def do_physics(self):
        self.acc.x += self.vel.x * Conf.FRIC
        # self.acc.y -= Conf.GRAV
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

    def update(self, keys):
        self.handle_input(keys)
        self.do_physics()
        self.animation.play('arch_walk')
        self.rect.midbottom = self.pos