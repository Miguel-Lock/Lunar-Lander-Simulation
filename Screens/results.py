import pygame
import sqlite3
from game_state_manager import BaseState
from gui_code.buttons import Button, exit_button_img, backtomenu_button_img
from constants import FONT, SCREENHEIGHT, SCREENWIDTH


# Results screen

class Results(BaseState):
    resultsOutput = False

    def draw_text(self, text, x, y, parse=True, color="white", font=FONT):
        """Draw text at a specific position on the screen"""
        if parse:
            text = text[:10]
        text_surface = font.render(text, True, color)
        self.display.blit(text_surface, (x, y))

    def run(self):
        self.background = pygame.image.load(
            "Screens/backgrounds/resultswithgrid.png").convert_alpha()
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

        titles = ["Attemp #", "Time", "Starting Wt", "Starting Fuel", "Ending Fuel", "Success?"]
        apendecies = ["", "s", "kg", "kg", "kg", ""]

        for i in range(len(titles)):
            x = 485 + (i * 223)
            y = 310
            self.draw_text(titles[i], x, y, parse=False)

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
                    # Format the Success column (last column, index 5)
                    if i == 5:  # Success column
                        text = "Yes" if (row[i] == 1 or row[i] is True) else "No"
                    else:
                        text = str(row[i]) + apendecies[i]
                    
                    self.draw_text(text, x, y)

        connDB.commit()
        connDB.close()

        if menu_button.draw() is True:
            self.gameStateManger.set_state('menu')
        if exit_button.draw() is True:
            self.quit()
