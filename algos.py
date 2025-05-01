from constants import GRAVITY, MMOON, RMOON, FORCEOFTHRUST, SCREENWIDTH, SCREENHEIGHT, SURFACE, FONT, SCREEN, ROCKET_BOTTOM, VERTICAL_DISTANCE, FPS, METERPERPX, PXPERMETER, TOTALVERTICALDISTANCE
import time


class MyAlgos:
    def __init__(self):
        # starting values
        # fuel tank
        self.totalFuelMass = 100
        # the weight of the lander and its payload
        self.totalRawMass = 1000
        # mass
        self.mass = self.totalRawMass + self.totalFuelMass
        self.newMass = 0
        # velocity: m/s
        self.velocity = 10
        self.newVelocity = 0
        # height m
        self.height = TOTALVERTICALDISTANCE
        self.newHeight = 0
        # mass of fuel used
        self.massFuel = 10
        # tick speed
        self.tick = self.fpsToSecond(FPS)

        #get the starting position of the lander
        self.downards_movement = self.pixelMeterConversion(self.velocity)
        self.converted_height = self.pixelMeterConversion(self.height)

    #determines if the lander will activate thrusters
    def move_down(self, firing_rockets):
         if not firing_rockets or self.totalFuelMass <= 0:
            return self.freeFall()
         elif firing_rockets:
            return self.thrust()
    
    #uses various physics to calculate the thrust for velocity and height
    def thrust(self):

        self.newVelocity = self.avgVel(self.velocity, self.netAvgatT(self.fuelBurn(self.massFuel, self.tick), 
            self.gMoonAtH(self.height), self.mass, self.massFuel, self.tick), self.tick)
        self.newHeight = self.CurAlt(self.height, self.velocity, self.tick, self.netAvgatT(self.fuelBurn(self.massFuel, self.tick), 
            self.gMoonAtH(self.height), self.mass, self.massFuel, self.tick))
        self.velocity = self.newVelocity
        self.height = self.newHeight
        self.totalFuelMass = self.totalFuelMass - (self.massFuel * self.tick)
        self.mass = self.totalRawMass + self.totalFuelMass
        time.sleep(self.tick)
        self.downards_movement = self.pixelMeterConversion(self.velocity)
        return self.downards_movement

    #calculates the freefall for the lander for the velocity and the height
    def freeFall(self):
        self.newVelocity = self.velocity + self.netAvgWithoutThrust(self.gMoonAtH(self.height))
        self.newHeight = self.CurAlt(self.height, self.velocity, self.tick, self.netAvgWithoutThrust(self.gMoonAtH(self.height)))
        self.velocity = self.newVelocity
        self.height = self.newHeight
        time.sleep(self.tick)
        self.downards_movement = self.pixelMeterConversion(self.velocity)
        return self.downards_movement

    #converts the FPS from constants to seconds
    def fpsToSecond(self, fps):
        return 1/fps

    # Gravitational acceleration at a certain altitude
    # h = height in meters
    # g = moon gravity
    # Mm = mass of moon
    # Rm = radius of moon
    def gMoonAtH(self, h):
        return (GRAVITY * MMOON) / ((RMOON + h) ** 2)

    # calculates how much force is applied per kg
    # this is a 300 N to 1 Kg/s burn
    def fuelBurn(self, MfAtF, dt):
        return 3000 * (-MfAtF * dt)

    # Average acceleration at time t
    # Ft = thrust appled now
    # GmH = gravitatial accelearation at h altitude
    # Mltl = mass of lander with fuel before thrust is applied
    # MfAtF = mass of fuel used while thrusting to get Ft
    def netAvgatT(self, Ft, GmH, Mltl, MfAtF, dt):
        fuelConsumed = MfAtF * dt
        return ((Ft - GmH * Mltl) / (Mltl - (0.5) * fuelConsumed))

    #!FIXME need to account the weight aswell for freefall
    def netAvgWithoutThrust(self, GmH):
        return GmH

    # Average velocity Model
    # vT = velicity at current movment
    # vt-l = velocity at previous current movement
    # aT = net average acceleration
    # dt = (delta T) the change in time
    def avgVel(self, vtl, aT, dt):
        return vtl + aT * dt

    # Current Altitute Calculator
    # htl = height of the lander before
    # vtl = velocity of lander before
    # dt = (delta T) the change in time
    # aT = net average acceleration
    def CurAlt(self, htl, vtl, dt, aT):
        return htl - (vtl * dt) - (0.5 * aT * dt ** 2)

    # 243px-1026px (bottom of lander to surface of moon)
    # thus 783px = 100,000 <-- Superceded by 10000
    # 1px = 128m
    def pixelMeterConversion(self, meters):
        return meters / METERPERPX

    def reset(self):
        self.__init__()



