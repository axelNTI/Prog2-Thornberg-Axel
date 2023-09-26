# denna kod visar hur vi kan kolla om saker krockar
# den kod som är "ny" är kommenterad, övriga rader har funnits med i tidigare exempel

import pygame

pygame.init()
fonster = pygame.display.set_mode((400, 300))  # skapa fönster med storleken 400x300


class Player(pygame.sprite.Sprite):  # det inom parentes säger VAD vi är (en så kallad Sprite)

    def __init__(self):  # denna funktion körs när objektet skapas
        super(Player, self).__init__()  # denna sak måste vara först i __init__
        self.image = pygame.Surface((50, 50))  # skapa bilden som tillhör karaktären
        self.image.fill((10,200,10))  # färglägg hela karaktären enfärgat
        self.rect = self.image.get_rect()  # rect styr var karaktären ska ritas ut

    def update(self):  # körs för varje frame
        list_of_collisions = pygame.sprite.spritecollide(self, object_list, False)  # hämta alla objekt vi krockar med
        for col in list_of_collisions:  # gör följande för varje krock-objekt
            if type(col) == Missil:  # är det vi krockat med en missil?
                self.kill()  # ta bort oss själva (Player)


class Missil(pygame.sprite.Sprite):  # det inom parentes säger VAD vi är (en så kallad Sprite)

    def __init__(self):  # denna funktion körs när objektet skapas
        super(Missil, self).__init__()  # denna sak måste vara först i __init__
        self.image = pygame.Surface((10, 10))  # skapa bilden som tillhör karaktären
        self.image.fill((10,0,10))  # färglägg hela karaktären enfärgat
        self.rect = self.image.get_rect()  # rect styr var karaktären ska ritas ut

    def update(self):  # körs för varje frame
        self.rect.x += 1  # missilen åker åt höger, notera att self.rect.x används

object_list = pygame.sprite.OrderedUpdates()  # en lista som innehåller alla objekt som ska ritas ut
player = Player()  # skapar en spelare
object_list.add(player)  # lägger till spelaren i listan på saker som ska ritas ut

clock = pygame.time.Clock()

avsluta = "n"
while avsluta != "y":
    fonster.fill((255, 0, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            avsluta = "y"
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  # SPACE -> skapa en missil
                nymissil = Missil()  # skapa en ny missil
                nymissil.rect.x = 100  # sätt ut missilens startposition i x-led
                nymissil.rect.y = 100  # sätt ut missilens startposition i y-led
                object_list.add(nymissil)  # lägg till missilen över saker att rita ut
            if event.key == pygame.K_RIGHT:  # gå höger
                player.rect.x += 25  # player.rect.x beskriver spelarens x-position
            if event.key == pygame.K_DOWN:  # gå nedåt
                player.rect.y += 25  # player.rect.y beskriver spelarens y-position

    for object in object_list: # uppdatera alla saker i object_list (missiler rör på sig/player kollar krock)
        object.update()

    object_list.draw(fonster)  # ritar ut ALLA saker i object_list

    pygame.display.update()
    clock.tick(60)
