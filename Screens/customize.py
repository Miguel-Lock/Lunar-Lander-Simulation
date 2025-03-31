import pygame
from game_state_manager import BaseState
from constants import SCREENWIDTH, SCREENHEIGHT, FONT, SCREEN
from gui_code.buttons import Button, backtomenu_button_img

class Customize(BaseState):
    def __init__(self, screen, gameStateManger):
        super().__init__(screen, gameStateManger)
        self.display = screen
        # Load background
        self.background = pygame.image.load(
            "Screens/backgrounds/customizebackground.png").convert_alpha()
        
        # Input fields
        self.input_boxes = []
        self.active_box = None
        self.create_input_boxes()

        # Default values
        self.fuel_mass = 3000  # kg
        self.astronauts = 2    # number of crew
        self.current_text = ""

    def create_input_boxes(self):
        # Create rectangles for input boxes
        fuel_box = pygame.Rect(SCREENWIDTH//4, 200, 140, 32)
        crew_box = pygame.Rect(SCREENWIDTH//4, 300, 140, 32)
        self.input_boxes = [
            {"rect": fuel_box, "text": "", "label": "Fuel Mass (kg): \n"},
            {"rect": crew_box, "text": "", "label": "Number of Astronauts: \n"}
        ]

    def run(self):
        # Draw background
        self.display.blit(self.background, (0, 0))

        # Back to menu button
        menu_button = Button(50, 50, backtomenu_button_img, 1)
        if menu_button.draw():
            self.gameStateManger.set_state('menu')

