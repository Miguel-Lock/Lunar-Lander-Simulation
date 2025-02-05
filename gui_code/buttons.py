import pygame
import sys
from game_state_manager import BaseState

main_font = pygame.font.SysFont(
    "gui_code/fonts/UbuntuNerdFont-Regular.ttf", 50)


class Button():
    def __init__(self, image, x, y, input):
        self.image = image
        self.x = x
        self.y = y
        self.input = input
