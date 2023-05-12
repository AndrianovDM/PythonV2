            # 1. Создание своих функции

# a = 42
# print(type(a), id(a))
# print(type(id))

# very_bad_programming_style = sum
# print(very_bad_programming_style([1, 2, 3]))

# def my_func():
#     pass

# плохо:
# if a != 5:
#     pass
# else:
#     a += 1

# Уже лучше:
# if a == 5:
#     a += 1
# else:
#     pass

# Отлично. Ничего лишнего:
# if a == 5:
#     a += 1

            # Аргументы функции

# def quadratic_equations(a: int | float, b: int | float, c: int |
# float) -> tuple[float, float] | float | str:
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
#     elif d == 0:
#         return -b / (2 * a)
#     else:
#         return 'Нет решений'
# print(quadratic_equations(2, -3, -9))

# def quadratic_equations(a: int | float, b: int | float, c: int |
# float) -> tuple[float, float] | float | None:
#     return None

# def quadratic_equations(a, b, c):
#     print(quadratic_equations(2, -3)) # TypeError: quadratic_equations() missing 1 required positional argument: 'c'

            # Изменяемые и неизменяемые аргументы

# def no_mutable(a: int) -> int:
#     a += 1
#     print(f'In func {a = }') # Для демонстрации работы, но не для привычки принтить из функции
#     return a

# a = 42
# print(f'In main {a = }')
# z = no_mutable(a)
# print(f'{a = }\t{z = }')


# def mutable(data: list[int]) -> list[int]:
#     for i, item in enumerate(data):
#         data[i] = item + 1
#     print(f'In func {data = }') # Для демонстрации работы, но не для привычки принтить из функции
#     return data

# my_list = [2, 4, 6, 8]
# print(f'In main {my_list = }')
# new_list = mutable(my_list)
# print(f'{my_list = }\t{new_list = }')

            # Возврат значения

# def quadratic_equations(a, b, c):
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
#     if d == 0:
#         return -b / (2 * a)
#     return None


            # Неявный return

# def no_return(data: list[int]):
#     for i, item in enumerate(data):
#         data[i] = item + 1
#     print(f'In func {data = }') # Для демонстрации работы, но не для привычки принтить из функции

# my_list = [2, 4, 6, 8]
# print(f'In main {my_list = }')
# new_list = no_return(my_list)
# print(f'{my_list = }\t{new_list = }')


# def quadratic_equations(a, b, c):
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
#     if d == 0:
#         return -b / (2 * a)


            # Значения по умолчанию

# def quadratic_equations(a, b=0, c=0):
#     d = b ** 2 - 4 * a * c
#     if d > 0:
#         return (-b + d ** 0.5) / (2 * a), (-b - d ** 0.5) / (2 * a)
#     if d == 0:
#         return -b / (2 * a)
    
# print(quadratic_equations(2, -9))

            # Изменяемый объект как значение по умолчанию

# def from_one_to_n(n, data=[]):
#     for i in range(1, n + 1):
#         data.append(i)
#     return data

# new_list = from_one_to_n(5)
# print(f'{new_list = }')
# other_list = from_one_to_n(7)
# print(f'{other_list = }')

# def from_one_to_n(n, data=None):
#     if data is None:
#         data = []
#     for i in range(1, n + 1):
#         data.append(i)
#     return data

            # Позиционные и ключевые параметры

# def func(positional_only_parameters, /, positional_or_keyword_parameters, *,
#     keyword_only_parameters):
#     pass

# ● Пример обычной функции:
# def standard_arg(arg):
#     print(arg) # Принтим для примера, а не для привычки
# standard_arg(42)
# standard_arg(arg=42)

# ● Пример только позиционной функции:
# def pos_only_arg(arg, /):
#     print(arg) # Принтим для примера, а не для привычки

# pos_only_arg(42)
# pos_only_arg(arg=42) # TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'

# ● Пример только ключевой функции:
# def kwd_only_arg(*, arg):
#     print(arg) # Принтим для примера, а не для привычки
# kwd_only_arg(42)
# kwd_only_arg(arg=42)

# ● Пример функции со всеми вариантами параметров:
# def combined_example(pos_only, /, standard, *, kwd_only):
#     print(pos_only, standard, kwd_only) # Принтим для примера, а не для привычки
# combined_example(1, 2, 3) # TypeError: combined_example() takes positional arguments but 3 were given
# combined_example(1, 2, kwd_only=3)
# combined_example(1, standard=2, kwd_only=3)
# combined_example(pos_only=1, standard=2, kwd_only=3) # TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'

# def triangulation(*, x, y, z):
#     pass
# triangulation(y=5, z=2, x=11)

                # Параметры args и kwargs

# def mean(args):
#     return sum(args) / len(args)
# print(mean([1, 2, 3]))
# print(mean(1, 2, 3)) # TypeError: mean() takes 1 positional argument but 3 were given

# def mean(*args):
#     return sum(args) / len(args)
# print(mean(*[1, 2, 3]))
# print(mean(1, 2, 3))

