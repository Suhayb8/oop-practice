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
print("----animal 🐶")
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def __init__(self,name, age, breed ):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        print("-_- 🐶 -_-")
        print("Woof!")
        print(self.name, self.age, self.breed)

dog = Dog("🐶John",9,"German Shepherd")
dog.speak()
class Cat(Animal):
    def __init__(self,name, age, breed ):
        super().__init__(name, age)
        self.breed = breed
    def speak(self):
        print("-_- 🐈 -_-")
        print("Meow!")
        print(self.name, self.age, self.breed)

cat = Cat("🐈lucky", 7, "Sphynx")
cat.speak()
