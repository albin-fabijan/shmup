import pygame
import random
from .paths import Paths
from .Enemy import Enemy

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
FPS = 30

class Yellow_Enemy(Enemy):
    def __init__(self):
        super(Yellow_Enemy, self).__init__()
        self.surf = pygame.image.load(Paths().select_sprite("yellow_1.png")).convert_alpha()
        self.size = self.surf.get_size()
        self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
        self.rect = self.image.get_rect(
            center=(                
                random.randint(5, SCREEN_WIDTH-5),
                220,
            )
        )
        self.speed = 1
        self.health = 3
        self.hurt = False
        self.to_kill = False
        self.frame = 0
        self.points = 20

    def update(self, bullets):
        self.rect.y += self.speed
        if pygame.sprite.spritecollideany(self, bullets):
            self.hurt = True
        if (self.health <= 0):
            self.to_kill = True
        if self.rect.bottom > SCREEN_HEIGHT + 50:
            self.kill()
        
        if (self.frame < 5) :
            self.surf = pygame.image.load(Paths().select_sprite("yellow_1.png")).convert_alpha()
            self.size = self.surf.get_size()
            self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
            self.frame += 1
        elif (self.frame < 10) :
            self.surf = pygame.image.load(Paths().select_sprite("yellow_2.png")).convert_alpha()
            self.size = self.surf.get_size()
            self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
            self.frame += 1
        elif (self.frame < 15) :
            self.surf = pygame.image.load(Paths().select_sprite("yellow_1.png")).convert_alpha()
            self.size = self.surf.get_size()
            self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
            self.frame += 1
        elif (self.frame < 20) :
            self.surf = pygame.image.load(Paths().select_sprite("yellow_3.png")).convert_alpha()
            self.size = self.surf.get_size()
            self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
            self.frame += 1
        else :
            self.frame = 0