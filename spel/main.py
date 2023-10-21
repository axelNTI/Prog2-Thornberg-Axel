import pygame
import random
import itertools
from classes import *


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


def create_systems(SYSTEM_COUNT, SYSTEM_RADIUS, WIDTH, HEIGHT) -> list:
    positions = random.sample(
        list(
            itertools.product(
                [
                    x
                    for x in range(
                        SYSTEM_RADIUS,
                        WIDTH - SYSTEM_RADIUS,
                        intround(2.5 * SYSTEM_RADIUS),
                    )
                ],
                [
                    y
                    for y in range(
                        SYSTEM_RADIUS,
                        HEIGHT - SYSTEM_RADIUS,
                        intround(2.5 * SYSTEM_RADIUS),
                    )
                ],
            )
        ),
        k=SYSTEM_COUNT,
    )
    list_of_systems = [System(position=positions[i]) for i in range(SYSTEM_COUNT)]
    return list_of_systems


def create_hyperlanes(list_of_systems) -> list:
    for object in list_of_systems:
        dict_of_distances = dict(
            sorted(
                {
                    object2: (
                        (object2.posx - object.posx) ** 2
                        + (object2.posy - object.posy) ** 2
                    )
                    ** 0.5
                    for object2 in list_of_systems
                    if object != object2
                }.items(),
                key=lambda item: item[1],
            )
        )
        i = 0
        hyperlane_amount = random.randint(2, 4)
        object_list = list(dict_of_distances.keys())
        while hyperlane_amount > len(object.hyperlanes):
            object2 = object_list[i]
            if object not in object2.hyperlanes and len(object2.hyperlanes) < 5:
                object.create_hyperlane(object.position, object2.position, object2)
            if i == len(object_list) - 1:
                break
            i += 1

    list_of_hyperlanes = list(
        dict.fromkeys(
            [
                j
                for sub in [object.hyperlanes for object in list_of_systems]
                for j in sub
            ]
        )
    )
    return list_of_systems, list_of_hyperlanes


def pygameSetup() -> None:
    SYSTEM_RADIUS = 15
    SYSTEM_COUNT = 50
    FRAME_RATE = 60
    pygame.init()
    infoObject = pygame.display.Info()
    WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
    display_window = pygame.display.set_mode(
        (infoObject.current_w, infoObject.current_h)
    )
    pygame.display.set_caption("Interstellar Exploration")
    # pygame.display.set_icon(Icon_name)
    clock = pygame.time.Clock()
    list_of_systems = create_systems(SYSTEM_COUNT, SYSTEM_RADIUS, WIDTH, HEIGHT)
    list_of_systems, list_of_hyperlanes = create_hyperlanes(list_of_systems)
    objects = list_of_systems, list_of_hyperlanes
    constants = display_window, SYSTEM_RADIUS, clock, FRAME_RATE
    pygameRun(objects, constants)


def pygameRun(objects, constants) -> None:
    list_of_systems, list_of_hyperlanes = objects
    display_window, SYSTEM_RADIUS, clock, FRAME_RATE = constants
    while True:
        display_window.fill((5, 5, 25))
        [
            pygame.draw.line(
                surface=display_window,
                color=(100, 100, 100),
                start_pos=object.startpos,
                end_pos=object.endpos,
                width=5,
            )
            for object in list_of_hyperlanes
        ]
        [
            pygame.draw.circle(
                surface=display_window,
                color=object.colour,
                center=(object.posx, object.posy),
                radius=SYSTEM_RADIUS,
            )
            for object in list_of_systems
        ]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return
        pygame.display.update()
        clock.tick(FRAME_RATE)


pygameSetup()
