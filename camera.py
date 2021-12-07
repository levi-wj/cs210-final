from pygame.math import Vector2 as v2

class Camera:
    def __init__(self, bottomright) -> None:
        self._pos = v2(0, 0)
        self._delay = 10
        self._bounds = bottomright 

    def move_towards(self, target):
        self._pos.x += (target.x - self._pos.x) / self._delay
        self._pos.y += (target.y - self._pos.y) / self._delay