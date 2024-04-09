import pygame
import random
from .Scene import Scene
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

class Game(Scene):
    def __init__(self, window):
        super().__init__()
        self.window = window

    def initialization(self):
        self.invincibility = 2000

        self.bg = pygame.image.load(Paths().select_sprite("background.png"))
        self.bg = pygame.transform.scale(
                self.bg,
                (self.window.SCREEN_WIDTH, self.window.SCREEN_HEIGHT)
        )

        # Create a custom event for adding a new enemy
        self.ADDBULLET = pygame.USEREVENT + 1
        self.ADDSHIP = pygame.USEREVENT + 2
        self.ADDENEMY = pygame.USEREVENT + 3
        self.ADDENEMYBULLET = pygame.USEREVENT + 4
        pygame.time.set_timer(self.ADDBULLET, 300)
        pygame.time.set_timer(self.ADDSHIP, 5000)
        pygame.time.set_timer(self.ADDENEMY, 1000)
        pygame.time.set_timer(self.ADDENEMYBULLET, 1500)

        # Instantiate player. Right now, this is just a rectangle.
        self.player = Player()

        self.levels = []

        self.ship_list = []

        for i in range(3) :
            newL = ["W", "W", "W", "W"]
            new_ship = Ship(newL)
            self.ship_list.append(new_ship)

        level_white = Level(self.ship_list)

        self.ship_list = []

        for i in range(5) :
            newL = ["W", "R", "G", "Y", "B", "V"]
            new_ship = Ship(newL)
            self.ship_list.append(new_ship)

        new_level = Level(self.ship_list)

        self.levels.append(level_white)
        self.levels.append(new_level)

        # Create groups to hold enemy sprites and all sprites
        # - enemies is used for collision detection and position updates
        # - all_sprites is used for rendering
        self.ships = pygame.sprite.Group()
        self.enemies = pygame.sprite.Group()
        self.yellows = pygame.sprite.Group()
        self.violets = pygame.sprite.Group()
        self.reds = pygame.sprite.Group()
        self.bullets = pygame.sprite.Group()
        self.enemy_bullets = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player) 
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        # Variable to keep the main loop running
        self.running = True

        self.bullets_shot = 0
        self.points = 0
        self.hits = 0
        self.enemy_count = 0
        self.win = False
        self.frame = 0

    def run(self):
        self.initialization()
        # Main loop
        while self.running:
            self.frame += 1
            self.level = None
            for l in self.levels :
                if (not l.finished) :
                    self.level = l
                    break
            
            self.display()
            self.input_loop()

            # Get the set of keys pressed and check for user input
            pressed_keys = pygame.key.get_pressed()

            # Update the player sprite based on user keypresses
            self.player.update(pressed_keys, self.enemy_bullets)

            # Update enemy position
            self.enemies.update(self.bullets)

            self.bullets.update(self.enemies)
            self.enemy_bullets.update(self.player_group)

            # Check if any enemies have collided with the player
            if (
                pygame.sprite.spritecollideany(self.player, self.enemies)
                and not self.player.invincible
            ):
                # If so, then remove the player and stop the loop
                self.player.health -= 1
                self.hits += 1
                self.player.hurt = False
                self.player.invincible = True

            if (self.player.invincible) :
                if (self.invincibility > 0) :
                    self.invincibility -= 5
                else :
                    self.player.invincible = False
                    self.invincibility = 2000
                    self.player.hurt = False

            for ship in self.ships :
                if (ship.hurt) :
                    ship.health -= 1
                    ship.hurt = False
                    for bullet in self.bullets :
                        if (bullet.to_kill) :
                            bullet.kill()

            for yellow in self.yellows :
                if (yellow.hurt) :
                    yellow.health -= 1
                    yellow.hurt = False
                    for bullet in self.bullets :
                        if (bullet.to_kill) :
                            bullet.kill()

            for red in self.reds :
                if (red.to_kill) :
                    for i in range(0, 4):
                        new_bullet = Bullet(red, i)
                        self.bullets.add(new_bullet)
                        self.all_sprites.add(new_bullet)

            for enemy in self.enemies :
                if enemy.rect.bottom > self.window.SCREEN_HEIGHT:
                    if (not self.player.invincible) :
                        self.player.health -= 1
                        self.hits += 1
                        self.player.hurt = False
                        self.player.invincible = True
                    enemy.kill()
                    self.enemy_count -= 1
                if (enemy.to_kill) :
                    self.points += enemy.points
                    enemy.kill()
                    self.enemy_count -= 1
                    for bullet in self.bullets :
                        if (bullet.to_kill) :
                            bullet.kill()
                if (enemy.won) :
                    enemy.kill()
                    self.enemy_count -= 1

            if (self.player.hurt) :
                self.player.hurt = False
                if (not self.player.invincible) :
                    self.player.health -= 1
                    self.hits += 1
                    self.player.invincible = True
                    for bullet in self.enemy_bullets :
                            if (bullet.to_kill) :
                                bullet.kill()

            if (self.level.ship_count == 0 and self.enemy_count <= 0) :
                pygame.time.wait(1000)
                self.level.finished = True

            self.stop = True
            for l in self.levels :
                if (not l.finished) :
                    self.stop = False

            if (self.stop) :
                self.player.kill()
                self.win = True
                self.running = False

            if (self.player.to_kill) :
                self.player.kill()
                self.win = False
                self.running = False

            # Update the display
            pygame.display.flip()
            self.window.clock.tick(self.window.FPS)

        print("Score : " + str(self.points*10))
        print("Bullets shot : " + str(self.bullets_shot))
        print("Hits : " + str(self.hits))
        print("Time : " + str(self.frame))
        final_score = (
                (self.points*10)
                - (self.bullets_shot*10)
                - (self.hits*500)
                - self.frame
        )
        print("Final Score : " + str(final_score))
        self.win = True
        for i, l in enumerate(self.levels):
            if (l.finished) :
                print("level " + str(i) + " done")
            else :
                self.win = False
        if (self.win) :
            print("You win")

    def display(self):
        # Fill the screen with black
        self.window.screen.blit(self.bg, (0,0))

        # Draw all sprites
        for entity in self.all_sprites:
            self.window.screen.blit(entity.image, entity.rect)

    def input_loop(self):
        # for loop through the event queue
        for event in pygame.event.get():
            # Check for KEYDOWN event
            if event.type == KEYDOWN:
                # If the Esc key is pressed, then exit the main loop
                if event.key == K_ESCAPE:
                    self.running = False
            # Check for QUIT event. If QUIT, then set running to false.
            elif event.type == QUIT:
                self.running = False

            elif event.type == self.ADDSHIP:
                if (self.level.ship_count > 0) :
                    new_enemy = self.level.ships[-self.level.ship_count]
                    self.enemies.add(new_enemy)
                    self.ships.add(new_enemy)
                    self.all_sprites.add(new_enemy)
                    self.level.ship_count -= 1
                    self.enemy_count += 1

            # Add a new enemy?
            elif event.type == self.ADDENEMY:
                # Create the new enemy and add it to sprite groups
                for ship in self.ships :
                    if (ship.enemy_count > 0 and not ship.move) :
                        letter = ship.enemies[-ship.enemy_count]
                        if (letter == "W") :
                            new_enemy = White_Enemy()
                            self.enemies.add(new_enemy)
                            self.all_sprites.add(new_enemy)
                            self.enemy_count += 1
                        elif (letter == "R") :
                            new_enemy = Red_Enemy()
                            self.enemies.add(new_enemy)
                            self.all_sprites.add(new_enemy)
                            self.enemy_count += 1
                        elif (letter == "Y") :
                            new_enemy = Yellow_Enemy()
                            self.enemies.add(new_enemy)
                            self.yellows.add(new_enemy)
                            self.all_sprites.add(new_enemy)
                            self.enemy_count += 1
                        elif (letter == "G") :
                            new_enemy = Green_Enemy()
                            self.enemies.add(new_enemy)
                            self.all_sprites.add(new_enemy)
                            self.enemy_count += 1
                        elif (letter == "B") :
                            new_enemy = Blue_Enemy()
                            self.enemies.add(new_enemy)
                            self.all_sprites.add(new_enemy)
                            self.enemy_count += 1
                        elif (letter == "V") :
                            new_enemy = Violet_Enemy()
                            self.enemies.add(new_enemy)
                            self.violets.add(new_enemy)
                            self.all_sprites.add(new_enemy)
                            self.enemy_count += 1
                        ship.enemy_count -= 1

            elif event.type == self.ADDBULLET:
                # Create the new enemy and add it to sprite groups
                if (self.player.shoot) :
                    new_bullet = Bullet(self.player, 0)
                    self.bullets.add(new_bullet)
                    self.all_sprites.add(new_bullet)
                    self.bullets_shot += 1

            elif event.type == self.ADDENEMYBULLET:
                for violet in self.violets :
                    new_bullet = Enemy_Bullet(violet)
                    self.enemy_bullets.add(new_bullet)
                    self.all_sprites.add(new_bullet)

