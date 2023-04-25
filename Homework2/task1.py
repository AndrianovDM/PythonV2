# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

def convert(num: int, base: int ) -> str:
    str_rep = ''
    while num:
        if (num % base) < 10:
            temp = num % base
        else:
            temp = chr(num % base + 87)

        str_rep = str(temp) + str_rep
        num //= base

    if base == 2:
        str_rep = "0b" + str_rep
    elif base == 8:
        str_rep = "0o" + str_rep
    elif base == 16:
        str_rep = "0x" + str_rep

    return str_rep

number = int(input('Введите число: '))
systeam = int(input('Ввидите тип системы исчисления: '))

if systeam == 2:
    print('Результат:', convert(number, systeam))
    print('Проверка:', bin(number))
elif systeam == 8:
    print('Результат:', convert(number, systeam))
    print('Проверка:', bin(number))

elif systeam == 16:
    print('Результат:', convert(number, systeam))
    print('Проверка:', bin(number))