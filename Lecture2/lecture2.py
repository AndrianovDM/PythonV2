                    # Функция type()
# a = 5
# print(type(a))
# a = "hello world"
# print(type(a))
# a = 42.0 * 3.141592 / 2.71828
# print(type(a))

                    # Функция isinstance()
# data = 42
# print(isinstance(data, int))

# data = 3.14
# print(isinstance(data, (int, float, complex)))
                    # Оператор is

# num = 2 + 2 * 2
# digit = 36 / 6
# print(num == digit)
# print(num is digit)
                    # Оператор is
# a = 5
# print(a, id(a))
# a += 1
# print(a, id(a))

# txt = 'Hello world!'
# print(txt, id(txt))
# txt = txt.replace(' ', '_')
# print(txt, id(txt))

# a = с = 2
# b = 3
# print(a, id(a), b, id(b), c, id(c))
# a = b + c
# print(a, id(a), b, id(b), c, id(c))

                    # Хэш hash() как проверка на неизменяемость
# x = 42
# y = 'text'
# z = 3.1415
# print(hash(x), hash(y), hash(z))
# my_list = [x, y, z]
# print(hash(my_list)) # получим ошибку, т.к. list изменяемый

                    # Аннотация типов
# a: int = 42
# b: float = float(input('Введи число: '))
# a = a / b

###########
# def my_func(data: list[int, float]) -> float:
#     res = sum(data) / len(data)
#     return res
# print(my_func([2, 5.5, 15, 8.0, 13.74]))
###########

# a: int | float = 42
# b: float = float(input('Введи число: '))
# a = a / b

                        # Атрибуты объекта
# print("Hello world!".__doc__)
# print(str.__doc__)

                        # Методы объекта

# print("Hello world!".upper())
# print("Hello world!".count('l'))

                        # Функция dir()
# print(dir("Hello world!"))
                        # Функция help()
# help("Hello world!")
# help(str)

                        # Целые числа, функция int()
# x = int("42")
# y = int(3.1415)
# z = int("hello", base=30)
# print(x, y, z, sep='\n')

# import sys
# STEP = 2 ** 16
# num = 1
# for _ in range(30):
#     print(sys.getsizeof(num), num)
#     num *= STEP
# print(sys.getsizeof(10 ** 100))

                    # Формат представления числа.
# num = 7_901_123_456_789

                    # Функции bin(), oct(), hex()
# num = 2 ** 16 - 1
# b = bin(num)
# o = oct(num)
# h = hex(num)
# print(b, o, h)

                    # Вещественные числа, функция float()
# print(0.1 + 0.2)
# pi = 3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375
# print(pi)

                    # Логические типы, функция bool()
# DEFAULT = 42
# num = int(input('Введите уровень или ноль для значения поумолчанию: '))
# level = num or DEFAULT
# print(level)

# name = input('Как вас зовут? ')
# if name:
#     print('Привет, ' + name)
# else:
#     print('Анонимус, приветствую')

# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# while data:
#     print(data.pop())

                    # Конкатенация строк
# LIMIT = 120
# ATTENTION = 'Внимание!'
# name = input('Твоё имя? ')
# age = int(input('Твой возраст? '))
# text = ATTENTION + ' Хоть тебе и осталось ' + str(100 - age) +\
#         " до ста лет, но длинна строки не должна превышать " +\
# str(LIMIT) + ' символов.'
# print(text)

# empty_str = ''
# en_str = 'Text'
# ru_str = 'Текст'
# unicode_str = '😀😍😉🙃'
# print(empty_str.__sizeof__())
# print(en_str.__sizeof__())
# print(ru_str.__sizeof__())
# print(unicode_str.__sizeof__())

                    # 5. Математика в Python
import math
import decimal
import fractions
                    # Модуль math
# print(math.pi, math.e, math.inf, math.nan, math.tau, sep='\n')

                    # Модуль decimal
# pi =decimal.Decimal('3.141_592_653_589_793_238_462_643_383_279_502_884_197_169_399_375')
# print(pi)
# num = decimal.Decimal(1) / decimal.Decimal(3)
# print(num)
# decimal.getcontext().prec = 120
# science = 2 * pi * decimal.Decimal(23.452346) ** 2
# print(science)

                    # Модуль fraction
# f1 = fractions.Fraction(1, 3)
# print(f1)
# f2 = fractions.Fraction(3, 5)
# print(f2)
# print(f1 * f2)
                    # Класс complex()
# a = complex(2, 3)
# b = complex('2+3j')
# print(a, b, a == b, sep='\n')