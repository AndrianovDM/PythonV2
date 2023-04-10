# Программа загадывает число от 0 до 1000. 
# Необходимо угадать число за 10 попыток. 
# Программа должна подсказывать «больше» или «меньше» после каждой попытки. 
# Для генерации случайного числа используйте код: 
# from random import randint num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_L = 1000
COUNT = 0
num = randint(LOWER_LIMIT, UPPER_L)

while COUNT <= 10:
    number = int(input("Введите число:"))
    if num == number:
        print("Вы угадали число!")
        break
    elif num > number:
        COUNT +=1
        print("БОЛЬШЕ")
        print(f"Осталось попыток: {10 - COUNT}")
        print()
    elif num < number:
        COUNT +=1
        print("МЕНЬШЕ")
        print(f"Осталось попыток: {10 - COUNT}")
        print()
    if COUNT==10:
        print("Вы не угадали число")
        break

    

