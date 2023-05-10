# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
from datetime import datetime
from sys import argv

def caled(data: str):
    day, month, year = map(int, data.split('.'))
    if 1 <= year <= 9999:
        if month in [1, 3, 5, 7, 8, 10, 12] and 1 <= day <= 31:
            return True
        elif month in [4, 6, 9, 11] and 1 <= day <= 30:
            return True
        else:
            if 1 <= day <= 28 + leap_year(year):
                return True
    return False

def leap_year(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def validate(data):
    try:
        num = datetime.strptime(data, "%d.%m.%Y").date()
        return True
    except:
        return False


if __name__ == "__main__":
    inp = input('Введите дату: ')
    if validate(inp) == True:
        print('Верная дата')
    else:
        print('Такой даты не существует')
