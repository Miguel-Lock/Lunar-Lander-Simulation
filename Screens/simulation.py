import pygame
import time  # for delay between landing and results
import sqlite3 # for database entries
from game_state_manager import BaseState
# from pygame.locals import RLEACCEL
from constants import SCREENWIDTH, SCREENHEIGHT, SURFACE, FONT, SCREEN, ROCKET_BOTTOM, PXPERMETER, METERPERPX, BASE_ROCKET_AND_FUEL, BASE_FUEL_AMT, BASE_ROCKET, SAFE_VELOCITY
from algos import MyAlgos
from gui_code.buttons import Button, exit_button_img

# Initialize pygame mixer for music
pygame.mixer.init()

# Load music file (flight of the valkyrie)
pygame.mixer.music.load("Screens/rocket_assets/RideOfValk.mp3")

# importing idle rocket png
tilapia_idle_img = pygame.image.load(
    'Screens/rocket_assets/Tilapia.png').convert_alpha()

# importing rocket thrust png
tilapia_thrust_img = pygame.image.load(
    'Screens/rocket_assets/TilapiaThrust.png').convert_alpha()
# importing rocket successful landing png
tilapia_success_img = pygame.image.load(
    'Screens/rocket_assets/TilapiaYay.png').convert_alpha()
# importing rocket crash png
tilapia_crash_img = pygame.image.load(
    'Screens/rocket_assets/TilapiaSad.png').convert_alpha()

# Simulation screen


class Simulation(BaseState):
    def __init__(self, screen, gameStateManger):
        super().__init__(screen, gameStateManger)
        self.display = screen
        self.all_sprites = pygame.sprite.Group()

        # Load background in init so it isn't loaded every frame
        self.background = pygame.image.load(
            # convert_alpha may or may not improve performance
            "Screens/backgrounds/simulationscreen.png").convert_alpha()
        pygame.mixer.music.play() # begins playing music
        self.reset()
        

    def reset(self):
        self.rocket = None
        self.start_time = 0
        self.elapsed_time = 0

    def run(self):
        # initialize rocket if it doesn't exist
        # moved inside run function to account for extra_mass
        if self.rocket is None:
            # Get extra mass from gameStateManger if it exists
            extra_mass = getattr(self.gameStateManger, 'extra_mass', 0)
            # create instance of OurFavoriteRocketShip
            self.rocket = OurFavoriteRocketShip(extra_mass=extra_mass)
            self.all_sprites.add(self.rocket)
            # Reset start_time when creating a new rocket
            self.start_time = pygame.time.get_ticks()

        self.display.blit(self.background, (0, 0))

        if not self.rocket.is_landed:
            self.elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000

        if self.rocket.algos.totalFuelMass < 0:
            self.rocket.algos.totalFuelMass = 0

        info_lines = [
            f"Downwards Velocity: {int(self.rocket.algos.velocity)} m/s",
            f"Fuel Remaining: {self.rocket.algos.totalFuelMass:.3f} kg",
            f"Engine: {self.rocket.thrust_switch()}",
            f"Time: {self.elapsed_time:.1f} s",
            f"Distance: {int(self.rocket.algos.height)} m"
        ]
        # Text for rocket info
        line_height = FONT.get_height()
        for i, line in enumerate(info_lines):
            line_surface = FONT.render(line, True, (255, 255, 255))
            self.display.blit(line_surface, (50, 50 + i * line_height))

        # Buttons for screen directions
        exit_button = Button(1660, 50, exit_button_img, 1)

        if exit_button.draw() is True:
            self.quit()

        # Key press detection
        keys = pygame.key.get_pressed()

        # Create a modified copy of keys when out of fuel
        if self.rocket.algos.totalFuelMass <= 0:
            # Convert keys to list so we can modify it
            keys_list = list(keys)
            # Disable the space key specifically
            keys_list[pygame.K_SPACE] = False
            # Use the modified keys
            keys = keys_list

        self.rocket.update(keys)  # update rocket on keypress
        # update screen on keypress
        self.display.blit(self.rocket.surf, self.rocket.rect)

        # after rocket lands
        # delays for 3 seconds and then displays results
        if self.rocket.is_landed is True:
            pygame.display.flip() # update the sprite to crash / successful landing
            # connects to database OR creates one if none is
            conn = sqlite3.connect('lunarlander.db')
            # creates cursor object to create queries
            cursor = conn.cursor()
            # creates table for DB if database does not exist yet
            cursor.execute(
                '''CREATE TABLE IF NOT EXISTS Attempts(
                attemptNum INTEGER PRIMARY KEY NOT NULL,
                attemptTime FLOAT,
                totalWeight INTEGER,
                totalFuel INTEGER,
                fuelRemaining INTEGER,
                attemptSuccess BOOLEAN)''')
            attemptQuery = "INSERT INTO Attempts VALUES (?, ?, ?, ?, ?, ?)"
            # run check to make sure attemptNum is equal to the next entry in database
            # this query returns number of attempts already in database
            cursor.execute('SELECT COUNT(attemptNum) FROM Attempts') 
            currentIteration = cursor.fetchone()

            initial_mass = BASE_ROCKET_AND_FUEL + getattr(self.gameStateManger, 'extra_mass', 0)
            fuel_used = initial_mass - int(self.rocket.algos.mass)
            remaining_fuel = BASE_FUEL_AMT - fuel_used

            values = (currentIteration[0]+1,
                    round(self.elapsed_time,1),
                    initial_mass,
                    BASE_FUEL_AMT,
                    self.rocket.algos.totalFuelMass,
                    self.rocket.safely_landed)
            # takes both the query and values and combines them to make a valid sql query to
            # insert post-flight information into the database
            cursor.execute(attemptQuery,values)
            conn.commit()
            conn.close()
            time.sleep(1)
            pygame.mixer.music.stop() # stops playing music once sim is finished
            self.reset()
            self.gameStateManger.set_state('results')


