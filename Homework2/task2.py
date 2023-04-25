# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

import re
import fractions

def fract(num:str) -> int:
    numbers = re.findall(r'\d+', num)
    return numbers

num_1 = input('Введите первую дробь: ')
num_2 = input('Введите вторую дробь: ')
num_one = fract(num_1)
num_two = fract(num_2)

if num_one[1] == num_two[1]:
    print('Сумма дробей:', f'{int(num_one[0]) + int(num_two[0])}/{int(num_one[1])}')
    print('Проверка:', fractions.Fraction(num_1) + fractions.Fraction(num_2))
else:
    print('Сумма дробей:', f'{int(num_one[0])*int(num_two[1]) + int(num_two[0])*int(num_one[1])}/{int(num_one[1])*int(num_two[1])}')
    print('Проверка:', fractions.Fraction(num_1) + fractions.Fraction(num_2))

print('Произведение дробей:', f'{int(num_one[0]) * int(num_two[0])}/{int(num_one[1]) * int(num_two[1])}')
print('Проверка:', fractions.Fraction(num_1) * fractions.Fraction(num_2))
