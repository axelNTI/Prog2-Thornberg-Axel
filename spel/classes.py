import random


class System:
    def __init__(self, position) -> None:
        self.colour = random.choice(
            (
                (255, 210, 125),
                (255, 163, 113),
                (166, 168, 255),
                (255, 250, 134),
                (168, 123, 255),
            )
        )
        self.posx, self.posy = position
        self.position = position
        self.hyperlanes = []
        self.neighboring_systems = []
        self.celestial_objects = []
        self.unvisisted = True

    def create_hyperlane(self, startpos, endpos, system) -> None:
        new_hyperlane = Hyperlane(startpos, endpos, self, system)
        self.hyperlanes.append(new_hyperlane)
        self.neighboring_systems.append(system)
        system.neighboring_systems.append(self)
        system.hyperlanes.append(new_hyperlane)

    def generate(self, colour) -> None:
        self.unvisisted = False
        star_amount = random.randint(1, 3)
        for i in range(star_amount):
            if star_amount == 1:
                pass
            else:
                if random.randint(1, 2) == 1:
                    pass
                else:
                    pass


class Hyperlane:
    def __init__(self, startpos, endpos, startstar, endstar) -> None:
        self.startpos = startpos
        self.endpos = endpos
        self.stars = startstar, endstar


class Celestial_Object:
    def __init__(self) -> None:
        pass


class Star(Celestial_Object):
    def __init__(self, colour) -> None:
        super().__init__()
        self.colour = colour


class Planet(Celestial_Object):
    def __init__(self) -> None:
        super().__init__()


class Moon(Celestial_Object):
    def __init__(self) -> None:
        super().__init__()
