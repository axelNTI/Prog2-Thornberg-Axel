# denna kod visar hur vi kan skriva ut text
# den kod som är "ny" är kommenterad, övriga rader har funnits med i tidigare exempel

import pygame

pygame.init()
fonster = pygame.display.set_mode((400, 300))


class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((10,200,10))
        self.rect = self.image.get_rect()

#HELA KLASSEN NY
class Text(pygame.sprite.Sprite):

    def __init__(self, text):
        super(Text, self).__init__()
        self.font = pygame.font.Font(None, 48)  # 48 är font-storleken
        self.image = self.font.render(text, 1, (255, 255, 0))  # 255, 255, 0 är färgen (gul)
        self.rect = self.image.get_rect()


object_list = pygame.sprite.OrderedUpdates()
player = Player()
object_list.add(player)

text1 = Text("hejsan")  # nytt
text1.rect.x = 200  # positionen för texten
object_list.add(text1)  # nytt

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
