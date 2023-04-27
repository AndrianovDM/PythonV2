       # Работа со списками

# list_1 = list()
# list_2 = list((3.14, True, "Hello world!"))
# list_3 = []
# list_4 = [3.14, True, "Hello world!"]

# my_list = [2, 4, 6, 8, 10, 12]
# print(my_list[0])
# print(my_list[6])

# my_list = [2, 4, 6, 8, 10, 12]
# print(my_list[-1])
# print(my_list[-10]) # IndexError: list index out of range

            # Метод append
# a = 42
# b = 'Hello world!'
# c = [1, 3, 5, 7]
# my_list = [None]
# my_list.append(a)
# print(my_list)
# my_list.append(b)
# print(my_list)
# my_list.append(c)
# print(my_list)
# my_list.append(my_list)
# print(my_list)
# # Вывод: [None, 42, 'Hello world!', [1, 3, 5, 7], [...]]

            # Метод extend

# a = 42
# b = 'Hello world!'
# c = [1, 3, 5, 7]
# my_list = [None]
# my_list.extend(a) # TypeError: 'int' object is not iterable
# print(my_list)
# my_list.extend(b)
# print(my_list)
# my_list.extend(c)
# print(my_list)
# my_list.extend(my_list)
# print(my_list

            # Метод pop

# my_list = [2, 4, 6, 8, 10, 12]
# spam = my_list.pop()
# print(spam, my_list)
# eggs = my_list.pop(1)
# print(eggs, my_list)
# err = my_list.pop(10) # IndexError: pop index out of range

            # Метод count

# my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
# spam = my_list.count(2)
# print(spam)
# eggs = my_list.count(3)
# print(eggs)

            # Метод index

# my_list = [2, 4, 6, 2, 8, 10, 12, 2, 4, 14, 2]
# spam = my_list.index(4)
# print(spam)
# eggs = my_list.index(4, spam + 1, 90)
# print(eggs)
# err = my_list.index(3) # ValueError: 3 is not in list

            # Метод insert

# my_list = [2, 4, 6, 8, 10, 12]
# my_list.insert(2, 555)
# print(my_list)
# my_list.insert(-2, 13)
# print(my_list)
# my_list.insert(42, 73) # my_list.append(73)
# print(my_list)

            # Метод remove

# my_list = [2, 4, 6, 8, 10, 12, 6]
# my_list.remove(6)
# print(my_list)
# my_list.remove(3) # ValueError: list.remove(x): x not in list
# print(my_list)

            # Cортировка списков

# my_list = ['H', 'e', 'l', 'l', 'o', 1, 3, 5, 7]
# my_list.sort() # TypeError: '<' not supported between instances of 'int' and 'str'
# res = sorted(my_list) # TypeError: '<' not supported between instances of 'int' and 'str'

            # Функция sorted()

# my_list = [4, 8, 2, 9, 1, 7, 2]
# sort_list = sorted(my_list)
# print(my_list, sort_list, sep='\n')
# rev_list = sorted(my_list, reverse=True)
# print(my_list, rev_list, sep='\n')

            # Метод sort()

# my_list = [4, 8, 2, 9, 1, 7, 2]
# my_list.sort()
# print(my_list)
# my_list.sort(reverse=True)
# print(my_list)

            # Функция reversed()

# my_list = [4, 8, 2, 9, 1, 7, 2]
# res = reversed(my_list)
# print(type(res), res)
# rev_list = list(reversed(my_list))
# print(rev_list)

# for item in reversed(my_list):
#     print(item)

            # Метод reverse() и синтаксический сахар [::-1]

# my_list = [4, 8, 2, 9, 1, 7, 2]
# my_list.reverse()
# print(my_list)

# my_list = [4, 8, 2, 9, 1, 7, 2]
# new_list = my_list[::-1]
# print(my_list, new_list, sep='\n')
# rev_list = list(reversed(my_list))

            # Срезы

# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# print(my_list[2:7:2])
# print(my_list[:7:2])
# print(my_list[2::2])
# print(my_list[2:7:])
# print(my_list[8:3:-1])
# print(my_list[3::])
# print(my_list[:7:])

            # Метод copy()

# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# new_list = my_list
# print(my_list, new_list, sep='\n')
# my_list[2] = 555
# print(my_list, new_list, sep='\n')

# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# new_list = my_list.copy()
# print(my_list, new_list, sep='\n')
# my_list[2] = 555
# print(my_list, new_list, sep='\n')

        # Зачем нужна функция copy.deepcopy()

# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_m = matrix.copy()
# print(matrix, new_m, sep='\n')
# matrix[0][1] = 555
# print(matrix, new_m, sep='\n')

# import copy
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# new_m = copy.deepcopy(matrix)
# print(matrix, new_m, sep='\n')
# matrix[0][1] = 555
# print(matrix, new_m, sep='\n')

            # Функция len

# my_list = [2, 4, 6, 2, 8, 10, 12, 14, 16, 18]
# matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
# print(len(my_list))
# print(len(matrix))
# print(len(matrix[1]))

            # Строки, str

# text = 'Hello world!'
# print(text[6])
# print(text[3:7])

# new_txt = text.replace('l', 'L', 2)
# print(text, new_txt, sep='\n')

            # Методы count, index, find

# text = 'Hello world!'
# print(text.count('l'))
# print(text.index('l'))
# print(text.find('l'))
# print(text.find('z'))

            # Реверс строк

# text = 'Hello world!'
# print(text[::-1])

            # Форматирование строк

# name = 'Alex'
# age = 12
# text = 'Меня зовут %s и мне %d лет' % (name, age)
# print(text)

            # Метод format

# name = 'Alex'
# age = 12
# text = 'Меня зовут {} и мне {} лет'.format(name, age)
# print(text)

            # f-строка

# name = 'Alex'
# age = 12
# text = f'Меня зовут {name} и мне {age} лет'
# print(text)
# print(f'{{Фигурные скобки}} и {{name}}')

            # Уточнение формата

# pi = 3.1415
# print(f'Число Пи с точностью два знака: {pi:.2f}')
# data = [3254, 4364314532, 43465474, 2342, 462256, 1747]
# for item in data:
#     print(f'{item:>10}')
# num = 2 * pi * data[1]
# print(f'{num = :_}')

# ● :.2f — число пи выводим с точность два знака после запятой
# ● :>10 — элементы списка выводятся с выравниванием по правому краю и
# общей шириной вывода в 10 символов
# ● = — выводим имя переменной, знак равенства с пробелами до и после него и
# только потом значение.
# ● :_ — число разделяется символом подчёркивания для деления на блоки по 3
# цифры

            # Метод split

# link = 'https://habr.com/ru/users/dzhoker1/posts/'
# urls = link.split('/')
# print(urls)
# a, b, c = input('Введите 3 числа через пробел: ').split()
# print(c, b, a)

# a, b, c, *_ = input('Введите не менее трёх чисел через пробел:').split()

            # Метод join

# data = ['https:', '', 'habr.com', 'ru', 'users', 'dzhoker1',
# 'posts']
# url = '/'.join(data)
# print(url)

            # Методы upper, lower, title, capitalize

# text = 'однажды в СТУДЁНУЮ зИмнЮЮ ПоРУ'
# print(text.upper())
# print(text.lower())
# print(text.title())
# print(text.capitalize())

# ● upper — все символы приводятся к верхнему регистру
# ● lower — все символы приводятся к нижнему регистру
# ● title — первый символ каждого слова (разделитель слов - пробел) приводится
# к верхнему регистру, остальные символы к нижнему
# ● capitalize — первый символ строки в верхнем регистре, остальные в нижнем

            # Методы startswith и endswith

# text = 'Однажды в студёную зимнюю пору'
# print(text.startswith('Однажды'))
# print(text.endswith('зимнюю', 0, -5))

            # Кортеж, tuple

# a = ()
# b1 = 1,
# b2 = (1,)
# c1 = 1, 2, 3,
# c2 = (1, 2, 3)
# d = tuple(range(3))
# print(a, b1, b2, c1, c2, d, sep='\n')

            # Словарь, dict

# a = {'one': 42, 'two': 3.14, 'ten': 'Hello world!'}
# b = dict(one=42, two=3.14, ten='Hello world!')
# c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello world!')])
# print(a == b == c)

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4}
# my_dict['ten'] = 10
# print(my_dict)

            # Доступ через квадратные скобки []

