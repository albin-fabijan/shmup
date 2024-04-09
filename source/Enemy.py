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
