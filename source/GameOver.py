import pygame

from .Scene import Scene

class GameOver(Scene):
    def __init__(self, window):
        super().__init__()
        self.window = window
        self.initialization()

    def initialization(self):
        self.running = True
        self.background_red = 192
        self.background_green = 0

    def update_internal_variables(self):
        self.background_green = (
            (self.background_green + 256 + 1) % 256
        )

    def event_loop(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            print("up")
            self.background_red = (
                (self.background_red + 256 + 1) % 256
            )
        elif keys[pygame.K_DOWN]:
            print("down")
            self.background_red = (
                (self.background_red + 256 - 1) % 256
            )

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False


    def display(self):
        self.window.screen.fill(
            (self.background_red, self.background_green, 0)
        )
