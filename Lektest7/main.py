class Rectangle:
    def __init__(self, name) -> None:
        self.height = 30
        self.width = 30
        self.name = name

    def area(self) -> None:
        print(self.width * self.height)


rectangle_A = Rectangle("A")
rectangle_A.height = 50
rectangle_B = Rectangle("B")
rectangle_B.area()
