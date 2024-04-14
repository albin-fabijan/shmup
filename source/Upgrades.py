import pygame

from .Paths import Paths
from .Scene import Scene

class Upgrades(Scene):
    def __init__(
        self,
        window,
        score,
        bullet_fire_rate_divisor,
        bullet_size_multiplier,
        bullet_speed_multiplier
    ):
        super().__init__()

        self.window = window
        self.score = score
        self.bullet_fire_rate_divisor = bullet_fire_rate_divisor
        self.bullet_size_multiplier = bullet_size_multiplier
        self.bullet_speed_multiplier = bullet_speed_multiplier

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

        BUTTON_DIMENSIONS = 100
        self.fire_rate_button = pygame.Rect(
            (
                self.window.SCREEN_WIDTH * 0.33 - (BUTTON_DIMENSIONS // 2),
                self.window.SCREEN_HEIGHT * 0.66 - (BUTTON_DIMENSIONS // 2)
            ),
            (BUTTON_DIMENSIONS, BUTTON_DIMENSIONS)
        )
        self.size_button = pygame.Rect(
            (
                self.window.SCREEN_WIDTH * 0.5 - (BUTTON_DIMENSIONS // 2),
                self.window.SCREEN_HEIGHT * 0.66 - (BUTTON_DIMENSIONS // 2)
            ),
            (BUTTON_DIMENSIONS, BUTTON_DIMENSIONS)
        )
        self.speed_button = pygame.Rect(
            (
                self.window.SCREEN_WIDTH * 0.66 - (BUTTON_DIMENSIONS // 2),
                self.window.SCREEN_HEIGHT * 0.66 - (BUTTON_DIMENSIONS // 2)
            ),
            (BUTTON_DIMENSIONS, BUTTON_DIMENSIONS)
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
                if self.fire_rate_button.collidepoint(event.pos):
                    self.bullet_fire_rate_divisor += 0.5
                    self.running = False
                elif self.size_button.collidepoint(event.pos):
                    self.bullet_size_multiplier += 0.5
                    self.running = False
                elif self.speed_button.collidepoint(event.pos):
                    self.bullet_speed_multiplier += 0.5
                    self.running = False

    def display(self):
        if not self.running:
            return

        self.window.screen.blit(self.background, (0,0))

        pygame.draw.rect(
            self.window.screen,
            (255, 0, 0),
            self.fire_rate_button
        )
        pygame.draw.rect(
            self.window.screen,
            (0, 255, 0),
            self.size_button
        )
        pygame.draw.rect(
            self.window.screen,
            (0, 0, 255),
            self.speed_button
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
            "level_id": 2,
            "bullet_fire_rate_divisor": self.bullet_fire_rate_divisor,
            "bullet_size_multiplier": self.bullet_size_multiplier,
            "bullet_speed_multiplier": self.bullet_speed_multiplier,
        }
