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
    
    def __str__(self) -> str:
        return f"Прямоугольник со сторонами {self.width}, {self.length} и периметром {self.get_perimeter()}"

if __name__ == "__main__":
    rect1 = Rectangle(2,3)
    rect2 = Rectangle(2,3)
    rect3 = rect1 + rect2
    print(rect3)

    rect4 = Rectangle(4,5)
    rect5 = Rectangle(2,3)
    rect6 = rect4 - rect5
    print(rect6)