from fastapi import FastAPI
from shapes import Circle, Rectangle, Triangle

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Shapes API!"}

@app.get("/circle_area/{radius}")
def circle_area(radius: float):
    circle = Circle(radius)
    return {"area": circle.area()}

@app.get("/rectangle_area/{width}/{height}")
def rectangle_area(width: float, height: float):
    rectangle = Rectangle(width, height)
    return {"area": rectangle.area()}

@app.get("/triangle_area/{base}/{height}")
def triangle_area(base: float, height: float):
    triangle = Triangle(base, height)
    return {"area": triangle.area()}

