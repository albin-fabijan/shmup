import pygame
import random
from .Paths import Paths
from .Enemy import Enemy

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
FPS = 30

class Ship(Enemy):
    def __init__(self, enemies):
        super(Ship, self).__init__()
        self.surf = pygame.image.load(Paths().select_sprite("Ship.png")).convert_alpha()
        self.size = self.surf.get_size()
        self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
        self.rect = self.image.get_rect(
            center=(                
                random.randint(5, SCREEN_WIDTH-5),
                random.randint(-100,-20),
            )
        )
        self.speed = 1
        self.health = 10
        self.hurt = False
        self.to_kill = False
        self.frame = 0
        self.points = 50
        self.move = True
        self.enemies = enemies
        self.enemy_count = len(self.enemies)
        self.won = False

    def update(self, bullets):
        if (self.move) :
            self.rect.y += self.speed
        if pygame.sprite.spritecollideany(self, bullets):
            self.hurt = True
        if (self.health <= 0):
            self.to_kill = True
        if self.rect.bottom > 220:
            self.move = False