# def school_print(**kwargs):
#     for key, value in kwargs.items():
#         print(f'По предмету "{key}" получена оценка {value}')
# school_print(химия=5, физика=4, математика=5, физра=5)

                # Области видимости: global и nonlocal

# def func(y: int) -> int:
#     x = 100
#     print(f'In func {x = }') # Для демонстрации работы, но не для привычки принтить из функции
#     return y + 1

# x = 42
# print(f'In main {x = }')
# z = func(x)
# print(f'{x = }\t{z = }')

# ● Глобальные переменные:
# def func(y: int) -> int:
#     global x
#     x += 100
#     print(f'In func {x = }') # Для демонстрации работы, но не для привычки принтить из функции
#     return y + 1

# x = 42
# print(f'In main {x = }')
# z = func(x)
# print(f'{x = }\t{z = }')

# ● Не локальные переменные:
# def main(a):
#     x = 1
#     def func(y):
#         nonlocal x
#         x += 100
#         print(f'In func {x = }') # Для демонстрации работы, но не для привычки принтить из функции
#         return y + 1
#     return x + func(a)

# x = 42
# print(f'In main {x = }')
# z = main(x)
# print(f'{x = }\t{z = }')


                # Доступ к константам

# LIMIT = 1_000
# def func(x, y):
#     result = x ** y % LIMIT
#     return result
# print(func(42, 73))

                # Анонимная функция lambda

# def add_two_def(a, b):
#     return a + b

# add_two_lambda = lambda a, b: a + b
# print(add_two_def(42, 3.14))
# print(add_two_lambda(42, 3.14))

# my_dict = {'two': 2, 'one': 1, 'four': 4, 'three': 3, 'ten': 10}
# s_key = sorted(my_dict.items())
# s_value = sorted(my_dict.items(), key=lambda x: x[1])
# print(f'{s_key = }\n{s_value = }')

                # Документирование кода функций

# def max_before_hundred(*args):
#     """Return the maximum number not exceeding 100."""
#     m = float('-inf')
#     for item in args:
#         if m < item < 100:
#             m = item
#     return m

# print(max_before_hundred(-42, 73, 256, 0))

# def max_before_hundred(*args):
#     """Return the maximum number not exceeding 100.
#     :param args: tuple of int or float numbers
#     :return: int or float number from the tuple args
#     """
#     ...

# help(max_before_hundred)

                # Функция map()

# texts = ["Привет", "ЗДОРОВА", "привеТствую"]
# res = map(lambda x: x.lower(), texts)
# print(*res)

                # Функция filter()

# numbers = [42, -73, 1024]
# res = tuple(filter(lambda x: x > 0, numbers))
# print(res)

                # Функция zip()

# names = ["Иван", "Николай", "Пётр"]
# salaries = [125_000, 96_000, 109_000]
# awards = [0.1, 0.25, 0.13, 0.99]
# for name, salary, award in zip(names, salaries, awards):
#     print(f'{name} заработал {salary:.2f} денег и премию {salary* award:.2f}')

                # Функции max(), min(), sum()

# lst_1 = []
# lst_2 = [42, 256, 73]
# lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр", 109_000)]
# print(max(lst_1, default='empty'))
# print(max(*lst_2))
# print(max(lst_3, key=lambda x: x[1]))

# lst_1 = []
# lst_2 = [42, 256, 73]
# lst_3 = [("Иван", 125_000), ("Николай", 96_000), ("Пётр", 109_000)]
# print(min(lst_1, default='empty'))
# print(min(*lst_2))
# print(min(lst_3, key=lambda x: x[1]))

# my_list = [42, 256, 73]
# print(sum(my_list))
# print(sum(my_list, start=1024))

                # Функции all(), any()

# def all(iterable):
#     for element in iterable:
#         if not element:
#             return False
#     return True

# numbers = [42, -73, 1024]
# if all(map(lambda x: x > 0, numbers)):
#     print('Все элементы положительные')
# else:
#     print('В последовательности есть отрицательные и/или нулевые элементы')

                # ● Функция any()

# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#     return False

# numbers = [42, -73, 1024]
# if any(map(lambda x: x > 0, numbers)):
#     print('Хотя бы один элемент положительный')
# else:
#     print('Все элементы не больше нуля')

                # ● Функция chr()

# print(chr(97))
# print(chr(1105))
# print(chr(128519))

                # ● Функция ord()

# print(ord('a'))
# print(ord('а'))
# print(ord('😉'))

                # ● Функция locals()

# SIZE = 10

# def func(a, b, c):
#     x = a + b
#     print(locals())
#     z = x + c
#     return z

# func(1, 2, 3)

                # ● Функция globals()

# SIZE = 10
# def func(a, b, c):
#     x = a + b
#     print(globals())
#     z = x + c
#     return z

# print(globals())
# print(func(1, 2, 3))

# x = 42
# glob_dict = globals()
# glob_dict['x'] = 73
# print(x)

                # ● Функция vars()

# print(vars(int))