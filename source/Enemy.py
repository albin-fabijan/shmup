import pygame
import random
from .Paths import Paths

class Enemy(pygame.sprite.Sprite):
    def __init__(self, speed, points):
        super().__init__()
        self.speed = speed
        self.points = points
        self.frame = 0

    def update(self, bullets):
        ...

    def change_sprite_depending_on_frame(self, sprites):
        for frame_range, sprite in sprites.items():
            if frame_range[0] <= self.frame <= frame_range[1]:
                return pygame.image.load(
                        Paths().select_sprite(sprite)
                ).convert_alpha()
