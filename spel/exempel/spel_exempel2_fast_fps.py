# denna kod visar hur vi kan styra hastigheten i programmet
# den kod som är "ny" är kommenterad, övriga rader har funnits med i tidigare exempel

import pygame

pygame.init()
fonster = pygame.display.set_mode((400, 300))

clock = pygame.time.Clock()  # skapa en klocka som håller reda på tiden

g = 0
avsluta = "n"
while avsluta != "y":
    fonster.fill((255, g, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            avsluta = "y"


    keys = pygame.key.get_pressed()
    if keys[pygame.K_j]:
        if g < 255:
            g = g + 1
    if keys[pygame.K_k]:
        if g > 0:
            g = g - 1

    pygame.display.update()

    clock.tick(60)  # kör spelet i 60 fps, denna rad ska vara längst ner i loopen som körs
    # denna klocka gör att programmet kollar om j eller k är nedtryckt 60 gånger per sekund
    # att gå från 0 i grönt till 255 i grönt borde ta cirka 4 sekunder