# TEN = 'ten'
# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict['two'])
# print(my_dict[TEN])
# print(my_dict[1]) # KeyError: 1

            # Доступ через метод get

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.get('two'))
# print(my_dict.get('five'))
# print(my_dict.get('five', 5))
# print(my_dict.get('ten', 5))

            # Метод setdefault

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# spam = my_dict.setdefault('five')
# print(f'{spam = }\t{my_dict=}')
# eggs = my_dict.setdefault('six', 6)
# print(f'{eggs = }\t{my_dict=}')
# new_spam = my_dict.setdefault('two')
# print(f'{new_spam=}\t{my_dict=}')
# new_eggs = my_dict.setdefault('one', 1_000)
# print(f'{new_eggs=}\t{my_dict=}')

            # Метод keys

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.keys())
# for key in my_dict.keys():
#     print(key)

            # Метод values

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.values())
# for value in my_dict.values():
#     print(value)

            # Метод items

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# print(my_dict.items())
# for tuple_data in my_dict.items():
#     print(tuple_data)
# for key, value in my_dict.items():
#     print(f'{key = } value before 100 - {100 - value}')

            # Метод popitem

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# spam = my_dict.popitem()
# print(f'{spam = }\t{my_dict=}')
# eggs = my_dict.popitem()
# print(f'{eggs = }\t{my_dict=}')

            # Метод pop

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# spam = my_dict.pop('two')
# print(f'{spam = }\t{my_dict=}')
# err = my_dict.pop('six') # KeyError: 'six'
# err = my_dict.pop() # TypeError: pop expected at least 1 argument, got 0

            # Метод update

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# my_dict.update(dict(six=6))
# print(my_dict)
# my_dict.update(dict([('five', 5), ('two', 42)]))
# print(my_dict)

# my_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'ten': 10}
# new_dict = my_dict | {'five': 5, 'two': 42} | dict(six=6)
# print(new_dict)

            # Множества set и frozenset

# my_set = {1, 2, 3, 4, 2, 5, 6, 7}
# print(my_set)
# my_f_set = frozenset((1, 2, 3, 4, 2, 5, 6, 7,))
# print(my_f_set)
# not_set = {1, 2, 3, 4, 2, 5, 6, 7, ['a', 'b']} # TypeError: unhashable type: 'list'

            # Метод add

# my_set = {3, 4, 2, 5, 6, 1, 7}
# my_set.add(9)
# print(my_set)
# my_set.add(7)
# print(my_set)
# my_set.add(9, 10) # TypeError: set.add() takes exactly one argument (2 given)
# my_set.add((9, 10))
# print(my_set)

            # Метод remove

# my_set = {3, 4, 2, 5, 6, 1, 7}
# my_set.remove(5)
# print(my_set)
# my_set.remove(10) # KeyError: 10

            # Метод discard

# my_set = {3, 4, 2, 5, 6, 1, 7}
# my_set.discard(5)
# print(my_set)
# my_set.discard(10)

            # Метод intersection

# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set.intersection(other_set)
# print(f'{my_set = }\n{other_set = }\n{new_set = }')

# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set & other_set
# print(f'{my_set = }\n{other_set = }\n{new_set = }')

            # Метод union

# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set.union(other_set)
# print(f'{my_set = }\n{other_set = }\n{new_set = }')
# new_set_2 = my_set | other_set
# print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')

            # Метод difference

# my_set = {3, 4, 2, 5, 6, 1, 7}
# other_set = {1, 4, 42, 314}
# new_set = my_set.difference(other_set)
# print(f'{my_set = }\n{other_set = }\n{new_set = }')
# new_set_2 = my_set - other_set
# print(f'{my_set = }\n{other_set = }\n{new_set_2 = }')

            # Классы bytes и bytearray

# text_en = 'Hello world!'
# res = text_en.encode('utf-8')
# print(res, type(res))
# text_ru = 'Привет, мир!'
# res = text_ru.encode('utf-8')
# print(res, type(res))

# x = bytes(b'\xd0\x9f\xd1\x80\xd0\xb8')
# y = bytearray(b'\xd0\x9f\xd1\x80\xd0\xb8')
# print(f'{x = }\n{y = }')