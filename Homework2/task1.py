# Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление. 
# Функцию hex используйте для проверки своего результата.

def convert(a: int , base: int) -> str :
    str_rep = ''
    while a:
        str_rep = str(a % base) + str_rep
        a //= base
    return str_rep

def convert(number: int, mod: int = 16) -> str:
    result = ''
    while number != 0:
        temp = number % mod if (number % mod) < 10 else chr(number % mod + 87)
        result = str(temp) + result
        number //= mod
    result = "0x" + result
    return result


print(convert(10, 8))
print(hex(40))