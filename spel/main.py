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
    return list(
        dict.fromkeys(
            [
                j
                for sub in [object.hyperlanes for object in list_of_systems]
                for j in sub
            ]
        )
    )


def game() -> None:
    SYSTEM_RADIUS = 15
    SYSTEM_COUNT = 65
    FRAME_RATE = 60
    star_view = False
    pygame.init()
    infoObject = pygame.display.Info()
    WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
    display_window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Interstellar Exploration")
    # pygame.display.set_icon(Icon_name)
    clock = pygame.time.Clock()
    list_of_systems = create_systems(SYSTEM_COUNT, SYSTEM_RADIUS, WIDTH, HEIGHT)
    list_of_hyperlanes = create_hyperlanes(list_of_systems)
    current_system = random.choice(list_of_systems)
    current_system.generate()
    values = (
        display_window,
        list_of_hyperlanes,
        SYSTEM_RADIUS,
        list_of_systems,
        clock,
        FRAME_RATE,
        star_view,
        current_system,
    )
    pygameRun(values)
    pygame.quit()


def pygameRun(values) -> None:
    (
        display_window,
        list_of_hyperlanes,
        SYSTEM_RADIUS,
        list_of_systems,
        clock,
        FRAME_RATE,
        star_view,
        current_system,
    ) = values
    while True:
        if star_view:
            display_window.fill((5, 5, 25))
            [
                pygame.draw.circle(
                    surface=display_window,
                    color=object.colour,
                    center=(object.posx, object.posy),
                    radius=SYSTEM_RADIUS,
                )
                for object in current_system.stars
                + current_system.planets
                + current_system.moons
            ]
        else:
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
                if event.key == pygame.K_m:
                    star_view = not star_view
        pygame.display.update()
        clock.tick(FRAME_RATE)


game()
