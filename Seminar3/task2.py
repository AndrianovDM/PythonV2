# Пользователь вводит данные. Сделайте проверку данных
# и преобразуйте если возможно в один из вариантов ниже:
# ✔ Целое положительное число
# ✔ Вещественное положительное или отрицательное число
# ✔ Строку в нижнем регистре, если в строке есть
# хотя бы одна заглавная буква
# ✔ Строку в нижнем регистре в остальных случаях

user_in = input('Введите данные: ')
print(user_in.istitle())

if user_in.isdigit():
    print(int(user_in), 'int')
elif user_in.find('.') != -1 and user_in.replace('.','').replace('-','').isdigit():
    print(float(user_in), 'float')
elif any([sym.isupper() for sym in user_in]):
    print(user_in.lower(), 'lower')
else:
    print(user_in.lower(), 'original')

