from tkinter import *
import random


class Dummy:
    def __init__(self, fonster):
        self.photo = PhotoImage(file=r"9/dummy.gif")
        self.label = Label(fonster, image=self.photo, borderwidth=0)
        self.posx = random.randint(0, 14)
        self.posy = random.randint(0, 14)

    def update(self):
        print("Dummy uppdaterar.")
        self.posx += random.randint(-1, 1)
        self.posy += random.randint(-1, 1)
        if self.posx < 0:
            self.posx = 0
        elif self.posx > 14:
            self.posx = 14
        if self.posy < 0:
            self.posy = 0
        elif self.posy > 14:
            self.posy = 14
        self.label.grid(column=self.posx, row=self.posy)
