# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е.
# ✔ Точность вычислений должна составлять
# не менее 42 знаков после запятой.

import math
from decimal import Decimal

Decimal.getcontext().prec = 43

d = Decimal(input('Enter diameter: '))

if d > 1000:
    print('You are wrong')

length = Decimal(math.pi) * d
area = Decimal(math.pi) * (d**2 / 4)

print(f'lenght: {length}, area: {area}')
print(len(str(length)))
print(len(str(area)))