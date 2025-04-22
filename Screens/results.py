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
        
        # Safely check if the table exists before attempting to query it
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='Attempts'")
        table_exists = cursor.fetchone() is not None
        
        results_data = []
        
        if table_exists:
            cursor.execute('SELECT COUNT(attemptNum) FROM Attempts')
            currentIteration = cursor.fetchone()
            newCurr = int(currentIteration[0])
            
            if newCurr > 0:
                # Get fuel remaining for current attempt
                cursor.execute(f"SELECT fuelRemaining FROM Attempts WHERE attemptNum = {newCurr}")
                curFuelRmn = cursor.fetchone()
                if curFuelRmn:  # Check that we got a result
                    fuelRmn = curFuelRmn[0]
                
                # Get lower bound to avoid negative attempt numbers
                lower_bound = max(1, newCurr - 4)
                
                # Loop through attempts from newest to oldest, but never below 1
                for attempt_num in range(newCurr, lower_bound - 1, -1):
                    cursor.execute(f"SELECT * FROM Attempts WHERE attemptNum = {attempt_num}")
                    row_data = cursor.fetchone()
                    if row_data:
                        results_data.append(row_data)

        
        # Display data section - only runs if we have data
        x_start = 500
        y_start = 410
        x_spacing = 223
        y_spacing = 100

        # Display data in grid
        for j in range(min(len(results_data), 5)): 
            row = results_data[j]
            for i in range(min(len(row), 6)):
                x = x_start + (i * x_spacing)
                y = y_start + (j * y_spacing)
                
                # Convert to string and display the data
                if row[i] is not None:
                    self.draw_text(str(row[i]), x, y)

        connDB.commit()
        connDB.close()

        if menu_button.draw() is True:
            self.gameStateManger.set_state('menu')
        if exit_button.draw() is True:
            self.quit()
