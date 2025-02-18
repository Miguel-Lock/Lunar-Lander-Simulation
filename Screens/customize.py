import pygame
from game_state_manager import BaseState
from gui_code.buttons import Button, start_button_img

# Customize screen


class Customize(BaseState):
    def run(self):
        self.background = pygame.image.load(
            "Screens/backgrounds/customizebackground.png").convert_alpha()
        self.display.blit(self.background, (0, 0))

        # buttons for screen direction
        customize_start_button = Button(1660, 975, start_button_img, 1)

        if customize_start_button.draw() is True:
            self.gameStateManger.set_state('simulation')
