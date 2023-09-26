# denna kod visar hur en spelare kan se ut som en bild och inte vara enfärgad
# koden förutsätter att du har en bildfil A_exempel5_face.png i samma mapp som python-filen
# den kod som är "ny" är kommenterad, övriga rader har funnits med i tidigare exempel

import pygame

pygame.init()
fonster = pygame.display.set_mode((400, 300))


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load("spel_exempel5_face.png")  # ladda in bilden (spelaren blir lika stor som bilden är)
        self.rect = self.image.get_rect()

object_list = pygame.sprite.OrderedUpdates()
player = Player()
object_list.add(player)

avsluta = "n"
while avsluta != "y":
    fonster.fill((255, 0, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            avsluta = "y"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.rect.x += 25
            if event.key == pygame.K_DOWN:
                player.rect.y += 25

    for object in object_list:
        object.update()

    object_list.draw(fonster)

    pygame.display.update()
