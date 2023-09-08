# Importerar modulen tkinter och klassen Dummy
from tkinter import *
from dummy import Dummy
from plant import Plant
from animal import Animal
from sheep import Sheep
from random import *

# Definerar storleken på skärmen samt hur ofta den uppdateras
time_between_updates = 100  # i millisekunder
width = 15  # antal rutor
height = 15  # antal rutor


# Skapar fönstret
fonster = Tk()

# Fyller det med tomma rutor (Jag använder VSCode)
empty = PhotoImage(file=r"9/empty.gif")


#
for i in range(width):
    for j in range(height):
        etikett = Label(fonster, image=empty, borderwidth=0)
        etikett.grid(column=i, row=j)


# Skapar en lista av flera instanser av Dummy Klassen
# list_of_objects = [Dummy(fonster) for i in range(10)]
list_of_plants = [Plant(fonster, width, height) for i in range(10)]
list_of_animals = [Sheep(fonster, width, height, 35) for i in range(10)]

list_of_plant_positions = [(object.posx, object.posy) for object in list_of_plants]


# Kör update()-funktionen för alla instanser av Dummy Klassen i listan.
def update_all_objects():
    global list_of_animals
    [
        object.move(width, height, list_of_animals, list_of_plant_positions)
        for object in list_of_animals
    ]
    fonster.after(time_between_updates, update_all_objects)


fonster.after(time_between_updates, update_all_objects)
fonster.mainloop()