class OurFavoriteRocketShip(pygame.sprite.Sprite):
    def __init__(self, extra_mass=0):
        super().__init__()
        self.surf = tilapia_idle_img
        self.rect = self.surf.get_rect()

        self.rect.centerx = SCREENWIDTH // 2
        self.rect.bottom = ROCKET_BOTTOM

        self.is_landed = False
        self.is_successful = False  # False if crashed, True otherwise
        self.algos = MyAlgos(extra_mass)
        self.is_thrust = False
        self.downY = 0

    def thrust_switch(self):
        switch = " "
        if self.is_thrust:
            switch = "ON"
        if not self.is_thrust:
            switch = "OFF"
        return switch

    def update(self, pressed_key):
        if not self.is_landed:
            # passes boolean so Algos know if thrusters are activated
            self.downY = self.algos.move_down(pressed_key[pygame.K_SPACE])
            # Moves down on y axis at rate self.downY
            self.rect.move_ip(0, self.downY)

            if pressed_key[pygame.K_SPACE] == 1:
                self.surf = tilapia_thrust_img
                self.is_thrust = True
            else:
                self.surf = tilapia_idle_img
                self.is_thrust = False

        # Check if rocket has landed
        if self.rect.bottom >= SURFACE:
            if abs(self.algos.velocity) > SAFE_VELOCITY: # if velocity is greater than 200, result is crash
                self.safely_landed = False
                self.surf = tilapia_crash_img # change to crash sprite
            else:
                self.safely_landed = True
                self.surf = tilapia_success_img
                #self.is_successful = true
            self.is_landed = True
            #self.surf = tilapia_idle_img  # reset image to idle
            self.rect.bottom = SURFACE  # Stop vertical movement
        else:
            self.is_landed = False

        # Keep the rocket from flying off the screen
        # if self.rect.top < 0:
        #    self.rect.top = 0
        if self.rect.bottom > SURFACE:
            self.rect.bottom = SURFACE

    # def getDistance(self):
    #    # get the current distance in metters based on rocket position
    #    pixels_from_surface = (SURFACE - self.rect.bottom)
    #    #return pixels_from_surface // PXPERMETER
    #    return (pixels_from_surface / 756) * 100000

    def reset(self):
        self.is_landed = False
        self.algos.reset()
        self.rect.center = (SCREENWIDTH // 2, SCREENHEIGHT // 8)
        self.surf = tilapia_idle_img  # reset image to idle
