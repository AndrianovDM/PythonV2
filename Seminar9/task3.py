# Напишите декоратор, который сохраняет в json файл
# параметры декорируемой функции и результат, который она
# возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ
# json словаря.
# Для декорирования напишите функцию, которая может
# принимать как позиционные, так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой
# функции.
import json

def deco(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        file_name = f'{func.__name__}.json'
        dump_dict = {}
        dump_dict["arguments"] = [*args]
        for key, value in kwargs.items():
            dump_dict[key] = value
        dump_dict["result"] = result
        json.dump(dump_dict, open(file_name, "a", encoding='utf-8'), indent = 4)
        return result
    return wrapper

@deco
def the_best_sum_ever(x, y):
    return x + y

print(the_best_sum_ever(x = 3, y = 5))
