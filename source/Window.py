import pygame

from .Game import Game

class Window:
    def __init__(self):
        self.SCREEN_WIDTH = 1000
        self.SCREEN_HEIGHT = 650
        self.FPS = 60

        self.clock = pygame.time.Clock()
        pygame.init()

        self.screen = pygame.display.set_mode(
                (self.SCREEN_WIDTH, self.SCREEN_HEIGHT)
        )

        self.current_scene = Game(self)

    def run_current_scene(self):
        while self.current_scene.running:
            self.current_scene.update_internal_variables()
            self.current_scene.event_loop()
            self.current_scene.display()

            pygame.display.flip()
            self.clock.tick(60) 
