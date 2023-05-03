# ✔ Функция получает на вход список чисел.
# ✔ Отсортируйте его элементы in place без использования
# встроенных в язык сортировок.
# ✔ Как вариант напишите сортировку пузырьком.
# Её описание есть в википедии.

def my_sort(data: list[int | float]) -> None:
    for i in range(len(data)-1):
        min_index = i
        for j in range(i + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
        if min_index != i:
            data[min_index], data[i] = data[i], data[min_index]


data = [9, 5, 4, 6, 7, 3, 2, 1, 8]
print(data)
my_sort(data)
print(data)