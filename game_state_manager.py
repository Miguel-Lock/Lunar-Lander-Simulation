import pygame
import sys

class BaseState:
    def __init__(self, display, gameStateManger):
        self.display = display
        self.gameStateManger = gameStateManger
    def quit(self):
        pygame.quit()
        sys.exit()

class GameStateManger:
    def __init__(self, currentState):
        self.currentState = currentState
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state