import pygame
import numpy as np


class Object:
    def __init__(self, posx, posy) -> None:
        self.posx = posx
        self.posy = posy


class Player(Object):
    def __init__(self, posx, posy) -> None:
        super().__init__(posx, posy)
        self.colour = (255, 255, 255)
        self.size = 25


class Enemy(Object):
    def __init__(self, posx, posy) -> None:
        super().__init__(posx, posy)


class Standard(Enemy):
    def __init__(self, posx, posy) -> None:
        super().__init__(posx, posy)
        self.speed = 3
        self.size = 25
        self.colour = (125, 125, 0)


class Fast(Enemy):
    def __init__(self, posx, posy) -> None:
        super().__init__(posx, posy)
        self.speed = 4
        self.size = 20
        self.colour = (175, 75, 0)


class Very_Fast(Enemy):
    def __init__(self, posx, posy) -> None:
        super().__init__(posx, posy)
        self.speed = 5
        self.size = 15
        self.colour = (225, 25, 0)


class Big(Enemy):
    def __init__(self, posx, posy) -> None:
        super().__init__(posx, posy)
        self.speed = 2
        self.size = 30
        self.colour = (75, 175, 0)


class Very_Big(Enemy):
    def __init__(self, posx, posy) -> None:
        super().__init__(posx, posy)
        self.speed = 1
        self.size = 35
        self.colour = (25, 225, 0)


def intround(value: float, precision: int = 0) -> int:
    return int(round(value, precision))


def setup() -> None:
    pygame.init()
    infoObject = pygame.display.Info()
    WIDTH, HEIGHT = infoObject.current_w, infoObject.current_h
    SCALE = WIDTH * HEIGHT / 2073600
    display_window = pygame.display.set_mode((WIDTH, HEIGHT))
    REFRESH_RATE = pygame.display.get_current_refresh_rate()
    REFRESH_RATE_MOD = 60 / REFRESH_RATE
    clock = pygame.time.Clock()
    player = Player(WIDTH / 2, HEIGHT / 2)
    list_of_enemies = np.random.choice(
        a=[
            Standard(np.random.randint(0, WIDTH), np.random.randint(0, HEIGHT)),
            Fast(np.random.randint(0, WIDTH), np.random.randint(0, HEIGHT)),
            Very_Big(np.random.randint(0, WIDTH), np.random.randint(0, HEIGHT)),
            Big(np.random.randint(0, WIDTH), np.random.randint(0, HEIGHT)),
            Very_Fast(np.random.randint(0, WIDTH), np.random.randint(0, HEIGHT)),
        ],
        size=10,
    )
    for i in list_of_enemies:
        print(i)
    up = False
    right = False
    down = False
    left = False
    game_loop(
        display_window,
        clock,
        player,
        list_of_enemies,
        up,
        right,
        down,
        left,
        WIDTH,
        HEIGHT,
        SCALE,
        REFRESH_RATE,
        REFRESH_RATE_MOD,
    )
    pygame.quit()


def game_loop(
    display_window,
    clock,
    player,
    list_of_enemies,
    up,
    right,
    down,
    left,
    WIDTH,
    HEIGHT,
    SCALE,
    REFRESH_RATE,
    REFRESH_RATE_MOD,
) -> None:
    while True:
        display_window.fill((5, 5, 25))
        [
            pygame.draw.circle(
                surface=display_window,
                color=object.colour,
                center=(object.posx, object.posy),
                radius=object.size * SCALE,
            )
            for object in [player] + list(list_of_enemies)
        ]
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    return
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    up = True
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    right = True
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    down = True
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    left = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_q:
                    return
                if event.key == pygame.K_w or event.key == pygame.K_UP:
                    up = False
                if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    right = False
                if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    down = False
                if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    left = False
        if up:
            player.posy -= 5 * REFRESH_RATE_MOD * SCALE
        if right:
            player.posx += 5 * REFRESH_RATE_MOD * SCALE
        if down:
            player.posy += 5 * REFRESH_RATE_MOD * SCALE
        if left:
            player.posx -= 5 * REFRESH_RATE_MOD * SCALE
        if not player.size <= player.posx < WIDTH - player.size:
            player.posx = min(
                [player.size, WIDTH - player.size], key=lambda x: abs(x - player.posx)
            )
        if not player.size <= player.posy < HEIGHT - player.size:
            player.posy = min(
                [player.size, HEIGHT - player.size], key=lambda y: abs(y - player.posy)
            )
        []
        pygame.display.update()
        clock.tick(REFRESH_RATE)


setup()
