import pygame
from game_state_manager import BaseState
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
