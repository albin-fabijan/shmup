import pygame
import random
from .Paths import Paths
from .Player import Player
from .Bullet import Bullet
from .WhiteEnemy import White_Enemy
from .GreenEnemy import Green_Enemy
from .YellowEnemy import Yellow_Enemy
from .BlueEnemy import Blue_Enemy
from .VioletEnemy import Violet_Enemy
from .RedEnemy import Red_Enemy
from .Ship import Ship
from .Level import Level
from .EnemyBullet import Enemy_Bullet

from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

# Define constants for the screen width and height
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
FPS = 15

class Game() :
    def run() :
        # Initialize pygame
        clock = pygame.time.Clock()
        pygame.init()

        invincibility = 2000

        # Create the screen object
        # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        bg = pygame.image.load(Paths().select_sprite("background.png"))
        bg = pygame.transform.scale(bg, (SCREEN_WIDTH, SCREEN_HEIGHT))

        # Create a custom event for adding a new enemy
        ADDBULLET = pygame.USEREVENT + 1
        ADDSHIP = pygame.USEREVENT + 2
        ADDENEMY = pygame.USEREVENT + 3
        ADDENEMYBULLET = pygame.USEREVENT + 4
        pygame.time.set_timer(ADDBULLET, 300)
        pygame.time.set_timer(ADDSHIP, 5000)
        pygame.time.set_timer(ADDENEMY, 1000)
        pygame.time.set_timer(ADDENEMYBULLET, 1500)

        # Instantiate player. Right now, this is just a rectangle.
        player = Player()

        levels = []

        ship_list = []

        for i in range(3) :
            newL = ["W", "W", "W", "W"]
            new_ship = Ship(newL)
            ship_list.append(new_ship)

        level_white = Level(ship_list)

        ship_list = []

        for i in range(5) :
            newL = ["W", "R", "G", "Y", "B", "V"]
            new_ship = Ship(newL)
            ship_list.append(new_ship)

        new_level = Level(ship_list)

        levels.append(level_white)
        levels.append(new_level)

        # Create groups to hold enemy sprites and all sprites
        # - enemies is used for collision detection and position updates
        # - all_sprites is used for rendering
        ships = pygame.sprite.Group()
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
        hits = 0
        enemy_count = 0
        win = False
        frame = 0

        # Main loop
        while running:
            frame += 1
            level = None
            for l in levels :
                if (not l.finished) :
                    level = l
                    break

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

                elif event.type == ADDSHIP:
                    if (level.ship_count > 0) :
                        new_enemy = level.ships[-level.ship_count]
                        enemies.add(new_enemy)
                        ships.add(new_enemy)
                        all_sprites.add(new_enemy)
                        level.ship_count -= 1
                        enemy_count += 1

                # Add a new enemy?
                elif event.type == ADDENEMY:
                    # Create the new enemy and add it to sprite groups
                    for ship in ships :
                        if (ship.enemy_count > 0 and not ship.move) :
                            letter = ship.enemies[-ship.enemy_count]
                            if (letter == "W") :
                                new_enemy = White_Enemy()
                                enemies.add(new_enemy)
                                all_sprites.add(new_enemy)
                                enemy_count += 1
                            elif (letter == "R") :
                                new_enemy = Red_Enemy()
                                enemies.add(new_enemy)
                                all_sprites.add(new_enemy)
                                enemy_count += 1
                            elif (letter == "Y") :
                                new_enemy = Yellow_Enemy()
                                enemies.add(new_enemy)
                                yellows.add(new_enemy)
                                all_sprites.add(new_enemy)
                                enemy_count += 1
                            elif (letter == "G") :
                                new_enemy = Green_Enemy()
                                enemies.add(new_enemy)
                                all_sprites.add(new_enemy)
                                enemy_count += 1
                            elif (letter == "B") :
                                new_enemy = Blue_Enemy()
                                enemies.add(new_enemy)
                                all_sprites.add(new_enemy)
                                enemy_count += 1
                            elif (letter == "V") :
                                new_enemy = Violet_Enemy()
                                enemies.add(new_enemy)
                                violets.add(new_enemy)
                                all_sprites.add(new_enemy)
                                enemy_count += 1
                            ship.enemy_count -= 1

                elif event.type == ADDBULLET:
                    # Create the new enemy and add it to sprite groups
                    if (player.shoot) :
                        new_bullet = Bullet(player, 0)
                        bullets.add(new_bullet)
                        all_sprites.add(new_bullet)
                        bullets_shot += 1

                elif event.type == ADDENEMYBULLET:
                    for violet in violets :
                        new_bullet = Enemy_Bullet(violet)
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
            if pygame.sprite.spritecollideany(player, enemies) and not player.invincible:
                # If so, then remove the player and stop the loop
                player.health -= 1
                hits += 1
                player.hurt = False
                player.invincible = True

            if (player.invincible) :
                if (invincibility > 0) :
                    invincibility -= 5
                else :
                    player.invincible = False
                    invincibility = 2000
                    player.hurt = False

            for ship in ships :
                if (ship.hurt) :
                    ship.health -= 1
                    ship.hurt = False
                    for bullet in bullets :
                        if (bullet.to_kill) :
                            bullet.kill()

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
                    if (not player.invincible) :
                        player.health -= 1
                        hits += 1
                        player.hurt = False
                        player.invincible = True
                    enemy.kill()
                    enemy_count -= 1
                if (enemy.to_kill) :
                    points += enemy.points
                    enemy.kill()
                    enemy_count -= 1
                    for bullet in bullets :
                        if (bullet.to_kill) :
                            bullet.kill()
                if (enemy.won) :
                    enemy.kill()
                    enemy_count -= 1

            if (player.hurt) :
                player.hurt = False
                if (not player.invincible) :
                    player.health -= 1
                    hits += 1
                    player.invincible = True
                    for bullet in enemy_bullets :
                            if (bullet.to_kill) :
                                bullet.kill()

            if (level.ship_count == 0 and enemy_count <= 0) :
                pygame.time.wait(1000)
                level.finished = True

            stop = True
            for l in levels :
                if (not l.finished) :
                    stop = False

            if (stop) :
                player.kill()
                win = True
                running = False

            if (player.to_kill) :
                player.kill()
                win = False
                running = False

            # Update the display
            pygame.display.flip()
            clock.tick(FPS)

        print("Score : " + str(points*10))
        print("Bullets shot : " + str(bullets_shot))
        print("Hits : " + str(hits))
        print("Time : " + str(frame))
        final_score = (points*10) - (bullets_shot*10) - (hits*500) - frame
        print("Final Score : " + str(final_score))
        i = 1
        win = True
        for l in levels :
            if (l.finished) :
                print("level " + str(i) + " done")
                i += 1
            else :
                win = False
        if (win) :
            print("You win")
