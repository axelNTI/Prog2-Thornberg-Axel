# i denna kod, om du håller nere j eller k när du kör programmet borde färgen på fönstret ändras
# den kod som är "ny" är kommenterad, övriga rader har funnits med i tidigare exempel/instruktionerna
# färgen ändras väldigt fort, i nästa exempel ska vi styra lite över hastigheten i spelet

import pygame

pygame.init()
fonster = pygame.display.set_mode((400, 300))

g = 0
avsluta = "n"
while avsluta != "y":
    fonster.fill((255, g, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            avsluta = "y"

    # notera att biten nedan är "utanför" for-loopen som kollar events
    keys = pygame.key.get_pressed()  # kollar vilka tangenter som är nedtryckta
    if keys[pygame.K_j]:  # är j nedtryckt?
        if g < 255:  # se till att vi inte går över maxvärdet
            g = g + 1
    if keys[pygame.K_k]:  # är k nedtryckt?
        if g > 0:  # se till att vi inte går under minvärdet
            g = g - 1

    pygame.display.update()
