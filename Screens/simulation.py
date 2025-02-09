import pygame
import time  # for delay between landing and results
from game_state_manager import BaseState
from pygame.locals import RLEACCEL
from constants import SCREENWIDTH, SCREENHEIGHT, SURFACE, FONT
from Screens.algos import MyAlgos

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

        # Text with directions
        font = FONT
        text_surface = font.render(
            # White text
            "Simulation. 1 for menu, 5 to quit", True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (self.display.get_width() // 2,
                            self.display.get_height() // 2)  # Center on screen
        self.display.blit(text_surface, text_rect)

        # Key press detection
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.gameStateManger.set_state('menu')
        if keys[pygame.K_5]:
            self.quit()

        self.rocket.update(keys)  # update rocket on keypress
        # update screen on keypress
        self.display.blit(self.rocket.surf, self.rocket.rect)

        # after rocket lands
        # idea: should we have a button to lead to the results
        # instead of automatically leading to results?
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
