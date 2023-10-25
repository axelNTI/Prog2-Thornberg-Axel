import pygame
import random
import itertools
from classes import *


# Personal links/comments for later:
# https://www.pygame.org/docs/ref/display.html#pygame.display.Info
# https://stackoverflow.com/questions/35617246/setting-a-fixed-fps-in-pygame-python-3
# https://www.geeksforgeeks.org/how-to-change-the-name-of-a-pygame-window/
# https://stackoverflow.com/questions/3838329/how-can-i-check-if-two-segments-intersect
#
#
#
# Fullscreen:
# display_window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#
# Borderless Windowed:
# display_window = pygame.display.set_mode((infoObject9.current_w, infoObject.current_h))


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
    def get_hyperlane_groups(system) -> list:
        for neighbor in system.neighboring_systems:
            get_hyperlane_groups(neighbor)

    def duplicate_removal() -> list:
        return list(
            dict.fromkeys(
                [
                    j
                    for sub in [object.hyperlanes for object in list_of_systems]
                    for j in sub
                ]
            )
        )

    for object_i in list_of_systems:
        list_of_systems_sorted = list(
            dict(
                sorted(
                    {
                        object_j: (
                            (object_j.posx - object_i.posx) ** 2
                            + (object_j.posy - object_i.posy) ** 2
                        )
                        ** 0.5
                        for object_j in list_of_systems
                        if object_i != object_j
                    }.items(),
                    key=lambda item: item[1],
                )
            ).keys()
        )
        i = 0
        hyperlane_amount = random.randint(1, 4)
        while hyperlane_amount > len(object_i.hyperlanes) and i < len(
            list_of_systems_sorted
        ):
            object_j = list_of_systems_sorted[i]
            if (
                object_i not in object_j.neighboring_systems
                and len(object_j.hyperlanes) < 4
            ):
                object_i.create_hyperlane(
                    object_i.position, object_j.position, object_j
                )
            i += 1
    list_of_clusters = []
    while len([j for sub in list_of_clusters for j in sub]) != len(list_of_systems):
        starting_system = random.choice(list_of_systems)
        list_of_clusters.append(starting_system)
        list_of_clusters = get_hyperlane_groups(starting_system)

    return duplicate_removal()


def game() -> None:
    def pygameRun() -> None:
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

    SYSTEM_RADIUS = 15
    SYSTEM_COUNT = 65
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
    list_of_hyperlanes = create_hyperlanes(list_of_systems)
    pygameRun()
    pygame.quit()


game()
