import pygame
from constants import SCREEN

# instantiate the images as variables
start_button_img = pygame.image.load(
    'gui_code/buttons/start_button.png').convert_alpha()
history_button_img = pygame.image.load(
    'gui_code/buttons/history_button.png').convert_alpha()
exit_button_img = pygame.image.load(
    'gui_code/buttons/exit_button.png').convert_alpha()

# button class to declare button instances


class Button():
    def __init__(self, x, y, image, scale):

        # makes the buttons scaleable
        w = image.get_width()
        h = image.get_height()
        self.image = pygame.transform.scale(
            image, (int(w * scale), int(h * scale)))

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # variable to store logic if left-click has been used on a button
        self.isClicked = False

    def draw(self):

        # the returned variable to be used for every button instance
        action = False

        # get mouse position
        mouse = pygame.mouse.get_pos()

        # check cursor hovering over Button
        if self.rect.collidepoint(mouse):
            # if the cursor is hovering over the button and left-clicked
            if pygame.mouse.get_pressed()[0] == 1 and self.isClicked is False:
                self.isClicked = True
                action = True

            if pygame.mouse.get_pressed()[0] == 0:
                self.isClicked = False

        # draw the button on the screen
        SCREEN.blit(self.image, (self.rect.x, self.rect.y))

        return action
