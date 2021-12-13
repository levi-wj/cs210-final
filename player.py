from enum import Enum 
import pygame
from spritesheet import Spritesheet
from pygame.locals import *
from pygame.math import Vector2 as v2
from conf import Conf

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups) -> None:
        self._layer = 10
        super().__init__(groups)

        self._animation = Spritesheet('sprites\\char\\archer.xml', scale=80)
        self._animation.play('arch_idle')
        self.image = self._animation.image()
        self.rect = self.image.get_rect()
        self.rect.bottomleft = pos

        self._pos = pos
        self._vel = v2(0, 0)
        self._acc = v2(0, 0)
        self._speed = 2.5
        self._grounded = False
        self._jump_power = 15
        self._anim_state = AnimState.IDLE

    def handle_input(self, keys):
        self._acc = v2(0, 0)
        new_state = AnimState.IDLE
        if keys[K_a]:
            self._acc.x = -self._speed
            new_state = AnimState.WALK
        if keys[K_d]:
            self._acc.x = self._speed
            new_state = AnimState.WALK
        if keys[K_w]:
            if self._grounded:
                self._acc.y = -self._jump_power
                new_state = AnimState.JUMP
        
        self._anim_state = new_state

    def check_collision(self, tilesgroup):
        col = pygame.sprite.spritecollide(self, tilesgroup, False)
        self._grounded = (col != [])
        if self._grounded:
            self._pos.y = col[0].rect.top

    def do_physics(self):
        self._acc.x += self._vel.x * Conf.FRIC
        if not self._grounded:
            self._acc.y += Conf.GRAV
        else:
            self._vel.y = 0
            self._acc.y = 0
        self._vel += self._acc
        self._pos += self._vel + 0.5 * self._acc
        
        self.rect.bottomleft = self._pos

    def animate(self):
        if self._anim_state == AnimState.WALK:
            self._animation.play('arch_walk')
        elif self._anim_state == AnimState.IDLE:
            self._animation.play('arch_idle')

        self.image = self._animation.image()
        # Flip to face the direction that we're moving
        if (self._vel.x > 0 and self.image.get_rect().width < 0) or (self._vel.x < 0 and self.image.get_rect().width > 0):
            self.image = pygame.transform.flip(self.image, True, False)

    def update(self, keys, tilesgroup):
        self.handle_input(keys)
        self.check_collision(tilesgroup)
        self.do_physics()
        self.animate()

    def render(self, display, offset):
        display.blit(self.image, (self.rect.x - offset.x, self.rect.y - offset.y))

class AnimState(Enum):
    IDLE = 0
    WALK = 1
    JUMP = 2
    SHOOT = 3