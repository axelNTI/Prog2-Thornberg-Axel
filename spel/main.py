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
    list_of_colours = (
        (255, 210, 125),
        (255, 163, 113),
        (166, 168, 255),
        (255, 250, 134),
        (168, 123, 255),
    )
    radius = 15
    list_of_systems = []
    for i in range(50):
        list_of_systems.append(
            System(
                width=infoObject.current_w,
                height=infoObject.current_h,
                colour=random.choice(list_of_colours),
                radius=radius,
                list_of_systems=list_of_systems,
            )
        )
    while True:
        # display_window.fill(
        #     (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # )
        display_window.fill((5, 5, 25))
        for obj in list_of_systems:
            pygame.draw.circle(
                surface=display_window,
                color=obj.colour,
                center=(obj.posx, obj.posy),
                radius=radius,
            )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.display.update()


pygameRun()
