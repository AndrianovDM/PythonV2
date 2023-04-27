# Задание №6
# Погружение в Python | Коллекции
# Пользователь вводит строку текста. Вывести каждое слово с новой строки.
# ✔ Строки нумеруются начиная с единицы.
# ✔ Слова выводятся отсортированными согласно кодировки Unicode.
# ✔ Текст выравнивается по правому краю так, чтобы у самого длинного
# слова был один пробел между ним и номером строки.

my_string = input('Enter a string ').split()

my_string.sort()

longest = len(max(my_string, key=len))

for num, element in enumerate(my_string, 1):
    print(f'{num} {element:>{longest}}')