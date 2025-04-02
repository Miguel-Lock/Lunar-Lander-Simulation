import pygame
import time
from game_state_manager import BaseState
from constants import SCREENWIDTH, SCREENHEIGHT, FONT, SCREEN
from gui_code.buttons import Button, backtomenu_button_img, start_button_img, yes_img, no_img, one_img, two_img, three_img
from gui_code.buttons import InputBox


class Customize(BaseState):
    def __init__(self, screen, gameStateManger):
        super().__init__(screen, gameStateManger)
        self.display = screen

        # Load background
        self.background = pygame.image.load(
            "Screens/backgrounds/customizebackground.png").convert_alpha()
        
        # variables for Miguel to use
        self.isRover = False
        self.astronautAmt = 0
        self.instrumentAmt = 0
        
        self.curr_state = "rover" # start with the rover section
        
    def run(self):

        self.background = pygame.image.load(
            "Screens/backgrounds/customizebackground.png").convert_alpha()
        self.display.blit(self.background, (0, 0))

        # handle different input sections according to current state
        if self.curr_state == "rover":
            self.rover_sec()
            time.sleep(0.5)
        elif self.curr_state == "astronauts":
            self.astro_sec()
            time.sleep(0.5)
        elif self.curr_state == "instrument":
            self.instrument_sec()
            time.sleep(0.5)
        elif self.curr_state == "start":
            self.start_sec()


        # Back to menu button
        menu_button = Button(50, 50, backtomenu_button_img, 1)
        if menu_button.draw():
            self.gameStateManger.set_state('menu')

        
    
    def rover_sec(self):
        # is there a rover?
        rover_text = FONT.render('Is there a Rover?', True, (255, 255, 255))
        self.display.blit(rover_text, (850, 400))

        yes_button = Button(850, 550, yes_img, 1)
        no_button = Button(850, 650, no_img, 1)

        if yes_button.draw():
            isRover = True
            print("Yes")
            self.curr_state = "astronauts"
        elif no_button.draw():
            isRover = False
            print("No")
            self.curr_state = "astronauts"
    

    def astro_sec(self):
        # how many astronauts from (1 - 3)
        astronaut_text = FONT.render('How many Astronauts? (1-3)', True, (255, 255, 255))
        self.display.blit(astronaut_text, (825, 400))

        one_button = Button(850, 550, one_img, 1)
        two_button = Button(950, 550, two_img, 1)
        three_button = Button(1050, 550, three_img, 1)

        if one_button.draw():
           self.astronautAmt = 1
           print("1")
           self.curr_state = "instrument"
        elif two_button.draw():
           self.astronautAmt = 2
           print("2")
           self.curr_state = "instrument"
        elif three_button.draw():
           self.astronautAmt = 3
           print("3")
           self.curr_state = "instrument"

    
    def instrument_sec(self):
        # how man instruments are there from (0 - 300)
        instrument_text = FONT.render('How many Instruments? (0-300)', True, (255, 255, 255))
        self.display.blit(instrument_text, (800, 400))

        yes_button = Button(850, 550, yes_img, 1)
        if yes_button.draw():
            isRover = True
            print("Yes")
            self.curr_state = "start"

    def start_sec(self):
        start_text = FONT.render('Press Start to Begin Simulation', True, (255, 255, 255))
        self.display.blit(start_text, (850, 400))
        # displays start button to start
        customize_start_button = Button(1660, 975, start_button_img, 1)
        if customize_start_button.draw() is True:
            self.gameStateManger.set_state('simulation')








