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
                self.window.SCREEN_HEIGHT * 0.66 - (button_dimensions // 2)
            ),
            (200, 200)
        )

        self.font = pygame.font.Font(None, 48)
        self.score_text_surface = self.font.render(
            str(self.score),
            True,
            (255, 255, 255)
        )
        self.score_text_middle = self.score_text_surface.get_width() // 2

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

        self.window.screen.blit(
            self.score_text_surface,
            (
                (self.window.SCREEN_WIDTH // 2) - self.score_text_middle,
                self.window.SCREEN_HEIGHT * 0.33
            )
        )

    def next_scene(self):
        return {
            "scene_name": "Game",
            "level_id": 1,
            "bullet_fire_rate_divisor": 1,
            "bullet_size_multiplier": 0.5,
            "bullet_speed_multiplier": 1.0,
        }
