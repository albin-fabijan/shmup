import pygame

from .Paths import Paths
from .Scene import Scene

class GameOver(Scene):
    def __init__(self, window, score):
        super().__init__()
        self.window = window
        self.score = score
        self.initialization()

    def initialization(self):
        print(self.score)
        self.running = True
        self.background = pygame.image.load(
            Paths().select_sprite("background-menu.png")
        )
        self.background = pygame.transform.scale(
                self.background,
                (self.window.SCREEN_WIDTH, self.window.SCREEN_HEIGHT)
        )

        button_dimensions = 200
        self.back_button = pygame.Rect(
            (
                self.window.SCREEN_WIDTH // 2 - (button_dimensions // 2),
                self.window.SCREEN_HEIGHT // 2 - (button_dimensions // 2)
            ),
            (200, 200)
        )

    def update_internal_variables(self):
        ...

    def event_loop(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                self.window.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.back_button.collidepoint(event.pos):
                    self.running = False

    def display(self):
        if not self.running:
            return

        self.window.screen.blit(self.background, (0,0))
        pygame.draw.rect(
            self.window.screen,
            (255, 0, 0),
            self.back_button
        )

    def next_scene(self):
        return {
            "scene_name": "Game",
        }
