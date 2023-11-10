import random
import math


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
        self.planets = []
        self.moons = []
        self.unvisisted = True

    def create_hyperlane(self, startpos, endpos, system) -> None:
        new_hyperlane = Hyperlane(startpos, endpos, self, system)
        self.hyperlanes.append(new_hyperlane)
        self.neighboring_systems.append(system)
        system.neighboring_systems.append(self)
        system.hyperlanes.append(new_hyperlane)

    def generate(self) -> None:
        self.unvisisted = False
        self.star = Star((0, 0), self.colour, None)
        terrestial_count = random.randint(1, 6)
        gas_count = random.randint(1, 6)
        for planet in range(terrestial_count):
            angle = random.uniform(0, 2 * math.pi)
            self.planets.append(
                Planet(
                    (math.cos(angle) * (planet + 1), math.sin(angle) * (planet + 1)),
                    self.star,
                )
            )
            terrestial_moons = random.randint(0, 2)


class Hyperlane:
    def __init__(self, startpos, endpos, startstar, endstar) -> None:
        self.startpos = startpos
        self.endpos = endpos
        self.stars = startstar, endstar


class Celestial_Object:
    def __init__(self, position, orbit) -> None:
        self.position = position
        self.orbit = orbit


class Star(Celestial_Object):
    def __init__(self, position, orbit, colour) -> None:
        super().__init__(position, orbit)
        self.colour = colour


class Planet(Celestial_Object):
    def __init__(self, position, orbit) -> None:
        super().__init__(position, orbit)


class Terrestial(Planet):
    def __init__(self, position, orbit) -> None:
        super().__init__(position, orbit)
        self.colour = random.choice(
            (240, 231, 231),
            (69, 24, 4),
            (193, 68, 14),
            (231, 125, 17),
            (253, 166, 0),
            (79, 76, 176),
            (107, 147, 214),
            (233, 239, 249),
            (159, 193, 100),
            (216, 197, 150),
            (248, 226, 176),
            (238, 203, 139),
            (227, 187, 118),
            (211, 165, 103),
            (173, 141, 84),
            (231, 232, 236),
            (173, 168, 165),
            (177, 173, 173),
            (140, 140, 148),
            (104, 105, 109),
        )


class Gas(Planet):
    def __init__(self, position, orbit) -> None:
        super().__init__(position, orbit)
        self.colour = random.choice(
            (237, 219, 173),
            (226, 191, 125),
            (195, 146, 79),
            (252, 238, 173),
            (196, 176, 139),
            (175, 219, 245),
            (147, 205, 241),
            (98, 174, 231),
            (66, 150, 220),
            (46, 132, 206),
            (71, 126, 253),
            (116, 214, 253),
            (61, 94, 249),
            (43, 55, 139),
            (31, 34, 85),
            (180, 167, 158),
            (220, 208, 184),
            (209, 167, 127),
            (227, 218, 223),
            (221, 180, 126),
        )


class Moon(Celestial_Object):
    def __init__(self, position, orbit) -> None:
        super().__init__(position, orbit)
