# Создайте функцию-замыкание, которая запрашивает два целых числа:
# ○ от 1 до 100 для загадывания,
# ○ от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит
# угадать загаданное число за указанное число попыток. 
from typing import Callable

def guess_fuction(guess:int, attempts: int) -> Callable:
    count = attempts

    def attempts_count():
        nonlocal count
        while count > 0:
            count -= 1
            val = int(input('Угадай число'))
            if val == guess:
                return 'Вы выиграли!'
        return 'Кол-во попыток исчерпано!'
    return attempts_count

game = guess_fuction(5,3)
print(game())