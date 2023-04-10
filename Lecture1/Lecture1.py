                            #  Переменные и требования к именам
# a = 5
# print(a)
# a = "hello world"
# print(a)
# a = 42.0 * 3.141592 / 2.71828
# print(a)

                            # Константы
# MAX_COUNT = 1000
# ZERO = 0
# DATA_AFTER_DELETE = 'No data'
# DAY = 60 * 60 * 24

                            # Функция id()
# a = 5
# print(id(a))
# a = "hello world"
# print(id(a))
# a = 42.0 * 3.141592 / 2.71828
# print(id(a))

                            # Ввод и вывод данных

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
# print(42)
# print(1, 2, 3, 4)
# print('Hello', ',', 'world', '!')

# print(42, sep='___', end='\n(=^.^=)\n')
# print(1, 2, 3, 4, sep='___', end='\n(=^.^=)\n')
# print('Hello', ',', 'world', '!', sep='___', end='\n(=^.^=)\n')

# number = 42
# print(number, sep='___', end='\n(=^.^=)\n')
# ONE = 1
# TWO = 2
# print(ONE, TWO, 3, 4, sep='> <', end='>')

                            # Ввод, функция input()

# result = input([prompt])
# name = input('Ваше имя: ')
# age = input('Ваш возраст: ')
# age = float(input('Ваш возраст: '))
# how_old = age - 18
# print(how_old, "лет назад ты стал совершеннолетним")

                            # Если, if

# pwd = 'text'
# res = input('Input password: ')
# if res == pwd:
#     print('Доступ разрешён')

# pwd = 'text'
# res = input('Input password: ')
# if res == pwd:
#     print('Доступ разрешён')
#     print('Но будьте осторожны')
# print('Работа завершена')

                            # Иначе, else

# pwd = 'text'
# res = input('Input password: ')
# if res == pwd:
#     print('Доступ разрешён')
#     print('Но будьте осторожны')
# else:
#     print('Доступ запрещён')
# print('Работа завершена')

# pwd = 'text'
# res = input('Input password: ')
# if res == pwd:
#     print('Доступ разрешён')
#     my_math = int(input('2 + 2 = '))
#     if 2 + 2 == my_math:
#         print('Вы в нормальном мире')
#     else:
#         print('Но будьте осторожны')
# else:
#     print('Доступ запрещён')
# print('Работа завершена')

                            # Еще если, elif

# color = input('Твой любимый цвет: ')
# if color == 'красный':
#     print('Любитель яркого')
# elif color == 'зелёный':
#     print('Ты не охотник?')
# elif color == 'синий':
#     print('Ха, классика!')
# else:
#     print('Тебя не понять')

                            # Выбор из вариантов, match и case

# color = input('Твой любимый цвет: ')
# match color:
#     case 'красный' | 'оранжевый':
#         print('Любитель яркого')
#     case 'зелёный':
#         print('Ты не охотник?')
#     case 'синий' | 'голубой':
#         print('Ха, классика!')
#     case _:
#         print('Тебя не понять')

                            # Логические конструкции, or, and, not

# year = int(input('Введите год в формате yyyy: '))
# if year % 4 != 0:
#     print("Обычный")
# elif year % 100 == 0:
#     if year % 400 == 0:
#         print("Високосный")
#     else:
#         print("Обычный")
# else:
#     print("Високосный")

# year = int(input('Введите год в формате yyyy: '))
# if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
#     print("Обычный")
# else:
#     print("Високосный")

# year = int(input('Введите год в формате yyyy: '))
# if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
#     print("Високосный")

                            # Проверка на вхождение, in

# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# num = int(input('Введи число: '))
# if num in data:
#     print('Леонардо передаёт привет!')

# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# num = int(input('Введи число: '))
# if num not in data:
#     print('Леонардо грустит :-(')

                            # Тернарный оператор

# my_math = int(input('2 + 2 = '))
# if 2 + 2 == my_math:
#     print('Верно!')
# else:
#     print('Вы уверены?')

# my_math = int(input('2 + 2 = '))
# print('Верно!' if 2 + 2 == my_math else 'Вы уверены?')

                            # Логический цикл while
# num = float(input('Введите число: '))
# count = 0
# while count < num:
#     print(count)
#     count += 2

                            # Возврат в начало цикла, continue

# num = float(input('Введите число: '))
# STEP = 2
# limit = num - STEP
# count = -STEP
# while count < limit:
#     count += STEP
#     if count % 12 == 0:
#         continue
#     print(count)


                            # Досрочное завершение цикла, break

# min_limit = 0
# max_limit = 10
# while True:
#     print('Введи число между', min_limit, 'и', max_limit, '? ')
#     num = float(input())
#     if num < min_limit or num > max_limit:
#         print('Неверно')
#     else:
#         break
# print('Было введено число ' + str(num))

                            # Действие после цикла, else

# min_limit = 0
# max_limit = 10
# count = 3

# while count > 0:
#     print('Попытка ' + str(count))
#     count -= 1
#     num = float(input('Введи число между ' + str(min_limit) + ' и' + str(max_limit) + ': '))
#     if num < min_limit or num > max_limit:
#         print('Неверно')
#     else:
#         break

# else:
#     print('Исчерпаны все попытки. Сожалею.')
#     quit()
# print('Было введено число ' + str(num))

                            # Цикл итератор for in

# data = [0, 1, 1, 2, 3, 5, 8, 13, 21]
# for item in data:
#     print(item)

                            # Цикл по целым числам, он же
                            # арифметический цикл, функция range()

# num = int(input('Введите число: '))
# for i in range(0, num, 2):
#     print(i)

# count = 10
# for i in range(count):
#     for j in range(count):
#         for k in range(count):
#             print(i, j, k)

# count = 10
# for i in range(count):
#     print(i)
# for i in range(count):
#     print(i)

# animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
# for animal in animals:
#     print(animal)

                            # Цикл с нумерацией элементов, функция
                            # enumerate()

# animals = ['cat', 'dog', 'wolf', 'rat', 'dragon']
# for i, animal in enumerate(animals, start=1):
#     print(i, animal)



