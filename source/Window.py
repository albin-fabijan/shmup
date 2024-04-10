import pygame

from .Game import Game

class Window:
    def __init__(self):
        self.SCREEN_WIDTH = 1000
        self.SCREEN_HEIGHT = 650
        self.FPS = 15

        self.clock = pygame.time.Clock()
        pygame.init()

        self.screen = pygame.display.set_mode(
                (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        )

        self.current_scene = Game(self)

        self.current_scene.run()
