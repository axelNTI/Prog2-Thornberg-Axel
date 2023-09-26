import pygame

pygame.init()
fonster = pygame.display.set_mode((400, 300))

avsluta = "n"
while avsluta != "y":
    fonster.fill((255, 0, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            avsluta = "y"
    pygame.display.update()
