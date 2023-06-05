from math import pi

class Circle:
    def __init__(self, radius: int = 1):
        self._radius = radius

    def get_length(self):
        return 2 * pi * self._radius
    
    def get_area(self):
        return pi * self._radius**2
    
class Rectangle:

    def __init__(self, side_a: int = 1, side_b: int | None = None):
        self._side_a = side_a
        self._side_b = side_b if side_b else side_a
    
    def get_perimeter(self):
        return 2 * (self._side_a + self._side_b)
    
    def get_area(self):
        return self._side_a * self._side_b

circle1 = Circle(3)
rectangle1 = Rectangle(2, 3)
square1 = Rectangle(5)
print(f'{rectangle1.get_perimeter() =:2f}, {rectangle1.get_area() =:2f}')
print(f'{square1.get_perimeter() =:2f}, {square1.get_area() =:2f}')
print(f'{circle1.get_area() = }, {circle1.get_length() = }')