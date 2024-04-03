import pygame
import random

SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700
FPS = 30

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = pygame.image.load("blue_1.png").convert()
        self.size = self.surf.get_size()
        self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
        self.rect = self.image.get_rect(
            center=(                
                random.randint(5, SCREEN_WIDTH-5),
                random.randint(-100,-20),
            )
        )
        self.speed = 1
        self.to_kill = False
        self.frame = 0

    # Move the sprite based on speed
    # Remove the sprite when it passes the left edge of the screen
    def update(self, bullets):
        self.rect.y += self.speed
        if pygame.sprite.spritecollideany(self, bullets):
            self.to_kill = True
        if self.rect.bottom > SCREEN_HEIGHT + 50:
            self.kill()
        
        if (self.frame < 10) :
            self.surf = pygame.image.load("blue_1.png").convert()
            self.size = self.surf.get_size()
            self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
            self.frame += 1
        elif (self.frame < 20) :
            self.surf = pygame.image.load("blue_2.png").convert()
            self.size = self.surf.get_size()
            self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
            self.frame += 1
        elif (self.frame < 30) :
            self.surf = pygame.image.load("blue_1.png").convert()
            self.size = self.surf.get_size()
            self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
            self.frame += 1
        elif (self.frame < 40) :
            self.surf = pygame.image.load("blue_3.png").convert()
            self.size = self.surf.get_size()
            self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
            self.frame += 1
        else :
            self.frame = 0