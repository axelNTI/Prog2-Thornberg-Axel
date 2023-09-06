from random import *

class LivingThing:

    def __init__(self):
        pass
    
    def set_position(self, width, height):
        self.posx = randint(0, width - 1)
        self.posy = randint(0, height - 1)
        self.label.grid(column=self.posx, row=self.posy)