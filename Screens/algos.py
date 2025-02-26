class MyAlgos:
    def __init__(self):
        self.downards_movement = 1 #starting gravity value

    def move_down(self, firing_rockets): #weight of change
        if not firing_rockets:
            self.downards_movement += .05
        elif firing_rockets:
            self.downards_movement -= 0.05
        return self.downards_movement

    def reset(self):
        self.__init__()