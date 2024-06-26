import pygame_gui
import pygame
import random
import pickle
import math
import os

# import numba as nu
# import multiprocessing as mp
import numpy as np
from classes_galaxy import *
from classes_system import *
from classes_ships import *


# Personal links/comments for later:
# https://www.pygame.org/docs/ref/display.html#pygame.display.Info
# https://stackoverflow.com/questions/35617246/setting-a-fixed-fps-in-pygame-python-3
# https://www.geeksforgeeks.org/how-to-change-the-name-of-a-pygame-window/
# https://stackoverflow.com/questions/3838329/how-can-i-check-if-two-segments-intersect
#
# Använd numpy
#
# Fullscreen:
# display_window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
#
# Borderless Windowed:
# display_window = pygame.display.set_mode((infoObject9.current_w, infoObject.current_h))


# Chatgpt (Jag orkade inte räkna ut rocket science):
def optimal_acceleration(initial_pos, target_pos, initial_vel, scalar_acceleration):
    initial_pos = np.array(initial_pos)
    target_pos = np.array(target_pos)
    initial_vel = np.array(initial_vel)
    # Step 1: Calculate displacement vector
    displacement = target_pos - initial_pos
    displacement_norm = np.linalg.norm(displacement)

    # Step 2: Calculate velocity vector
    velocity_norm = np.linalg.norm(initial_vel)
    if velocity_norm == 0:
        return np.zeros_like(initial_vel)
    velocity_direction = initial_vel / velocity_norm

    # Step 3: Calculate angle between displacement and velocity vectors
    cos_theta = np.dot(displacement, initial_vel) / (displacement_norm * velocity_norm)

    # Handle potential edge cases where vectors are collinear or nearly collinear
    if abs(cos_theta) > 1.0:
        cos_theta = np.sign(cos_theta) * 1.0  # Clamp to [-1, 1]
    sin_theta = np.sqrt(1 - cos_theta**2)

    # Step 4: Calculate tangential and radial components of acceleration
    radial_accel_magnitude = scalar_acceleration * cos_theta
    radial_accel = radial_accel_magnitude * (displacement / displacement_norm)

    if sin_theta != 0:
        tangential_accel_magnitude = scalar_acceleration * sin_theta
        tangential_accel = tangential_accel_magnitude * velocity_direction
    else:
        tangential_accel = np.zeros_like(initial_vel)

    # Step 5: Combine components to get optimal acceleration
    optimal_accel = tangential_accel - radial_accel

    return optimal_accel


def screen_coords_to_game_coords(
    x: int, y: int, WIDTH: int, HEIGHT: int, SCALE: float
) -> tuple:
    return (x - WIDTH / 2) / SCALE, (y - HEIGHT / 2) / SCALE


def game_coords_to_screen_coords(
    x: int, y: int, WIDTH: int, HEIGHT: int, SCALE: float
) -> tuple:
    return x * SCALE + WIDTH / 2, y * SCALE + HEIGHT / 2


def intround(value: float) -> int:
    return int(round(value, 0))


def create_systems(num_systems: int, radius: int) -> np.ndarray:
    """
    Create an array of systems with random positions within a given radius.

    Args:
        num_systems (int): The number of systems to create.
        radius (int): The radius within which the systems will be created.

    Returns:
        np.ndarray: An array of System objects with random positions.
    """
    x_values, y_values = np.mgrid[1 : 2 * radius, 1 : 2 * radius]
    distances = np.hypot(x_values - radius, y_values - radius)
    mask = distances <= radius
    valid_coordinates = np.column_stack((x_values[mask], y_values[mask]))
    np.random.shuffle(valid_coordinates)
    positions = valid_coordinates[:num_systems]
    return np.array(list(map(System, positions)))


def create_hyperlanes(system_arr: np.ndarray) -> np.ndarray:
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
    hyperlane_arr = list(
        dict.fromkeys(
            [j for sub in [lane.hyperlanes for lane in system_arr] for j in sub]
        )
    )
    return hyperlane_arr


def recursive_get_hyperlane_jumps(system: object, starting_system: object) -> float:
    # Get the amount of jumps between the starting system and the current system.
    raise NotImplementedError


