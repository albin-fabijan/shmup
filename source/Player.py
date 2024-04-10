import pygame

from .Paths import Paths

from pygame.locals import (
    K_LEFT,
    K_RIGHT,
    K_SPACE
)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()    
        self.surf = pygame.image.load(Paths().select_sprite("cannon.png")).convert_alpha()
        self.size = self.surf.get_size()
        self.image = pygame.transform.scale(self.surf, (int(self.size[0]), int(self.size[1])))
        self.rect = self.image.get_rect(center=(SCREEN_WIDTH/2,SCREEN_HEIGHT))
        self.to_kill = False
        self.shoot = False
        self.health = 3
        self.hurt = False
        self.invincible = False

    def update(self, pressed_keys, enemy_bullets):
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-6, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(6, 0)
        if pressed_keys[K_SPACE]:
            self.shoot = True
        else :
            self.shoot = False

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

        if pygame.sprite.spritecollideany(self, enemy_bullets):
            self.hurt = True
            print("damage")
        if (self.health <= 0) :
            self.to_kill = True
