import pygame_gui
import pygame
import random
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


def intround(value: float) -> int:
    return int(round(value, 0))


def create_systems(SYSTEM_COUNT: int) -> list:
    positions = random.sample(
        [(x, y) for x in range(1, 30) for y in range(1, 30)],
        k=SYSTEM_COUNT,
    )
    return [System(position=positions[i]) for i in range(SYSTEM_COUNT)]


def create_hyperlanes(system_arr: list) -> list:
    for object_i in system_arr:
        system_arr_sorted = list(
            dict(
                sorted(
                    {
                        object_j: (
                            (object_j.posx - object_i.posx) ** 2
                            + (object_j.posy - object_i.posy) ** 2
                        )
                        ** 0.5
                        for object_j in system_arr
                        if object_i != object_j
                    }.items(),
                    key=lambda item: item[1],
                )
            ).keys()
        )
        i = 0
        hyperlane_amount = random.randint(1, 4)
        while hyperlane_amount > len(object_i.hyperlanes) and i < len(
            system_arr_sorted
        ):
            object_j = system_arr_sorted[i]
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
            [j for sub in [object.hyperlanes for object in system_arr] for j in sub]
        )
    )


def game_setup() -> None:
    SYSTEM_COUNT = 65
    FRAME_RATE = 60
    pygame.init()
    infoObject = pygame.display.Info()
    WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
    SCALE = min(WIDTH, HEIGHT) / 1080
    display_window = pygame.display.set_mode((WIDTH, HEIGHT))
    manager = pygame_gui.UIManager((WIDTH, HEIGHT))
    current_view = "main_menu"
    pygame.display.set_caption("Interstellar Exploration")
    # pygame.display.set_icon(Icon_name)
    clock = pygame.time.Clock()
    system_arr = create_systems(SYSTEM_COUNT)
    hyperlane_arr = create_hyperlanes(system_arr)
    current_system = random.choice(system_arr)
    current_system.generate()
    pygame_run(
        display_window,
        hyperlane_arr,
        system_arr,
        clock,
        FRAME_RATE,
        current_system,
        WIDTH,
        HEIGHT,
        SCALE,
        current_view,
        manager,
    )
    pygame.quit()


def main_menu_mode(
    display_window: pygame.surface.Surface, manager: pygame_gui.ui_manager.UIManager
):
    hello_button = pygame_gui.elements.UIButton(
        relative_rect=pygame.Rect((350, 275), (100, 50)),
        text="Say Hello",
        manager=manager,
    )


def system_view_mode(
    display_window: pygame.surface.Surface,
    current_system: object,
    WIDTH: int,
    HEIGHT: int,
    SCALE: float,
) -> str:
    display_window.fill((5, 5, 25))
    [
        pygame.draw.circle(
            surface=display_window,
            color=(100, 100, 100),
            center=(
                intround(object.orbit.posx * SCALE + WIDTH / 2),
                intround(object.orbit.posy * SCALE + HEIGHT / 2),
            ),
            radius=intround(object.hypotenuse * SCALE),
            width=intround(1 * SCALE),
        )
        for object in current_system.planets + current_system.moons
    ]
    [
        pygame.draw.circle(
            surface=display_window,
            color=object.colour,
            center=(
                intround(SCALE * object.posx + WIDTH / 2),
                intround(SCALE * object.posy + HEIGHT / 2),
            ),
            radius=intround(object.size * SCALE * 0.5),
        )
        for object in [current_system.star]
        + current_system.planets
        + current_system.moons
    ]


def galaxy_view_mode(
    display_window, hyperlane_arr, system_arr, current_system, SCALE, HEIGHT, WIDTH
):
    display_window.fill((5, 5, 25))
    [
        pygame.draw.line(
            surface=display_window,
            color=(100, 100, 100),
            start_pos=(
                intround(object.startposx * SCALE * 36 + WIDTH**2 / HEIGHT),
                intround(object.startposy * SCALE * 36),
            ),
            end_pos=(
                intround(object.endposx * SCALE * 36 + WIDTH**2 / HEIGHT),
                intround(object.endposy * SCALE * 36),
            ),
            width=intround(5.4 * SCALE),
        )
        for object in hyperlane_arr
    ]
    [
        pygame.draw.circle(
            surface=display_window,
            color=object.colour,
            center=(
                intround(object.posx * SCALE * 36 + WIDTH**2 / HEIGHT),
                intround(object.posy * SCALE * 36),
            ),
            radius=intround(15 * SCALE),
        )
        for object in system_arr
    ]
    # pygame.draw.circle(
    #     surface=display_window,
    #     color=object.colour,
    #     center=(object.posx + WIDTH / 2, object.posy + HEIGHT / 2),
    #     radius=intround(object.size * SCALE * 0.5),
    # )


def pygame_run(
    display_window,
    hyperlane_arr,
    system_arr,
    clock,
    FRAME_RATE,
    current_system,
    WIDTH,
    HEIGHT,
    SCALE,
    current_view,
    manager,
) -> None:
    current_view = "galaxy_view"  # Temp, will be remove when main menu is implemented.
    while True:
        if current_view == "main_menu":
            main_menu_mode(manager, current_view)
        elif current_view == "system_view":
            system_view_mode(display_window, current_system, WIDTH, HEIGHT, SCALE)
        elif current_view == "galaxy_view":
            galaxy_view_mode(
                display_window,
                hyperlane_arr,
                system_arr,
                current_system,
                SCALE,
                HEIGHT,
                WIDTH,
            )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return
                if event.key == pygame.K_m:
                    if current_view == "system_view":
                        current_view = "galaxy_view"
                    elif current_view == "galaxy_view":
                        current_view = "system_view"
        pygame.display.update()


game_setup()
