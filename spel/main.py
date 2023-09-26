import pygame
import random

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
# display_window = pygame.display.set_mode((infoObject.current_w, infoObject.current_h))
#


def pygameRun() -> None:
    pygame.init()
    infoObject = pygame.display.Info()
    display_window = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    pygame.display.set_caption("Interstellar Exploration")
    # pygame.display.set_icon(Icon_name)
    while True:
        # display_window.fill(
        #     (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        # )
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return


pygameRun()
