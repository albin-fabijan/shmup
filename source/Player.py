import pygame

from .paths import Paths

from pygame.locals import (
    K_LEFT,
    K_RIGHT,
)

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700
FPS = 30

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()    
        self.surf = pygame.image.load(Paths().select_sprite("galaga.png")).convert()
        self.size = self.surf.get_size()
        self.image = pygame.transform.scale(self.surf, (int(self.size[0]/20), int(self.size[1]/20)))
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT))

    def update(self, pressed_keys):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-10, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(10, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT