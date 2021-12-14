from pygame.math import Vector2 as v2
from pygame.locals import *

class Camera:
    def __init__(self, bottomright) -> None:
        self._delay = v2(6, 20)
        self._movespeed = 10
        self._bounds = bottomright 
        self._offset = v2(300, self._bounds.y / 1.8)
        self.pos = v2(self._offset.x, self._offset.y)

    def move_towards(self, target):
        self.pos.x += (target.x - self.pos.x) / self._delay.x
        self.pos.y += (target.y - self.pos.y) / self._delay.y

    def move(self, keys):
        direction = v2(0, 0)
        if keys[K_a]:
            direction.x = -1
        if keys[K_d]:
            direction.x = 1
        if keys[K_w]:
            direction.y = -1
        if keys[K_s]:
            direction.y = 1
        
        self.pos.x += direction.x * self._movespeed
        self.pos.y += direction.y * self._movespeed

    def get_drawing_offset(self):
        return v2(self.pos.x - self._offset.x, self.pos.y - self._offset.y)