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
        self.jump_points = []
        self.unvisisted = True

    def create_hyperlane(self, startpos, endpos, system) -> None:
        new_hyperlane = Hyperlane(startpos, endpos, self, system)
        self.hyperlanes.append(new_hyperlane)
        self.neighboring_systems.append(system)
        system.neighboring_systems.append(self)
        system.hyperlanes.append(new_hyperlane)

    def generate(self) -> None:
        self.unvisisted = False
        self.star = Star((0, 0), self.colour)
        PLANET_CONSTANT = 500
        MOON_CONSTANT = 7.5
        terrestial_planet_count = random.randint(1, 6)
        gas_count = random.randint(1, 6)
        for planet in range(terrestial_planet_count):
            angle = random.uniform(0, 2 * math.pi)
            hypotenuse = (
                PLANET_CONSTANT * (planet + 1) / (terrestial_planet_count + gas_count)
            )
            planet_object = Terrestial_Planet(
                (math.cos(angle) * hypotenuse, math.sin(angle) * hypotenuse),
                self.star,
                hypotenuse,
            )
            self.planets.append(planet_object)
            terrestial_moons_count = random.randint(0, 2)
            for terrestial_moon in range(terrestial_moons_count):
                angle = random.uniform(0, 2 * math.pi)
                hypotenuse = (
                    planet_object.size**0.5
                    * MOON_CONSTANT
                    * (terrestial_moon + 1)
                    / 2
                    + planet_object.size * 0.5
                )
                self.moons.append(
                    Terrestial_Moon(
                        (
                            math.cos(angle) * hypotenuse + planet_object.posx,
                            math.sin(angle) * hypotenuse + planet_object.posy,
                        ),
                        planet_object,
                        hypotenuse,
                    )
                )
        for gas in range(gas_count):
            angle = random.uniform(0, 2 * math.pi)
            hypotenuse = (
                PLANET_CONSTANT
                * (gas + terrestial_planet_count + 1)
                / (terrestial_planet_count + gas_count)
            )
            gas_object = Gas(
                (math.cos(angle) * hypotenuse, math.sin(angle) * hypotenuse),
                self.star,
                hypotenuse,
            )
            self.planets.append(gas_object)
            gas_moons_count = random.randint(1, 4)
            for gas_moon in range(gas_moons_count):
                angle = random.uniform(0, 2 * math.pi)
                hypotenuse = (
                    gas_object.size**0.5 * MOON_CONSTANT * (gas_moon + 1) / 4
                    + gas_object.size * 0.5
                )
                self.moons.append(
                    Terrestial_Moon(
                        (
                            math.cos(angle) * hypotenuse + gas_object.posx,
                            math.sin(angle) * hypotenuse + gas_object.posy,
                        ),
                        gas_object,
                        hypotenuse,
                    )
                )
        for jump_point in self.neighboring_systems:
            self.jump_points.append(Jump_Point())


class Hyperlane:
    def __init__(self, startpos, endpos, startstar, endstar) -> None:
        self.startpos = startpos
        self.startposx, self.startposy = startpos
        self.endpos = endpos
        self.endposx, self.endposy = endpos
        self.stars = startstar, endstar


class Celestial_Body:
    def __init__(self, position) -> None:
        self.posx, self.posy = position
        self.position = position


class Star(Celestial_Body):
    def __init__(self, position, colour) -> None:
        super().__init__(position)
        self.colour = colour
        self.size = 50


class Orbital(Celestial_Body):
    def __init__(self, position, orbit, hypotenuse) -> None:
        super().__init__(position)
        self.orbit = orbit
        self.hypotenuse = hypotenuse


class Terrestial(Orbital):
    def __init__(self, position, orbit, hypotenuse) -> None:
        super().__init__(position, orbit, hypotenuse)
        self.colour = random.choice(
            (
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
        )


class Gas(Orbital):
    def __init__(self, position, orbit, hypotenuse) -> None:
        super().__init__(position, orbit, hypotenuse)
        self.size = random.randint(20, 30)
        self.colour = random.choice(
            (
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
        )


class Terrestial_Planet(Terrestial):
    def __init__(self, position, orbit, hypotenuse) -> None:
        super().__init__(position, orbit, hypotenuse)
        self.size = random.randint(12, 25)


class Terrestial_Moon(Terrestial):
    def __init__(self, position, orbit, hypotenuse) -> None:
        super().__init__(position, orbit, hypotenuse)
        self.size = random.randint(5, 10)


class Jump_Point:
    def __init__(self) -> None:
        pass


class Ship:
    def __init__(self) -> None:
        self.colour = random.choice(
            (
                (186, 228, 253),
                (100, 140, 152),
                (90, 120, 139),
                (136, 172, 212),
                (72, 96, 129),
            )
        )


class Capital(Ship):
    def __init__(self) -> None:
        super().__init__()
        self.size = 5
        self.posx = 25
        self.posy = 25
