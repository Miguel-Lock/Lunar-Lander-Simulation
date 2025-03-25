import pygame
import time  # for delay between landing and results
from game_state_manager import BaseState
# from pygame.locals import RLEACCEL
from constants import SCREENWIDTH, SCREENHEIGHT, SURFACE, FONT, SCREEN, ROCKET_BOTTOM
from algos import MyAlgos
from gui_code.buttons import Button, exit_button_img

# importing idle rocket png
tilapia_idle_img = pygame.image.load(
    'Screens/rocket_assets/Tilapia.png').convert_alpha()

# importing rocket thrust png
tilapia_thrust_img = pygame.image.load(
    'Screens/rocket_assets/TilapiaThrust.png').convert_alpha()

# Simulation screen


class Simulation(BaseState):
    def __init__(self, screen, gameStateManger):
        super().__init__(screen, gameStateManger)
        self.display = screen
        self.all_sprites = pygame.sprite.Group()

        # create instance of OurFavoriteRocketShip
        self.rocket = OurFavoriteRocketShip()
        self.all_sprites.add(self.rocket)  # add rocket to all_sprites group

        # Load background in init so it isn't loaded every frame
        self.background = pygame.image.load(
            # convert_alpha may or may not improve performance
            "Screens/backgrounds/simulationscreen.png").convert_alpha()

    def run(self):
        self.display.blit(self.background, (0, 0))

        info_lines = [
            f"Speed: {self.rocket.rect.y}",
            f"Velocity: {self.rocket.rect.y}",
            f"Fuel Remaining: {self.rocket.rect.y}",
            f"Engine: {self.rocket.thrust_switch()}"
        ]
        # Text for rocket info
        line_height = FONT.get_height()
        for i, line in enumerate(info_lines):
            line_surface = FONT.render(line, True, (255, 255, 255))
            self.display.blit(line_surface, (50, 50 + i * line_height))

        # Buttons for screen directions
        exit_button = Button(1660, 50, exit_button_img, 1)

        if exit_button.draw() is True:
            self.quit()

        # Key press detection
        keys = pygame.key.get_pressed()
        self.rocket.update(keys)  # update rocket on keypress
        # update screen on keypress
        self.display.blit(self.rocket.surf, self.rocket.rect)

        # after rocket lands
        # delays for 3 seconds and then displays results
        if self.rocket.is_landed is True:
            time.sleep(3)
            self.rocket.reset()
            self.gameStateManger.set_state('results')


class OurFavoriteRocketShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = tilapia_idle_img
        self.rect = self.surf.get_rect()

        self.rect.centerx = SCREENWIDTH // 2
        self.rect.bottom = ROCKET_BOTTOM

        self.is_landed = False
        self.is_successful = False  # False if crashed, True otherwise
        self.algos = MyAlgos()  # this is how we are going to use algorithms
        self.is_thrust = False

    def thrust_switch(self):
        switch = " "
        if self.is_thrust:
            switch = "ON"
        if not self.is_thrust:
            switch = "OFF"
        return switch

    def update(self, pressed_key):
        if not self.is_landed:
            # passes boolean so Algos know if thrusters are activated
            self.downY = self.algos.move_down(pressed_key[pygame.K_SPACE])
            # Moves down on y axis at rate self.downY
            self.rect.move_ip(0, self.downY)

            if pressed_key[pygame.K_SPACE] == 1:
                self.surf = tilapia_thrust_img
                self.is_thrust = True
            else:
                self.surf = tilapia_idle_img
                self.is_thrust = False

        # Check if rocket has landed
        if self.rect.bottom >= SURFACE:
            self.surf = tilapia_idle_img  # reset image to idle
            self.is_landed = True
            self.rect.bottom = SURFACE  # Stop vertical movement
        else:
            self.is_landed = False

        # Keep the rocket from flying off the screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SURFACE:
            self.rect.bottom = SURFACE

    def reset(self):
        self.is_landed = False
        self.algos.reset()
        self.rect.center = (SCREENWIDTH // 2, SCREENHEIGHT // 8)
        self.surf = tilapia_idle_img  # reset image to idle
