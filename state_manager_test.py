import pygame
import sys

SCREENWIDTH, SCREENHEIGHT = 1920,1080
FPS=60

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
        self.clock = pygame.time.Clock()

        self.gameStateManger = GameStateManger('menu')
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
                    self.quit()

            self.states[self.gameStateManger.get_state()].run()

            pygame.display.update()
            self.clock.tick(FPS)

class BaseState:
    def __init__(self, display, gameStateManger):
        self.display = display
        self.gameStateManger = gameStateManger
    def quit(self):
        pygame.quit()
        sys.exit()

class Menu(BaseState):
    def run(self):
        self.display.fill('red')

        font = pygame.font.Font(None, 36)
        text_surface = font.render("Menu. 2 for customize, 3 for history, 5 to quit", True, (255, 255, 255))  # White text
        text_rect = text_surface.get_rect()
        text_rect.center = (self.display.get_width() // 2, self.display.get_height() // 2)  # Center on screen
        self.display.blit(text_surface, text_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_2]:
            self.gameStateManger.set_state('customize')
        if keys[pygame.K_3]:
            self.gameStateManger.set_state('history')
        if keys[pygame.K_5]:
            self.quit()
        if keys[pygame.K_9]:
            self.gameStateManger.set_state('menu')

class History(BaseState):
    def run(self):
        self.display.fill('pink')

        font = pygame.font.Font(None, 36)
        text_surface = font.render("History. 1 for menu, 5 to quit", True, (255, 255, 255))  # White text
        text_rect = text_surface.get_rect()
        text_rect.center = (self.display.get_width() // 2, self.display.get_height() // 2)  # Center on screen
        self.display.blit(text_surface, text_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.gameStateManger.set_state('menu')
        if keys[pygame.K_5]:
            self.quit()

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

class Simulation(BaseState):
    def run(self):
        self.display.fill('orange')

        font = pygame.font.Font(None, 36)
        text_surface = font.render("Simulation. 1 for menu, 5 to quit", True, (255, 255, 255))  # White text
        text_rect = text_surface.get_rect()
        text_rect.center = (self.display.get_width() // 2, self.display.get_height() // 2)  # Center on screen
        self.display.blit(text_surface, text_rect)

        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            self.gameStateManger.set_state('menu')
        if keys[pygame.K_5]:
            self.quit()



class GameStateManger:
    def __init__(self, currentState):
        self.currentState = currentState
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state
        


if __name__ == "__main__":
    game = Game()
    game.run()