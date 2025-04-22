import pygame
import sqlite3
from game_state_manager import BaseState
from gui_code.buttons import Button, exit_button_img, backtomenu_button_img
from constants import FONT, SCREENHEIGHT, SCREENWIDTH


# Results screen

class Results(BaseState):
    resultsOutput = False

    def draw_text(self, text, x, y, color="white", font=FONT):
        """Draw text at a specific position on the screen"""
        text_surface = font.render(text[:10], True, color)
        self.display.blit(text_surface, (x, y))

    def run(self):
        self.background = pygame.image.load(
            "Screens/backgrounds/resultswithbackground.png").convert_alpha()
        self.display.blit(self.background, (0, 0))

        exit_button = Button(1660, 150, exit_button_img, 1)
        menu_button = Button(1660, 50, backtomenu_button_img, 1)
        connDB = sqlite3.connect('lunarlander.db')
        cursor = connDB.cursor()
        cursor.execute('SELECT COUNT(attemptNum) FROM Attempts') # gives num of tuples
        currentIteration = cursor.fetchone() # var for the most recent tuple
        newCurr = int(currentIteration[0])
        # grabs fuel remaining for current attempt
        cursor.execute(f"SELECT fuelRemaining FROM Attempts WHERE attemptNum = {newCurr}")
        curFuelRmn = cursor.fetchone()
        fuelRmn = curFuelRmn[0]
        # update for other database variables in the future
        # output last 5 attempts by taking tuple amounts, and placing limiter when attempt = 0
        if Results.resultsOutput == False:
            i = newCurr
            for newCurr in range(i,i-5,-1):
                if newCurr <= 0:
                    break
                else:
                    cursor.execute(f"SELECT * FROM Attempts WHERE attemptNum = {newCurr}")
                    outputTuple = cursor.fetchall()
                    print(outputTuple)
            Results.resultsOutput = True

        x_start = 500
        y_start = 410
        x_spacing = 223
        y_spacing = 100

        for i in range(6):  # 6 columns
            x = x_start + (i * x_spacing)
            
            for j in range(5):  # 5 rows 
                y = y_start + (j * y_spacing)
                self.draw_text("MISSION STATISTICS", x, y)

        connDB.commit()
        connDB.close()

        if menu_button.draw() is True:
            self.gameStateManger.set_state('menu')
        if exit_button.draw() is True:
            self.quit()
