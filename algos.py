from constants import GRAVITY, MMOON, RMOON, FORCEOFTHRUST
import time
class MyAlgos:
    def __init__(self):
        self.gravity_value = 1 #starting gravity value
        #height of the lander
        h = 100000 #m

    def gravity(self): #weight of change
        self.gravity_value *= 1.005
        return self.gravity_value
    
    def fpsToSecond(fps):
        return 1/fps

    #Gravitational acceleration at a certain altitude
    #h = height in meters
    # g = moon gravity 
    # Mm = mass of moon 
    # Rm = radius of moon
    def gMoonAtH(h):
        return (GRAVITY * MMOON) / ((RMOON + h) ** 2)

    #calculates how much force is applied per kg
    #this is a 100 N to 1 Kg/s burn
    def fuelBurn(MfAtF, dt):
        return 100 * (MfAtF * dt)

    #Average acceleration at time t
    # Ft = thrust appled now
    # GmH = gravitatial accelearation at h altitude
    # Mltl = mass of lander with fuel before thrust is applied
    # MfAtF = mass of fuel used while thrusting to get Ft
    def netAvgatT(Ft, GmH, Mltl, MfAtF, dt):
        fuelConsumed = MfAtF * dt
        return ((Ft - GmH * Mltl) / (Mltl - (0.5) * fuelConsumed))

    
    def netAvgWithoutThrust(GmH):
        return GmH

    #Average velocity Model
    # vT = velicity at current movment
    # vt-l = velocity at previous current movement
    # aT = net average acceleration
    # dt = (delta T) the change in time
    def avgVel(vtl, aT, dt):
        return vtl + aT * dt

    #Current Altitute Calculator
    # htl = height of the lander before
    # vtl = velocity of lander before
    # dt = (delta T) the change in time
    # aT = net average acceleration
    def CurAlt(htl, vtl, dt, aT):
        return htl - (vtl * dt) - (0.5 * aT * dt ** 2)
    
        #243px-1026px (bottom of lander to surface of moon)
        #thus 783px = 100,000
        #1px = 128m
    def altitudeToPixel(altitude_M, topP=243, surfaceP=1026, initial_altitude=100000):
        #calculates the pixel range and meters per pixel
        Pixel_range = surfaceP - topP #1026 - 243 = 783
        m_per_pixel = initial_altitude / Pixel_range # 127.74 metters per px
        #determines how many pixels the altitude spans
        pixel_offset = altitude_M / m_per_pixel
        pixel_y = surfaceP - pixel_offset
        return pixel_y
    


    #Tests to ensure Algo correctness:

    #Tests the math for gMoonAtH
    #correct if the awnser is 1.58 m/s^2
    print("Test for Gravitatoinal Acceleration at height 20000m: ", gMoonAtH(20000), "PASS")
    #Tests for the fuel burn
    #correct if the awser is 1000 N
    print("Fuel burn is: ", fuelBurn(10, 1), "PASS")
    #Tests the math for Average Acceleratoin at Time
    #correct if the awnser is -1.12 m/s^2
    print("Test for Average Acceleratoin at time: ", netAvgatT(fuelBurn(10, 1), gMoonAtH(100000), 3000, 10, 1), "PASS")
    #Test for the Average velocity Model
    #correct if the awnser is 98.88 m/s
    print("Test for Average velocity model: ", avgVel(100, netAvgatT(fuelBurn(10, 1), gMoonAtH(100000), 3000, 10, 1), 1), "PASS")
    #Test for the current Altitute Calculator
    #correct if the awnser is 99901 m
    print("Test for Current Altitude: ", CurAlt(100000, 100, 1, -1.1170330701784104), "PASS")
    #test for pixel conversion
    print ("pixel for 100000m alt: ", altitudeToPixel(100000))
    print ("pixel for 0m alt: ", altitudeToPixel(0))
    #test for FPStoSecond
    print ("60 fps to second: ", fpsToSecond(60))

#starting values
    #mass
    mass = 3000
    newMass = 0
    #velocity: m/s
    velocity = 100
    newVelocity = 0
    #height m
    height = 100000
    newHeight = 0
    #mass of fuel used
    massFuel = 10
    #tick speed 
    tickSpeed = fpsToSecond(60)

#prints out the starting stats
    print("starting stats:")
    print("mass = ", mass)
    print("velocity = ", velocity)
    print("height = ", height)
    print(" ")


#if the velocity reaches 5 m/s then it starts to free fall and controls the fall to 5 m/s
    while height > 0:
        #thruster
        if velocity > 5:
            newVelocity = avgVel(velocity, netAvgatT(fuelBurn(massFuel, fpsToSecond(60)), gMoonAtH(height), mass, massFuel, fpsToSecond(60)), fpsToSecond(60))
            newHeight = CurAlt(height, velocity, fpsToSecond(60), netAvgatT(fuelBurn(massFuel, fpsToSecond(60)), gMoonAtH(height), mass, massFuel, fpsToSecond(60)))
            print("velocity: ", newVelocity, "m/s")
            print("height: ", newHeight, "m")
            print("pixels: ", altitudeToPixel(height))
            print("mass: ", mass, " kg")
            print(" ")
            velocity = newVelocity 
            height = newHeight
            mass = mass - (massFuel * fpsToSecond(60))
            time.sleep(fpsToSecond(60))

        #freefall
        if velocity < 5:
            newVelocity = velocity + netAvgWithoutThrust(gMoonAtH(height))
            newHeight = CurAlt(height, velocity, fpsToSecond(60), netAvgWithoutThrust(gMoonAtH(height)))
            print("velocity: ", newVelocity, "m/s")
            print("height: ", newHeight, "m")
            print("pixels: ", altitudeToPixel(height))
            print("mass: ", mass, " kg")
            print(" ")
            velocity = newVelocity 
            height = newHeight
            time.sleep(fpsToSecond(60))


#notes for relism:
#1. the thrust to weight ratio seems to be a bit off. relistically its only about 1/5th
#the ammount of force needed to stop. a converstion factor of 1000 N per kg/s insted of 100N would be better
#2. the inital conditions seem a bit off expecally the starting altitude and the velocity of decent
# relistically it should be around 10000-15000m with a velocity of 10m/s
#3. the mass relative to engine thrust is unrealistic. eather change the thrust ammount or decrease weight of lander