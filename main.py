import pygame
from Player import Player
from Bullet import Bullet
from Enemy import Enemy

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 1100
SCREEN_HEIGHT = 700
FPS = 30

# Initialize pygame
clock = pygame.time.Clock()
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
ADDBULLET = pygame.USEREVENT + 2
pygame.time.set_timer(ADDENEMY, 1000)
pygame.time.set_timer(ADDBULLET, 1000)

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Variable to keep the main loop running
running = True

# Main loop
while running:
    # for loop through the event queue
    for event in pygame.event.get():
        # Check for KEYDOWN event
        if event.type == KEYDOWN:
            # If the Esc key is pressed, then exit the main loop
            if event.key == K_ESCAPE:
                running = False
        # Check for QUIT event. If QUIT, then set running to false.
        elif event.type == QUIT:
            running = False

        # Add a new enemy?
        elif event.type == ADDENEMY:
            # Create the new enemy and add it to sprite groups
            new_enemy = Enemy()
            enemies.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == ADDBULLET:
            # Create the new enemy and add it to sprite groups
            new_bullet = Bullet(player)
            bullets.add(new_bullet)
            all_sprites.add(new_bullet)

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Update the player sprite based on user keypresses
    player.update(pressed_keys)

    # Update enemy position
    enemies.update(bullets)

    bullets.update(enemies)

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        player.kill()
        running = False

    for enemy in enemies :
        if enemy.rect.bottom > SCREEN_HEIGHT:
            player.kill()
            running = False
        if (enemy.to_kill) :
            enemy.kill()
            for bullet in bullets :
                if (bullet.to_kill) :
                    bullet.kill()

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)