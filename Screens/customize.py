import pygame
from game_state_manager import BaseState

class Customize(BaseState):
    def run(self):
        self.display.fill('black')

        font = pygame.font.Font(None, 36)
        text_surface = font.render("Customize. 1 for menu, 4 for simulation, 5 to quit", True, (255, 255, 255))  # White text
        text_rect = text_surface.get_rect()
        text_rect.center = (self.display.get_width() // 2, self.display.get_height() // 2)  # Center on screen
        self.display.blit(text_surface, text_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.gameStateManger.set_state('menu')
        if keys[pygame.K_4]:
            self.gameStateManger.set_state('simulation')
        if keys[pygame.K_5]:
            self.quit()