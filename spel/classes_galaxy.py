import random
import math
from classes_system import *


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
