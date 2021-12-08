from pygame.math import Vector2 as v2

class Camera:
    def __init__(self, bottomright) -> None:
        self._delay = v2(6, 20)
        self._bounds = bottomright 
        self._offset = v2(300, self._bounds.y / 1.4)
        self.pos = v2(self._offset.x, self._offset.y)

    def move_towards(self, target):
        self.pos.x += (target.x - self.pos.x) / self._delay.x
        self.pos.y += (target.y - self.pos.y) / self._delay.y

    def get_drawing_offset(self):
        return v2(self.pos.x - self._offset.x, self.pos.y - self._offset.y)