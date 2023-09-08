class Car:
    def __init__(self, weight, price, colour, reg_number):
        self.weight = weight
        self.price = price
        self.colour = colour
        self.reg_number = reg_number


car = Car(1200, 95000, "Red", "ABC123")


class Truck(Car):
    def __init__(self, weight, price, colour, reg_number, storage_amount):
        super().__init__(weight, price, colour, reg_number)
        self.storage_amount = storage_amount


truck = Truck(12000, 3500000, "White", "DBC321", 950)
