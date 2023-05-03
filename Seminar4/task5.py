# ✔ Функция принимает на вход три списка одинаковой длины:
# ✔ имена str,
# ✔ ставка int,
# ✔ премия str с указанием процентов вида «10.25%».
# ✔ Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# ✔ Сумма рассчитывается как ставка умноженная на процент премии. 

names = ['John', 'Adam', 'Ivan']
salaries = [15000, 20000, 25000]
bonuses = ['10.0%', '7.25%', '5%']


def calc_bonus(names: list[str], salaries: list[int], bonuses: list[str]) -> dict[str, float]:
    result = {}
    for name, salary, bonus in zip(names, salaries, bonuses):
        bonus_amount = salary * float(bonus[:-1]) / 100
        result[name] = bonus_amount
    return result

print(calc_bonus(names, salaries, bonuses))