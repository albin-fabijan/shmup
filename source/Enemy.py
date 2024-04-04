import pygame
import random
from .paths import Paths

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()

    def update(self, bullets):
        ...