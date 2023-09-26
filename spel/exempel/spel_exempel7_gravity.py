# denna kod visar hur en spelare kan påverkas av gravitation
# den kod som är "ny" är kommenterad, övriga rader har funnits med i tidigare exempel

import pygame

pygame.init()
fonster = pygame.display.set_mode((400, 300))

clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):

    diffx = 0
    diffy = 0
    yspeed = 0  # yspeed håller koll på vår hastighet i y-led

    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill((10,200,10))
        self.rect = self.image.get_rect()

    def update(self):

        self.yspeed += 1  # vi faller neråt pga gravitation
        print("yspeed:", self.yspeed)  # vi skriver ut print för lärandets skull

        self.rect.x += self.diffx

        list_of_collisions = pygame.sprite.spritecollide(self, object_list, False)
        for col in list_of_collisions:
            if type(col) == Solid:

                if (self.rect.right > col.rect.left and self.rect.left < col.rect.left):
                    self.rect.right = col.rect.left

                if (self.rect.left < col.rect.right and self.rect.right > col.rect.right):  # hakat i fran högersidan pa solid
                    self.rect.left = col.rect.right


        self.rect.y += self.diffy
        self.rect.y += self.yspeed  # vi påverkas av gravitationen/hopp

        list_of_collisions = pygame.sprite.spritecollide(self, object_list, False)
        for col in list_of_collisions:
            if type(col) == Solid:


                if (self.rect.bottom > col.rect.top and self.rect.y < col.rect.top):
                    self.rect.bottom = col.rect.top
                    self.yspeed = 0  # när vi krockar uppåt/nedåt resettas yspeed


                if (self.rect.top < col.rect.bottom and self.rect.bottom > col.rect.bottom):
                    self.rect.top = col.rect.bottom
                    self.yspeed = 0  # när vi krockar uppåt/nedåt resettas yspeed

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
solid.rect.x = 10
solid.rect.y = 200
object_list.add(solid)

avsluta = "n"
while avsluta != "y":
    fonster.fill((255, 0, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            avsluta = "y"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE: #  space för att hoppa
                player.yspeed -= 13  # påverka yspeed negativt (vi rör oss uppåt)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_RIGHT]:
        player.diffx += 1
    if keys[pygame.K_LEFT]:
        player.diffx -= 1

    for object in object_list:
        object.update()

    object_list.draw(fonster)

    pygame.display.update()
    clock.tick(60)
