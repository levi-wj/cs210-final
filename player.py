from enum import Enum 
import pygame
from spritesheet import Spritesheet
from pygame.locals import *
from pygame.math import Vector2 as v2
from conf import Conf

class Player(pygame.sprite.Sprite):
    def __init__(self, pos) -> None:
        super().__init__()
        self.surf = pygame.Surface((96, 96))
        self.rect = self.surf.get_rect(center=(pos.x, pos.y))
        self.setup_sprite()

        self.pos = pos
        self.vel = v2(0, 0)
        self.acc = v2(0, 0)
        self.speed = 2.5
        self.jump_speed = 2
        self.anim_state = AnimState.IDLE

    def setup_sprite(self):
        self.animation = Spritesheet('sprites\\archer.xml', scale=3)
    
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
        
        self.rect.midbottom = self.pos

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