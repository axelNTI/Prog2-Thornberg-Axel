# denna kod visar hur en spelare kan hindras från att åka genom solida block (t.ex. mark)
# den kod som är "ny" är kommenterad, övriga rader har funnits med i tidigare exempel

import pygame

pygame.init()
fonster = pygame.display.set_mode((400, 300))

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):

    # dessa håller koll på hur mycket vi ska förflytta oss i x-led
    diffx = 0
    diffy = 0

    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((10,200,10))
        self.rect = self.image.get_rect()

    def update(self):  # körs för varje frame


        # först ändrar vi bara position i x-led
        self.rect.x += self.diffx

        # kolla efter krockar i x-led
        list_of_collisions = pygame.sprite.spritecollide(self, object_list, False)  # hämta alla objekt vi krockar med
        for col in list_of_collisions:  # gör följande för varje krock-objekt
            if type(col) == Solid:  # är det vi krockat med ett solid-block?

                # kollar bara krockar i x-led
                if (self.rect.right > col.rect.left and self.rect.left < col.rect.left):  # hakat i fran vänstersidan pa solid
                    self.rect.right = col.rect.left

                if (self.rect.left < col.rect.right and self.rect.right > col.rect.right):  # hakat i fran högersidan pa solid
                    self.rect.left = col.rect.right

        # sen ändrar vi position i y-led
        self.rect.y += self.diffy

        # kolla efter krockar i y-led
        list_of_collisions = pygame.sprite.spritecollide(self, object_list, False)  # hämta alla objekt vi krockar med
        for col in list_of_collisions:  # gör följande för varje krock-objekt
            if type(col) == Solid:  # är det vi krockat med ett solid-block?

                # kolla y-axeln
                if (self.rect.bottom > col.rect.top and self.rect.y < col.rect.top):  # hakat i fran undersidan pa solid
                 self.rect.bottom = col.rect.top

                if (self.rect.top < col.rect.bottom and self.rect.bottom > col.rect.bottom):  # hakat i fran ovansidan pa solid
                    self.rect.top = col.rect.bottom

        # nollställ dessa variabler för vi har redan förflyttat oss enligt dem
        self.diffx = 0
        self.diffy = 0



class Solid(pygame.sprite.Sprite):  # vi skapar en "klass" för solida block

    def __init__(self):  # denna körs när blocket skapas
        super(Solid, self).__init__()  # denna sak måste vara först i __init__
        self.image = pygame.Surface((200, 200))  # sätt storleken på blocket
        self.image.fill((10,0,10))  # sätt färgen på blocket
        self.rect = self.image.get_rect()  # rect kan styra var blocket ska ritas ut



object_list = pygame.sprite.OrderedUpdates()
player = Player()
object_list.add(player)

solid = Solid()  # skapa ett nytt block
solid.rect.x = 100  # sätt ut blockets position i x-led
solid.rect.y = 200  # sätt ut blockets position i y-led
object_list.add(solid)  # lägg blocket i listan över saker att rita ut

avsluta = "n"
while avsluta != "y":
    fonster.fill((255, 0, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            avsluta = "y"

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.diffx += 1  # ändrar inte direkt på self.rect.x, själva ändringen görs av Player-klassen
    if keys[pygame.K_LEFT]:
        player.diffx -= 1
    if keys[pygame.K_DOWN]:
        player.diffy += 1
    if keys[pygame.K_UP]:
        player.diffy -= 1

    for object in object_list:
        object.update()

    object_list.draw(fonster)

    pygame.display.update()
    clock.tick(60)
