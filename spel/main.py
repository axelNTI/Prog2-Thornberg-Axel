import pygame
import random
import itertools
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
def intround(value) -> int:
    return int(round(value, 0))


def create_systems(SYSTEM_COUNT, SYSTEM_RADIUS, width, height) -> list:
    list_of_systems = [System() for i in range(SYSTEM_COUNT)]
    positions = random.sample(
        list(
            itertools.product(
                [
                    x
                    for x in range(
                        SYSTEM_RADIUS,
                        width - SYSTEM_RADIUS,
                        intround(2.5 * SYSTEM_RADIUS),
                    )
                ],
                [
                    y
                    for y in range(
                        SYSTEM_RADIUS,
                        height - SYSTEM_RADIUS,
                        intround(2.5 * SYSTEM_RADIUS),
                    )
                ],
            )
        ),
        k=SYSTEM_COUNT,
    )
    [
        object.set_position(position=positions[list_of_systems.index(object)])
        for object in list_of_systems
    ]
    return list_of_systems


def create_hyperlanes(list_of_systems) -> list:
    return


def pygameSetup() -> None:
    SYSTEM_RADIUS = 15
    SYSTEM_COUNT = 25
    pygame.init()
    infoObject = pygame.display.Info()
    width, height = infoObject.current_w, infoObject.current_h
    display_window = pygame.display.set_mode(
        (infoObject.current_w, infoObject.current_h)
    )
    pygame.display.set_caption("Interstellar Exploration")
    # pygame.display.set_icon(Icon_name)
    clock = pygame.time.Clock()
    list_of_systems = create_systems(SYSTEM_COUNT, SYSTEM_RADIUS, width, height)
    list_of_hyperlanes = create_hyperlanes(list_of_systems)
    pygameRun(display_window, list_of_systems, SYSTEM_RADIUS, clock)


def pygameRun(display_window, list_of_systems, SYSTEM_RADIUS, clock) -> None:
    while True:
        display_window.fill((5, 5, 25))
        for object in list_of_systems:
            pygame.draw.circle(
                surface=display_window,
                color=object.colour,
                center=(object.posx, object.posy),
                radius=SYSTEM_RADIUS,
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
