import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height


# Uncomment below to test in console

'''
shapes =[
    Circle(6),
    Rectangle(8, 2),
    Triangle(10, 2)
]
for shape in shapes:
    print(f" {shape.__class__.__name__} area: {shape.area()}")
'''

