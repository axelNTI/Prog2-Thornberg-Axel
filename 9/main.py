# Importerar modulen tkinter och klassen Dummy
from tkinter import *
from classes import Plant, Sheep, Wolf

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


list_of_plants = [Plant(fonster, width, height) for i in range(15)]
list_of_sheep = [Sheep(fonster, width, height, 35) for i in range(5)]
list_of_wolves = [Wolf(fonster, width, height, 35) for i in range(2)]

tick = 0


def update_all_objects():
    global list_of_plant_positions
    global list_of_sheep_positions
    global list_of_wolf_positions
    global list_of_plants
    global list_of_sheep
    global list_of_wolves

    global tick

    for object in list_of_sheep + list_of_wolves:
        list_of_plant_positions = {
            object: (object.posx, object.posy) for object in list_of_plants
        }
        list_of_sheep_positions = {
            object: (object.posx, object.posy) for object in list_of_sheep
        }
        list_of_wolf_positions = {
            object: (object.posx, object.posy) for object in list_of_wolves
        }
        if isinstance(object, Sheep):
            object.update(width, height, list_of_sheep)
            for object2 in list_of_plant_positions:
                if (object.posx, object.posy) == list_of_plant_positions[object2]:
                    list_of_plants.remove(object2)
                    object2.label.destroy()
                    object.current_food = object.max_food
                    break

        elif isinstance(object, Wolf):
            object.update(width, height, list_of_wolves)
            for object2 in list_of_sheep_positions:
                if (object.posx, object.posy) == list_of_sheep_positions[object2]:
                    list_of_sheep.remove(object2)
                    object2.label.destroy()
                    object.current_food = object.max_food
                    break

    tick += 1

    if tick % 10 == 0:
        for i in range(len(list_of_plants)):
            list_of_plants = list_of_plants[i].grow(
                list_of_plants, fonster, width, height
            )

    fonster.after(time_between_updates, update_all_objects)


fonster.after(time_between_updates, update_all_objects)
fonster.mainloop()
