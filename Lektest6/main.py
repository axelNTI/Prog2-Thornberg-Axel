import random


class Rect:
    def __init__(self, height) -> None:
        self.width = 100
        self.height = height

    def area(self) -> int:
        return self.height * self.width


[
    print(j)
    for j in [i.area() for i in [Rect(random.randint(1, 500)) for _ in range(100)]]
    if j > 45000
]
