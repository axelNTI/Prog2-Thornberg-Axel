import random

list_of_colours = (
    (255, 210, 125),
    (255, 163, 113),
    (166, 168, 255),
    (255, 250, 134),
    (168, 123, 255),
)


class System:
    def __init__(self) -> None:
        self.colour = random.choice(list_of_colours)

    def set_position(self, radius, list_of_coordinates) -> list:
        self.posx, self.posy = random.choice(list_of_coordinates)
        list_of_coordinates.remove((self.posx, self.posy))
        return list_of_coordinates
