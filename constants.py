import pygame  # import pygame to initialize a global font variable

pygame.init()  # must initialize pygame

SCREENWIDTH = 1920
SCREENHEIGHT = 1080
SURFACE = SCREENHEIGHT - (SCREENHEIGHT // 20)
ROCKET_BOTTOM = SCREENHEIGHT // 4
VERTICAL_DISTANCE = SURFACE - ROCKET_BOTTOM
FPS = 60
FONT = pygame.font.Font("gui_code/fonts/UbuntuNerdFont-Regular.ttf", 30)
SCREEN = pygame.display.set_mode(
    (SCREENWIDTH, SCREENHEIGHT))  # global screen size/variable
