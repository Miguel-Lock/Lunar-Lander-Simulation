import pygame
from game_state_manager import BaseState
from constants import SCREENWIDTH, SCREENHEIGHT, FONT, SCREEN
from gui_code.buttons import Button, backtomenu_button_img, start_button_img
from gui_code.buttons import InputBox

text = ""
input_active = True


class Customize(BaseState):
    def __init__(self, screen, gameStateManger):
        super().__init__(screen, gameStateManger)
        self.display = screen
        # Load background
        self.background = pygame.image.load(
            "Screens/backgrounds/customizebackground.png").convert_alpha()
        self.bruh = InputBox(850, 450, 140, 60, test)
        
    def run(self):
        # Draw background
        self.display.blit(self.background, (0, 0))

        # Back to menu button
        menu_button = Button(50, 50, backtomenu_button_img, 1)
        if menu_button.draw():
            self.gameStateManger.set_state('menu')

        # buttons for screen direction
        customize_start_button = Button(1660, 975, start_button_img, 1)

        if customize_start_button.draw() is True:
            self.gameStateManger.set_state('simulation')



