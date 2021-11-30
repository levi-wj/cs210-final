from enum import Enum 
import pygame
from spritesheet import Spritesheet
from pygame.locals import *
from pygame.math import Vector2 as v2
from conf import Conf

class Player(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        self._layer = 10
        super().__init__()

        self.animation = Spritesheet('sprites\\char\\archer.xml', scale=3)
        self.animation.play('arch_idle')
        self.image = self.animation.image()
        self.rect = self.image.get_rect()

        self.pos = pos
        self.vel = v2(0, 0)
        self.acc = v2(0, 0)
        self.speed = 2.5
        self.jump_speed = 2
        self.anim_state = AnimState.IDLE

    def handle_input(self, keys):
        self.acc = v2(0, 0)
        new_state = AnimState.IDLE
        if keys[K_a]:
            self.acc.x = -self.speed
            new_state = AnimState.WALK
        if keys[K_d]:
            self.acc.x = self.speed
            new_state = AnimState.WALK
        if keys[K_w]:
            self.acc.y = -self.jump_speed
            new_state = AnimState.JUMP
        
        self.anim_state = new_state

    def do_collision(self):
        pass

    def do_physics(self):
        self.acc.x += self.vel.x * Conf.FRIC
        # self.acc.y += Conf.GRAV
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        self.rect.bottomleft = self.pos

    def animate(self):
        if self.anim_state == AnimState.WALK:
            self.animation.play('arch_walk')
        elif self.anim_state == AnimState.IDLE:
            self.animation.play('arch_idle')

        self.image = self.animation.image()
        # Flip to face the direction that we're moving
        if (self.vel.x > 0 and self.image.get_rect().width < 0) or (self.vel.x < 0 and self.image.get_rect().width > 0):
            self.image = pygame.transform.flip(self.image, True, False)

    def update(self, keys):
        self.handle_input(keys)
        self.do_collision()
        self.do_physics()
        self.animate()

class AnimState(Enum):
    IDLE = 0
    WALK = 1
    JUMP = 2
    SHOOT = 3