import random

class System:
    def __init__(self, width, height, colour, radius, list_of_systems) -> None:
        self.posx = random.randint(radius, width - radius)
        self.posy = random.randint(radius, height - radius)
        self.colour = colour
        for obj in list_of_systems: