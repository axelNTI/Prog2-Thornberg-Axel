import random


class Celestial_Body:
    def __init__(self, position) -> None:
        self.posx, self.posy = position
        self.position = position

    def __str__(self) -> str:
        return str(self.__dict__)


class Star(Celestial_Body):
    def __init__(self, position, colour) -> None:
        super().__init__(position)
        self.colour = colour
        self.size = 50
        self.resources = {"Energy": random.randint(100, 200)}

    def __str__(self) -> str:
        return str(self.__dict__)


class Orbital(Celestial_Body):
    def __init__(self, position, orbit, hypotenuse) -> None:
        super().__init__(position)
        self.orbit = orbit
        self.hypotenuse = hypotenuse

    def __str__(self) -> str:
        return str(self.__dict__)


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

    def __str__(self) -> str:
        return str(self.__dict__)


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
        self.resources = {
            "Gas": random.randint(50, 150),
            "Energy": random.randint(10, 150),
        }

    def __str__(self) -> str:
        return str(self.__dict__)


class Terrestial_Planet(Terrestial):
    def __init__(self, position, orbit, hypotenuse) -> None:
        super().__init__(position, orbit, hypotenuse)
        self.size = random.randint(12, 25)
        self.resources = {
            "Energy": random.randint(10, 100),
            "Minerals": random.randint(10, 100),
            "Food": random.randint(0, 100),
        }

    def __str__(self) -> str:
        return str(self.__dict__)


class Terrestial_Moon(Terrestial):
    def __init__(self, position, orbit, hypotenuse) -> None:
        super().__init__(position, orbit, hypotenuse)
        self.size = random.randint(5, 10)
        self.resources = {
            "Energy": random.randint(5, 50),
            "Minerals": random.randint(5, 50),
        }

    def __str__(self) -> str:
        return str(self.__dict__)


class Jump_Point:
    def __init__(self) -> None:
        raise NotImplementedError

    def __str__(self) -> str:
        return str(self.__dict__)
