import random

list_of_colours = (
    (255, 210, 125),
    (255, 163, 113),
    (166, 168, 255),
    (255, 250, 134),
    (168, 123, 255),
)


class System:
    def __init__(self, position) -> None:
        self.colour = random.choice(list_of_colours)
        self.posx, self.posy = position
        self.hyperlanes = []
    
    def create_hyperlanes(self, startpos, endpos):
        self.hyperlanes.append([])


class Hyperlane:
    def __init__(self) -> None:
        pass
