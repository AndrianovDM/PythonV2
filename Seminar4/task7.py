# ✔ Функция получает на вход словарь с названием компании в качестве ключа
# и списком с доходами и расходами (3-10 чисел) в качестве значения.
# ✔ Вычислите итоговую прибыль или убыток каждой компании. Если все компании
# прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

dict1 = {'Merck': [1, 2, 4, 5, -8, 4, 6, -3, -36], 'Apple': [8, 5, 3, -5, 9, 14, -12],
'Samsung': [56, 32, 8, -12, 4, 23, 9],
'Tesla': [2, 4, -4, 6, -8, 12, 16]}

dict2 = {'Merck': [1, 2, 4, 5, 8, 4, 6, 3], 'Apple': [8, 5, 3, 5, 9, 14, 12],
'Samsung': [56, 32, 8, 12, 4, 23, 9],
'Tesla': [2, 4, 4, 6, 8, 12, 16]}

def yearly_income(input_dict: dict[str, list[int]]) -> bool:
    for key in input_dict:
        if sum(input_dict[key]) <= 0: return False
    return True

print(yearly_income(dict1), yearly_income(dict2))