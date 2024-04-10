import math
import random

import pygame

from .Paths import Paths
from .Enemy import Enemy

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
FPS = 30
AMPLITUDE = 10
FREQUENCY = 0.005

class Blue_Enemy(Enemy):
    def __init__(self):
        super().__init__(2, 30)
        self.surf = pygame.image.load(Paths().select_sprite("blue_1_right.png")).convert_alpha()
        self.size = self.surf.get_size()
        self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
        self.rect = self.image.get_rect(
            center=(                
                random.randint(5, SCREEN_WIDTH-5),
                220,
            )
        )
        self.to_kill = False
        self.won = False

        self.sprites = {
            (0, 4): "blue_1",
            (5, 9): "blue_2",
            (10, 14): "blue_1",
            (15, 19): "blue_3",
        }

    def update(self, bullets):
        time_elapsed = pygame.time.get_ticks()
        self.rect.y += self.speed
        x = AMPLITUDE * math.sin(FREQUENCY * time_elapsed)
        self.rect.x += x
        if pygame.sprite.spritecollideany(self, bullets):
            self.to_kill = True
        if self.rect.bottom > SCREEN_HEIGHT + 50:
            self.won = True

        self.frame = (self.frame + 20 + 1) % 20

        if x > 0:
            direction = "_right.png"
        else:
            direction = "_left.png"

        self.surf = self.change_sprite_depending_on_frame(
            self.sprites,
            direction
        )
        self.size = self.surf.get_size()
        self.image = pygame.transform.scale(
            self.surf,
            (int(self.size[0]*2), int(self.size[1]*2))
        )

    def change_sprite_depending_on_frame(self, sprites, direction):
        for frame_range, sprite in sprites.items():
            if frame_range[0] <= self.frame <= frame_range[1]:
                return pygame.image.load(
                        Paths().select_sprite(sprite + direction)
                ).convert_alpha()
