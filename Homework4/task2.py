# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def dictionary_return(**kwargs):
    dict = {}
    for key, value in kwargs.items():
        if isinstance(value, int or str or float or bool or tuple):
            dict[value] = key
        else:
            dict[str(value)] = key
    return dict

print(dictionary_return(car_brand='BMW', year_of_release= 2020, electric_car = True, 
                        engine_capacity = 3.5, functions = ['подогрев сидений', 'климат контроль', 'автопилот']))

