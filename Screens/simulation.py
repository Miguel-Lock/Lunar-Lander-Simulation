import pygame
from game_state_manager import BaseState

# Simulation screen


class Simulation(BaseState):
    def run(self):
        self.background = pygame.image.load(
            "Screens/backgrounds/simulationscreen.png")
        self.display.blit(self.background, (0, 0))
        # self.display.fill('orange')

        # Text with directions
        font = pygame.font.Font(None, 36)
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
