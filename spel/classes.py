import random


class System:
    def __init__(self, position) -> None:
        self.colour = random.choice((
            (255, 210, 125),
            (255, 163, 113),
            (166, 168, 255),
            (255, 250, 134),
            (168, 123, 255),
        ))
        self.posx, self.posy = position
        self.position = position
        self.hyperlanes = []
        self.connected_systems = []

    def create_hyperlane(self, startpos, endpos, object) -> None:
        new_hyperlane = Hyperlane(startpos, endpos, self, object)
        self.hyperlanes.append(new_hyperlane)
        self.connected_systems.append(object)
        object.connected_systems.append(self)
        object.hyperlanes.append(new_hyperlane)


class Hyperlane:
    def __init__(self, startpos, endpos, startstar, endstar) -> None:
        self.startpos = startpos
        self.endpos = endpos
        self.stars = startstar, endstar
