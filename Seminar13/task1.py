def get_data():
    while True:
        try:
            a = input('Введите целое и вещественное число: ')
            a = int(a)
            return a
        except ValueError as e:
            print (f'Ошибка ввода данных {e}')

if __name__ == '__main__':
    print(get_data())