import pygame
import random
from .Paths import Paths
from .Enemy import Enemy

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
FPS = 30

class Violet_Enemy(Enemy):
    def __init__(self):
        super(Violet_Enemy, self).__init__()
        self.surf = pygame.image.load(Paths().select_sprite("violet_1.png")).convert_alpha()
        self.size = self.surf.get_size()
        self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
        self.rect = self.image.get_rect(
            center=(                
                random.randint(5, SCREEN_WIDTH-5),
                220,
            )
        )
        self.speed = 2
        self.to_kill = False
        self.frame = 0
        self.create_bullet = False
        self.bullets = []
        self.points = 30
        self.won = False

    def update(self, bullets):
        self.create_bullet = False
        self.rect.y += self.speed
        if (self.rect.y%100 == 0) :
            self.create_bullet = True
        if pygame.sprite.spritecollideany(self, bullets):
            self.to_kill = True
        if self.rect.bottom > SCREEN_HEIGHT + 50:
            self.won = True
        
        if (self.frame < 5) :
            self.surf = pygame.image.load(Paths().select_sprite("violet_1.png")).convert_alpha()
            self.size = self.surf.get_size()
            self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
            self.frame += 1
        elif (self.frame < 10) :
            self.surf = pygame.image.load(Paths().select_sprite("violet_2.png")).convert_alpha()
            self.size = self.surf.get_size()
            self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
            self.frame += 1
        elif (self.frame < 15) :
            self.surf = pygame.image.load(Paths().select_sprite("violet_1.png")).convert_alpha()
            self.size = self.surf.get_size()
            self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
            self.frame += 1
        elif (self.frame < 20) :
            self.surf = pygame.image.load(Paths().select_sprite("violet_3.png")).convert_alpha()
            self.size = self.surf.get_size()
            self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
            self.frame += 1
        else :
            self.frame = 0
