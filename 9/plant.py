from living_thing import LivingThing
from tkinter import *
from random import *


class Plant(LivingThing):
    def __init__(self, fonster, width, height):
        super().__init__()
        self.photo = PhotoImage(file=r"9/plant.gif")
        self.label = Label(fonster, image=self.photo, borderwidth=0)
        self.set_position(width, height)
