# denna kod visar skärmen kan "flyttas" när en spelare rör sig åt höger
# den kod som är "ny" är kommenterad, övriga rader har funnits med i tidigare exempel

import pygame

pygame.init()
fonster = pygame.display.set_mode((400, 300))

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):


    diffx = 0
    diffy = 0

    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((10,200,10))
        self.rect = self.image.get_rect()

    def update(self):



        self.rect.x += self.diffx

        list_of_collisions = pygame.sprite.spritecollide(self, object_list, False)
        for col in list_of_collisions:
            if type(col) == Solid:


                if (self.rect.right > col.rect.left and self.rect.left < col.rect.left):
                    self.rect.right = col.rect.left

                if (self.rect.left < col.rect.right and self.rect.right > col.rect.right):
                    self.rect.left = col.rect.right


        self.rect.y += self.diffy


        list_of_collisions = pygame.sprite.spritecollide(self, object_list, False)
        for col in list_of_collisions:
            if type(col) == Solid:

                if (self.rect.bottom > col.rect.top and self.rect.y < col.rect.top):
                 self.rect.bottom = col.rect.top

                if (self.rect.top < col.rect.bottom and self.rect.bottom > col.rect.bottom):
                    self.rect.top = col.rect.bottom

        self.diffx = 0
        self.diffy = 0



class Solid(pygame.sprite.Sprite):

    def __init__(self):
        super(Solid, self).__init__()
        self.image = pygame.Surface((200, 200))
        self.image.fill((10,0,10))
        self.rect = self.image.get_rect()



object_list = pygame.sprite.OrderedUpdates()
player = Player()
object_list.add(player)

solid = Solid()
solid.rect.x = 100
solid.rect.y = 200
object_list.add(solid)

level_width = 600  # banan är 600 pixlar bred (fönstret är 400)

# denna funktion räknar ut många pixlar vi ska flytta kameran åt höger
def calcOffset():
    offset = player.rect.centerx - fonster.get_width()/2  # vi utgår från spelarens center och tar bort halva fönstrets bredd

    offset_min = 0  # minsta tillåtna värdet på offset
    offset_max = level_width - fonster.get_width() # maximala tillåtna värdet på offset

    offset = max(offset_min, offset)  # ser till att offset har minst värdet av offset_min
    offset = min(offset_max, offset)  # ser till att offset har maximalt värdet av offset_max
    return offset  # vi returnerar offset tillbaka

avsluta = "n"
while avsluta != "y":

    offset = calcOffset() # räkna ut offset (hur mycket kameran ska flytta åt höger)
    print("offset just nu:", offset)  # för att enklare lära oss offset printar vi ut den


    fonster.fill((255, 0, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            avsluta = "y"

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.diffx += 1
    if keys[pygame.K_LEFT]:
        player.diffx -= 1
    if keys[pygame.K_DOWN]:
        player.diffy += 1
    if keys[pygame.K_UP]:
        player.diffy -= 1

    for object in object_list:
        object.update()

    #object_list.draw(fonster) DENNA RAD UTKOMMENTERAD, ISTÄLLET GÖR VI "SAMMA SAK" FAST MED RADERNA NEDAN
    for object in object_list:  # för varje objekt som ska ritas ut
        fonster.blit(object.image, (object.rect.x-offset, object.rect.y))  # rita ut objektets bild men vi korrigerar x-värdet

    pygame.display.update()
    clock.tick(60)
