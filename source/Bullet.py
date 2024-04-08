import pygame
from .Paths import Paths

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player, direction):
        super(Bullet, self).__init__()    
        self.surf = pygame.image.load(Paths().select_sprite("bullet.png")).convert_alpha()
        self.size = self.surf.get_size()
        self.image = pygame.transform.scale(self.surf, (int(self.size[0]/2), int(self.size[1]/2)))
        self.rect = self.image.get_rect(center=(player.rect.x+10, player.rect.y))
        self.speed = -20
        self.to_kill = False
        self.direction = direction # 0 = up, 1 = down, 2 = right, 3 = left

    def update(self, enemies):
        if (self.direction == 0) :
            self.rect.y += self.speed
        elif (self.direction == 1) :
            self.rect.y -= self.speed
        elif (self.direction == 2) :
            self.rect.x += self.speed
        elif (self.direction == 3) :
            self.rect.x -= self.speed
        if pygame.sprite.spritecollideany(self, enemies):
            self.to_kill = True
        if self.rect.bottom < -10:
            self.kill()
