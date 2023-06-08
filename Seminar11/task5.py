class Rectangle:

    def __init__(self, width: float, length: float = None) -> None:
        self.width = width
        self.length = length if length else width

    def get_perimeter(self) -> float:
        return 2 * (self.width * self.length)
    
    def get_area(self) -> float:
        return self.width * self.length
    
    def __add__(self, other):
        return Rectangle(self.width + other.width, self.length + other.length)

    def __sub__(self, other):
        return Rectangle(abs(self.width - other.width), abs(self.length - other.length))
    
    def __lt__(self, other):
        return self.get_area() < other.get_area()

    def __le__(self, other):
        return self.get_area() <= other.get_area()

    def __eq__(self, other):
        return self.get_area() == other.get_area()

    def __str__(self) -> str:
        return f"Прямоугольник со сторонами {self.width}, {self.length} и периметром {self.get_perimeter()}"

if __name__ == "__main__":
    rect1 = Rectangle(2,2)
    rect2 = Rectangle(3,3)
    print(rect1 < rect2)
    print(rect1 > rect2)