class Rectangle:

    def __init__(self, width: float, length: float = None) -> None:
        self.width = width
        self.length = length if length else width
    
    @property
    def width(self):
        return self._width
    
    @property
    def length(self):
        return self._length
    
    @length.setter
    def length(self, new_len):
        if new_len <= 0:
            raise ValueError('Length cannot be lesser than or equal to zero')
        self._length = new_len
    
    @width.setter
    def width(self, new_width):
        if new_width <= 0:
            raise ValueError('Length cannot be lesser than or equal to zero')
        self._width = new_width
    
    def get_perimeter(self) -> float:
        return 2 * (self._width + self._length)
    
    def get_area(self) -> float:
        return self._width * self._length
    
    def __str__(self):
        return ( f'\nRectangle: {self.width} X {self.length}'
                 f'\nPerimeter: {self.get_perimeter()}' 
                 f'\nArea:      {self.get_area()}')
    
    def __repr__(self):
        return f'Rectangle:({self.width}, {self.length})'

def main():
    some_rect = Rectangle(10, 20)
    print(f'{some_rect = }')
    some_rect.length = 100
    some_rect.width = 200
    print(f'{some_rect = }')
    try:
        some_rect.length = 0
    except Exception as exc:
        print(f'\003[31m{exc.__class__.__name__}:{exc}\033[0m')
    
    try:
        some_rect.width = -100
    except Exception as exc:
        print(f'\003[31m{exc.__class__.__name__}:{exc}\033[0m')
    print(f'{some_rect = }')

if __name__ == '__main__':
    main()   
