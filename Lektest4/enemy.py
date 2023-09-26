class Enemy:
    def __init__(self, hp) -> None:
        self.width = 30
        self.height = 30
        self.hp = hp

    def info(self) -> None:
        print(f"Width: {self.width}\nHeight: {self.height}\nHP: {self.hp}")


enemy_1 = Enemy(7)
enemy_1.height = 50

enemy_2 = Enemy(10)
enemy_2.info()
