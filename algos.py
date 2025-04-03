from constants import GRAVITY, MMOON, RMOON, FORCEOFTHRUST, SCREENWIDTH, SCREENHEIGHT, SURFACE, FONT, SCREEN, ROCKET_BOTTOM, VERTICAL_DISTANCE, FPS, METERPERPX, PXPERMETER
import time


class MyAlgos:
    def __init__(self, extra_mass=0):
        # starting values
        # mass
        self.mass = 3000 + extra_mass
        self.newMass = 0
        # velocity: m/s
        self.velocity = 100
        self.newVelocity = 0
        # height m
        self.height = 100000
        self.newHeight = 0
        # mass of fuel used
        self.massFuel = 10
        # tick speed

        self.downards_movement = self.pixelMeterConversion(self.velocity)

    def move_down(self, firing_rockets):  # weight of change
        if not firing_rockets:
            # self.downards_movement += .05

            self.newVelocity = self.velocity + \
                self.netAvgWithoutThrust(self.gMoonAtH(self.height))
            self.newHeight = self.CurAlt(self.height, self.velocity, self.fpsToSecond(
                60), self.netAvgWithoutThrust(self.gMoonAtH(self.height)))
            self.velocity = self.newVelocity
            self.height = self.newHeight
            time.sleep(self.fpsToSecond(60))

            self.downards_movement = self.pixelMeterConversion(self.velocity)
        elif firing_rockets:
            # self.downards_movement -= 0.05

            self.newVelocity = self.avgVel(self.velocity, self.netAvgatT(self.fuelBurn(self.massFuel, self.fpsToSecond(
                60)), self.gMoonAtH(self.height), self.mass, self.massFuel, self.fpsToSecond(60)), self.fpsToSecond(60))
            self.newHeight = self.CurAlt(self.height, self.velocity, self.fpsToSecond(60), self.netAvgatT(self.fuelBurn(
                self.massFuel, self.fpsToSecond(60)), self.gMoonAtH(self.height), self.mass, self.massFuel, self.fpsToSecond(60)))
            self.velocity = self.newVelocity
            self.height = self.newHeight
            self.mass = self.mass - (self.massFuel * self.fpsToSecond(60))
            time.sleep(self.fpsToSecond(60))

            self.downards_movement = self.pixelMeterConversion(self.velocity)
        return self.downards_movement

    def gravity(self):  # weight of change
        self.gravity_value *= 1.005
        return self.gravity_value

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
    # this is a 100 N to 1 Kg/s burn
    def fuelBurn(self, MfAtF, dt):
        # SOMETHING IS WRONG HERE!!!!!!! The rEtURN NUMBER SHOULD NOT BE SO BIG!
        return -1500000 * (MfAtF * dt)

    # Average acceleration at time t
    # Ft = thrust appled now
    # GmH = gravitatial accelearation at h altitude
    # Mltl = mass of lander with fuel before thrust is applied
    # MfAtF = mass of fuel used while thrusting to get Ft
    def netAvgatT(self, Ft, GmH, Mltl, MfAtF, dt):
        fuelConsumed = MfAtF * dt
        return ((Ft - GmH * Mltl) / (Mltl - (0.5) * fuelConsumed))

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
    # thus 783px = 100,000
    # 1px = 128m
    def pixelMeterConversion(self, meters):
        #return (meters * VERTICAL_DISTANCE) / 100000
        return meters / METERPERPX

    def reset(self):
        self.__init__()


# notes for relism:
# 1. the thrust to weight ratio seems to be a bit off. relistically its only about 1/5th
# the ammount of force needed to stop. a converstion factor of 1000 N per kg/s insted of 100N would be better
# 2. the inital conditions seem a bit off expecally the starting altitude and the velocity of decent
# relistically it should be around 10000-15000m with a velocity of 10m/s
# 3. the mass relative to engine thrust is unrealistic. eather change the thrust ammount or decrease weight of lander
