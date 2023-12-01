import random


class Fleet:
    def __init__(self) -> None:
        self.ships = []


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
        self.posx = 0
        self.posy = 0
