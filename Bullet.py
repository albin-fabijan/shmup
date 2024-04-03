import pygame

class Bullet(pygame.sprite.Sprite):
    def __init__(self, player):
        super(Bullet, self).__init__()    
        self.surf = pygame.image.load("bullet.png").convert()
        self.size = self.surf.get_size()
        self.image = pygame.transform.scale(self.surf, (int(self.size[0]/5), int(self.size[1]/5)))
        self.rect = self.image.get_rect(center=(player.rect.x+25, player.rect.y))
        self.speed = -10
        self.to_kill = False

    # Move the sprite based on user keypresses
    def update(self, enemies):
        self.rect.y += self.speed
        if pygame.sprite.spritecollideany(self, enemies):
            self.to_kill = True
        if self.rect.bottom < -10:
            self.kill()