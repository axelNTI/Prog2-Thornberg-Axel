class Dator:

    def __init__(self):
        self.name = 'Null'
        self.price = 0

    def skriv_ut_pris(self):
        print(f'{self.price} kr')

mindator = Dator()
mindator.name = 'Legion'
mindator.price = 3500
mindator.skriv_ut_pris()