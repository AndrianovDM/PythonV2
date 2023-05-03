# Функция получает на вход строку из двух чисел через пробел.
# ✔ Сформируйте словарь, где ключом будет
# символ из Unicode, а значением — целое число.
# ✔ Диапазон пар ключ-значение от наименьшего из введённых
# пользователем чисел до наибольшего включительно.


def f(num: str) -> dict[str,int]:
    start, stop =map(int, num.split())
    if (start > stop):
        start,stop = stop,start
    result ={}
    for i in range(start, stop + 1):
        result[chr(i)] = i
    return result

print(f("65 97"))
print(f("97 65"))