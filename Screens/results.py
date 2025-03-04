import pygame
from game_state_manager import BaseState
from gui_code.buttons import Button, exit_button_img, backtomenu_button_img
from constants import FONT, SCREENHEIGHT, SCREENWIDTH


# Results screen


class Results(BaseState):
    def run(self):
        self.background = pygame.image.load(
            "Screens/backgrounds/resultbackground.png").convert_alpha()
        self.display.blit(self.background, (0, 0))

        exit_button = Button(1660, 150, exit_button_img, 1)
        menu_button = Button(1660, 50, backtomenu_button_img, 1)

        # results text
        info_lines = [
            f"Average Velocity: ",
            f"Fuel Remaining: ",
            f"Engine: "
        ]
        # Text for rocket info
        line_height = FONT.get_height()
        for i, line in enumerate(info_lines):
            line_surface = FONT.render(line, True, (255, 255, 255))
            self.display.blit(line_surface, ((SCREENWIDTH//2.5),
                              (SCREENWIDTH//3.5) + i * line_height))

        if menu_button.draw() is True:
            self.gameStateManger.set_state('menu')
        if exit_button.draw() is True:
            self.quit()
