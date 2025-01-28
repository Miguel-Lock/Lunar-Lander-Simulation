import pygame
import sys

# All screens inherit from this class
class BaseState:
    def __init__(self, display, gameStateManger):
        self.display = display
        self.gameStateManger = gameStateManger
    def quit(self):
        pygame.quit()
        sys.exit()

# Manages what screen is currently being displayed
class GameStateManger:
    def __init__(self, currentState):
        self.currentState = currentState
    def get_state(self):
        return self.currentState
    def set_state(self, state):
        self.currentState = state