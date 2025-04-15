import pygame
import sqlite3
from game_state_manager import BaseState
from gui_code.buttons import Button, exit_button_img, backtomenu_button_img
from constants import FONT, SCREENHEIGHT, SCREENWIDTH


# Results screen

class Results(BaseState):
    resultsOutput = False
    def run(self):
        self.background = pygame.image.load(
            "Screens/backgrounds/resultbackground.png").convert_alpha()
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
        # results text
        info_lines = [
            # shipHealth, totalFuel, fuelAmtUsed, fuelRemaining, totalWeight, passengersAmt, cargoWght, attemptTime, attemptSuccess, failureReason
            f"Ship Health: 100 HP",
            f"Total Fuel: 100 Gal",
            f"Fuel Remaining: {fuelRmn} Gal",
            f"Total Weight: 342 lbs ",
            f"Total Passenger Weight: 165 lbs",
            f"Total Cargo Weight: 177 lbs",
            f"Attempt Time: 2:21",
            f"Attempt Success?: Yes",
            f"Failure Reason: N/A",
        ]
        connDB.commit()
        connDB.close()
        # Text for rocket info
        line_height = FONT.get_height()
        for i, line in enumerate(info_lines):
            line_surface = FONT.render(line, True, (255, 255, 255))
            self.display.blit(line_surface, ((SCREENWIDTH//2.5),
                              (SCREENWIDTH//3.5) + i * line_height))

        if menu_button.draw() is True:
            self.gameStateManger.set_state('menu')
        if exit_button.draw() is True:
            self.quit()
