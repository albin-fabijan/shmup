import pygame

from .Paths import Paths
from .Scene import Scene

class Upgrades(Scene):
    def __init__(
        self,
        window,
        score,
        next_level_id,
        bullet_fire_rate_divisor,
        bullet_size_multiplier,
        bullet_speed_multiplier
    ):
        super().__init__()

        self.window = window
        self.score = score
        self.next_level_id = next_level_id
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
        sprite = pygame.sprite.Sprite()
        sprite.__init__()
        sprite.surf = pygame.image.load(Paths().select_sprite("fire-rate-power-up.png")).convert_alpha()
        sprite.size = sprite.surf.get_size()
        sprite.image = pygame.transform.scale(sprite.surf, (int(sprite.size[0]*2), int(sprite.size[1]*2)))
        sprite.rect = sprite.image.get_rect(
            center=(
                self.window.SCREEN_WIDTH * 0.33,
                self.window.SCREEN_HEIGHT * 0.66
            ),
            size=(BUTTON_DIMENSIONS, BUTTON_DIMENSIONS)
        )
        self.fire_rate_button = sprite

        sprite = pygame.sprite.Sprite()
        sprite.__init__()
        sprite.surf = pygame.image.load(Paths().select_sprite("bullet-size-power-up.png")).convert_alpha()
        sprite.size = sprite.surf.get_size()
        sprite.image = pygame.transform.scale(sprite.surf, (int(sprite.size[0]*2), int(sprite.size[1]*2)))
        sprite.rect = sprite.image.get_rect(
            center=(
                self.window.SCREEN_WIDTH * 0.5,
                self.window.SCREEN_HEIGHT * 0.66
            ),
            size=(BUTTON_DIMENSIONS, BUTTON_DIMENSIONS)
        )
        self.size_button = sprite

        sprite = pygame.sprite.Sprite()
        sprite.__init__()
        sprite.surf = pygame.image.load(Paths().select_sprite("bullet-speed-power-up.png")).convert_alpha()
        sprite.size = sprite.surf.get_size()
        sprite.image = pygame.transform.scale(sprite.surf, (int(sprite.size[0]*2), int(sprite.size[1]*2)))
        sprite.rect = sprite.image.get_rect(
            center=(
                self.window.SCREEN_WIDTH * 0.66,
                self.window.SCREEN_HEIGHT * 0.66
            ),
            size=(BUTTON_DIMENSIONS, BUTTON_DIMENSIONS)
        )
        self.speed_button = sprite

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
                if self.fire_rate_button.rect.collidepoint(event.pos):
                    self.bullet_fire_rate_divisor += 0.5
                    self.running = False
                elif self.size_button.rect.collidepoint(event.pos):
                    self.bullet_size_multiplier += 0.5
                    self.running = False
                elif self.speed_button.rect.collidepoint(event.pos):
                    self.bullet_speed_multiplier += 0.5
                    self.running = False

    def display(self):
        if not self.running:
            return

        self.window.screen.blit(self.background, (0,0))

        self.window.screen.blit(self.fire_rate_button.surf, self.fire_rate_button.rect.center)
        self.window.screen.blit(self.size_button.surf, self.size_button.rect.center)
        self.window.screen.blit(self.speed_button.surf, self.speed_button.rect.center)

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
            "level_id": self.next_level_id,
            "bullet_fire_rate_divisor": self.bullet_fire_rate_divisor,
            "bullet_size_multiplier": self.bullet_size_multiplier,
            "bullet_speed_multiplier": self.bullet_speed_multiplier,
        }
