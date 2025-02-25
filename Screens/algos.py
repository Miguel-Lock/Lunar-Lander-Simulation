class MyAlgos:
    def __init__(self):
        self.gravity_value = 1 #starting gravity value

    def gravity(self): #weight of change
        self.gravity_value *= 1.005
        return self.gravity_value

    def reset(self):
        self.__init__()