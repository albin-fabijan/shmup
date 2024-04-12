from functools import partial

import pygame

from .Game import Game
from .GameOver import GameOver

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

        self.running = True

        self.current_scene = Game(self)

    def run_current_scene(self):
        while self.running:
            while self.current_scene.running:
                self.current_scene.update_internal_variables()
                self.current_scene.event_loop()
                self.current_scene.display()

                if not self.current_scene.running:
                    break

                pygame.display.flip()
                self.clock.tick(60) 

            next_scene = self.current_scene.next_scene()
            match next_scene[0]:
                case "Game":
                    self.current_scene = Game(self)
                case "GameOver":
                    self.current_scene = GameOver(self)
