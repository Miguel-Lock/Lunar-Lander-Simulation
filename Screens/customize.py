import pygame
from game_state_manager import BaseState
from constants import SCREENWIDTH, SCREENHEIGHT, FONT, SCREEN
from gui_code.buttons import Button, backtomenu_button_img, start_button_img, button_img
from gui_code.buttons import InputBox

# global variables for Miguel
isRover = False
astronaut_amt = 0   # should be 1-3
instrument_num = 0  # should be 1-300

isFinished = False

class Customize(BaseState):
    def __init__(self, screen, gameStateManger):
        super().__init__(screen, gameStateManger)
        self.display = screen

        # Load background
        self.background = pygame.image.load(
            "Screens/backgrounds/customizebackground.png").convert_alpha()
        
       
    def run(self):    

        rover_text = FONT.render('Is there a Rover?', True, (255, 255, 255))
        astronaut_text = FONT.render('How many Astronauts? (1-3)', True, (255, 255, 255))
        instrument_text = FONT.render('How many Instruments? (0-300)', True, (255, 255, 255))

        # is there a rover?
        self.display.blit(rover_text, (950, 300))
        yes_button = Button(950, 450, button_img, 1)
        no_button = Button(950, 550, button_img, 1)

        if yes_button.draw():
            isRover = True
            print("Yes")
        elif no_button.draw():
            isRover = False
            print("No")

       
        
        # astronaut count 1-3
        # mass of additional instruments (0 - 300)

        # Back to menu button
        menu_button = Button(50, 50, backtomenu_button_img, 1)
        if menu_button.draw():
            self.gameStateManger.set_state('menu')

        # buttons for screen direction
        customize_start_button = Button(1660, 975, start_button_img, 1)

        if customize_start_button.draw() is True:
            self.gameStateManger.set_state('simulation')



