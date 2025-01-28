import pygame
import sys
from game_state_manager import GameStateManger
from Screens.menu import Menu
from Screens.customize import Customize
from Screens.history import History
from Screens.simulation import Simulation

#This is a test

SCREENWIDTH, SCREENHEIGHT = 1920,1080
FPS=60

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
        self.clock = pygame.time.Clock()

        # Program starts with the menu screen
        self.gameStateManger = GameStateManger('menu')

        # All screens
        self.menu = Menu(self.screen, self.gameStateManger)
        self.customize = Customize(self.screen, self.gameStateManger)
        self.history = History(self.screen, self.gameStateManger)
        self.simulation = Simulation(self.screen, self.gameStateManger)

        self.states = {
            'menu': self.menu,
            'customize': self.customize,
            'history': self.history,
            'simulation': self.simulation
        }
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                #This works universally for all states
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            self.states[self.gameStateManger.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()