import pygame
import sys
from game_state_manager import BaseState
from constants import FONT

main_font = pygame.font.SysFont(
    "gui_code/fonts/UbuntuNerdFont-Regular.ttf", 50)


class Button():
    def __init__(self, image, x, y, text):
        self.image = image
        self.x_pos = x
        self.y_pos = y
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.text_input = text
        self.text = FONT.render(self.text_input, True, "white")
        self.text_rect = self.text.get_rect(center=(self.x, self.y))

    # places button image and text on the screen
    def update(self):
        self.display.blit(self.image, self.rect)
        self.display.blit(self.text, self.text_rect)

    def check(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[0] in range(self.rect.top, self.rect.bottom):
            print("Button Pressed")
