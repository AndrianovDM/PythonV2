# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# ✔ Избегайте магических чисел
# ✔ Добавьте аннотацию типов где это возможно

# def convert(a:int, base:int) -> str:
#     str_rep= ''
#     while a:
#         str_rep = str(a % base) + str_rep
#         a //= base
#     return str_rep

num = int(input('Enter a number: '))

a = num
str_rep = ''
while a:
    str_rep = str(a % 2) + str_rep
    a //= 2

print(f'binary representation: 0b{str_rep}')
print(bin(num))

str_rep = ''
a = num
while a:
    str_rep = str(a % 8) + str_rep
    a //= 8

print(f'octal representation: 0o{str_rep}')
print(oct(num))

