from animal import Animal
from tkinter import *
from random import *

class Sheep(Animal):

    def __init__(self, fonster, width, height, max_food):
        super().__init__(max_food)
        self.photo = PhotoImage(file= r"9/sheep.gif")
        self.label = Label(fonster, image=self.photo, borderwidth=0)
        self.set_position(width, height)