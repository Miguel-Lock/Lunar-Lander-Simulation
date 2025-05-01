import pygame  # import pygame to initialize a global font variable

pygame.init()  # must initialize pygame

SCREENWIDTH = 1920
SCREENHEIGHT = 1080
SURFACE = SCREENHEIGHT - (SCREENHEIGHT / 20)  # 1026
ROCKET_BOTTOM = (SCREENHEIGHT / 4)  # 270
VERTICAL_DISTANCE = SURFACE - ROCKET_BOTTOM  # 756
TOTALVERTICALDISTANCE = 15000 # m height to lander
METERPERPX = TOTALVERTICALDISTANCE / VERTICAL_DISTANCE  # 132.3
PXPERMETER = VERTICAL_DISTANCE / TOTALVERTICALDISTANCE  # 0.00756
FPS = 60
FONT = pygame.font.Font("gui_code/fonts/UbuntuNerdFont-Regular.ttf", 30)
BIGFONT = pygame.font.Font("gui_code/fonts/UbuntuNerdFont-Regular.ttf", 45)
SCREEN = pygame.display.set_mode(
    (SCREENWIDTH, SCREENHEIGHT))  # global screen size/variable
GRAVITY = 0.0000000000667430  # m^3/(s^2 * kg) <- G
MMOON = 73476730900000000000000  # Kg (Mass of the moon)
RMOON = 1740000  # m (radius of the moon)
# All CONSTANTS FOR LANDER ARE BASED ON APOLLO LUNAR MODULE (LM)
BASE_ROCKET = 2000
BASE_FUEL_AMT = 150  # kg
BASE_ROCKET_AND_FUEL = BASE_ROCKET + BASE_FUEL_AMT  # kg
SAFE_VELOCITY = 5