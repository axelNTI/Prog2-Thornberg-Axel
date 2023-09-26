# denna kod visar hur vi kan ha en text som kan ändras på
# den kod som är "ny" är kommenterad, övriga rader har funnits med i tidigare exempel
# texten ändras om du trycker på högerpil eller nedåtpil under körning

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
class Changeabletext(pygame.sprite.Sprite):

    def __init__(self, text, x_pos, y_pos):
        super(Changeabletext, self).__init__()
        self.font = pygame.font.Font(None, 48)
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.update_text(text)

    def update_text(self, text):
        self.image = self.font.render(text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = self.x_pos
        self.rect.y = self.y_pos


object_list = pygame.sprite.OrderedUpdates()
player = Player()
object_list.add(player)

text1 = Changeabletext("hejsan", 200, 10)  # 200 är x-positionen, 10 är y-positionen
object_list.add(text1)

avsluta = "n"
while avsluta != "y":
    fonster.fill((255, 0, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            avsluta = "y"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.rect.x += 25
                text1.update_text("höger-pil")  # nytt
            if event.key == pygame.K_DOWN:
                player.rect.y += 25
                text1.update_text("nedåt-pil")  # nytt

    for object in object_list:
        object.update()

    object_list.draw(fonster)

    pygame.display.update()
