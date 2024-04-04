import pygame
from .paths import Paths

class Enemy_Bullet(pygame.sprite.Sprite):
    def __init__(self, player, goes_up):
        super(Enemy_Bullet, self).__init__()    
        self.surf = pygame.image.load(Paths().select_sprite("bullet.png")).convert_alpha()
        self.size = self.surf.get_size()
        self.image = pygame.transform.scale(self.surf, (int(self.size[0]/2), int(self.size[1]/2)))
        self.rect = self.image.get_rect(center=(player.rect.x+10, player.rect.y))
        self.speed = -20
        self.to_kill = False
        self.goes_up = goes_up

    def update(self, enemies):
        self.rect.y -= self.speed
        if pygame.sprite.spritecollideany(self, enemies):
            self.to_kill = True