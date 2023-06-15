class MyExceptions(Exception):
    pass

class MyMinLengthError(MyExceptions):

    def __init__(self, param, value):
        self.param = param
        self.value = value
    
    def __str__(self):

        if self.param < self.value:
            return f'Сторона треугольника не может быть меньше нуля\n' \
            f'Заданное число {self.param} < {self.value}'
        
        elif self.param == self.value:
            return f'Сторона треугольника не может быть равна нулю\n' \
            f'Заданное число {self.param} = {self.value}'
        

class MyTriangleError(MyExceptions):
    
    def __init__(self, value1: int, value2: int, value3: int):
        self.a = value1
        self.b = value2
        self.c = value3
    
    def __str__(self):
        print(f"Tреугольника со сторонами {self.a}, {self.b}, {self.c} не существует!")


class Triangle:

    def __init__(self, a: int, b: int, c: int) -> None:
        if a > 0:
            self.a = a
        else:
            raise MyMinLengthError(a, 0)
        if b > 0:
            self.b = b
        else:
            raise MyMinLengthError(b, 0)
        if c > 0:
            self.c = c
        else:
            raise MyMinLengthError(c, 0)
        
    def check_sides(self):

        check1 = self.a + self.b
        check2 = self.a + self.c
        check3 = self.b + self.c
        if (check1 < self.c or check2 < self.b or check3 < self.a):
            raise MyTriangleError(self.a, self.b, self.c)
        else:
            if (self.a == self.b and self.b == self.c and self.c == self.a):
                print("Треугольник равносторонний")
            elif (self.a == self.b or self.b == self.c or self.c == self.a):
                print("Треугольник равнобедренный")
            else:
                print("Треугольник разносторонний")

if __name__ == "__main__":
    try:
        a = int(input("Введите длинну стороны треугольника №1: " ))
        b = int(input("Введите длинну стороны треугольника №2: "))
        c = int(input("Введите длинну стороны треугольника №3: "))

    except ValueError as val:
        print(f"Нужно задать число: {val}")

    t1 = Triangle(a, b, c)
    t1.check_sides()