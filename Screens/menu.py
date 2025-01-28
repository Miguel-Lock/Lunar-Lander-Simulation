import pygame
from game_state_manager import BaseState

#main menu screen
class Menu(BaseState):
    def run(self):
        self.display.fill('red')

        # Text with directions
        font = pygame.font.Font(None, 36)
        text_surface = font.render("Menu. 2 for customize, 3 for history, 5 to quit", True, (255, 255, 255))  # White text
        text_rect = text_surface.get_rect()
        text_rect.center = (self.display.get_width() // 2, self.display.get_height() // 2)  # Center on screen
        self.display.blit(text_surface, text_rect)

        # Key press detection
        keys = pygame.key.get_pressed()
        if keys[pygame.K_2]:
            self.gameStateManger.set_state('customize')
        if keys[pygame.K_3]:
            self.gameStateManger.set_state('history')
        if keys[pygame.K_5]:
            self.quit()
        if keys[pygame.K_9]:
            self.gameStateManger.set_state('menu')