def game_setup() -> None:
    SYSTEM_COUNT = 50
    FRAME_RATE = 60
    RADIUS = 15
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
    system_arr = create_systems(SYSTEM_COUNT, RADIUS)
    hyperlane_arr = create_hyperlanes(system_arr)
    current_system = random.choice(system_arr)
    current_system.generate(True)
    player_fleet = Fleet((0, 0))
    player_fleet.ships.append(Capital())
    pygame_run(
        display_window,
        clock,
        manager,
        hyperlane_arr,
        system_arr,
        FRAME_RATE,
        current_system,
        WIDTH,
        HEIGHT,
        SCALE,
        current_view,
        player_fleet,
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
    player_fleet: object,
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
    [
        pygame.draw.circle(
            surface=display_window,
            color=object.colour,
            center=(
                intround(SCALE * object.get_position_x(player_fleet) + WIDTH / 2),
                intround(SCALE * object.get_position_y(player_fleet) + HEIGHT / 2),
            ),
            radius=intround(object.size * SCALE),
        )
        for object in player_fleet.ships
    ]

    # Display the resources of the celestial bodies.
    for object in [current_system.star] + current_system.planets + current_system.moons:
        text = pygame.font.SysFont("arial", intround(15 * SCALE)).render(
            str(object.resources), True, (255, 255, 255)
        )
        display_window.blit(
            text,
            (
                intround(SCALE * object.posx + WIDTH / 2),
                intround(SCALE * object.posy + HEIGHT / 2),
            ),
        )

    # Display the resources of the fleet in the top left corner with each resource having its own line.
    for i, resource in enumerate(player_fleet.resources):
        display_resource = resource.replace("_", " ")
        text = pygame.font.SysFont("arial", intround(15 * SCALE)).render(
            f"{display_resource}: {player_fleet.resources[resource]}",
            True,
            (255, 255, 255),
        )
        display_window.blit(text, (intround(10 * SCALE), intround(20 * SCALE * i)))

    # Display the target position of the fleet.
    if player_fleet.target_position:
        pygame.draw.circle(
            display_window,
            (255, 0, 0),
            (
                intround(player_fleet.target_posx * SCALE + WIDTH / 2),
                intround(player_fleet.target_posy * SCALE + HEIGHT / 2),
            ),
            intround(5 * SCALE),
        )


def galaxy_view_mode(
    display_window: pygame.surface.Surface,
    hyperlane_arr: list,
    system_arr: list,
    current_system: object,
    SCALE: float,
    HEIGHT: int,
    WIDTH: int,
):
    display_window.fill((5, 5, 25))
    [
        pygame.draw.line(
            surface=display_window,
            color=(100, 100, 100),
            start_pos=(
                intround(object.startposx * SCALE * 36 + (WIDTH - HEIGHT) / 2),
                intround(object.startposy * SCALE * 36),
            ),
            end_pos=(
                intround(object.endposx * SCALE * 36 + (WIDTH - HEIGHT) / 2),
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
                intround(object.posx * SCALE * 36 + (WIDTH - HEIGHT) / 2),
                intround(object.posy * SCALE * 36),
            ),
            radius=intround(15 * SCALE),
        )
        for object in system_arr
    ]


def pygame_run(
    display_window: pygame.surface.Surface,
    clock: pygame.time.Clock,
    manager: pygame_gui.ui_manager.UIManager,
    hyperlane_arr: list,
    system_arr: list,
    FRAME_RATE: int,
    current_system: object,
    WIDTH: int,
    HEIGHT: int,
    SCALE: float,
    current_view: str,
    player_fleet: object,
) -> None:
    current_view = "system_view"  # Temp, will be removed when main menu is implemented.
    # slow_down = False  # Move to setup.
    while True:
        if player_fleet.target_position:

            player_fleet.acceleration = min(
                [ship.acceleration for ship in player_fleet.ships]
            )
            player_fleet.accx, player_fleet.accy = optimal_acceleration(
                player_fleet.position,
                player_fleet.target_position,
                player_fleet.velocity,
                player_fleet.acceleration,
            )

            print(player_fleet.accx, player_fleet.accy)

            player_fleet.velx += player_fleet.accx
            player_fleet.vely += player_fleet.accy
            player_fleet.posx += player_fleet.velx
            player_fleet.posy += player_fleet.vely

            player_fleet.position = player_fleet.posx, player_fleet.posy
            distance = np.hypot(
                player_fleet.posx - player_fleet.target_posx,
                player_fleet.posy - player_fleet.target_posy,
            )

            # Check if the fleet has reached the target.
            if distance < 5:
                player_fleet.target_position = None
                player_fleet.velx = 0
                player_fleet.vely = 0
                player_fleet.velocity = 0
                player_fleet.accx = 0
                player_fleet.accy = 0
                player_fleet.acceleration = 0
        in_orbit = [
            object
            for object in [current_system.star]
            + current_system.planets
            + current_system.moons
            if np.hypot(
                object.posx - player_fleet.posx,
                object.posy - player_fleet.posy,
            )
            < object.size * 1.2
        ]
        for object in in_orbit:
            for resource in object.resources:
                player_fleet.resources[resource] += object.resources[resource]
        if current_view == "main_menu":
            main_menu_mode(manager, current_view)
        elif current_view == "system_view":
            system_view_mode(
                display_window, current_system, WIDTH, HEIGHT, SCALE, player_fleet
            )
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
                if event.key == pygame.K_s:
                    # Rewrite this to allow for multiple save files when main menu is implemented.
                    with open(
                        os.path.join(os.path.dirname(__file__), "save_data.pkl"), "wb"
                    ) as file:
                        pickle.dump(
                            (
                                hyperlane_arr,
                                system_arr,
                                current_system,
                                current_view,
                                player_fleet,
                            ),
                            file,
                        )
                # if event.key == pygame.K_h:
                #     # Slow the fleet down to a stop.
                #     player_fleet.target_position = None
                #     slow_down = True

            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3 and current_view == "system_view":
                    position = pygame.mouse.get_pos()
                    player_fleet.target_posx = (position[0] - WIDTH / 2) / SCALE
                    player_fleet.target_posy = (position[1] - HEIGHT / 2) / SCALE
                    player_fleet.target_position = (
                        player_fleet.target_posx,
                        player_fleet.target_posy,
                    )

        # if slow_down:
        #     # Get direction of the fleet.
        #     angle = math.atan2(player_fleet.vely, player_fleet.velx)
        #     # Calculate the acceleration in the x and y directions.
        #     player_fleet.accx = -player_fleet.acceleration * math.cos(angle)
        #     player_fleet.accy = -player_fleet.acceleration * math.sin(angle)
        #     # Update the velocity of the fleet.
        #     player_fleet.velx += player_fleet.accx
        #     player_fleet.vely += player_fleet.accy
        #     # Update the position of the fleet.
        #     player_fleet.posx += player_fleet.velx
        #     player_fleet.posy += player_fleet.vely
        #     player_fleet.position = player_fleet.posx, player_fleet.posy
        #     # Check if the fleet has reached a stop.
        #     if player_fleet.velx == 0 and player_fleet.vely == 0:
        #         slow_down = False
        pygame.display.update()
        clock.tick(FRAME_RATE)


if __name__ == "__main__":
    game_setup()
