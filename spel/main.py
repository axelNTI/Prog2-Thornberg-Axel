import pygame
import random
from classes import System

# Personal links/comments for later:
# https://www.pygame.org/docs/ref/display.html#pygame.display.Info
# https://stackoverflow.com/questions/35617246/setting-a-fixed-fps-in-pygame-python-3
# https://www.geeksforgeeks.org/how-to-change-the-name-of-a-pygame-window/
#
#
#
# Fullscreen:
# display_window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#
# Windowed Fullscreen:
# display_window = pygame.display.set_mode((infoObject9.current_w, infoObject.current_h))
#


def pygameRun() -> None:
    pygame.init()
    infoObject = pygame.display.Info()
    display_window = pygame.display.set_mode(
        (infoObject.current_w, infoObject.current_h)
    )
    pygame.display.set_caption("Interstellar Exploration")
    # pygame.display.set_icon(Icon_name)
    radius = 15
    system_count = 1
    list_of_systems = [System() for i in range(system_count)]
    list_of_coordinates = []
    for posx in range(radius, infoObject.current_w - radius):
        for posy in range(radius, infoObject.current_h - radius):
            list_of_coordinates.append((posx, posy))
    for object in list_of_systems:
        list_of_coordinates = object.set_position(
            radius=radius, list_of_coordinates=list_of_coordinates
        )
    while True:
        display_window.fill((5, 5, 25))
        for object in list_of_systems:
            pygame.draw.circle(
                surface=display_window,
                color=object.colour,
                center=(object.posx, object.posy),
                radius=radius,
            )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.update()


pygameRun()
