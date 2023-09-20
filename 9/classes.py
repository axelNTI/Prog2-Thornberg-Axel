from random import *
from tkinter import *


class LivingThing:
    def __init__(self, width, height):
        self.posx = randint(0, width - 1)
        self.posy = randint(0, height - 1)
        self.label.grid(column=self.posx, row=self.posy)


class Plant(LivingThing):
    def __init__(self, fonster, width, height):
        self.photo = PhotoImage(file=r"9/plant.gif")
        self.label = Label(fonster, image=self.photo, borderwidth=0)
        super().__init__(width, height)

    def grow(self, list_of_plants, fonster, width, height):
        list_of_plants.append(Plant(fonster, width, height))
        return list_of_plants


class Animal(LivingThing):
    def __init__(self, width, height, max_food):
        super().__init__(width, height)
        self.max_food = max_food
        self.current_food = max_food

    def update(self, width, height, list_of_animals):
        self.posx += randint(-1, 1)
        self.posy += randint(-1, 1)
        if not 0 <= self.posx < width - 1:
            self.posx = min([0, width - 1], key=lambda x: abs(x - self.posx))
        if not 0 <= self.posy < height - 1:
            self.posy = min([0, height - 1], key=lambda y: abs(y - self.posy))
        self.label.grid(column=self.posx, row=self.posy)
        self.current_food -= 1
        if self.current_food <= 0:
            list_of_animals.remove(self)
            self.label.destroy()
        return list_of_animals


class Sheep(Animal):
    def __init__(self, fonster, width, height, max_food):
        self.photo = PhotoImage(file=r"9/sheep.gif")
        self.label = Label(fonster, image=self.photo, borderwidth=0)
        self.food = Plant
        super().__init__(width, height, max_food)


class Wolf(Animal):
    def __init__(self, fonster, width, height, max_food):
        self.photo = PhotoImage(file=r"9/wolf.gif")
        self.label = Label(fonster, image=self.photo, borderwidth=0)
        self.food = Sheep
        super().__init__(width, height, max_food)
