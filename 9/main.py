# Importerar modulen tkinter och klassen Dummy
from tkinter import *
from plant import Plant
from sheep import Sheep
from wolf import Wolf
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
list_of_plants = [Plant(fonster, width, height) for i in range(1)]
list_of_sheep = [Sheep(fonster, width, height, 35) for i in range(1)]
list_of_wolves = [Wolf(fonster, width, height, 35) for i in range(1)]

list_of_plant_positions = [(object.posx, object.posy) for object in list_of_plants]
list_of_sheep_positions = [(object.posx, object.posy) for object in list_of_sheep]


# Kör update()-funktionen för alla instanser av Dummy Klassen i listan.
def update_all_objects():
    global list_of_sheep
    global list_of_sheep_positions
    global list_of_plant_positions
    global list_of_plants
    global list_of_wolves
    for object in list_of_sheep:
        list_of_sheep, list_of_plant_positions = object.move(
            width, height, list_of_sheep, list_of_plant_positions
        )
    for object in list_of_plants:
        if (object.posx, object.posy) not in list_of_plant_positions:
            object.label.destroy()
    for object in list_of_wolves:
        list_of_wolves, list_of_sheep_positions = object.move(
            width, height, list_of_wolves, list_of_sheep_positions
        )
    for object in list_of_sheep:
        if (object.posx, object.posy) not in list_of_sheep_positions:
            object.label.destroy()

    fonster.after(time_between_updates, update_all_objects)


fonster.after(time_between_updates, update_all_objects)
fonster.mainloop()
