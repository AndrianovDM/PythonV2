# 1. Ещё раз про import

# import sys
# print(sys)
# print(sys.builtin_module_names)
# print(*sys.path, sep='\n')

# ● Антипримеры импорта

# def randint(*args):
#     return 'Не то, что вы искали!'

# import random
# print(random.randint(1, 6))

# Правильно:
# import sys
# import random

# Неправильно:
# import sys, random

# Использование from и as

# from sys import builtin_module_names, path
# print(builtin_module_names)
# print(*path, sep='\n')

# import random as rnd
# from sys import builtin_module_names as bmn, path as p
# print(bmn)
# print(*p, sep='\n')
# print(rnd.randint(1, 6))
# print(path) # NameError: name 'path' is not defined
# print(sys.path) # NameError: name 'sys' is not defined

# Плохой import * (импорт звёздочка)

# from random import randint
# SIZE = 100
# _secret = 'qwerty'
# __top_secret = '1q2w3e4r5t6y'
# def func(a: int, b: int) -> str:
#     z = f'В диапазоне от {a} до {b} получили {randint(a, b)}'
#     return z
# result = func(1, 6)

# ● Файл main.py

# from super_module import *
# SIZE = 49.5
# print(f'{SIZE = }\n{result = }')
# print(f'{z = }') # NameError: name 'z' is not defined
# print(f'{_secret = }') # NameError: name '_secret' is not defined
# print(f'{func(100, 200) = }\n{randint(10, 20) = }')
# def func(a: int, b: int) -> int:
#     return a + b
# print(f'{func(100, 200) = }')

            # Переменная __all__

# from random import randint
# __all__ = ['func', '_secret']
# SIZE = 100
# _secret = 'qwerty'
# __top_secret = '1q2w3e4r5t6y'
# def func(a: int, b: int) -> str:
#     z = f'В диапазоне от {a} до {b} получили {randint(a, b)}'
#     return z
# result = func(1, 6)

# 2. Виды модулей

# """Four basic mathematical operations.
# Addition, subtraction, multiplication and division as functions.
# """
# _START_SUM = 0
# _START_MULT = 1
# _BEGINNING = 0
# _CONTINUATION = 1
# def add(*args):
#     res = _START_SUM
#     for item in args:
#         res += item
#     return res

# def sub(*args):
#     res = args[_BEGINNING]
#     for item in args[_CONTINUATION:]:
#         res -= item
#     return res

# def mul(*args):
#     res = _START_MULT
#     for item in args:
#         res *= item
#     return res

# def div(*args):
#     res = args[_BEGINNING]
#     for item in args[_CONTINUATION:]:
#         res /= item
#     return res

# Пишем свой модуль: __name__ == '__main__'

# print(f'{add(2, 4) = }')
# print(f'{add(2, 4, 6, 8) = }')
# print(f'{sub(10, 2) = }')
# print(f'{mul(2, 2, 2, 2, 2) = }')
# print(f'{div(-100, 5, -2) = }')

# import base_math
# x = base_math.mul # Плохой приём
# y = base_math._START_MULT # Очень плохой приём
# z = base_math.sub(73, 42)
# print(x(2, 3))
# print(y)
# print(z)

# """Two advanced mathematical operations.
# Integer division and exponentiation."""
# __all__ = ['div', 'exp']
# _BEGINNING = 0
# _CONTINUATION = 1
# def div(*args):
#     res = args[_BEGINNING]
#     for item in args[_CONTINUATION:]:
#         res //= item
#     return res

# def exp(*args):
#     res = args[_BEGINNING]
#     for item in args[_CONTINUATION:]:
#         res **= item
#     return res

# if __name__ == '__main__':
#     print(f'{div(42, 4) = }')
#     print(f'{exp(2, 4, 6, 8) = }')

                # Модуль random

# import random as rnd
# START = -100
# STOP = 1_000
# STEP = 10
# data = [2, 4, 6, 8, 42, 73]
# print(rnd.random())
# rnd.seed(42)
# state = rnd.getstate()
# print(rnd.random())
# rnd.setstate(state)
# print(rnd.random())
# print(rnd.randint(START, STOP))
# print(rnd.uniform(START, STOP))
# print(rnd.choice(data))
# print(rnd.randrange(START, STOP, STEP))
# print(data)
# rnd.shuffle(data)
# print(data)
# print(rnd.sample(data, 2))
# print(rnd.sample(data, 2, counts=[1, 1, 1, 1, 1, 100]))