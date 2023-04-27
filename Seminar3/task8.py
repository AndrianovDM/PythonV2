# Задание №8
# Погружение в Python | Коллекции
# ✔ Три друга взяли вещи в поход. Сформируйте
# словарь, где ключ — имя друга, а значение —
# кортеж вещей. Ответьте на вопросы:
# ✔ Какие вещи взяли все три друга
# ✔ Какие вещи уникальны, есть только у одного друга
# ✔ Какие вещи есть у всех друзей кроме одного
# и имя того, у кого данная вещь отсутствует
# ✔ Для решения используйте операции
# с множествами. Код должен расширяться
# на любое большее количество друзей.

dict_1 = {'Friend_1': ('Фонарик', 'Палатка','Спичики', 'Тушенка', 'Удочка', 'Спальник', 'Лопата'),
          'Friend_2': ('Котелок', 'Спички','Тушенка', 'Спиннинг', 'Спальник', 'Наживка'),
          'Friend_3': ('Фонарик', 'Палатка','Тушенка', 'Удочка', 'Спальник', 'Наживка', 'Лопата')}

set_1  = set()
for k in dict_1:
    if not set_1:
        set_1 = set(dict_1[k])
    else:
        set_1 &= set(dict_1[k])
print(set_1)


my_tuple = dict_1.keys()
lst = []
for friend in my_tuple:
    my_set = set(dict_1[friend])
    for other in [x for x in my_tuple if x != friend]:
        my_set -= set(dict_1[other])
    if my_set:
        print(my_set)

for friend in my_tuple:
    to_remove = set(dict_1[friend])
    my_set = set()
    for other in [x for x in my_tuple if x != friend]:
        if not my_set:
            my_set = set(dict_1[other])
        else:
            my_set &= set(dict_1[other])
    my_set -= to_remove
    if my_set:
        print(f'{friend} doens\'t take {my_set}')
