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

    def __str__(self) -> str:
        return str(self.__dict__)


class Ship:
    def __init__(self, acceleration) -> None:
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

    def __str__(self) -> str:
        return str(self.__dict__)


class Capital(Ship):
    def __init__(self) -> None:
        super().__init__(acceleration=5)
        self.size = 5
        self.x_offset = 0
        self.y_offset = 0

    def __str__(self) -> str:
        return str(self.__dict__)

    def get_position_x(self, fleet: Fleet) -> int:
        return fleet.posx + self.x_offset

    def get_position_y(self, fleet: Fleet) -> int:
        return fleet.posy + self.y_offset
