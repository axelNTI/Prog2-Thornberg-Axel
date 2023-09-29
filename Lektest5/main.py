import random


class Dice:
    def __init__(self) -> None:
        pass

    def roll(self) -> int:
        self.roll = random.randint(1, 6)
        if self.roll == 1:
            self.roll = random.randint(1, 6)
        return self.roll


list_of_dice = [Dice() for _ in range(1000)]

list_of_rolls = [object.roll() for object in list_of_dice]

average = sum(list_of_rolls) / len(list_of_rolls)
print(average)
