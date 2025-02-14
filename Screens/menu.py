import pygame
from game_state_manager import BaseState
from constants import FONT
from gui_code.buttons import Button, start_button_img, exit_button_img, history_button_img

# main menu screen


class Menu(BaseState):
    def run(self):
        self.background = pygame.image.load(
            "Screens/backgrounds/start_background.png").convert_alpha()
        self.display.blit(self.background, (0, 0))

        # the button instances
        start_button = Button(850, 450, start_button_img, 1)
        exit_button = Button(850, 750, exit_button_img, 1)
        history_button = Button(850, 600, history_button_img, 1)

        if start_button.draw() is True:
            self.gameStateManger.set_state('customize')
        if exit_button.draw() is True:
            self.quit()
        if history_button.draw() is True:
            self.gameStateManger.set_state('history')

        # Text with directions
        # font = FONT
        # text_surface = font.render(
        #    # White text
        #    "Menu. 2 for customize, 3 for history, 5 to quit", True, (255, 255, 255))
        # text_rect = text_surface.get_rect()
        # text_rect.center = (self.display.get_width() // 2,
        #                    self.display.get_height() // 4)  # Center on screen
        # self.display.blit(text_surface, text_rect)

        # Key press detection
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_2]:
        #    self.gameStateManger.set_state('customize')
        # if keys[pygame.K_3]:
        #    self.gameStateManger.set_state('history')
        # if keys[pygame.K_5]:
        #    self.quit()
        # if keys[pygame.K_9]:
        #    self.gameStateManger.set_state('menu')
