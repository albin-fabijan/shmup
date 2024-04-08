import pygame
import sys

class ScreenMenu:
    def __init__(self):
        self.buttons = []
        self.clock = None
        self.screen = None

    def main(self):
        self.display_windows()
        self.display_chaine()
        pygame.mixer.music.load("ost\\Moonlight Beach.mp3")
        pygame.mixer.music.play(-1)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    self.check_button_click(event.pos)

    def display_chaine(self):
        self.display_background()
        self.display_button("sprite\\button-game\\game01.png", 0.3, "game")
        self.display_button("sprite\\button-option\\option01.png", 0.45, "option")
        self.display_button("sprite\\button-leaderboard\\leaderboard01.png", 0.6, "leaderboard")
        self.display_button("sprite\\button-back\\back01.png", 0.75, "back")
        self.display_book_button()

    def display_windows(self):
        pygame.init()
        info = pygame.display.Info()
        screen_width = info.current_w
        screen_height = info.current_h
        self.screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption("Fenêtre en plein écran")
        self.clock = pygame.time.Clock()

    def display_background(self):
        background = pygame.image.load("sprite\\background-menu.png")
        background = pygame.transform.scale(background, (self.screen.get_width(), self.screen.get_height()))
        self.screen.blit(background, (0, 0))
        pygame.display.flip()

    def display_button(self, image_path, vertical_position_ratio, button_id):
        button_image = pygame.image.load(image_path)
        button_rect = button_image.get_rect()
        button_width_scaled = int(self.screen.get_width() * 0.17)
        button_height_scaled = int(button_rect.height * (button_width_scaled / button_rect.width))
        button_image_scaled = pygame.transform.scale(button_image, (button_width_scaled, button_height_scaled))
        button_x = (self.screen.get_width() - button_width_scaled) // 2
        button_y = self.screen.get_height() * vertical_position_ratio - button_height_scaled // 2
        self.screen.blit(button_image_scaled, (button_x, button_y))
        self.buttons.append((button_x, button_y, button_width_scaled, button_height_scaled, button_id))
        pygame.display.flip()

    def display_book_button(self):
        button_image = pygame.image.load("sprite\\book01.png")
        button_rect = button_image.get_rect()
        button_width_scaled = int(self.screen.get_width() * 0.12)
        button_height_scaled = int(button_rect.height * (button_width_scaled / button_rect.width))
        button_image_scaled = pygame.transform.scale(button_image, (button_width_scaled, button_height_scaled))
        button_x = self.screen.get_width() // 6
        button_y = self.screen.get_height() * 0.9 - button_height_scaled
        self.screen.blit(button_image_scaled, (button_x, button_y))
        self.buttons.append((button_x, button_y, button_width_scaled, button_height_scaled, "book"))
        pygame.display.flip()

    def check_button_click(self, pos):
        for button in self.buttons:
            button_x, button_y, button_width, button_height, button_id = button
            if button_x <= pos[0] <= button_x + button_width and button_y <= pos[1] <= button_y + button_height:
                if button_id == "game":
                    self.animated_button("sprite\\button-game\\game", 0.3)
                elif button_id == "option":
                    self.animated_button("sprite\\button-option\\option", 0.45)
                elif button_id == "leaderboard":
                    self.animated_button("sprite\\button-leaderboard\\leaderboard", 0.6)
                elif button_id == "back":
                    self.animated_button("sprite\\button-back\\back", 0.75)
                    quit()
                elif button_id == "book":
                    if not self.is_button_animating(button_id):
                        self.set_button_animating(button_id)
                    break

    def is_button_animating(self, button_id):
        return any(button[4] == button_id for button in self.buttons)

    def set_button_animating(self, button_id):
        for button in self.buttons:
            if button[4] == button_id:
                button_index = self.buttons.index(button)
                self.buttons[button_index] = button[:4] + ("animating",)

    def reset_button_animating(self, button_id):
        for button in self.buttons:
            if button[4] == "animating":
                button_index = self.buttons.index(button)
                self.buttons[button_index] = button[:4] + (button_id,)

    def animated_button(self, base_path, vertical_position_ratio):
        animation_images = [f"{base_path}{i:02d}.png" for i in range(1, 6)]
        for image_path in animation_images:
            button_image = pygame.image.load(image_path)
            button_rect = button_image.get_rect()
            button_width_scaled = int(self.screen.get_width() * 0.17)
            button_height_scaled = int(button_rect.height * (button_width_scaled / button_rect.width))
            button_image_scaled = pygame.transform.scale(button_image, (button_width_scaled, button_height_scaled))
            button_x = (self.screen.get_width() - button_width_scaled) // 2
            button_y = self.screen.get_height() * vertical_position_ratio - button_height_scaled // 2
            self.screen.blit(button_image_scaled, (button_x, button_y))
            pygame.display.flip()
            self.clock.tick(10)

    def chaine_hint(self):
        self.book_display()
        self.display_button("sprite\\button-next\\next01.png", 0.75, "next")
        self.clicked_next(1)

        self.display_background()
        self.display_book_button()
        self.book_display()
        self.display_button("sprite\\button-next\\next01.png", 0.75, "next")
        self.clicked_next(1)

        self.display_background()
        self.display_book_button()
        self.book_display()
        self.display_button("sprite\\button-back\\back01.png", 0.75, "next")
        self.clicked_next(2)
        self.display_chaine()

    def book_display(self):
        book_image = pygame.image.load("sprite\\book-animate\\1.png")
        book_rect = book_image.get_rect()
        book_width_scaled = int(self.screen.get_width() * 0.6)
        book_height_scaled = int(book_rect.height * (book_width_scaled / book_rect.width))
        book_image_scaled = pygame.transform.scale(book_image, (book_width_scaled, book_height_scaled))
        book_x = (self.screen.get_width() - book_width_scaled) // 2
        book_y = (self.screen.get_height() - book_height_scaled) // 2
        self.screen.blit(book_image_scaled, (book_x, book_y))

    def clicked_next(self, button_ide):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                for button in self.buttons:
                    button_x, button_y, button_width, button_height, button_id = button
                    if button_x <= pos[0] <= button_x + button_width and button_y <= pos[1] <= button_y + button_height:
                        if button_id == "next":
                            if button_ide == 1:
                                self.animated_button("sprite\\button-next\\next", 0.75)
                            else:
                                self.animated_button("sprite\\button-back\\back", 0.75)
                            return

if __name__ == "__main__":
    menu = ScreenMenu()
    menu.main()
