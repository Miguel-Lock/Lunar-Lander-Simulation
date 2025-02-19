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
    

    #Gravitational acceleration at a certain altitude
    #h = height in meters
    # g = moon gravity 
    # Mm = mass of moon 
    # Rm = radius of moon
    def gMoonAtH(h):
        return (GRAVITY * MMOON) / ((RMOON + h) ** 2)

    #calculates how much force is applied per kg
    #this is a 100 N to 1 Kg/s burn
    def fuelBurn(MfAtF):
        return 100 * MfAtF

    #Average acceleration at time t
    # Ft = thrust appled now
    # GmH = gravitatial accelearation at h altitude
    # Mltl = mass of lander with fuel before thrust is applied
    # MfAtF = mass of fuel used while thrusting to get Ft
    def netAvgatT(Ft, GmH, Mltl, MfAtF):
        return ((Ft - GmH * Mltl) / (Mltl - (0.5) * MfAtF))

    
    def netAvgWithoutThrust(GmH):
        return GmH

    #Average velocity Model
    # vT = velicity at current movment
    # vt-l = velocity at previous current movement
    # aT = net average acceleration
    # dt = (delta T) the change in time
    def avgVel(vtl, aT, dt):
        return (vtl + aT) * dt

    #Current Altitute Calculator
    # htl = height of the lander before
    # vtl = velocity of lander before
    # dt = (delta T) the change in time
    # aT = net average acceleration
    def CurAlt(htl, vtl, dt, aT):
        return htl - (vtl * dt) - (0.5 * aT * dt ** 2)


    #Tests to ensure Algo correctness:

    #Tests the math for gMoonAtH
    #correct if the awnser is 1.58 m/s^2
    print("Test for Gravitatoinal Acceleration at height 20000m: ", gMoonAtH(20000), "PASS")
    #Tests for the fuel burn
    #correct if the awser is 1000 N
    print("Fuel burn is: ", fuelBurn(10), "PASS")
    #Tests the math for Average Acceleratoin at Time
    #correct if the awnser is -1.12 m/s^2
    print("Test for Average Acceleratoin at time: ", netAvgatT(fuelBurn(10), gMoonAtH(100000), 3000, 10), "PASS")
    #Test for the Average velocity Model
    #correct if the awnser is 98.88 m/s
    print("Test for Average velocity model: ", avgVel(100, netAvgatT(fuelBurn(10), gMoonAtH(100000), 3000, 10), 1), "PASS")
    #Test for the current Altitute Calculator
    #correct if the awnser is 99901 m
    print("Test for Current Altitude: ", CurAlt(100000, 100, 1, -1.1170330701784104), "PASS")


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

#prints out the starting stats
    print("starting stats:")
    print("mass = ", mass)
    print("velocity = ", velocity)
    print("height = ", height)
    print(" ")

#this is a test with the above starting values where the lander startes at a height of 100000m and imediatly applies thrusters
    while velocity > 5:
        newVelocity = avgVel(velocity, netAvgatT(fuelBurn(massFuel), gMoonAtH(height), mass, massFuel), 1)
        newHeight = CurAlt(height, velocity, 1, netAvgatT(fuelBurn(massFuel), gMoonAtH(height), mass, massFuel))
        print("velocity: ", newVelocity, "m/s")
        print("height: ", newHeight, "m")
        print("mass: ", mass, " kg")
        print(" ")
        velocity = newVelocity 
        height = newHeight
        mass = mass - massFuel
        time.sleep(1)

# #this is a test with the above starting values where the lander is just fee falling from 100000m
#     while height >= 0:
#         newVelocity = velocity + netAvgWithoutThrust(gMoonAtH(height))
#         newHeight = CurAlt(height, velocity, 1, netAvgWithoutThrust(gMoonAtH(height)))
#         print("velocity: ", newVelocity, "m/s")
#         print("height: ", newHeight, "m")
#         print("mass: ", mass, " kg")
#         print(" ")
#         velocity = newVelocity 
#         height = newHeight
#         #time.sleep(1)

        