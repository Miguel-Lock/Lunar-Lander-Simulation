import pygame
from game_state_manager import BaseState
from gui_code.buttons import Button, exit_button_img, backtomenu_button_img


# Results screen


class Results(BaseState):
    def run(self):
        self.background = pygame.image.load(
            "Screens/backgrounds/resultbackground.png").convert_alpha()
        self.display.blit(self.background, (0, 0))

        exit_button = Button(1660, 150, exit_button_img, 1)
        menu_button = Button(1660, 50, backtomenu_button_img, 1)

        if menu_button.draw() is True:
            self.gameStateManger.set_state('menu')
        if exit_button.draw() is True:
            self.quit()
