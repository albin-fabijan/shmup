import pygame
import random
from .Paths import Paths
from .Enemy import Enemy

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
FPS = 30

class White_Enemy(Enemy):
    def __init__(self):
        super().__init__(2, 10)
        self.surf = pygame.image.load(Paths().select_sprite("white_1.png")).convert_alpha()
        self.size = self.surf.get_size()
        self.image = pygame.transform.scale(self.surf, (int(self.size[0]*2), int(self.size[1]*2)))
        self.rect = self.image.get_rect(
            center=(                
                random.randint(5, SCREEN_WIDTH-5),
                220,
            )
        )
        self.to_kill = False
        self.won = False

        self.sprites = {
            (0, 4): "white_1.png",
            (5, 9): "white_2.png",
            (10, 14): "white_1.png",
            (15, 19): "white_3.png",
        }

    def update(self, bullets):
        self.rect.y += self.speed
        if pygame.sprite.spritecollideany(self, bullets):
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
