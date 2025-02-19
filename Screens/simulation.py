import pygame
import time  # for delay between landing and results
from game_state_manager import BaseState
from pygame.locals import RLEACCEL
from constants import SCREENWIDTH, SCREENHEIGHT, SURFACE
from algos import MyAlgos
from gui_code.buttons import Button, backtomenu_button_img, exit_button_img

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

        # Buttons for screen directions
        exit_button = Button(1660, 150, exit_button_img, 1)
        menu_button = Button(1660, 50, backtomenu_button_img, 1)

        if menu_button.draw() is True:
            self.gameStateManger.set_state('menu')
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
            self.gameStateManger.set_state('results')


class OurFavoriteRocketShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((40, 75))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.center = (SCREENWIDTH // 2, SCREENHEIGHT // 8)

        self.is_landed = False
        self.algos = MyAlgos()  # this is how we are going to use the algorithms

    def update(self, pressed_key):
        if not self.is_landed:
            self.downY = self.algos.gravity()  # Update gravity value
            # Moves down on y axis at rate self.downY
            self.rect.move_ip(0, self.downY)

        # Check if rocket has landed
        if self.rect.bottom >= SURFACE:
            self.is_landed = True
            self.rect.bottom = SURFACE  # Stop vertical movement
        else:
            self.is_landed = False
            if pressed_key[pygame.K_SPACE]:
                self.rect.move_ip(0, -5)

        # Keep the rocket from flying off the screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SURFACE:
            self.rect.bottom = SURFACE
