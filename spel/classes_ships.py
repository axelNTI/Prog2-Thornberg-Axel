import random


class Fleet:
    def __init__(self, position: tuple[int]) -> None:
        self.position = position
        self.posx, self.posy = position
        self.velocity_x, self.velocity_y = self.velocity = (0, 0)
        self.ships = []
        self.target_position = None

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

    def __str__(self) -> str:
        return str(self.__dict__)
