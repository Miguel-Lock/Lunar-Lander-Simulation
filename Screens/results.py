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
        info_text = f"Average Velocity: \nFuel Remaining: \nDid your Rocket Land? Nope.\nOther: (idk what to put here)\n"
        rocket_info = FONT.render(info_text, True, (255, 255, 255))
        info_rect = rocket_info.get_rect()
        info_rect.topleft = (SCREENWIDTH // 2, SCREENHEIGHT // 2)
        self.display.blit(rocket_info, info_rect)

        if menu_button.draw() is True:
            self.gameStateManger.set_state('menu')
        if exit_button.draw() is True:
            self.quit()
