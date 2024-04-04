import pygame
import random
from source.paths import Paths
from source.Player import Player
from source.Bullet import Bullet
from source.White_Enemy import White_Enemy
from source.Green_Enemy import Green_Enemy
from source.Yellow_Enemy import Yellow_Enemy
from source.Blue_Enemy import Blue_Enemy
from source.Violet_Enemy import Violet_Enemy
from source.Red_Enemy import Red_Enemy
from source.Enemy_Bullet import Enemy_Bullet

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
FPS = 15

# Initialize pygame
clock = pygame.time.Clock()
pygame.init()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
bg = pygame.image.load(Paths().select_sprite("background.png"))
bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

# Create a custom event for adding a new enemy
ADDBULLET = pygame.USEREVENT + 1
ADDENEMY = pygame.USEREVENT + 2
ADDENEMYBULLET = pygame.USEREVENT + 3
pygame.time.set_timer(ADDBULLET, 300)
pygame.time.set_timer(ADDENEMY, 1000)
pygame.time.set_timer(ADDENEMYBULLET, 1500)

# Instantiate player. Right now, this is just a rectangle.
player = Player()

# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering
enemies = pygame.sprite.Group()
yellows = pygame.sprite.Group()
violets = pygame.sprite.Group()
reds = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemy_bullets = pygame.sprite.Group()
player_group = pygame.sprite.Group()
player_group.add(player) 
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

# Variable to keep the main loop running
running = True

bullets_shot = 0
points = 0

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
            # rand = random.randint(1,30)
            # if (rand <= 5) :
            #     new_enemy = White_Enemy()
            #     enemies.add(new_enemy)
            #     all_sprites.add(new_enemy)
            # elif (rand <= 10) :
            #     new_enemy = Red_Enemy()
            #     enemies.add(new_enemy)
            #     all_sprites.add(new_enemy)
            # elif (rand <= 15) :
            #     new_enemy = Yellow_Enemy()
            #     enemies.add(new_enemy)
            #     yellows.add(new_enemy)
            #     all_sprites.add(new_enemy)
            # elif (rand <= 17) :
            #     new_enemy = Green_Enemy()
            #     enemies.add(new_enemy)
            #     all_sprites.add(new_enemy)
            # elif (rand <= 19) :
            #     new_enemy = Blue_Enemy()
            #     enemies.add(new_enemy)
            #     all_sprites.add(new_enemy)
            # else :
            #     new_enemy = Violet_Enemy()
            #     enemies.add(new_enemy)
            #     violets.add(new_enemy)
            #     all_sprites.add(new_enemy)

            new_enemy = Red_Enemy()
            enemies.add(new_enemy)
            reds.add(new_enemy)
            all_sprites.add(new_enemy)

        elif event.type == ADDBULLET:
            # Create the new enemy and add it to sprite groups
            if (player.shoot) :
                new_bullet = Bullet(player, 0)
                bullets.add(new_bullet)
                all_sprites.add(new_bullet)
                bullets_shot += 1

        elif event.type == ADDENEMYBULLET:
            for enemy in violets :
                new_bullet = Enemy_Bullet(enemy, 1)
                enemy_bullets.add(new_bullet)
                all_sprites.add(new_bullet)

    # Get the set of keys pressed and check for user input
    pressed_keys = pygame.key.get_pressed()

    # Fill the screen with black
    screen.blit(bg, (0,0))

    # Update the player sprite based on user keypresses
    player.update(pressed_keys, enemy_bullets)

    # Update enemy position
    enemies.update(bullets)

    bullets.update(enemies)
    enemy_bullets.update(player_group)

    # Draw all sprites
    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)

    # Check if any enemies have collided with the player
    if pygame.sprite.spritecollideany(player, enemies):
        # If so, then remove the player and stop the loop
        player.kill()
        running = False

    for yellow in yellows :
        if (yellow.hurt) :
            yellow.health -= 1
            yellow.hurt = False
            for bullet in bullets :
                if (bullet.to_kill) :
                    bullet.kill()

    for red in reds :
        if (red.to_kill) :
            new_bullet = Bullet(red, 0)
            bullets.add(new_bullet)
            all_sprites.add(new_bullet)
            new_bullet = Bullet(red, 1)
            bullets.add(new_bullet)
            all_sprites.add(new_bullet)
            new_bullet = Bullet(red, 2)
            bullets.add(new_bullet)
            all_sprites.add(new_bullet)
            new_bullet = Bullet(red, 3)
            bullets.add(new_bullet)
            all_sprites.add(new_bullet)

    for enemy in enemies :
        if enemy.rect.bottom > SCREEN_HEIGHT:
            player.kill()
            running = False
        if (enemy.to_kill) :
            points += enemy.points
            enemy.kill()
            for bullet in bullets :
                if (bullet.to_kill) :
                    bullet.kill()

    if (player.to_kill) :
        player.kill()
        running = False

    # Update the display
    pygame.display.flip()
    clock.tick(FPS)

print("Bullets shot : " + str(bullets_shot))
print("Score : " + str(points)) 