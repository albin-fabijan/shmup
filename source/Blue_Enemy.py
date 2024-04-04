import pygame
import random
import math
from .paths import Paths

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
FPS = 30
AMPLITUDE = 10
FREQUENCY = 0.005

class Blue_Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Blue_Enemy, self).__init__()
        self.surf = pygame.image.load(Paths().select_sprite("white_1.png")).convert_alpha()
        self.size = self.surf.get_size()
        self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
        self.rect = self.image.get_rect(
            center=(                
                random.randint(5, SCREEN_WIDTH-5),
                random.randint(-100,-20),
            )
        )
        self.speed = 2
        self.to_kill = False
        self.frame = 0
        self.points = 30

    def update(self, bullets):
        time_elapsed = pygame.time.get_ticks()
        self.rect.y += self.speed
        x = AMPLITUDE * math.sin(FREQUENCY * time_elapsed)
        self.rect.x += x
        if pygame.sprite.spritecollideany(self, bullets):
            self.to_kill = True
        if self.rect.bottom > SCREEN_HEIGHT + 50:
            self.kill()
        
        if (x > 0) :
            if (self.frame < 5) :
                self.surf = pygame.image.load(Paths().select_sprite("blue_right_1.png")).convert_alpha()
                self.size = self.surf.get_size()
                self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
                self.frame += 1
            elif (self.frame < 10) :
                self.surf = pygame.image.load(Paths().select_sprite("blue_right_2.png")).convert_alpha()
                self.size = self.surf.get_size()
                self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
                self.frame += 1
            elif (self.frame < 15) :
                self.surf = pygame.image.load(Paths().select_sprite("blue_right_1.png")).convert_alpha()
                self.size = self.surf.get_size()
                self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
                self.frame += 1
            elif (self.frame < 20) :
                self.surf = pygame.image.load(Paths().select_sprite("blue_right_3.png")).convert_alpha()
                self.size = self.surf.get_size()
                self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
                self.frame += 1
            else :
                self.frame = 0
        else :
            if (self.frame < 5) :
                self.surf = pygame.image.load(Paths().select_sprite("blue_left_1.png")).convert_alpha()
                self.size = self.surf.get_size()
                self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
                self.frame += 1
            elif (self.frame < 10) :
                self.surf = pygame.image.load(Paths().select_sprite("blue_left_2.png")).convert_alpha()
                self.size = self.surf.get_size()
                self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
                self.frame += 1
            elif (self.frame < 15) :
                self.surf = pygame.image.load(Paths().select_sprite("blue_left_1.png")).convert_alpha()
                self.size = self.surf.get_size()
                self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
                self.frame += 1
            elif (self.frame < 20) :
                self.surf = pygame.image.load(Paths().select_sprite("blue_left_3.png")).convert_alpha()
                self.size = self.surf.get_size()
                self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
                self.frame += 1
            else :
                self.frame = 0