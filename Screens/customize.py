import pygame
import time
from game_state_manager import BaseState
from constants import SCREENWIDTH, SCREENHEIGHT, FONT, SCREEN
from gui_code.buttons import Button, backtomenu_button_img, start_button_img, yes_img, no_img
from gui_code.buttons import one_img, two_img, three_img, ten_img, fifty_img, hundred_img


class Customize(BaseState):
    def __init__(self, screen, gameStateManager):
        super().__init__(screen, gameStateManager)
        self.display = screen
        self.background = pygame.image.load(
            "Screens/backgrounds/customizebackground.png"
        ).convert_alpha()

        # varaibles for MATT AND MIGUEL
        self.isRover = False
        self.astronautAmt = 0
        self.instrumentAmt = 0
        self.extraMass = 0
        self.curr_state = "rover"

    def run(self):
        # just use them — they persist across calls
        self.display.blit(self.background, (0, 0))

        # handle different input sections according to current state
        if self.curr_state == "rover":
            self.rover_sec()
        elif self.curr_state == "astronauts":
            self.astro_sec()
        elif self.curr_state == "instrument":
            self.instrument_sec()
        elif self.curr_state == "start":
            self.start_sec()

        # Back to menu button
        menu_button = Button(50, 50, backtomenu_button_img, 1)
        if menu_button.draw():
            self.gameStateManger.set_state('menu')

        
    
    def rover_sec(self):
        # is there a rover?
        rover_text = FONT.render('Is there a Rover?', True, (255, 255, 255))
        self.display.blit(rover_text, (435, 350))

        yes_button = Button(450, 450, yes_img, 1)
        no_button = Button(450, 550, no_img, 1)

        if yes_button.draw():
            self.isRover = True # FOR MIGUEL AND MATT
            self.extraMass += 200
            print("Add Rover, +200kg")
            self.curr_state = "astronauts"
        elif no_button.draw():
            self.isRover = False
            print("No Rover")
            self.curr_state = "astronauts"
    

    def astro_sec(self):
        # how many astronauts from (1 - 3)
        astronaut_text = FONT.render('How many Astronauts? (1-3)', True, (255, 255, 255))
        self.display.blit(astronaut_text, (765, 350))


        # display infomations selected
        if self.isRover:
            rover_text = FONT.render('Rover = Yes', True, (255, 255, 255))
            self.display.blit(rover_text, (435, 350))
            # THIS NEEDS TO DISPLAY THE AMOUNT OF POUNDS ADDED ONTO THE ROCKET
            rover_info = FONT.render('Adds 200 kg', True, (255, 255, 255))
            self.display.blit(rover_info, (435, 400))
        else:
            rover_text = FONT.render('Rover = No', True, (255, 255, 255))
            self.display.blit(rover_text, (435, 350))
            rover_info = FONT.render('Adds 0 kg', True, (255, 255, 255))
            self.display.blit(rover_info, (435, 400))


        one_button = Button(900, 450, one_img, 1)
        two_button = Button(900, 550, two_img, 1)
        three_button = Button(900, 650, three_img, 1)

        if one_button.draw():
           self.astronautAmt = 1    # FOR MIGUEL AND MATT
           self.extraMass += 120
           print("Chose 1 Astronaut, adds 120kg")
           self.curr_state = "instrument"
        elif two_button.draw():
           self.astronautAmt = 2
           self.extraMass += 240
           print("Chose 2 Astronauts, adds 240kg")
           self.curr_state = "instrument"
        elif three_button.draw():
           self.astronautAmt = 3
           self.extraMass += 360
           print("Chose 3 Astronauts, adds 360kg")
           self.curr_state = "instrument"

    
    def instrument_sec(self):
        # how man instruments are there from (0 - 300)
        instrument_text = FONT.render('How many Instruments? (10, 50, 100)', True, (255, 255, 255))
        self.display.blit(instrument_text, (1150, 350))

        # display infomations selected
        if self.isRover:
            rover_text = FONT.render('Rover = Yes', True, (255, 255, 255))
            self.display.blit(rover_text, (435, 350))
            rover_info = FONT.render('Adds 200 kg', True, (255, 255, 255))
            self.display.blit(rover_info, (435, 400))
        else:
            rover_text = FONT.render('Rover = No', True, (255, 255, 255))
            self.display.blit(rover_text, (435, 350))
            rover_info = FONT.render('Adds 0 kg', True, (255, 255, 255))
            self.display.blit(rover_info, (435, 400))

        if self.astronautAmt == 1:
            astro_text = FONT.render('1 Astronaut', True, (255, 255, 255))
            self.display.blit(astro_text, (765, 350))
            astro_info = FONT.render('Adds 120 kg', True, (255, 255, 255))
            self.display.blit(astro_info, (765, 400))
        elif self.astronautAmt == 2:
            astro_text = FONT.render('2 Astronauts', True, (255, 255, 255))
            self.display.blit(astro_text, (765, 350))
            astro_info = FONT.render('Adds 240 kg', True, (255, 255, 255))
            self.display.blit(astro_info, (765, 400))
        elif self.astronautAmt == 3:
            astro_text = FONT.render('3 Astronauts', True, (255, 255, 255))
            self.display.blit(astro_text, (765, 350))
            astro_info = FONT.render('Adds 360 kg', True, (255, 255, 255))
            self.display.blit(astro_info, (765, 400))

        ten_button = Button(1350, 450, ten_img, 1)
        fifty_button = Button(1350, 550, fifty_img, 1)
        hundred_button = Button(1350, 650, hundred_img, 1)
        if ten_button.draw():
            self.instrumentAmt = 10 # FOR MIGUEL AND MATT
            self.extraMass += 50
            print("Chose 10, adds 50kg")
            self.curr_state = "start"
        elif fifty_button.draw():
            self.instrumentAmt = 50
            self.extraMass += 250
            print("Chose 50, adds 250kg")
            self.curr_state = "start"
        elif hundred_button.draw():
            self.instrumentAmt = 100
            self.extraMass += 500
            print("Chose 100, adds 500kg")
            self.curr_state = "start"


    def start_sec(self):
        start_text = FONT.render('Press Start to Begin Simulation', True, (255, 255, 255))
        self.display.blit(start_text, (700, 900))        

        # display infomations selected
        if self.isRover:
            rover_text = FONT.render('Rover = Yes', True, (255, 255, 255))
            self.display.blit(rover_text, (435, 350))
            rover_info = FONT.render('Adds 200 kg', True, (255, 255, 255))
            self.display.blit(rover_info, (435, 400))
        else:
            rover_text = FONT.render('Rover = No', True, (255, 255, 255))
            self.display.blit(rover_text, (435, 350))
            rover_info = FONT.render('Adds 0 kg', True, (255, 255, 255))
            self.display.blit(rover_info, (435, 400))

        if self.astronautAmt == 1:
            astro_text = FONT.render('1 Astronaut', True, (255, 255, 255))
            self.display.blit(astro_text, (765, 350))
            astro_info = FONT.render('Adds 120 kg', True, (255, 255, 255))
            self.display.blit(astro_info, (765, 400))
        elif self.astronautAmt == 2:
            astro_text = FONT.render('2 Astronauts', True, (255, 255, 255))
            self.display.blit(astro_text, (765, 350))
            astro_info = FONT.render('Adds 240 kg', True, (255, 255, 255))
            self.display.blit(astro_info, (765, 400))
        elif self.astronautAmt == 3:
            astro_text = FONT.render('3 Astronauts', True, (255, 255, 255))
            self.display.blit(astro_text, (765, 350))
            astro_info = FONT.render('Adds 360 kg', True, (255, 255, 255))
            self.display.blit(astro_info, (765, 400))

       
        if self.instrumentAmt == 10:
            inst_text = FONT.render('10 instruments on board', True, (255, 255, 255))
            self.display.blit(inst_text, (1150, 350))
            inst_info = FONT.render('Adds 50 kg', True, (255, 255, 255))
            self.display.blit(inst_info, (1150, 400))
        elif self.instrumentAmt == 50:
            inst_text = FONT.render('50 instruments on board', True, (255, 255, 255))
            self.display.blit(inst_text, (1150, 350))
            inst_info = FONT.render('Adds 250 kg', True, (255, 255, 255))
            self.display.blit(inst_info, (1150, 400))
        elif self.instrumentAmt == 100:
            inst_text = FONT.render('100 instruments on board', True, (255, 255, 255))
            self.display.blit(inst_text, (1150, 350))
            inst_info = FONT.render('Adds 500 kg', True, (255, 255, 255))
            self.display.blit(inst_info, (1150, 400))


        # displays start button to start
        customize_start_button = Button(1660, 975, start_button_img, 1)
        if customize_start_button.draw() is True:
            print(f'Adding {self.extraMass} kg')
            self.gameStateManger.extra_mass = self.extraMass
            self.gameStateManger.set_state('simulation')
