import random


class Fleet:
    def __init__(self, position: tuple[int]) -> None:
        self.position = self.posx, self.posy = position
        self.velocity = self.velx, self.vely = (0, 0)
        self.acceleration = self.accx, self.accy = (0, 0)
        self.ships = []
        self.target_position = None
        self.target_posx = None
        self.target_posy = None
        self.resources = {
            "Energy": 0,
            "Minerals": 0,
            "Alloys": 0,
            "Food": 0,
            "Consumer_goods": 0,
            "Volatile_motes": 0,
            "Exotic_gases": 0,
            "Rare_crystals": 0,
            "Living_metal": 0,
            "Zro": 0,
            "Dark_matter": 0,
            "Nanites": 0,
        }

    def __str__(self) -> str:
        return str(self.__dict__)


class Ship:
    def __init__(self, acceleration, x_offset, y_offset) -> None:
        self.acceleration = acceleration
        self.colour = random.choice(
            (
                (186, 228, 253),
                (100, 140, 152),
                (90, 120, 139),
                (136, 172, 212),
                (72, 96, 129),
            )
        )
        self.x_offset = x_offset
        self.y_offset = y_offset

    def __str__(self) -> str:
        return str(self.__dict__)

    def get_position_x(self, fleet: Fleet) -> int:
        return fleet.posx + self.x_offset

    def get_position_y(self, fleet: Fleet) -> int:
        return fleet.posy + self.y_offset


class Capital(Ship):
    def __init__(self) -> None:
        super().__init__(1, 0, 0)
        self.size = 5
        self.strategy = "defensive"

    def __str__(self) -> str:
        return str(self.__dict__)


class Manufactory(Ship):
    def __init__(self) -> None:
        super().__init__(acceleration=0.5)
        self.size = 3
        self.strategy = "withdrawal"

    def __str__(self) -> str:
        return str(self.__dict__)
