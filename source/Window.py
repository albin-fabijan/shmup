from functools import partial

import pygame

from .Game import Game
from .GameOver import GameOver
from .Upgrades import Upgrades

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

        self.current_scene = Game(
            self,
            3,
            ["W", "W", "W", "W"],
            1,
            0.5,
            1,
        )

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
            if next_scene is None:
                self.running = False
                break

            match next_scene["scene_name"]:
                case "Game":
                    self.current_scene = Game(
                            self,
                            next_scene["boat_number"],
                            next_scene["enemy_types"],
                            next_scene["bullet_fire_rate_divisor"],
                            next_scene["bullet_size_multiplier"],
                            next_scene["bullet_speed_multiplier"],
                    )
                case "GameOver":
                    self.current_scene = GameOver(self, next_scene["score"])
                case "Upgrades":
                    self.current_scene = Upgrades(
                        self,
                        next_scene["score"],
                        next_scene["bullet_fire_rate_divisor"],
                        next_scene["bullet_size_multiplier"],
                        next_scene["bullet_speed_multiplier"],
                    )
