from Direction import Direction


class MovableObject:
    def __init__(self, sprites, x, y, speed):
        self.sprites = sprites
        self.x = x
        self.y = y
        self.speed = speed
        self.current_sprite = 0
        self.direction = Direction.NONE

    def get_current_sprite(self):
        return self.sprites[self.current_sprite]

    def draw(self, display):
        current_sprite = self.get_current_sprite()
        display.blit(current_sprite, (self.x, self.y))
