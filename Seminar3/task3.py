# ✔ Создайте вручную кортеж содержащий элементы разных типов.
# ✔ Получите из него словарь списков, где:
# ключ — тип элемента,
# значение — список элементов данного типа.

import pprint

my_tuple = (1, 2, "A", 4.5, "B", 7, [1,2,3], ["C","D"], True, False)

my_dict = {}

for element in my_tuple:
    my_dict.setdefault(type(element), []).append(element)

pprint.pprint(my_dict)