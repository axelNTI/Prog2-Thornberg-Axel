from living_thing import LivingThing
from tkinter import *
from random import *


class Animal(LivingThing):
    def __init__(self, max_food):
        super().__init__()
        self.max_food = max_food
        self.current_food = max_food

    def move(self, width, height, list_of_animals, list_of_plant_positions, food):
        self.posx += randint(-1, 1)
        self.posy += randint(-1, 1)
        if not 0 <= self.posx < width - 1:
            self.posx = min([0, width - 1], key=lambda x: abs(x - self.posx))
        if not 0 <= self.posy < height - 1:
            self.posy = min([0, height - 1], key=lambda y: abs(y - self.posy))
        self.label.grid(column=self.posx, row=self.posy)
        self.current_food -= 1
        if food == 'plant':
            if [(self.posx, self.posy == posx, posy) for posx, posy in list_of_plant_positions]:
                list_of_plant_positions.remove((self.posx, self.posy))
                self.current_food = self.max_food
        print(self.current_food)
        if self.current_food <= 0:
            list_of_animals.remove(self)
            self.label.destroy()
        return (list_of_animals, list_of_plant_positions)
