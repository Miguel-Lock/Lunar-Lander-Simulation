import pygame
from constants import SCREEN, FONT
clock = pygame.time.Clock()

# instantiate the images as variables
start_button_img = pygame.image.load(
    'gui_code/buttons/start_button.png').convert_alpha()
history_button_img = pygame.image.load(
    'gui_code/buttons/history_button.png').convert_alpha()
exit_button_img = pygame.image.load(
    'gui_code/buttons/exit_button.png').convert_alpha()
backtomenu_button_img = pygame.image.load(
    'gui_code/buttons/BacktoMenu.png').convert_alpha()
button_img = pygame.image.load(
    'gui_code/buttons/default_button.png').convert_alpha()
yes_img = pygame.image.load(
    'gui_code/buttons/yes.png').convert_alpha()
no_img = pygame.image.load(
    'gui_code/buttons/no.png').convert_alpha()
one_img = pygame.image.load(
    'gui_code/buttons/1.png').convert_alpha()
two_img = pygame.image.load(
    'gui_code/buttons/2.png').convert_alpha()
three_img = pygame.image.load(
    'gui_code/buttons/3.png').convert_alpha()


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

        # the return variable to be used for every button instance
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


class InputBox:
    def __init__(self, x, y, width, height, input_text=''):
        self.rect = pygame.Rect(x, y, width, height)
        self.color_inactive = pygame.Color('lightskyblue3')
        self.color_active = pygame.Color('dodgerblue2')
        self.color = self.color_inactive
        self.font = FONT
        self.text = input_text
        self.txt_surface = self.font.render(self.text, True, (255, 0, 0))
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Toggle active state on click inside the box
            if self.rect.collidepoint(event.pos):
                self.active = True
                self.color = self.color_active
                # Optionally clear the text on click:
                # self.text = ""
            else:
                self.active = False
                self.color = self.color_inactive

        if event.type == pygame.KEYDOWN and self.active:
            if event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.key == pygame.K_RETURN:
                # On Enter, disable editing (or perform an action)
                self.active = False
                self.color = self.color_inactive
            else:
                self.text += event.unicode
            # Update the text surface after any change.
            self.txt_surface = self.font.render(self.text, True, (255, 0, 0))

    def draw(self):
        # Draw the input box border
        pygame.draw.rect(SCREEN, self.color, self.rect, 2)
        # Blit the current text.
        SCREEN.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))