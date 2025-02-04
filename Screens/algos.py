class MyAlgos:
    def __init__(self):
        self.gravity_value = .5 #starting gravity value

    def gravity(self): #weight of change
        self.gravity_value += 1
        return self.gravity_value