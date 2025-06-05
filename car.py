class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def drive(self):
        print(f"Driving {self.brand} {self.model}")

car1 = Car("G's", "BMW")
car2 = Car("Bugatti", "BMW")

car1.drive()
car2.drive()
