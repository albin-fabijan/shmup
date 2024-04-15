import pygame
from .Paths import Paths

class Heart(pygame.sprite.Sprite):
    def __init__(self, id):
        super().__init__()
        self.surf = pygame.image.load(Paths().select_sprite("heart.png")).convert_alpha()
        self.size = self.surf.get_size()
        self.image = pygame.transform.scale(self.surf, (int(self.size[0]*5), int(self.size[1]*5)))
        self.rect = self.image.get_rect(
            center=(30+(50*id), 30)
        )        
        self.empty = False

    def update(self, empty):
        self.empty = empty
        if (self.empty) :
            self.image.set_alpha(50)
        else :
            self.image.set_alpha(128)