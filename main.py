import pygame
import sys
from game_state_manager import GameStateManger
from Screens.menu import Menu
from Screens.customize import Customize
from Screens.history import History
from Screens.simulation import Simulation
from Screens.results import Results
from constants import FPS, SCREEN


class Game:
    def __init__(self):
        pygame.init()
        # self.screen = SCREEN
        self.clock = pygame.time.Clock()

        # Program starts with the menu screen
        self.gameStateManger = GameStateManger('menu')

        # All screens
        self.menu = Menu(SCREEN, self.gameStateManger)
        self.customize = Customize(SCREEN, self.gameStateManger)
        self.history = Results(SCREEN, self.gameStateManger)
        self.simulation = Simulation(SCREEN, self.gameStateManger)
        self.results = Results(SCREEN, self.gameStateManger)

        self.states = {
            'menu': self.menu,
            'customize': self.customize,
            'history': self.history,
            'simulation': self.simulation,
            'results': self.results
        }

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                # This works universally for all states
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

            self.states[self.gameStateManger.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    game = Game()
    game.run()
