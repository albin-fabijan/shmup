import pygame
from .Paths import Paths

class Bullet(pygame.sprite.Sprite):
    def __init__(
            self,
            player,
            current_direction,
            bullet_size_multiplier,
            bullet_speed_multiplier,
        ):
        super(Bullet, self).__init__()    
        self.surf = pygame.image.load(Paths().select_sprite("bullet.png")).convert_alpha()
        self.BASE_SIZE = self.surf.get_size()
        self.image = pygame.transform.scale(
            self.surf,
            (
                int(self.BASE_SIZE[0]*bullet_size_multiplier),
                int(self.BASE_SIZE[1]*bullet_size_multiplier)
            )
        )
        self.rect = self.image.get_rect(center=(player.rect.x+10, player.rect.y))
        self.BASE_SPEED = 5
        self.speed = self.BASE_SPEED * bullet_speed_multiplier
        self.to_kill = False
        self.directions = {
            0: self._move_up,
            1: self._move_down,
            2: self._move_right,
            3: self._move_left,
        }
        self.current_direction = current_direction

    def update(self, enemies):
        self.directions[self.current_direction]()

        if pygame.sprite.spritecollideany(self, enemies):
            self.to_kill = True

        if self.rect.bottom < -10:
            self.kill()

    def _move_up(self):
        self.rect.y -= self.speed

    def _move_down(self):
        self.rect += self.speed

    def _move_right(self):
        self.rect -= self.speed

    def _move_left(self):
        self.rect += self.speed
