import pygame
from game_state_manager import BaseState
from pygame.locals import RLEACCEL
from constants import SCREENWIDTH, SCREENHEIGHT, SURFACE

# Simulation screen
class Simulation(BaseState):
    def __init__(self, screen, BaseState):
        super().__init__(screen, BaseState)
        #self.display = screen #commented now, may be used later?
        #container to manage all sprites (used for collision detection and mass updates)
        self.all_sprites = pygame.sprite.Group()

        self.rocket = OurFavoriteRocketShip() #create instance of OurFavoriteRocketShip
        self.all_sprites.add(self.rocket) #add rocket to all_sprites group

    def run(self):
        self.display.fill('orange')

        # Text with directions
        font = pygame.font.Font(None, 36)
        text_surface = font.render("Simulation. 1 for menu, 5 to quit", True, (255, 255, 255))  # White text
        text_rect = text_surface.get_rect()
        text_rect.center = (self.display.get_width() // 2, self.display.get_height() // 2)  # Center on screen
        self.display.blit(text_surface, text_rect)

        # Key press detection
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.gameStateManger.set_state('menu')
        if keys[pygame.K_5]:
            self.quit()

        self.rocket.update(keys) # update rocket on keypress
        self.display.blit(self.rocket.surf, self.rocket.rect) # update screen on keypress

class OurFavoriteRocketShip(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.surf = pygame.Surface((40, 75))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()
        self.rect.center = (SCREENWIDTH // 2, SCREENHEIGHT // 8)

        self.is_landed = False

        self.downY = 2

    def update(self, pressed_key):
        if not self.is_landed:
            self.rect.move_ip(0, self.downY) #Moves down on y axis at rate self.downY

        # Check if rocket has landed
        if self.rect.bottom >= SURFACE:
            self.is_landed = True
            self.rect.bottom = SURFACE # Stop vertical movement
            self.rightX = 0  # Stop horizontal movement
        else:
            self.is_landed = False
            if pressed_key[pygame.K_SPACE]:
                self.rect.move_ip(0, -5)

        # Keep the rocket on the screen & above the surface
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREENWIDTH:
            self.rect.right = SCREENWIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SURFACE:
            self.rect.bottom = SURFACE