'''
Description:
    The player controller and renderer

OOP Principles Used:
     Abstraction, Inheritance

Reasoning:
    This class uses abstraction because the methods used by other classes are very simplified
    This class uses inheritance because the player inherits from the pygame sprite class
'''


from enum import Enum 
import pygame
from spritesheet import Spritesheet
from pygame.locals import *
from pygame.math import Vector2 as v2
from projectile import Projectile
from conf import Conf


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, nextlevel, groups) -> None:
        self._layer = 10
        super().__init__(groups)

        self._name = 'archer'
        self._animation = Spritesheet('sprites\\char\\archer.xml', scale=80)
        self._animation.play('arch_idle')
        self.image = self._animation.image()
        hitbox = self.image.get_rect()
        hitbox.w /= 2.5
        self.rect = hitbox 
        self.rect.bottomleft = pos
        self._hitbox_offset = 25
        self._nextlevel = nextlevel
        self._arrowimg = pygame.image.load('sprites/arrow.png').convert_alpha()
        self._shootdelay = 0
        self._projectiles = []
        self.groups = groups
        self._collayer = None

        self._startpos = pos
        self._pos = pos
        self._vel = v2(0, 0)
        self._acc = v2(0, 0)
        self._speed = 2.5
        self._grounded = False
        self._jump_power = 15
        self._anim_state = AnimState.IDLE


    def sign(self, x): 
        if x < 0:
            return -1
        else:
            return 1


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
                self._vel.y = -self._jump_power
                new_state = AnimState.JUMP
        if keys[K_SPACE]:
            self.shoot()
        
        self._anim_state = new_state


    def check_collision(self, tilesgroup):
        self._collayer = tilesgroup
        for tile in tilesgroup:
            self._grounded = tile.rect.collidepoint(self.rect.bottomleft) or tile.rect.collidepoint(self.rect.midbottom) or tile.rect.collidepoint(self.rect.bottomright)
            ceiling = tile.rect.collidepoint(self.rect.topleft) or tile.rect.collidepoint(self.rect.midtop) or tile.rect.collidepoint(self.rect.topright)
            wall = tile.rect.collidepoint(self.rect.midleft) or tile.rect.collidepoint(self.rect.midright)
            if wall:
                if tile._name == 'assassin':
                    self.pos = self._startpos
                if self._vel.x > 0:
                    self._pos.x = tile.rect.left - self.rect.w - 1
                else:
                    self._pos.x = tile.rect.right
                self._vel.x = 0
                return
            if self._grounded or ceiling:
                if tile._name == 'assassin':
                    self.pos = self._startpos
                self._vel.y = 0
                self._acc.y = 0
                if self._grounded:
                    self._pos.y = tile.rect.top
                else:
                    self._pos.y = tile.rect.bottom + self.rect.h
                break


    def do_physics(self):
        self._acc.x += self._vel.x * Conf.FRIC
        if not self._grounded:
            self._acc.y += Conf.GRAV
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

    
    def shoot(self):
        if self._shootdelay < 0:
            self._projectiles.append(Projectile(v2(self.rect.centerx, self.rect.centery), self._arrowimg, v2(15 * self.sign(self._vel.x), 0), self._collayer, self.groups))
            self._shootdelay = 3
        

    def check_win(self):
        return self._pos.x > (Conf.LVLWIDTH * 32) - 80


    def update(self, keys, tilesgroup):
        self.check_collision(tilesgroup)
        self.handle_input(keys)
        self.do_physics()
        self.animate()

        self._shootdelay -= .1
        for projectile in self._projectiles:
            projectile.update()
            if projectile._pos.x > Conf.LVLWIDTH * 32:
                self._projectiles.remove(projectile)

        if self.check_win():
            self._nextlevel()

        if self._pos.y > 3000:
            self._pos = self._startpos
            self.rect.bottomleft = self._pos


    def render(self, display, offset):
        # Draw hitbox
        # pygame.draw.rect(display, (220, 150, 150), (self.rect.left - offset.x, self.rect.top - offset.y, self.rect.w, self.rect.h))
        display.blit(self.image, (self.rect.x - offset.x - self._hitbox_offset, self.rect.y - offset.y))


class AnimState(Enum):
    IDLE = 0
    WALK = 1
    JUMP = 2
    SHOOT = 3