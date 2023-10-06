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
# Borderless Windowed:
# display_window = pygame.display.set_mode((infoObject9.current_w, infoObject.current_h))
#
def intround(flo) -> int:
    return int(round(flo, 0))


def pygameSetup() -> None:
    RADIUS = 15
    SYSTEM_COUNT = 25
    pygame.init()
    infoObject = pygame.display.Info()
    display_window = pygame.display.set_mode(
        (infoObject.current_w, infoObject.current_h)
    )
    pygame.display.set_caption("Interstellar Exploration")
    # pygame.display.set_icon(Icon_name)
    list_of_systems = [System() for i in range(SYSTEM_COUNT)]
    list_of_coordinates = []
    for x in range(RADIUS, infoObject.current_w - RADIUS, intround(2.5 * RADIUS)):
        for y in range(RADIUS, infoObject.current_h - RADIUS, intround(2.5 * RADIUS)):
            list_of_coordinates.append((x, y))
    for object in list_of_systems:
        list_of_coordinates = object.set_position(
            radius=RADIUS, list_of_coordinates=list_of_coordinates
        )
    clock = pygame.time.Clock()
    pygameRun(display_window, list_of_systems, RADIUS, clock)


def pygameRun(display_window, list_of_systems, RADIUS, clock) -> None:
    while True:
        display_window.fill((5, 5, 25))
        for object in list_of_systems:
            pygame.draw.circle(
                surface=display_window,
                color=object.colour,
                center=(object.posx, object.posy),
                radius=RADIUS,
            )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return
        pygame.display.update()
        clock.tick(60)
    

pygameSetup()
