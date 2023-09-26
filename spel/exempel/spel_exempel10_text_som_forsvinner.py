# denna kod visar hur vi kan ha en text som försvinner av sig själv efter en viss tid
# den kod som är "ny" är kommenterad, övriga rader har funnits med i tidigare exempel
# texten dyker upp om du trycker på nedåtpil under körning

import pygame

pygame.init()
fonster = pygame.display.set_mode((400, 300))
clock = pygame.time.Clock()  # vi måste ha klocka för att ha fast fps (se exempel 2)

class Player(pygame.sprite.Sprite):

    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((10,200,10))
        self.rect = self.image.get_rect()

# HELA KLASSEN NY
class Tidstext(pygame.sprite.Sprite):

    def __init__(self, text):
        super(Tidstext, self).__init__()
        self.font = pygame.font.Font(None, 48)
        self.image = self.font.render(text, 1, (255, 255, 0))
        self.rect = self.image.get_rect()
        self.timeleft = 60  # texten visas i 60 frames (1 sekund då vi kör 60 fps)

    def update(self):  # körs varje frame
        if self.timeleft > 0:  # om den ska visas längre, räkna ner
            self.timeleft -= 1
        else:  # om den inte ska visas längre, "döda" den
            self.kill()

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
                text1 = Tidstext("du tryckte ned")  # här skapas texten (när vi trycker nedåt-pil)
                object_list.add(text1)  # lägger som vanligt in den i object_list

    for object in object_list:
        object.update()
        
    object_list.draw(fonster)
    pygame.display.update()
    clock.tick(60)  # kör spelet i 60 fps, denna är viktig för den styr hur snabbt texten försvinner
