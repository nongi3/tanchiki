from win32api import GetSystemMetrics
from accessify import private
import pygame

from Player import Player
from ImageLoader import ImageLoader


class Game:
    def __init__(self):
        pygame.init()
        self.window_width = GetSystemMetrics(0)
        self.window_height = GetSystemMetrics(1)
        self.display = pygame.display.set_mode((self.window_width, self.window_height))#, flags=pygame.FULLSCREEN)
        self.image_loader = ImageLoader()
        self.player = Player(self.image_loader.get_player_images())

    @private
    def draw(self):
        self.player.draw(self.display)
        pygame.display.flip()

    @private
    def exit_commands(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    exit()

    @private
    def move(self):
        self.player.move(0.01, 0)

    def start(self):
        while True:
            self.exit_commands()
            self.draw()
            self.move()


game = Game()
game.start()
