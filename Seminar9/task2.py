# Дорабатываем задачу 1.
# Превратите внешнюю функцию в декоратор.
# Он должен проверять входят ли переданные в функциюугадайку числа в диапазоны [1, 100] и [1, 10].
# Если не входят, вызывать функцию со случайными числами
# из диапазонов.
import random
from typing import Callable

def guess_fuction(fun: Callable) -> Callable:
    def rapper(guess:int, attempts: int):
        guess = guess if 1 < guess < 100 else random.randint(1, 100)
        attempts = attempts if 1 < attempts < 10 else random.randint(1, 10)
        return fun(guess, attempts)
    return rapper

@guess_fuction
def attempts_count(guess:int, attempts: int):
    while attempts > 0:
        attempts -= 1
        val = int(input('Угадай число'))
        if val == guess:
            return 'Вы выиграли!'
    return 'Кол-во попыток исчерпано!'

print(attempts_count(150, 15))
