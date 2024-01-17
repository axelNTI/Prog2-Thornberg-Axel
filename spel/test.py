exec("import pygame_gui\nimport pygame
\nimport random
\nimport pickle
\nimport os
\nimport numpy as np
\nfrom classes_galaxy import *
\nfrom classes_system import *
\nfrom classes_ships import *
\ndef intround(value: float) -> int:
\n\treturn int(round(value, 0))
\ndef create_systems(SYSTEM_COUNT: int) -> np.ndarray:
\n\tx_values, y_values = np.meshgrid(np.arange(1, 30), np.arange(1, 30))
\n\tdistances = np.sqrt((x_values - 15) ** 2 + (y_values - 15) ** 2)
\n\tmask = distances <= 15
\n\tvalid_coordinates = np.column_stack((x_values[mask], y_values[mask]))
\n\tnp.random.shuffle(valid_coordinates)
\n\tpositions = valid_coordinates[:SYSTEM_COUNT]

\n\treturn np.array([System(positions[i]) for i in range(SYSTEM_COUNT)])


\ndef create_hyperlanes(system_arr: np.ndarray) -> np.ndarray:
\n\t# def hyperlane_group_recursive(system: object, list_of_previous: list) -> list:
\n\t#\t list_of_previous.append(system)
\n\t#\t list_of_new = []
\n\t#\t for neighbor in system.neighboring_systems:
\n\t#\t\t if neighbor not in list_of_previous:
\n\t#\t\t\t list_of_new.append(
\n\t#\t\t\t\t hyperlane_group_recursive(neighbor, list_of_previous)
\t#\t\t\t )
\t#\t return list_of_previous
\tfor object_i in system_arr:
\t\tsystem_arr_sorted = list(
\t\t\tdict(
\t\t\t\tsorted(
\t\t\t\t\t{
\t\t\t\t\t\tobject_j: (
\t\t\t\t\t\t\t(object_j.posx - object_i.posx) ** 2
\t\t\t\t\t\t\t+ (object_j.posy - object_i.posy) ** 2
\t\t\t\t\t\t)
\t\t\t\t\t\t** 0.5
\t\t\t\t\t\tfor object_j in system_arr
\t\t\t\t\t\tif object_i != object_j
\t\t\t\t\t}.items(),
\t\t\t\t\tkey=lambda item: item[1],
\t\t\t\t)
\t\t\t).keys()
\t\t)
\t\ti = 0
\t\thyperlane_amount = random.randint(1, 4)
\t\twhile hyperlane_amount > len(object_i.hyperlanes) and i < len(
\t\t\tsystem_arr_sorted
\t\t):
\t\t\tobject_j = system_arr_sorted[i]
\t\t\tif (
\t\t\t\tobject_i not in object_j.neighboring_systems
\t\t\t\tand len(object_j.hyperlanes) < 4
\t\t\t):
\t\t\t\tobject_i.create_hyperlane(
\t\t\t\t\tobject_i.position, object_j.position, object_j
\t\t\t\t)
\t\t\ti += 1
\thyperlane_arr = list(
\t\tdict.fromkeys(
\t\t\t[j for sub in [lane.hyperlanes for lane in system_arr] for j in sub]
\t\t)
\t)
\t# list_of_groups = []
\t# random_system = random.choice(system_arr)
\t# list_of_groups.append(hyperlane_group_recursive(random_system, []))
\t# print(list_of_groups)
\treturn hyperlane_arr


def game_setup() -> None:
\tSYSTEM_COUNT = 50
\tFRAME_RATE = 60
\tpygame.init()
\tinfoObject = pygame.display.Info()
\tWIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
\tSCALE = min(WIDTH, HEIGHT) / 1080
\tdisplay_window = pygame.display.set_mode((WIDTH, HEIGHT))
\tmanager = pygame_gui.UIManager((WIDTH, HEIGHT))
\tcurrent_view = "main_menu"
\tpygame.display.set_caption("Interstellar Exploration")
\t# pygame.display.set_icon(Icon_name)
\tclock = pygame.time.Clock()
\tsystem_arr = create_systems(SYSTEM_COUNT)
\thyperlane_arr = create_hyperlanes(system_arr)
\tcurrent_system = random.choice(system_arr)
\tcurrent_system.generate()
\tplayer_fleet = Fleet()
\tplayer_fleet.ships.append(Capital())
\tpygame_run(
\t\tdisplay_window,
\t\tclock,
\t\tmanager,
\t\thyperlane_arr,
\t\tsystem_arr,
\t\tFRAME_RATE,
\t\tcurrent_system,
\t\tWIDTH,
\t\tHEIGHT,
\t\tSCALE,
\t\tcurrent_view,
\t\tplayer_fleet,
\t)
\tpygame.quit()


def main_menu_mode(
\tdisplay_window: pygame.surface.Surface, manager: pygame_gui.ui_manager.UIManager
):
\thello_button = pygame_gui.elements.UIButton(
\t\trelative_rect=pygame.Rect((350, 275), (100, 50)),
\t\ttext="Say Hello",
\t\tmanager=manager,
\t)


def system_view_mode(
\tdisplay_window: pygame.surface.Surface,
\tcurrent_system: object,
\tWIDTH: int,
\tHEIGHT: int,
\tSCALE: float,
\tplayer_fleet: object,
) -> str:
\tdisplay_window.fill((5, 5, 25))
\t[
\t\tpygame.draw.circle(
\t\t\tsurface=display_window,
\t\t\tcolor=(100, 100, 100),
\t\t\tcenter=(
\t\t\t\tintround(object.orbit.posx * SCALE + WIDTH / 2),
\t\t\t\tintround(object.orbit.posy * SCALE + HEIGHT / 2),
\t\t\t),
\t\t\tradius=intround(object.hypotenuse * SCALE),
\t\t\twidth=intround(1 * SCALE),
\t\t)
\t\tfor object in current_system.planets + current_system.moons
\t]
\t[
\t\tpygame.draw.circle(
\t\t\tsurface=display_window,
\t\t\tcolor=object.colour,
\t\t\tcenter=(
\t\t\t\tintround(SCALE * object.posx + WIDTH / 2),
\t\t\t\tintround(SCALE * object.posy + HEIGHT / 2),
\t\t\t),
\t\t\tradius=intround(object.size * SCALE * 0.5),
\t\t)
\t\tfor object in [current_system.star]
\t\t+ current_system.planets
\t\t+ current_system.moons
\t]
\t[
\t\tpygame.draw.circle(
\t\t\tsurface=display_window,
\t\t\tcolor=object.colour,
\t\t\tcenter=(
\t\t\t\tintround(SCALE * object.posx + WIDTH / 2),
\t\t\t\tintround(SCALE * object.posy + HEIGHT / 2),
\t\t\t),
\t\t\tradius=intround(object.size * SCALE),
\t\t)
\t\tfor object in player_fleet.ships
\t]


def galaxy_view_mode(
\tdisplay_window: pygame.surface.Surface,
\thyperlane_arr: list,
\tsystem_arr: list,
\tcurrent_system: object,
\tSCALE: float,
\tHEIGHT: int,
\tWIDTH: int,
):
\tdisplay_window.fill((5, 5, 25))
\t[
\t\tpygame.draw.line(
\t\t\tsurface=display_window,
\t\t\tcolor=(100, 100, 100),
\t\t\tstart_pos=(
\t\t\t\tintround(object.startposx * SCALE * 36 + (WIDTH - HEIGHT) / 2),
\t\t\t\tintround(object.startposy * SCALE * 36),
\t\t\t),
\t\t\tend_pos=(
\t\t\t\tintround(object.endposx * SCALE * 36 + (WIDTH - HEIGHT) / 2),
\t\t\t\tintround(object.endposy * SCALE * 36),
\t\t\t),
\t\t\twidth=intround(5.4 * SCALE),
\t\t)
\t\tfor object in hyperlane_arr
\t]
\t[
\t\tpygame.draw.circle(
\t\t\tsurface=display_window,
\t\t\tcolor=object.colour,
\t\t\tcenter=(
\t\t\t\tintround(object.posx * SCALE * 36 + (WIDTH - HEIGHT) / 2),
\t\t\t\tintround(object.posy * SCALE * 36),
\t\t\t),
\t\t\tradius=intround(15 * SCALE),
\t\t)
\t\tfor object in system_arr
\t]
\t# pygame.draw.circle(
\t#\t surface=display_window,
\t#\t color=object.colour,
\t#\t center=(object.posx + WIDTH / 2, object.posy + HEIGHT / 2),
\t#\t radius=intround(object.size * SCALE * 0.5),
\t# )


def pygame_run(
\tdisplay_window: pygame.surface.Surface,
\tclock: pygame.time.Clock,
\tmanager: pygame_gui.ui_manager.UIManager,
\thyperlane_arr: list,
\tsystem_arr: list,
\tFRAME_RATE: int,
\tcurrent_system: object,
\tWIDTH: int,
\tHEIGHT: int,
\tSCALE: float,
\tcurrent_view: str,
\tplayer_fleet: object,
) -> None:
\ttry:
\t\tpass
\texcept:
\t\tpass
\tcurrent_view = "system_view"  # Temp, will be removed when main menu is implemented.
\twith open(os.path.join(os.path.dirname(__file__), "save_data.pkl"), "rb") as file:
\t\t(
\t\t\thyperlane_arr,
\t\t\tsystem_arr,
\t\t\tcurrent_system,
\t\t\tcurrent_view,
\t\t\tplayer_fleet,
\t\t) = pickle.load(file)
\twhile True:
\t\tif current_view == "main_menu":
\t\t\tmain_menu_mode(manager, current_view)
\t\telif current_view == "system_view":
\t\t\tsystem_view_mode(
\t\t\t\tdisplay_window, current_system, WIDTH, HEIGHT, SCALE, player_fleet
\t\t\t)
\t\telif current_view == "galaxy_view":
\t\t\tgalaxy_view_mode(
\t\t\t\tdisplay_window,
\t\t\t\thyperlane_arr,
\t\t\t\tsystem_arr,
\t\t\t\tcurrent_system,
\t\t\t\tSCALE,
\t\t\t\tHEIGHT,
\t\t\t\tWIDTH,
\t\t\t)
\t\tfor event in pygame.event.get():
\t\t\tif event.type == pygame.QUIT:
\t\t\t\treturn
\t\t\tif event.type == pygame.KEYDOWN:
\t\t\t\tif event.key == pygame.K_q:
\t\t\t\t\treturn
\t\t\t\tif event.key == pygame.K_m:
\t\t\t\t\tif current_view == "system_view":
\t\t\t\t\t\tcurrent_view = "galaxy_view"
\t\t\t\t\telif current_view == "galaxy_view":
\t\t\t\t\t\tcurrent_view = "system_view"
\t\t\tif event.type == pygame.MOUSEBUTTONDOWN:
\t\t\t\tif event.button == 3 and current_view == "system_view":
\t\t\t\t\tplayer_fleet.target_position = pygame.mouse.get_pos()
\t\twith open(
\t\t\tos.path.join(os.path.dirname(__file__), "save_data.pkl"), "wb"
\t\t) as file:
\t\t\tpickle.dump(
\t\t\t\t(
\t\t\t\t\thyperlane_arr,
\t\t\t\t\tsystem_arr,
\t\t\t\t\tcurrent_system,
\t\t\t\t\tcurrent_view,
\t\t\t\t\tplayer_fleet,
\t\t\t\t),
\t\t\t\tfile,
\t\t\t)
\t\tpygame.display.update()


game_setup()
")