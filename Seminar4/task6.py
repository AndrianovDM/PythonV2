# ✔ Функция получает на вход список чисел и два индекса.
# ✔ Вернуть сумму чисел между между переданными индексами.
# ✔ Если индекс выходит за пределы списка, сумма считается
# до конца и/или начала списка.

def sumator(list_to_sum: list[int], i:int, k:int) -> int:
    if i > k: return 0
    list_len = len(list_to_sum)
    result = list_to_sum[max(i, 0):min(k, list_len)]
    return sum(result)

list_inp = [1, 4, -5, 3, -100, 3, 5_000]

print(sumator(list_inp, -3, 1))
print(sumator(list_inp, 1, 3))
print(sumator(list_inp, 10, 15))
print(sumator(list_inp, 2, 1))