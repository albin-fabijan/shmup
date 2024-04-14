import pygame
import random
from .Paths import Paths
from .Enemy import Enemy

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
FPS = 30

class Yellow_Enemy(Enemy):
    def __init__(self):
        super().__init__(0.5, 20)
        self.surf = pygame.image.load(Paths().select_sprite("yellow_1.png")).convert_alpha()
        self.size = self.surf.get_size()
        self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
        self.y = 220
        self.rect = self.image.get_rect(
            center=(                
                random.randint(5, SCREEN_WIDTH-5),
                self.y,
            )
        )
        self.health = 3
        self.hurt = False
        self.to_kill = False
        self.won = False

        self.sprites = {
            (0, 4): "yellow_1.png",
            (5, 9): "yellow_2.png",
            (10, 14): "yellow_1.png",
            (15, 19): "yellow_3.png",
        }

    def update(self, bullets):
        self.y += self.speed
        self.rect.y = self.y
        if pygame.sprite.spritecollideany(self, bullets):
            self.hurt = True
        if (self.health <= 0):
            self.to_kill = True
        if self.rect.bottom > SCREEN_HEIGHT + 50:
            self.won = True

        self.frame = (self.frame + 20 + 1) % 20
        
        self.surf = self.change_sprite_depending_on_frame(self.sprites) 
        self.size = self.surf.get_size()
        self.image = pygame.transform.scale(
            self.surf,
            (int(self.size[0]*2), int(self.size[1]*2))
        )
