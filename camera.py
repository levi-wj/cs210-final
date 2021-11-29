from pygame.math import Vector2 as v2

class Camera:
    def __init__(self) -> None:
        self.pos = v2(0, 0)
        self.delay = 10

    def move_towards(self, pos):
        self.x += (pos.x - self.x) / self.delay
        self.y += (pos.y - self.y) / self.delay