import pygame

from .Paths import Paths
from .Scene import Scene

class GameOver(Scene):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.initialization()

    def initialization(self):
        self.running = True
        self.background = pygame.image.load(
            Paths().select_sprite("background-menu.png")
        )
        self.background = pygame.transform.scale(
                self.background,
                (self.window.SCREEN_WIDTH, self.window.SCREEN_HEIGHT)
        )

    def update_internal_variables(self):
        ...

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def display(self):
        if not self.running:
            return

        self.window.screen.blit(self.background, (0,0))
