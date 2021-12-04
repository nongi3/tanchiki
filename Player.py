from abc import ABC

from MoveableObject import MovableObject


class Player(MovableObject, ABC):
    def __init__(self, sprites, speed=0, x=10, y=10):
        super().__init__(sprites, x, y, speed)
        self.width = 40
        self.height = 40

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

